Frag-o-Matic Base Role
======================
[Confluence - Base Role (fom-base)](http://confluence.fom.be/pages/viewpage.action?pageId=26510532)

Inhoud
------
Ter referentie: [Confluence-pagina](http://confluence.fom.be/display/NET/Cookbook:+linux+default+host) met de (oude) barebones template van een Linux host.

Wat heeft een goeie base role nodig? Roles die aan master/client election doen moeten bv. worden afgesplitst en worden hieronder apart opgelijst. Roles met een grote lijst aan default attributes vallen ook onder deze regel.

Deze playbook zorgt voor het volgende:
* FoM kernel
* Kernel parameters (sysctl.conf)
* Safe SSHd config
* Git/Ansible deployment key
* Monitoring agent
* NTP

Bijkomende packages: 
* sudo
* syslog
* open-vm-tools
* arping
* tcpdump
* ethtool
* dnsutils
* git
* htop
* hping3

Deze taken worden elk in hun eigen rollen geïmplementeerd:
* Users, keys en hun favoriete shell/PS1

APT
---
De APT-setup is gebaseerd op [deze StackOverflow thread](http://serverfault.com/questions/22414/how-can-i-run-debian-stable-but-install-some-packages-from-testing)