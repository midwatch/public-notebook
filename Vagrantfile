# -*- mode: ruby -*-
# vi: set ft=ruby :

HOME = ENV["HOME"]
DEV_CFG_ROOT = ENV["DEV_CFG_ROOT"]

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.ssh.forward_agent = true
  config.vm.hostname = "public-notebook"
  config.vm.provision "file", source: "#{HOME}/.gitconfig",
                              destination: ".gitconfig",
                              run: "always"
  config.vm.provision "file", source: "#{DEV_CFG_ROOT}/secrets/sro-public-notebook/invoke.yaml",
                              destination: ".invoke.yaml",
                              run: "always"
  config.vm.provision "file", source: "#{DEV_CFG_ROOT}/secrets/sro-public-notebook/key_file.json",
                              destination: "key_file.json",
                              run: "always"
  config.vm.provision "shell", path: "bin/vagrant_provision.sh"
  config.vm.provision "shell", path: "bin/vagrant_provision_user.sh", privileged: false
end
