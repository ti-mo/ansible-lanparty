Out-of-Band Management
======================
Er wordt een oplossing uitgewerkt op basis van de volgende resources:

[OOB With Network Namespaces](http://blog.bofh.it/debian/id_446)
[SSHd ForceCommand](http://askubuntu.com/questions/397674/run-scripts-automatically-in-server-after-ssh-connection)
[nsenter op Debian/Ubuntu](http://programster.blogspot.be/2014/05/ubuntu-docker-enter-running-container.html)
[nsenter manpage](http://man7.org/linux/man-pages/man1/nsenter.1.html)

Het enige probleem hiermee is misschien het 'grote' (5+) aantal geneste processen omdat nsenter pas wordt uitgevoerd nadat de gebruiker is ingelogd in de OOB namespace. Als er daarna nog `su (user)` wordt gedaan om daarna terug naar root te sudo'en moeten we misschien nadenken over een andere aanpak.

Bash-processen laten spawnen in de juiste namespace door SSHd zou een goede oplossing zijn!

> /usr/local/bin/nsenter-main
> #!/bin/sh -e
> exec nsenter --net --mount --target 1 --wd=$HOME -F "$@"
