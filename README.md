pm_vagrant
==========

Project Management Vagrant

It's easy to run this dev instance. Start by cloning this repo and its submodules (`git submodule update`), and installing [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/). Then, run `vagrant up`, sit back, and wait for provisioning to finish.

Once the VM is up, type `vagrant ssh` to get into the VM. Then, type `cd /vagrant` and `./start_django.sh` to start up the dev server.

You should now have a working dev instance you can access at `localhost:8000` in your browser.

Finally, you can suspend your vm with `vagrant suspend`, or shut it down entirely with `vagrant halt`.

The dev instance uses sqlite, and places the database at `/vagrant/dev.db` in the vm, or `dev.db` in the root of your clone of the repo. If the dev instance has issues booting, try deleting this file and re-creating the vagrant vm.

The full production instance is similar to the dev instance, but uses MySQL instead of SQLite, Solr instead of Whoosh, and adds Celery with RabbitMQ, all hosted by Apache with mod_wsgi.
