#https://repo.saltstack.com/#ubuntu
cp /vagrant/configs/minion.conf /etc/salt/minion.d/minion.conf
service salt-minion restart

cp /vagrant/configs/.bashrc /root/.bashrc
source /root/.bashrc
