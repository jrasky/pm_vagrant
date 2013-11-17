# Vagrant configuration file

Vagrant.configure("2") do |config|
  config.vm.box = "precise32"
  config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-i386-vagrant-disk1.box"
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.provision "shell", path: "pm_setup.sh"
end
