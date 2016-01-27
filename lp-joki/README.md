lp-joki - Lightweight Latency Tracker
===

## Introduction

Joki builds an internal data structure to start its FPing workers and
to keep track of which tags to apply to data that's sent to InfluxDB.

## Basic Configuration

`lp-joki` has a basic built-in sanity check for its configuration.
Configuring an InfluxDB server (using `lp-influxdb`) is required.

Specify the InfluxDB endpoint on the Joki node as follows:

```
# Set on Joki node
influxdb_server: 10.1.1.151
influxdb_port: 8090 (optional)
```

Make sure to open a UDP listener on the `lp-influxdb` node:

```
# Set on InfluxDB node
influxdb_udp_listeners:
  joki: 8090
```

In the above example, `joki` specifies the database name, `8090` the
UDP listen port.

## Setting Probes

Share the following piece of configuration between the `lp-gw` node(s) and
the `lp-joki` node:

```
netif:
  modem1:
    route: 1
  modem2:
    route: 2

gw_priorities:
  prio1: 1
  prio2: 2
  browse: 3
```

`lp-joki` and `lp-gw` will generate a series of TOS values that map to their
respective routes and queues. This enables the Joki node to send packets along
a (set of) specific (unique) network path through the `lp-gw` topology and
accurately measure its RTT.

_netif.<key> is chosen as the probeset's short name. This value must be used
as the `probes` value for the targets below._

## Setting Targets

Adding targets is straightforward. Omitting `probes` in a ping_targets entry
implies a value of `all`. This allows a network path to be chosen for a probe.

```
ping_targets:
  google:
    fullname: Google
    address: 8.8.8.8
    probes: all
  modem1:
    fullname: Modem
    address: 192.168.0.1
  
  # Ping a modem's external address (hairpinning)
  # Great for measuring locally imposed loss/bloat/latency
  modem1_ext:
    fullname: "Modem's External Address"
    address: 12.34.56.78
    probes: modem1
```
