# salt course

This repo is a basic set up of the most used features

The following is instructor notes and may not make sense to everyone


### Basic

- Installing salt
  - repo.saltstack.com
- Master configuration (see configs folder)
- Accepting keys
  - `auto_accept: True` is also an option
- Issuing commands
  - targeting minions with grains or perl compliant regular expressions
  - modules, functions, arguments, and how to read documentation
- States and top files
  - targeting in top files
  - environments
  - `state.highstate` vs `state.apply`
- Grains
  - salt['grains.get']('something', 'default-value')
  - grains['something']
- Pillars
- jinja2
  - accessing pillar and grain data to populate states
- debug mode and debug commands
  - salt-master -l debug
  - salt-call -l debug
  - `state.show_sls <statename>`
  - minion and master log files
  - sometimes a minion appears twice in the salt-key output?


### Intermediate

- Custom modules and runners
  - overriding built-in features
  - extending salt with new features
  - `saltutil.sync_all` (is also run by highstate)
- Eventbus
  - going from automating to automatic
  - sending events via commands and states: `salt-run event.send my/custom/event '{"foo": "bar"}'`
- Beacons (diskusage in pillars)
  - see the events in the eventbus
- Reactors (diskwarning in runners)
  - react to beacons
  - presence events (accepting new keys, removing old ones)
  - makes various integrations to slack and other systems a possibility
- Rest web API
  - needs its own user account, see the saltapi state
  - needs its own permissions, see the saltapi config file
  - finally restart the salt-api service
  - code example: api_example_rest.py


### Advanced

- Returners (rethinkdb example)
  - what is a returner, architecture behind it
- Pyobjects (nginx example)
  - all of python available, notice capitalisation of modules
- Gitfs (golang example)
  - dodgy feature, hopefully it works
  - formulas uses "maps" to give sane defaults, typically based on OS
  - github.com/saltstack-formulas/golang-formula
- AD Authentication
  - ldap protocol, will not be demoed but a config template is available
- Salt client API
  - code example: api_example_client.py
- Source code
  - github.com/saltstack/salt
  - find the test.ping function


### Not covered but can be found in salts documentation

- Exhaustive look at minion and master configuration files
- External pillars (consul, json api, many more)
- Orchestration
- Proxy minions
- Renderers (partly covered with Pyobjects)
- Salt cloud
- Salt mine (like grains, but more up-to-date)
- Salt ssh (agentless minions)
- Spm (salt package manager)
- Syndics
- Thorium
- Transport (tcp, raet, zeromq)
- Windows specificities (powershell, DSC)


# Prerequisites

- vagrant 1.9.7 (or greater)
- virtualbox 5 (or greater)


# Bootstrap

These scripts install salt and copies configuration files into their respective folders

```
  /bootstrap.sh
  /master.sh
  /minion.sh
```


# Usage

```bash
vagrant up
vagrant ssh master
sudo salt '*' test.ping # confirm minions respond

# Optional
sudo salt '*' state.highstate    # install rethinkdb and set up salt-api
sudo service salt-master restart # enable salt returner
sudo service salt-api restart    # enable salt-api configs
```
