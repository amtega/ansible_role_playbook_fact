# Ansible playbook_fact role

This is an [Ansible](http://www.ansible.com) role that setup a fact with info about the playbook that is running from the git repository containing the repo.

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

The role setup the following fact:

```yaml
playbook_info:
  project: <project>  # The playbook's project
  version: <version>  # Version of the project
  file: <file>        # Playbook file
```

Also the role setups a local fact on the servers running the playbook that can be accesed using `ansible_local.playbooks_info`. This local fact contains a list of dicts with the info about the playbooks ran on the servers.

## Example Playbook

This is an example playbook:

```yaml
---

- hosts: all
  roles:
    - role: amtega.playbook_fact
```

## Testing

Tests are based on docker containers. You can setup docker engine quickly using the playbook `files/setup.yml` available in the role [amtega.docker_engine](https://galaxy.ansible.com/amtega/docker_engine).

Once you have docker, you can run the tests with the following commands:

```shell
$ cd amtega.playbook_fact/tests
$ ansible-playbook main.yml
```

## License

Copyright (C) 2020 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
