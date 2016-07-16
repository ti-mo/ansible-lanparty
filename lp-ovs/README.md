lp-ovs - OpenVSwitch
===

These examples are based on [the Debian info on the OVS GitHub page](https://github.com/osrg/openvswitch/blob/master/debian/openvswitch-switch.README.Debian).

Using OVS with one phys interface
---

In case your hardware does not have multiple physical network ports,
it is possible to run both an LXC bridge and a 'native' interface on
the same physical port.

Set up the network configuration of the host prior to running the role.
Run the role and reboot (or ifup/down -a).

Below is a working example of an `/etc/network/interfaces` configuration
on a system with one physical port. The host binds to a management address
with a VLAN tag and LXC containers can be attached to the `br-lan` bridge.

```
auto br-lan
iface br-lan inet manual
  ovs_ports eth0 vlan4
  ovs_type OVSBridge

auto eth0
allow-hotplug eth0
iface eth0 inet manual
  ovs_bridge br-lan
  ovs_type OVSPort

auto vlan4
allow-hotplug vlan4
iface vlan4 inet static
  address 10.1.1.1
  netmask 255.255.255.0
  gateway 10.1.1.254
  ovs_bridge br-lan
  ovs_type OVSIntPort
  ovs_options tag=4
```

For more info on quirks of the Debian-OVS `/e/n/i` integration, see:
http://blog.scottlowe.org/2016/06/30/ovs-integration-debian-network-scripts

Note: the kernel will NOT respond to packets destined to an address
bound on eth0 as soon as it is enslaved by a Linux bridge or ovs-system.

_However_, adding a vlan interface on eth0 and binding an address on it
is possible. This gives full flexibility for running containers on any
vlan tagged to the node, as well as creating extra vlan interfaces inside
the host OS.

Bonding Interfaces
---

Bonding multiple physical interfaces together for higher throughput or
resilience is also possible. This works mostly like native Linux bonding.

```
auto br-lan
iface br-lan inet manual
        ovs_type OVSBridge
        ovs_ports bond0 vlan4

auto bond0
iface bond0 inet manual
        ovs_bridge br-lan
        ovs_type OVSBond
        ovs_bonds eth0 eth1
        ovs_options bond_mode=balance-slb
```

LACP can also be activated by adding `lacp=active` to 'ovs_options'.
