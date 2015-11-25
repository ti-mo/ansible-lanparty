ansible-lanparty
---

Collection of integrated Ansible roles used to run LAN events.
This repository consists of roles that are _purpose-built_, _lean_
and as easy as possible to understand and modify. The roles are built to
simplify and accelerate, not to obscure.

It is primarily used in temporary environments, so great care is taken to
avoid specific startup sequence dependencies between systems. The whole stack
needs to come up automatically after a power cut or a physical move.

It was created for a Debian-based OS by the organizers of
[Frag-o-Matic](http://fom.be) and [ZanziLan](http://zanzilan.be).
Feel free to get in touch through any of the advertised contact details or come
grab a beer at one of our events!

Disclaimer
===

_The 0.1.x track will suffer breaking changes and possibly history re-writes._ Patch notes will always be provided.

This project was only recently published on GitHub and was previously
maintained privately. There is no documentation, and a scratch setup will be
very frustrating and time-consuming without a working example. Please bear with
us as we work out these aspects.

Feel free to hack on the code, log issues and send PRs in the meantime!

Feature Overview
===

* _internet gateways with low-latency-oriented packet shaping_ - serve hundreds (thousands) of gamers using residential WAN links
* (Dynamic) DNS, DHCP, Samba shares
* TeamSpeak 3 servers w/ MySQL
* STEAM binary content caching
* Twitch HLS stream caching
* Systems management (APT cache, Users, SSH Keys, NTP)
* Monitoring
    - Smokeping latency graphing
    - LibreNMS
* LXC containers integrated w/ OVS bridges
* Centralized logging and log shipping
* eBot for automating CS:GO competitions
* BGPanel for gameserver management (phase-out)
* cloud-init server to accelerate provisioning on VMware farms
