
machines = [
  {name: 'http1-server', ip: '192.88.1.10'},
  {name: 'http2-server', ip: '192.88.1.11'},
  {name: 'client', ip: '192.88.2.10'},
]


def get_box(machine)
  if machine[:name] == 'client'
    "box-cutter/ubuntu1404-desktop"
  else
    "ubuntu/trusty64"
  end
end


Vagrant.configure("2") do |config|

  machines.each do |machine|

    config.vm.define machine[:name] do |c|
      c.vm.box = get_box(machine)
      c.vm.hostname = machine[:name]
      c.vm.network :private_network, ip: machine[:ip], netmask: '255.255.255.0'

      c.vm.provider :virtualbox do |vb, override|
        if machine[:name] == 'client'
          vb.gui = true
        end

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
          "client" => ["client"],
        }
        ansible.playbook = 'provisioning/playbook.yml'
        ansible.sudo = true
      end
    end
  end

end
