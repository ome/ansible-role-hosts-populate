Hosts Populate
==============

[![Build Status](https://travis-ci.org/ome/ansible-role-hosts-populate.svg)](https://travis-ci.org/ome/ansible-role-hosts-populate)
[![Ansible Role](https://img.shields.io/ansible/role/41888.svg)](https://galaxy.ansible.com/ome/hosts_populate/)


Populates `/etc/hosts` with static addresses for a list of hostgroups.


Role Variables
--------------

Optional variables:
- `hosts_populate_iface`: Lookup the host IP using this network interface, default `eth0`
- `hosts_populate_openstack_groups`: List of openstack groups, hosts from these groups will be included in `/etc/hosts`.
  In practice this will probably work with non-openstack groups too.
- `hosts_populate_regex_alias`: Include a host alias, defined by the first `(group)` in this regex.

Warning: This role requires full control of `/etc/hosts`.


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
