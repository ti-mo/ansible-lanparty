eBot Server
===========

eBot requires a pthread-enabled PHP binary.
Build a custom package using the instructions at [DigitalOcean](https://www.digitalocean.com/community/questions/enable-zts-support-on-ubuntu-14-04)

* `apt-get source php5`
* In `debian/rules`, add `--enable-maintainer-zts` to `COMMON_CONFIG`
* `sudo apt-get build-dep php5`
* `DEB_BUILD_OPTIONS= -j8`
* Distribute using your local package repo
