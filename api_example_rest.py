import requests

url    = 'http://192.168.56.2:8000'
TARGET = '*'
CREDS  = {'username': 'salt_api',
          'password': 'everythingisawesome',
          'eauth'   : 'pam'}

session = requests.Session()

def _send_payload(payload):
    login = session.post(url+'/login', json=CREDS)

    if not login.ok:
        raise Exception("error! could not authenticate! status code: {}".format(login.status_code))

    response = session.post(url, json=payload)

    if response.status_code != 200:
        raise Exception("error! salt api returned status code: {}".format(response.status_code))

    return response.json()

def salt_ping(): #return Boolean
    PAYLOAD = [{
        'client': 'local',
        'tgt'   : TARGET,
        'fun'   : 'test.ping'
    }]

    result = _send_payload(PAYLOAD)
    return result


result = salt_ping()
for r in result['return']:
    print(r)

# service salt-api restart

'''
curl -sSk http://localhost:8000/login \
    -H 'Accept: application/x-yaml' \
    -d username=salt_api \
    -d password=everythingisawesome \
    -d eauth=pam

curl -sSk http://localhost:8000 \
    -H 'Accept: application/x-yaml' \
    -H 'X-Auth-Token: a4da7c2bda10f8be99f6b6f4648b8ccc03e0792e'\
    -d client=local \
    -d tgt='*' \
    -d fun=test.ping
'''
