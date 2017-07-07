import testinfra.utils.ansible_runner
import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_index(File):
    f = File("/etc/hosts")
    assert re.search(
        '^# Group all$\n^\d+\.\d+\.\d+\.\d+ host-populate$',
        f.content, re.MULTILINE)
