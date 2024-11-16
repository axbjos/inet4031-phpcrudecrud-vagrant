# -*- mode: ruby -*-
# vi: set ft=ruby :

# Single Server LAMP Stack Running the PHP Crude CRUD Web Application
# See the GitHub repo for details

# Vagrant uses Ruby, so Ruby Do Loop...
Vagrant.configure("2") do |config|
  
  # UNCOMMENT THE BOX LINE APPROPRIATE FOR YOUR SYSTEM!!!
  #config.vm.box = "ubuntu/jammy64"
  config.vm.box = "bento/ubuntu-24.04"

  # For host only make sure you know what you are doing
  # This line is ONLY for Virtualbox Users.
  # Comment this line out if you are a VMware Fusion User.
  #config.vm.network "private_network", ip: "192.168.56.10"

  # Now move on to web server provisioning

  # Copy necessary files to the VM
  # This copies a simple file out to the webserver that can be used to verify PHP is working
  config.vm.provision "file", source: "phptest.php", destination: "phptest.php"

  # Now run a bunch of shell commands to get the web app in place
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y apache2
    apt-get install -y php libapache2-mod-php php-mysql
    systemctl restart apache2.service
    cp phptest.php /var/www/html

    echo "loading php web app"
    git clone https://github.com/axbjos/inet4031_phpcrudecrud_lamp.git
    cd inet4031_phpcrudecrud_lamp
    mv * /var/www/html
  SHELL

  # Now move on to database server provisioning

  # Stage the configurations files needed - make sure they are in your local directory for 
  # copying out to the VM
  # addusers.sql is a script file used to add the needed users to the MySQL database
  config.vm.provision "file", source: "addusers.sql", destination: "addusers.sql"
  #config.vm.provision "file", source: "50-server.cnf", destination: "50-server.cnf"

  # Now configure the database
  # These commands will install the MariaDB distribution of MySQL
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt install -y mariadb-server
    git clone https://github.com/datacharmer/test_db.git
    cd  test_db
    mysql -t < employees.sql
    cd ..
    # uncomment the next two if you want the DB accessible on all interfaces
    cp 50-server.cnf /etc/mysql/mariadb.conf.d/
    systemctl restart mariadb
    cd /home/vagrant
    echo "securing mysql and adding joeaxberg user"
    mysql -t < addusers.sql
    echo "done"
  SHELL

end
