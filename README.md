[![build-test](https://github.com/darkwizard242/ansible-role-packer/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-packer/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-packer/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-packer/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/packer) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-packer&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-packer) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-packer&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-packer) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-packer&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-packer) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-packer?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-packer?color=orange&style=flat-square)

# Ansible Role: Packer

Role to install (_by default_) [packer](https://packer.io/) package on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
packer_app: packer
packer_version: 1.11.0
packer_os: "{{ ansible_system | lower }}"
packer_architecture_map:
  amd64: amd64
  arm: arm64
  x86_64: amd64
  armv6l: armv6
  armv7l: armv7
  aarch64: arm64
  32-bit: "386"
  64-bit: amd64
packer_dl_url: https://releases.hashicorp.com
packer_dl_loc: /tmp
packer_bin_path: /usr/local/bin
packer_file_owner: root
packer_file_group: root
packer_file_mode: '0755'
```

### Variables table:

Variable                | Description
----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------
packer_app              | Defines the app to install i.e. **packer**
packer_version          | Defined to dynamically fetch the desired version to install. Defaults to: **1.11.0**
packer_os               | Defines os type. Used for obtaining the correct type of binaries based on OS type.
packer_architecture_map | Defines os architecture. Used to set the correct type of binaries based on OS System Architecture.
packer_dl_url           | Defines URL to download the packer binary from.
packer_dl_loc           | Defined to dynamically set where to place the binary archive for `packer` temporarily. Defaults to: **/tmp**
packer_bin_path         | Defined to dynamically set the appropriate path to store packer binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
packer_file_owner       | Owner for the binary file of packer.
packer_file_group       | Group for the binary file of packer.
packer_file_mode        | Mode for the binary file of packer.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **packer**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.packer
```

For customizing behavior of role (i.e. specifying the desired **packer** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.packer
  vars:
    packer_version: 1.5.4
```

For customizing behavior of role (i.e. placing binary of **packer** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.packer
  vars:
    packer_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-packer/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
