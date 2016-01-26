lp-samba - Samba File Shares
---

Adding Users
---
Adding a user is done in two steps. First, the UNIX user; second, the Samba user using pdbedit.

Setting a valid shell for the user is not required.

```
$ sudo usermod -aG sambashare <user>
$ pdbedit -a -u <user>
```

The password specified in `pdbedit` is the password that can be used to log in over Samba.

Folder Permissions
---
In order to allow multiple users to read and modify files on the share created by others, setGID can be used.

By default, `lp-samba` specifies a default umask of 2775, but this is only enforced on files that are created through Samba itself. Existing folder structures can be easily modified using a command like:

```
$ sudo find /media/share -type d -exec chmod 2775 {} \;
```
