
Ansible Role: Packer
=========

Role to install (_by default_) `packer` package  on **Debian/Ubuntu** and **EL** systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
packer_app: packer
packer_version: 1.4.3
packer_osarch: linux_amd64
packer_dl_url: https://releases.hashicorp.com
packer_dl_loc: /tmp
packer_bin_path: /usr/local/bin
```

Variable `packer_app`: Defines the app to install i.e. **packer**

Variable `packer_version`: Defined to dynamically fetch the desired version to install. Defaults to: **1.4.3**

Variable `packer_osarch`: Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux_amd64**

Variable `packer_dl_loc`: Defined to dynamically choose where to place the binary archive for `packer` temporarily. Defaults to: **/tmp**

Variable `packer_dl_url`: Defines URL to download the packer binary from.

Variable `packer_bin_path`: Defined to dynamically choose the appropriate path to store packer binary into. Defaults to (as generally on any user's PATH): **/usr/local/bin** 

Dependencies
------------

None

Example Playbook
----------------

For default behaviour of role (i.e. installation of **packer**) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.packer
```

For customizing behavior of role (i.e. specifying the  desired **packer** version) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.packer
      vars:
        packer_version: 1.4.2
```

For customizing behavior of role (i.e. placing binary of **packer** package in different location) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.packer
      vars:
        packer_bin_path: /bin/
```

License
-------

[MIT](https://github.com/darkwizard242/ansible-role-packer/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
