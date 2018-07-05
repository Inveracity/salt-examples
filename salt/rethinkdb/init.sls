{% set app_name       = 'rethinkdb'           %}
{% set data_directory = '/opt/rethinkdb' %}

rethinkdb-pkgrepo:
  pkgrepo.managed:
    - humanname: RethinkDB PPA
    - name: deb http://download.rethinkdb.com/apt {{ grains['oscodename'] }} main
    - file: /etc/apt/sources.list.d/rethinkdb.list
    - key_url: http://download.rethinkdb.com/apt/pubkey.gpg
    - require_in:
      - pkg: rethinkdb

rethinkdb-user:
  user.present:
    - name: rethinkdb
    - createhome: false
    - gid_from_name: true

install-rethinkdb:
  pkg.installed:
    - name: rethinkdb

data directory rethinkdb:
  file.directory:
    - name: {{ data_directory }}
    - user: rethinkdb
    - group: rethinkdb
    - mode: 755
    - makedirs: True

python-pip-rethinkdb:
  pkg.installed:
    - name: python-pip

rethinkdb-python-driver:
  pip.installed:
    - name: rethinkdb
    - require:
      - pkg: python-pip-rethinkdb

rethinkdb-chown-lib:
  file.directory:
    - name: /var/lib/rethinkdb
    - user: rethinkdb
    - group: rethinkdb
    - require:
      - pkg: rethinkdb

rethinkdb-config:
  file.managed:
    - name: /etc/rethinkdb/instances.d/{{ app_name }}.conf
    - source: salt://rethinkdb/rethinkdb.instance.conf
    - template: jinja
    - user: rethinkdb
    - group: rethinkdb
    - defaults:
        app_name: {{ app_name }}
        data_directory: {{ data_directory }}
    - require:
      - pkg: rethinkdb
      - user: rethinkdb
  cmd.wait:
    - name: /etc/init.d/rethinkdb restart
    - require:
      - file: rethinkdb-chown-lib
    - watch:
      - file: rethinkdb-config


# access webinterface
# http://192.168.56.3:28010
