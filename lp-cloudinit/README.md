lp-cloudinit
===

To consume this metadata through cloud-init, create the following files in your base image:

```
file: /var/lib/cloud/seed/nocloud-net/meta-data

#include
http://cloud.example.lan/meta-data
```

```
file: /var/lib/cloud/seed/nocloud-net/user-data

#include
http://cloud.example.lan/user-data
```

Make sure to point cloud-init to the URL you've deployed this role on.

_cloud-init will not pull metadata on every boot._ Remove `/var/lib/instances/nocloud` when rolling a base image.
Metadata will be downloaded when the image is first booted (and when networking is available), after which config management should take over.
