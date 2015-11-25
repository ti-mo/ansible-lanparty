lp-mysql
========

To-Do
-----
* Clustering Support

Usage
-----
```
---
mysql:
  port: 3306
  bind_address: "0.0.0.0"
  repl:
    id: 7
    role: master
  root_pass: super-secret-root-passwd
  backend_group: mysql-group        # Used by lp-mysql-client to find back-ends
  apps:
    my-app:
      db: app-db-name
      user: app-user
      pass: super-secret-app-password
 ```
