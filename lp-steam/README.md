lp-steam
===

srcds myths - busted
---
1. Binding on 00.00.00.00 is no different from binding on 0.0.0.0
	* rcon functionality is not impacted using either alias
	* broadcast discovery remains functional
	* `netstat -tulpn` generates the exact same output using both aliases (all listening on 0.0.0.0)
	* `rcon status` displays a listen address of `0.0.0.0:27015` in both cases

2. Broadcast discovery ceases to function as soon as a valid RFC1918 IP is bound (public address space could not be tested at the time of writing)

3. Rcon ceases to function as soon as one of the following criteria is true:
	* -usercon parameter missing from command line
	* -console parameter missing
	* +ip parameter missing

4. the 127.0.1.1 address is only displayed in `rcon status` in case:
	* 127.0.1.1 is mentioned in /etc/hosts
	* +ip parameter is missing from command line

While analyzing `netstat -tulpn`, it's clear that the `udp/ip` value in `rcon status` always matches the TCP (not UDP!) socket opened by srcds for rcon purposes. This traffic is not UDP.

It's safe to conclude that 3. and 4. correlate perfectly, seeing as rcon ceases to function when the `+ip` parameter is not specified on the command line. As a result of this, a local TCP socket is opened on 127.0.1.1, an address that is unreachable from outside the host. This traffic can never make it onto the network.

Sticking to the ruleset above, we would construct the following command line:

```
$ ./srcds_run -usercon -console +ip 0.0.0.0
```

Even running a VAC-enabled LAN server is possible using these parameters (by adding sv_lan 0), which would definitely be recommended for larger events.
