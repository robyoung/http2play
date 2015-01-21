# HTTP/2 Playgrond

Play around with HTTP/1.1 and HTTP/2 (SPDY/3.1 at the moment) side by side.

## Dependencies

- [Vagrant](https://www.vagrantup.com)
- [VirtualBox](https://www.virtualbox.org)
- [Ansible](http://www.ansible.com/home) (installed as part of setup)
- [virtualenv](http://virtualenv.readthedocs.org/en/latest/) (recommended)

## Setup

- Create a virtualenv `virtualenv venv`
- Install python dependencies `pip install -r requirements.txt`
- Bring up the VMs `vagrant up`
- Update your `/etc/hosts` file with the following

```
192.88.1.10 http1-server-govuk-with-assets http1-server-govuk-no-assets http1-small-site
192.88.1.11 http2-server-govuk-with-assets http2-server-govuk-no-assets http2-small-site
```

## What you have

You should have two virtual machines serving up a few small static sites over TLS.

Site                                   | Protocol | Description
-------------------------------------- | -------- | -----------
https://http1-small-site               | HTTP/1.1 | A single basic HTML page
https://http1-server-govuk-no-assets   | HTTP/1.1 | The GOV.UK homepage with all assets served from their normal location
https://http1-server-govuk-with-assets | HTTP/1.1 | The GOV.UK homepage with all assets served from the same host
https://http2-small-site               | SPDY/3.1 | A single basic HTML page
https://http2-server-govuk-no-assets   | SPDY/3.1 | The GOV.UK homepage with all assets served from their normal location
https://http2-server-govuk-with-assets | SPDY/3.1 | The GOV.UK homepage with all assets served from the same host

## Copyright

All assets relating to GOV.UK pages (under `provisioning/roles/static-site/files`)
are covered by the [Crown Copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright/crown-copyright/).
