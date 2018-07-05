testuser:
  user.present:
    - password: $1$jTydYI2E$fcJNfkvn4hV3xlkBsAHBe1 # "password"
    - groups:
      - root

{% for admin in pillar['admins'] %}
{{ admin }}:
  user.present:
    - password: $1$jTydYI2E$fcJNfkvn4hV3xlkBsAHBe1 # "password"
    - groups:
      - root
{% endfor %}
