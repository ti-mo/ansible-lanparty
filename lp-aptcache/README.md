Frag-o-Matic Package Cache/Repo
===============================
[Confluence - APT-Cacher-NG (fom-ac-ng)](http://confluence.fom.be/pages/viewpage.action?pageId=26510539)

Maintaining the Repository
--------------------------
Dit werd opgebouwd mbv. [Setting up your own APT repo](https://www.debian-administration.org/article/286/Setting_up_your_own_APT_repository_with_upload_support) en [Reprepro Manual](http://mirrorer.alioth.debian.org/reprepro.1.html).

Package toevoegen aan `fom` suite:
In `/var/www/pkg`: `reprepro -Vb . includedeb fom (filename)`
`reprepro list`

Kijk uit voor file permissions.
