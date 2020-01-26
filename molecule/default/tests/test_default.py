import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packer_binary_exists(host):
    assert host.file('/usr/local/bin/packer').exists


def test_packer_binary_file(host):
    assert host.file('/usr/local/bin/packer').is_file


def test_packer_binary_which(host):
    assert host.check_output('which packer') == '/usr/local/bin/packer'
