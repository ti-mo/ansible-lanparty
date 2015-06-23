Frag-o-Matic Users
==================
[Confluence - User Role (fom-users)](http://confluence.fom.be/pages/viewpage.action?pageId=26510904)

Usage
-----
```
# in vars/fom-users.yml
---
users:
  - name: myuser
    uid: 9001
    shell: /usr/bin/zsh ## Shell moet geïnstalleerd zijn op de node
    password: '$6$wCcsVc77LSo$xrQOp.RSwtnMkHPYsjsaH2jcPDOwXJ8.NfRO0Gu91ULNSlwSPAmvGpxikgIsFRH9GQ1HmjH/X7mxCCIv8ZNfZ0'
    keys:
      - name: id_myuser ## File moet bestaan: files/keys/myuser/id_myuser.pub
 
# Password hash kan worden gegenereerd met:
# openssl passwd -1 -salt xyz yourpass
```