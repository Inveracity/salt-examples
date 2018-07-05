# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "master" do |dev|
    dev.vm.box = "ubuntu/xenial64"
    dev.vm.host_name = "master"
    dev.vm.network :private_network, ip: "192.168.56.2"
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "2048"]
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.customize ["modifyvm", :id, "--cpus", "2"]
        vb.linked_clone = true
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    config.vm.synced_folder ".", "/vagrant",
        type: "virtualbox",
        mount_options: ["dmode=775,fmode=775"]
    end
    config.vm.provision "shell", path: "bootstrap.sh"
    config.vm.provision "shell", path: "master.sh"
  end

  config.vm.define "minion" do |dev|
    dev.vm.box = "ubuntu/xenial64"
    dev.vm.host_name = "minion"
    dev.vm.network :private_network, ip: "192.168.56.3"
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "2048"]
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.customize ["modifyvm", :id, "--cpus", "2"]
        vb.linked_clone = true
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    config.vm.synced_folder ".", "/vagrant",
        type: "virtualbox",
        mount_options: ["dmode=775,fmode=775"]
    end
    config.vm.provision "shell", path: "bootstrap.sh"
    config.vm.provision "shell", path: "minion.sh"
  end

end
