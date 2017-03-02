#### vagrant

vagrant init new_config absolute_location_of_the_box

Open the file Vagrantfile with an editor.
Add modifyvm statements as below to set the
memory (in MB) and the number of assigned CPUs.

    config.vm.provider "virtualbox" do |vb|
      # Don't boot with headless mode
      vb.gui = true
      # Use VBoxManage to customize the VM. For example to change memory:
      vb.customize ["modifyvm", :id, "--memory", "12288"]
      vb.customize ["modifyvm", :id, "--cpus", "4"]
    end

`vagrant up`

vagrant makes use of `virtualbox` so you must have it in `PATH` variable.


