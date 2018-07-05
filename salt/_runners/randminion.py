import salt.client
import salt.config
import salt.runner
from random import choice

def target(mod='test.ping'):
    ''' run exec module on random minion '''

    print 'execution module selected: {0}'.format(mod)

    # load master config
    opts = salt.config.master_config('/etc/salt/master')
    print "master config loaded"

    # load runner client with master config
    runner = salt.runner.RunnerClient(opts)

    print 'fetching minions'
    # run manage.up to fetch active minions
    list_of_minions = runner.cmd('manage.up', [])

    # let python randomly choose a minion
    random_target = choice(list_of_minions)
    print 'random minion chosen'

    # load the execution module client
    local = salt.client.LocalClient()
    print 'local client loaded'

    # run execution module on randomly targeted minion
    return local.cmd(random_target, mod)

def otherfunction():
    return "stuff!"


# salt-run randminion.target mod='mymod.hello'
# salt-run randminion.otherfunction
