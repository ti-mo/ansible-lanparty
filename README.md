ansible-lanparty
---

Collection of integrated Ansible roles used to run LAN events.
This repository consists of roles that are _purpose-built_, _lean_
and as easy as possible to understand and modify. The roles are built to
simplify and accelerate, not to obscure.

It is primarily used in temporary environments, so great care is taken to
avoid specific startup sequence dependencies between systems. The whole stack
needs to come up automatically after a power cut or a physical move.

It was created for a Debian-based OS by the organizers of [Frag-o-Matic](https://fom.be). Feel free to get in touch through any of the advertised
contact details or come grab a beer at one of our events!

Contents
===

- [lp-depot](lp-depot/README.md) - game download cache with nginx
- [lp-ts](lp-ts/README.md) - run your own local TeamSpeak 3 server
- [lp-collectd](lp-collectd/README.md) - gather metrics from machines and containers
- [lp-ebot](lp-ebot/README.md) - CS:GO match automation with eBot
- [lp-influxdb](lp-influxdb/README.md) - time series database for metrics and statistics
- [lp-grafana](lp-grafana/README.md) - beautiful graphs with Grafana
- [lp-observium](lp-observium/README.md) - monitor infrastructure with LibreNMS
