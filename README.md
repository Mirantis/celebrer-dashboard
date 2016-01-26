=================
Celebrer Dashboard
=================

Horizon plugin for Celebrer.

Setup Instructions
==================
This instruction assumes that Horizon is already installed and it's installation
folder is <horizon>. Detailed information on how to install Horizon can be
found at http://docs.openstack.org/developer/horizon/quickstart.html#setup.

The installation folder of Celebrer Dashboard will be referred to as <celebrer-dashboard>.

The following should get you started::

Clone the repository into your local OpenStack directory:

    $ git clone https://github.com/Mirantis/celebrer-dashboard.git

Install celebrer-dashboard

    $ sudo pip install -e <celebrer-dashboard>

and then

    $ cp -b <celebrer-dashboard>/_50_celebrer.py.example <horizon>/openstack_dashboard/local/enabled/_50_celebrer.py

When you're ready, you would need to either restart your apache:

    $ sudo service apache2 restart
