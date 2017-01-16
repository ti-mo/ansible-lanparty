lp-consul - Consul Service Discovery
===

## Generating a secret

Run `consul keygen` to have Consul generate a value. Set the `consul_secret` variable to this value. Keep in mind this secret cannot be changed without manual intervention once the cluster is up and running.

This is mandatory, `lp-consul` will throw an error when this secret is missing.

## Specifying Advertised Interface

The `consul_interface` parameter can be used to specify the network interface
(eg. 'lan') to use to advertise to the cluster. This needs to be set on hosts
with multiple network interfaces. (eg. ISP, firewalls, baremetals, ..)

## DNS Domain

`consul_domain` (default: 'consul'): shared parameter w/ `lp-ns`, specifies
the NS domain the Consul cluster is authoritative for. In case of 'foo', eg.
`nslookup nginx.service.foo`.

## Server Nodes

### Inventory Group

Installing Consul in server mode is done by adding the server nodes to the group defined in `consul_inventory_group` (default: `consul`):

```
[consul]
lp-consul-01
lp-consul-02
lp-consul-03
```

### Server Shutdown

Server nodes do not gracefully leave the cluster when the `consul` service stops [due to the following bug](https://github.com/hashicorp/consul/issues/750) and a couple of related issues. Servers are supposed to be up and should not change addresses.

### Server UI

Consul servers depend on `lp-nginx` for providing a local proxy with access control for the locally-served Web UI. The Web UI is at `<consul-server>/ui`.

Access can be controlled by setting the widely-used `trusted_networks` variable, which will govern access on the nginx front-end itself.

## Client Nodes

Client nodes can be added by just applying `lp-consul` to them.

They will join the cluster of the group of nodes defined in `consul_inventory_group` (default: `consul`).

Clients gracefully leave the cluster upon termination as they are killed using SIGINT.

### Integration with other roles

Roles that want to install Consul health checks and service definitions should
optionally depend on lp-consul like so:

```
# meta/main.yml
dependencies:
  - role: lp-consul
    when: consul_agent_enable | default(false) == true
```

The Consul package will be installed, dirs in `/etc/consul.d` will be created
and the health checks and service definitions can be safely dropped in `/etc/consul.d/checks` and `/etc/consul.d/services` accordingly.

Build a similar condition to apply a playbook containing the checks and
definitions to the system, eg. `consul.yml`. Setting `consul_agent_enable` on
node level will install a Consul client and the checks. Also, write a handler.
