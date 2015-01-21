
machines = [
  {name: 'http1-server', ip: '192.88.1.10'},
  {name: 'http2-server', ip: '192.88.1.11'},
]


Vagrant.configure("2") do |config|

  machines.each do |machine|

    config.vm.define machine[:name] do |c|
      c.vm.box = "ubuntu/trusty64"
      c.vm.hostname = machine[:name]
      c.vm.network :private_network, ip: machine[:ip], netmask: '255.255.255.0'

      c.vm.provider :virtualbox do |vb, override|
        vb.customize [
          'modifyvm', :id,
          '--rtcuseutc', 'on',
          '--natdnsproxy1', 'on',
          '--natdnshostresolver1', 'on',
          '--name', machine[:name]]
      end

      c.vm.provision :ansible do |ansible|
        ansible.groups = {
          "server" => ["http1-server", "http2-server"],
        }
        ansible.playbook = 'provisioning/playbook.yml'
        ansible.sudo = true
      end
    end
  end

end
