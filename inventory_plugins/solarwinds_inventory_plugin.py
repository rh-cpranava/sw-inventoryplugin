#solarwinds_inventory_plugin.py
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    name: solarwinds_inventory_plugin 
    plugin_type: inventory
    short_description: Returns Ansible inventory from Solarwinds URL, username and password
    description: Returns Ansible inventory from Solarwinds URL, username and password
    options:
      plugin:
        description: Name of the plugin
        required: true
      server: 
        description: Server IP
        required: true
        env:
          - name: SW_SERVER
      user:
        description: User
        required: true
        env:
          - name: SW_USER
      password:
        description: Password
        required: true
        env:
          - name: SW_PASS
      port:
        description: Port
        required: true    
'''
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.errors import AnsibleError, AnsibleParserError
import requests
class InventoryModule(BaseInventoryPlugin):
    NAME = 'solarwinds_inventory_plugin'
    def verify_file(self, path):
        '''Return true/false if this is possibly a valid file for this plugin to
    consume
        '''
        return True 

    def parse(self, inventory, loader, path, cache):
        '''Return dynamic inventory from source '''
        super(InventoryModule, self).parse(inventory, loader, path, cache)
        # Read the inventory YAML file
        self._read_config_data(path)
        self.server = self.get_option('server')
        self.user = self.get_option('user')
        self.password = self.get_option('password')
        self.port = self.get_option('port')
        query = "SELECT SysName, DNS, IP, MachineType FROM Orion.Nodes"
        url = "https://"+self.server+":"+str(self.port)+"/SolarWinds/InformationService/v3/Json/Query"
        req = requests.get(url, params="query="+query, verify=False, auth=(self.user, self.password))
        query_results = req.json()
        for hosts in query_results['results']:
            self.inventory.add_host(host=hosts['IP'])
           