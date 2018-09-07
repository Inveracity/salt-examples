#https://repo.saltstack.com/#ubuntu
apt-get install -y salt-master salt-api

sed -i "\$ainclude:\n\ \ - /vagrant/configs/*" /etc/salt/master

service salt-master restart

cp /vagrant/configs/.bashrc /root/.bashrc
source /root/.bashrc
