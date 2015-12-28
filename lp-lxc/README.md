lp-lxc - OVS-integrated Linux Containers
===

TODO: This documentation clearly needs to be extended with network
configuration examples, storage types, details about the OVS integration, etc.

Usage
---

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
