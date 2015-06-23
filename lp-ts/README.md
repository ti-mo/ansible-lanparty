Frag-o-Matic TeamSpeak3 Playbook
--------------------------------
[Confluence - TeamSpeak (fom-ts)](http://confluence.fom.be/pages/viewpage.action?pageId=26510900)
[TeamSpeak3 Quick Start](http://media.teamspeak.com/ts3_literature/TeamSpeak%203%20Server%20Quick%20Start.txt)

Backwards-compatible mysql libs are at http://archive.debian.org/debian/pool/main/m/mysql-dfsg-5.0

Beschrijving
============
Deze TeamSpeak3-server gebruikt MySQL als back-end en genereerde bij het opstarten de volgende Squery-account.

------------------------------------------------------------------
               Server Query Admin Account created                 
         loginname= "serveradmin", password= "XpYaJeiR"
------------------------------------------------------------------

Er werd voor MySQL gekozen om ervoor te zorgen dat Voice nodes voor 99% disposable zijn. Misschien willen we gaan experimenteren met het opzetten van meerdere voice-servers om de load zoveel mogelijk te spreiden gezien de performance-penalties we ondervinden bij het hosten op VMware. MySQL komt ook de schaalbaarheid ten goede omdat het default SQLite is.

Dit stelt ons ook in staat om enorm snel op baremetal te deployen als er iets fout gaat met een Voice-node zonder heel de database te verliezen en zonder elke editie opnieuw een TeamSpeak-server in te moeten richten. (thank god) 

Bouncing Resources
==================
Resources die de service herstarten bij wijzigingen zijn:
- Nieuwe tarball downloaden/installeren
- MySQL config
- Init script

Playbook
========
Het playbook werd geschreven met behulp van [TeamSpeak Server Quick Start](http://media.teamspeak.com/ts3_literature/TeamSpeak%203%20Server%20Quick%20Start.txt). Dit is wat het playbook doet:

- libmysqlclient downloaden
- libmysqlclient symlinken naar libmariadb om compatibiliteitsredenen
- TeamSpeak system user aanmaken
- Install en download dirs aanmaken
- Tarball binnenhalen en uitpakken, leading dir strippen en rsyncen naar de install dir
- MySQL config renderen
- Init script installen
