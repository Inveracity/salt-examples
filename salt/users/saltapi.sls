{% set apiuser = pillar['saltapi']['username'] %}
{% set apipassword = pillar['saltapi']['password'] %}

api user:
  user.present:
    - name: {{ apiuser }}
    - password: {{ apipassword}}
    - groups:
      - root

