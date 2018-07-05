base:
  '*':
    - admins
    - monitors.diskusage
    - mongodb

  'master':
    - saltapi
