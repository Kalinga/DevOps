#/usr/bin/bash

# state of all active Vagrant environments on the system
vagrant destroy -f proj_vm

vagrant destroy -f dockerhost

vagrant global-status --prune

# shuts down the running machine Vagrant is managing.
# vagrant halt dockerhost
echo ""
echo $(pwd)
echo $(date)
echo ""
# start the VM using vagrantfile in the current directory
vagrant up

# takes changes in the vagrant file into consideration by provisioning
# this works after one time vagrant up is used
# vagrant reload --provision
echo ""
echo $(date)

cd dockerhost
echo $(pwd)

# Launch the other VM which host all docker containers
vagrant up

echo ""
echo $(date)

vagrant global-status