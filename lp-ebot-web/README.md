lp-ebot-web
===

This role is responsible for creating / migrating the database scheme,
make sure to (successfully) run this role somewhere before running `lp-ebot` to
avoid starting the bot without a valid database.

Creating an admin user
---

This step needs to be done manually as running it through config management
is unreliable (and insecure!).

From the ebot-web installation directory (typically /var/www/ebot), run:
```
php symfony guard:create-user --is-super-admin admin@ebot admin password
```

Log in to the admin panel using `http://<your-ebot-web-address>/admin.php`.

Troubleshooting
---

#### Manually converging database schema

In case the deployment fails halfway through, chances are the database schema
has fail to install. (Specifically, `Config | Install Symfony database`) Run
this from your eBot-Web install directory to retry (typically /var/www/ebot):

```
php symfony doctrine:insert-sql
```

Furthermore, make absolutely sure that:

* `databases.yml` contains the correct credentials
* the 'ebot' database was successfully created (using `lp-mysql-client`)
* MySQL is fully functional (type `mysql` as any user after running `lp-mysql`)
