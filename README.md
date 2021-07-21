[![build-test](https://github.com/darkwizard242/ansible-role-packer/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-packer/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-packer/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-packer/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/43173?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43173?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43173?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-packer&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-packer) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-packer&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-packer) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-packer&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-packer) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-packer&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-packer) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-packer?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-packer?color=orange&style=flat-square)

# Ansible Role: Packer

Role to install (_by default_) [packer](https://packer.io/) package on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
packer_app: packer
packer_version: 1.7.4
packer_osarch: linux_amd64
packer_dl_url: https://releases.hashicorp.com
packer_dl_loc: /tmp
packer_bin_path: /usr/local/bin
```

### Variables table:

Variable        | Value (default)                  | Description
--------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------
packer_app      | packer                           | Defines the app to install i.e. **packer**
packer_version  | 1.7.4                            | Defined to dynamically fetch the desired version to install. Defaults to: **1.7.4**
packer_osarch   | linux_amd64                      | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux_amd64**
packer_dl_url   | <https://releases.hashicorp.com> | Defines URL to download the packer binary from.
packer_dl_loc   | /tmp                             | Defined to dynamically set where to place the binary archive for `packer` temporarily. Defaults to: **/tmp**
packer_bin_path | /usr/local/bin                   | Defined to dynamically set the appropriate path to store packer binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
