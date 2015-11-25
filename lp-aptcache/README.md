lp-aptcache
===========

Maintaining the Repository
--------------------------
This was built using [Setting up your own APT repo](https://www.debian-administration.org/article/286/Setting_up_your_own_APT_repository_with_upload_support) and [Reprepro Manual](http://mirrorer.alioth.debian.org/reprepro.1.html).

Add package to the `party` suite:
In `/var/www/pkg`: `reprepro -Vb . includedeb party (filename)`
`reprepro list`

Make sure file permissions are set when executing as root in /var/www.