#solarwinds_inventory_plugin.py

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    name: solarwinds_inventory_plugin 
    plugin_type: inventory
    short_description: Returns Ansible inventory from Solarwinds URL, username and password
    description: Returns Ansible inventory from Solarwinds URL, username and password
'''
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.errors import AnsibleError, AnsibleParserError
class InventoryModule(BaseInventoryPlugin):
    NAME = 'solarwinds_inventory_plugin'
    def verify_file(self, path):
        '''Return true/false if this is possibly a valid file for this plugin to
consume
        '''
        pass
    def parse(self, inventory, loader, path, cache):
       '''Return dynamic inventory from source '''
       pass

