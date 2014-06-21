environment
==============
make development environment. using ubuntu 14.04.

required
==============
* vagrant(1.4.3)
* ubuntu 14.04 LTS
* ansible(1.5.5)

#. install vagrant

go url http://www.vagrantup.com

#. start vagrant

```sh
vagrant up
```

* add ssh key

** using ssh-copy-id

```sh
ssh-kygen -t rsa
brew install ssh-copy-id
ssh-copy-id -i path/to/id_rsa.pub vagrant@192.168.100.100
```

* test ping
if ok, showen this.
```sh
ansible -i hosts 192.168.100.100 -m ping -vvvv
```

    192.168.100.100 | success >> {
        "changed": false,
        "ping": "pong"
    }

if failed, use `-vvvv` option(debug)

* play ansible

```sh
ansible-playbook -i hosts playbook.yml
```
