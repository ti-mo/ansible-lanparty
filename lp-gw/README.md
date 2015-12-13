lp-gw - Internet Gateway
===

Interface Configuration
---
_/etc/network/interfaces will NOT be managed for LXC containers! Modify the
interface declarations you gave to lp-lxc instead!_

Interfaces can be defined in the `netif` hash and should be declared on a host
level. Enabling Ansible's hash merging allows you to define host interface
templates.

This is a complete example that showcases what the role can do:

```
netif:
  lan:                 ## The interface facing our clients
    addr: 10.1.1.5
    netmask: 255.255.255.0
    internal: true     ## Generate routes to `gw_internal_networks`
    nexthop: 10.1.1.1  ## over 10.1.1.1, useful for hardware core router
  isp1:                ## Interface in transit network with isp1
    addr: 10.16.61.1
    netmask: 255.255.255.0
    route: 1              ## Mark interface as external
    nexthop: 10.16.61.10  ## Route packets over 10.16.61.10
  isp2:                ## Directly connected to a modem
    addr: dhcp         ## Disables routes in routing tables
    nat: yes           ## Masquerade outgoing packets
    route: 2           ## This will generate an unused routing table
```

Routing
---

In order to keep the environment as lean and error-resilient as possible, we
apply dynamically-configured static routing. This avoids any dependencies that
cross system boundaries and configures machines in a fully deterministic way.

When chaining gateways together (eg. 1 core, 4 ISPs), it's necessary to define
a return path on each ISP host. Without a return path, ISP gateways will send
all traffic destined to private addresses over their DHCP-assigned default
gateways.

_It might be necessary to temporarily add a return path manually._ With the
correct configuration, once Ansible has been run on the remote gateway, routes
towards internal networks will be configured permanently and will persist
across reboots.

```
gw_internal_networks:
  - 10.1.1.0/24

netif:
  lan:
    addr: 192.168.0.2
    netmask: 255.255.255.0
    internal: true
    nexthop: 192.168.0.1
  wan:
    addr: dhcp
```

The configuration above will add a path to 10.1.1.0/24 over 192.168.0.1 to the
main routing table. Any packets destined to 10.1.1.0/24 will be sent to
192.168.0.1 over the `lan` interface.

Link Selection
---

The role allows you to configure an outgoing interface (directly connected WAN
link or other hop) based on multiple criteria. It is heavily focused towards
source-based routing. Selecting links with different WAN addresses often yield
unwanted side effects, eg. a game launcher connecting to port 443 with one
source address and the game client connecting to 27015 with another.

A routing table per interface defined in the `netif` hash is added to `/etc/iproute2/rt_tables` when the interface's `route` parameter is set. `route`
must be a unique number, as it is used to identify the interface's routing
table.

_DHCP interfaces will always have their default gateways added to the `main`
table by dhclient. Adding more than one DHCP interface is not recommended!_

Mapping a range of addresses on your network to a specific outgoing interface
can be done as follows:

```
gw_routes:
  visitors: [ 10.1.1.0/24, isp2 ]
```

Given the `isp2` interface is defined on the host `gw_routes` is set on,
traffic from 10.1.1.0/24 will leave over interface `isp2`.

Ranges can be overridden (eg. you want to allocate a dedicated link with a
higher upload profile to a live streamer) as follows:

```
gw_force_routes:
  stream: [ 10.1.1.123/32, isp3 ]
```

This condition will be evaluated earlier in the ruleset, the rules in
`gw_routes` will be ignored for 10.1.1.123.

Service Definitions (QoS)
---

The role comes with a pre-populated hash of `gw_ipsets` for popular (game) service providers, as well as a definition of RFC1918 net blocks (private address space). These can be extended at your own convenience for use in the iptables/nftables ruleset.

Feature Overview
---

Many deployment scenarios are supported. Different scenarios have varying requirements and benefits. Some features can be explicitly enabled or disabled,
some are simply optional and can be configured by defining certain behaviour.

### Minimal Mode

Install a lightweight gateway with all features disabled BUT the following:

* TC ruleset on marked interfaces
* NAT on marked interfaces (implicitly enables conntrack)
* DSCP-to-fwmark conversion

Useful in scenarios where one lp-gw instance functions as a central gateway,
doing packet classification and link selection and tagging all packets with
DSCP. Enable this on a per-host basis using:

```
gw_config:
  minimal: true
```

### MAC Spoofing

Some ISPs require the customer to send a DHCP request with a specific MAC
address in order to receive a pre-determined, 'fixed' address.

_This is disabled in LXC containers, set the MAC in lp-lxc instead!__

```
netif:
  wan:
    addr: dhcp
    macspoof: be:ef:be:ef:12:34
```

This allows, after bouncing the interface, to override the interface's MAC
address. To combine this with interface renaming, read the paragraph below.

### Interface Renaming (Udev)

Interface names like enp2s0 or eth1 are difficult to identify and easy to mix
up. Just define the interface as you'd like it to appear and make sure to
include the _original_ MAC address as seen on the network card or hypervisor.

_This is disabled in LXC containers, set the interface name in lp-lxc instead!_

```
netif:
  lan:
    addr: 10.1.1.1
    netmask: 255.255.255.0
    mac: or:ig:in:al:ad:dr
```

Additionally, you can spoof the MAC on this interface, too:

```
netif:
  lan:
    addr: 10.1.1.1
    netmask: 255.255.255.0
    mac: or:ig:in:al:ad:dr
    macspoof: be:ef:be:ef:12:34
```

This will:

1. Generate a Udev rule that will rename the interface during system
initialization based on the hardware address
2. Configure the interface with the hwaddr given in `macspoof`
3. Bring up the interface
4. Assign the defined address to the interface (dhcp too!)

### Access Control

#### gw_whitelist - exempt hosts from filtering

User-configurable array of hosts to allow to send any traffic over the gateway. Useful in cases where you want a recursive resolver or a caching proxy to access external DNS directly.

```
gw_whitelist:
  - 10.0.0.1/32
```

#### gw_blacklist - block traffic over gateway

In order to prevent specific hosts to initiate connections over the gateway, or to block a certain destination port towards the internet, `gw_blacklist` can be used. Handy for blocking abusers or to force users to use a local DNS server.

The example below will block ALL outgoing traffic initiated by the `10.0.1.0/24` range and all TCP & UDP traffic towards port 53.

```
gw_blacklist:
  hosts:
    - 10.0.1.0/24
  ports:
    - 53
```

### gw_trashing - Connection Trashing

Trash or demote flows once they accumulate a certain size.
[ from (fw_mark.class), to (fw_mark.class), threshold (bytes), direction ]

The example below demotes a 'browsing' flow to 'downloading' once it reaches 4MB in volume.

```
gw_trashing:
  - [ 'browse', 'download', '4000000', 'both' ]
```

### gw_smokeping_host - obey DSCP from clients

Set the address or CIDR of the Smokeping host(s) in `gw_smokeping_host`.

```
gw_smokeping_host: 10.1.1.5/32
```
