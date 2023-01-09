#### 1. Install rosetta
```bash
/usr/sbin/softwareupdate --install-rosetta --agree-to-license
```	
#### 2. Install vagrant with homebrew
```bash
brew install --cask vagrant
```
#### 3. Create an account on vmware
[wmware homepage](https://customerconnect.vmware.com/)
	
#### 4. Download & Install VMWare Fusion Tech Preview
[VMWare Fusion Tech Preview download](https://customerconnect.vmware.com/downloads/get-download?downloadGroup=FUS-PUBTP-2021H1)

#### 5. Create link
```bash
ln -s /Applications/VMWare\ Fusion\ Tech\ Preview.app /Applications/VMWare\ Fusion.app
```
#### 6. Install vmware provider

[wmware vagrant provider](https://releases.hashicorp.com/vagrant-vmware-utility/1.0.21/vagrant-vmware-utility_1.0.21_x86_64.dmg)

#### 7. Install Plugin
```bash
vagrant plugin install vagrant-vmware-desktop
```
#### 8. Create folder vms/ubuntu,
```bash
cd
mkdir Documents/vms/ubuntu
cd Documents/vms/ubuntu
nano Vagrantfile
```
 
#### 9. Copy paste  below content in the Vagrantfile
```ruby  
Vagrant.configure("2") do |config|
  config.vm.box = "rethinc-oss/ubuntu-2204-arm64"
  config.vm.box_version = "20220819"
  config.vm.network "private_network", ip: "192.168.56.11"
  config.vm.provider "vmware_desktop" do |vmware|
    vmware.gui = true
    vmware.allowlist_verified = true
  end
end
```
	
#### 10. Bring up vm
```bash
Open terminal, Go to the folder where you created Vagrantfile & issue below command.
vagrant up
vagrant ssh
```
#### 11. Check IP address
```bash
sudo -i
ip addr show
```

#### 12. Exit from vm
```bash
exit
exit
vagrant halt
```

#### 13. Create folder vms/fedora
```bash
cd
mkdir Documents/vms/fedora
cd Documents/vms/fedora
nano Vagrantfile
```

- Copy paste  below content in the Vagrantfile
```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "jacobw/fedora35-arm64"
  config.vm.network "private_network", ip: "192.168.56.12"
  config.vm.provider "vmware_desktop" do |vmware|
    vmware.gui = true
    vmware.allowlist_verified = true
  end
end
```

#### 14. Bring up vm
Open terminal, Go to the folder where you created Vagrantfile & issue below command.
```bash
vagrant up
vagrant ssh
```
#### 15.  Check IP address
```bash
sudo -i
ip addr show
```

#### 16.  Exit from vm
```bash
exit
exit
vagrant halt
```