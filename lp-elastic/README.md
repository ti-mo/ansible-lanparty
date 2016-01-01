lp-elastic
===

Minimal clustering elasticsearch configuration w/ Nginx proxy. Nginx is
configured without buffering and is mainly used for access control.
(using `trusted_networks`)

elasticsearch only listens on localhost and Nginx listens on 0.0.0.0:80.

Trusted Networks
---

Make sure to define a trusted network in the `trusted_networks` list. Without
this, nodes will refuse to cluster and requests from clients will fail.

Requests from the node's `ansible_default_ipv4` and from 127.0.0.1 are added
automatically.

Useful REST Calls
---

Some elasticsearch queries to aid in troubleshooting:

* Get list of ind(ic|ex)es: `curl "localhost/_cat/indices?v"`
* Show cluster status: `curl "localhost/_cluster/health?pretty=true"`
* Drop an index: `curl -XDELETE "localhost/syslog-2015.12.31.15"`
