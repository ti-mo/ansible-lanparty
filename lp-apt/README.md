
lp-apt - Manage Apt Package Sites
===

This is a role that can easily be included by others. There is an example
implementation in `lp-base`. Set your variables in the including role and
depend on `lp-apt` like so:

```
# your-role/meta/main.yml
---
allow_duplicates: yes
dependencies:
  - lp-apt
```

## Managing GPG Keys (apt-key)

Variable: `apt_keys`

A dict of URLs of GPG keys to install using `apt-key`. Please take care to
host your keys on an encrypted endpoint.

```
apt_keys:
  lanparty: https://pkg.incline.eu/GPG-KEY-lanparty
```

## Defining Apt Sources

Variable: `apt_sources`

This is a very simple (but powerful) example of how to configure an Apt package site.

```
apt_sources:
  stable:
    distro: jessie
    components:
      - main
      - contrib
      - non-free
    source: true
    priority: 500
  lanparty:
    site: pkg.incline.eu
    priority: 600
```

An entry in `apt_sources` takes the following parameters:

### Site 

Key: `site` (default: `httpredir.debian.org/debian`)

The URL to fetch packages from. Does _not_ support TLS at the moment, since
that cannot be used with an Apt proxy (cannot be cached).

### Distro

Key: `distro` (default: the key of the entry itself, eg. `stable`)

This sets the distribution as seen in the repo URL. (eg. jessie, testing, etc.)

### Components

Key: `components` (default: `[ 'main' ]`)

A list of components to allow packages to be installed from. `'main'` should
be present in most if not all Debian repositories. Other common components are
`non-free`, `contrib`, etc.

### Priority

Key: `priority` (default: 500)

Make sure to read [apt_preferences(5)](https://linux.die.net/man/5/apt_preferences), more specifically 'How Apt Interprets Priorities'.

The current 'stable' distribution should be kept at 500, custom repositories
and debian-security between 501 and 990 included, everything else below 500.

### Source

Key: `source` (default: false)

Set to `true` to render a corresponding `deb-src` entry in the repository's
`.list` file.
