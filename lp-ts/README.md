TeamSpeak3 Role
---------------
This role was written using the [TeamSpeak3 Quick Start](http://media.teamspeak.com/ts3_literature/TeamSpeak%203%20Server%20Quick%20Start.txt) document, more specifically the MySQL integration.

The systemd unit will check whether or not the remote MySQL port is open using netcat in ExecStartPre (I know..). TS3 will start whether or not MySQL runs, and will fall back to SQLite when the remote is offline, leading to unexpected behaviour. More elegant solutions are very welcome.

ABI-compatible mysql libs are installed from http://archive.debian.org/debian/pool/main/m/mysql-dfsg-5.0, hopefully they link against something more up-to-date soon.
