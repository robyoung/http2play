
machines = [
  {name: 'http1-server', ip: '192.88.1.10'},
  {name: 'http2-server', ip: '192.88.1.11'},
]

Vagrant.configure("2") do |config|
  config.vm.box = 'ubuntu/trusty64'

  machines.each do |machine|
    config.vm.define machine[:name] do |c|
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
    end
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = 'provisioning/playbook.yml'
  end
end
