import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PACKER_BINARY_PATH = '/usr/local/bin/packer'


def test_packer_binary_exists(host):
    host.file('PACKER_BINARY_PATH').exists


def test_packer_binary_file(host):
    host.file('PACKER_BINARY_PATH').is_file


def test_packer_binary_run(host):
    host.check_output('whereis packer') == PACKER_BINARY_PATH
