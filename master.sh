#https://repo.saltstack.com/#ubuntu
apt-get install -y salt-master salt-api

cp /vagrant/configs/fileroots.conf /etc/salt/master.d/fileroots.conf
cp /vagrant/configs/reactor.conf /etc/salt/master.d/reactor.conf
cp /vagrant/configs/auth.conf /etc/salt/master.d/auth.conf
cp /vagrant/configs/api.conf /etc/salt/master.d/api.conf
cp /vagrant/configs/returner.conf /etc/salt/master.d/returner.conf
cp /vagrant/configs/gitfs.conf /etc/salt/master.d/gitfs.conf

service salt-master restart

cp /vagrant/configs/.bashrc /root/.bashrc
source /root/.bashrc
