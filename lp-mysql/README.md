Frag-o-Matic MySQL Role
=======================
[Confluence - MySQL (fom-mysql)](http://confluence.fom.be/pages/viewpage.action?pageId=26510886)

To-Do
-----
* Clustering Support
* Schema Import Behaviour

Het gedrag van een schema import bij het meegeven van meerdere databases moet verder worden getest. Het is mogelijk dat alle schema's opnieuw worden geïmporteerd als er een change wordt geregistreerd aan één database in  de lijst.

Usage
-----
```
# in vars/foo-app.yml
---
users:
  - name: timo
 
mysql:
  port: 3306
  bind_address: "0.0.0.0"
  repl:
    id: 7
    role: master
  root_pass: super-secret-root-passwd
  client_inv: webapp-group ## Ansible Inventory Group met MySQL client hosts
  databases:
    - name: foo_db
     (schema: /usr/local/app/schema.sql) ## Deze file moet bestaan op de eerste host in `client_inv`
  user:
    name: foo_user
    pass: bar
 
# in playbook
---
- hosts: mysql-group
  roles:
    - fom-mysql
  vars_files:
    - vars/foo-app.yml
```
