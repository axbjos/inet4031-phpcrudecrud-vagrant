# Vagrant Automation for the PHP Crude CRUD App

## Background

This Vagrantfile will create a single server running the following (LAMP Stack):

- Ubuntu 24.04 Linux
- MariaDB distribution of MySQL
- Apache 2 Webserver
- PHP Programming Language and Modules

The Vagrant Box used to clone the VM is Bento's Ubuntu 24.04 that can be used on either x86 or ARM64 systems.

A sample 300,000 record "Employee" database will be uploaded to the DB (cloned from the datacharmer repo)

A sample PHP application that implements all CRUD operations in very Crude fashion: aka the PHP Crude CRUD App.

Please review the Vagrantfile for specific configuration details.

The end result should be a running server with everything working.  Simply navigate to the IP address in the Vagrantfile

---

## Prerequistites

### Intel Based Windows and Macs:

- Vagrant http://vagrantup.com
- Virtualbox http://virtualbox.org

### M1/M2/M3/M4 aka Apple Silicon Macs:

- VMware Fusion for Apple Silicon
- Vagrant
- Vagrant VMware Utility
- Vagrant VMware Provider

As of November 2024 Vagrant does not work with the Apple Silicon Version of VirtualBox (I can't get it to work anyway). The "bent" 24.04 cross-platform box, Vagrant, and VMware Fusion do seem to work.

Consult the Vagrant Documentation if Necessary

---

## Manual Install Alternative

Create your own Ubuntu Virtual Machine manually using whatever hypervisor you wish.

Then just run all the shell commands shown in the Vagrant file on your VM

## Docker

Look at my ------ repo for an example of how to containerize the app.

A ready to go app is also available on Dockhub.  Will add the pull link soon.

