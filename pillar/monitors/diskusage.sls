beacons:
  diskusage:
    - /: 99% # usage percentage, set to 1% to test
    - interval: 10

# salt '*' saltutil.sync_pillar

# look at _runners for diskwarning.py
# look at configs for reactor.conf
# look at pillars/monitors for diskusage.sls
