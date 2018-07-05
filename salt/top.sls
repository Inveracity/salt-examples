base:
  '*':
    - users

  'master':
    - users.saltapi
    - rethinkdb.rethink-python

  'minion':
    - rethinkdb
    - nginx
    - golang
