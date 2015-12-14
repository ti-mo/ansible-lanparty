lp-collectd
---

Installer for `collectd-core`. The package comes without any configuration,
so it's exactly what we need.

The role creates `/etc/collectd.d`, and renders a boilerplate configuration
to `/etc/collectd/collectd.conf` other roles (like `lp-gw`) drop their own
into `collectd.d/*.conf` and are included by `collectd.conf`.

InfluxDB Back-end
---

At present, the only configuration variables are:

```
collectd_server: 127.0.0.1
collectd_server_port: 25826
```

`collectd_server` has no default and needs to be set in order for the `network`
plugin to be activated. `collectd_server_port` defaults to 25826.
