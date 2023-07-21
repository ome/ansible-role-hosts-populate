import os
import re
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_index(host):
    f = host.file("/etc/hosts-molecule")
    assert re.search(
        r'^# Group all\n^\d+\.\d+\.\d+\.\d+ hosts-populate$', # noqa
        f.content_string, re.MULTILINE)
