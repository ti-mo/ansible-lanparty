lp-lxc - OVS-integrated Linux Containers
===

TODO: Document container definitions.

## Usage

Playbook example with a restart prompt.

```
- hosts: metal
  sudo: true
  roles:
    - lp-lxc
  
  vars_prompt:
    - name: lxc_restart
      prompt: "Ansible can automatically take care of network configuration on modified containers.\nRestart LXC containers when container config changes? (type YES in caps)\nCAREFUL, THIS WILL RESTART ANY MODIFIED CONTAINER!"
      default: 'NO'
      private: no
```

## Networking with OpenVSwitch

See the `lp-ovs` README.md for exact information on how to configure
OpenVSwitch with bonding and vlan tagging in Debian.

`lxc_bridge`: variable that controls the bridge to attach containers to

## Migrating containers to other hosts

Containers can easily be migrated When migrating containers (and its rootfs/) to another host using `rsync`. Keep in mind that the subUIDs/subGIDs need to remain untouched for the remote copy to be intact; they cannot be translated by `rsync` during the copy.

On the source host:

```
# lxc-stop -n zl-cache
# rsync --numeric-ids --rsync-path="sudo rsync" -av /var/lib/lxc/zl-cache
timo@10.16.4.158:/var/lib/lxc
```

On the destination host:

`# lxc-start -n zl-cache`
