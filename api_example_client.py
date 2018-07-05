import salt.config
import salt.loader
from pprint import pprint

__opts__ = salt.config.minion_config('/etc/salt/master')
__grains__ = salt.loader.grains(__opts__)
__opts__['grains'] = __grains__
__utils__ = salt.loader.utils(__opts__)
__salt__ = salt.loader.minion_mods(__opts__, utils=__utils__)

pprint(__opts__)                # good way to see default values
pprint(__grains__['id'])        # get id from grains
pprint(__salt__['test.ping']()) # get result of test.ping

# More info
# https://docs.saltstack.com/en/latest/ref/clients/index.html
