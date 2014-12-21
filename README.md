# HTTP/2 Playgrond

Play around with HTTP/1.1 and HTTP/2 (SPDY/3.1 at the moment) side by side.

## Get started

You will need [Vagrant](https://www.vagrantup.com), [VirtualBox](https://www.virtualbox.org)
and [Ansible](http://www.ansible.com/home). I would always recommend using a [virtualenv](http://virtualenv.readthedocs.org/en/latest/).

Then just `vagrant up`.

You should have one virtual machines serving up a small static site over TLS and
one desktop Ubuntu machine.

https://http1-small-site should be using HTTP/1.1

https://http2-small-site should be using SPDY/3.1


HELP:
https://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed
http://wiki.wireshark.org/SSL


