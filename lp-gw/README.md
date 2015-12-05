lp-gw - Internet Gateway
===

Routing Tables
---
A routing table per interface defined in the `netif` hash is added to `/etc/iproute2/rt_tables` by default. Tables will be added in order and have their indexes set to their position in the hash. Re-ordering the hash will switch up the table IDs, so doing this at runtime with rules in memory will cause issues.

IPsets
---
The role comes with a pre-populated hash of `ipsets` for popular (Game) Service Providers, as well as a definition of RFC1918 net blocks (private address space). These can be extended at your own convenience for use in the iptables/nftables ruleset.

IPTables / NFTables
---

### Feature toggles

Many deployment scenarios are supported. Different scenarios have varying requirements and benefits.

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
