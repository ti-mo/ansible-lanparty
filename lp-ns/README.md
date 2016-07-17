lp-ns - Caching and Authoritative Name Server
===

## Consul Domain

`consul_domain` (default: 'consul'): shared parameter w/ `lp-consul`, specifies
the NS domain the Consul cluster is authoritative for. In case of 'foo', eg.
`nslookup nginx.service.foo`.

## Consul DNS Forwarding

BIND can be configured to forward requests for the domain specified in
`consul_domain` to its local Consul agent. This makes Consul service discovery
available to standard DNS clients.

`consul_publish_dns` (default: false): Expose Consul service discovery to the
rest of the network through regular DNS. Needs `consul_agent_enable` to
function properly.
