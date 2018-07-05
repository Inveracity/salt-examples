#https://repo.saltstack.com/#ubuntu
wget -O - https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main" > /etc/apt/sources.list.d/saltstack.list
apt-get update
apt-get install -y salt-minion
apt-get install -y python-pip
python -m pip install -U pip
cp /vagrant/configs/minion.conf /etc/salt/minion.d/minion.conf
service salt-minion restart
