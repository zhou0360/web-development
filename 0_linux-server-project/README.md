**Description**

This Linux Server Configuration project was part of my [Full Stack Web Developer](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004) Nanodegree program at Udacity.

- **IP Address: ** 18.207.43.144

- **SSH Port: ** 2200

- **SSH Username: ** grader

- **URL: ** http://18.207.43.144.xip.io

**Summary**

**1.1 Create a Linux Server instance on AWS Lightsail**
- Create an account in [AWS Lightsail](https://lightsail.aws.amazon.com/)
- Choose Linux/Unix, OS Only and Ubuntu 16.04 LTS
- Under *Home* and *Networking*, create static IP
  - My static public address is **18.207.43.144**

**1.2 Create a DNS or URL for Linux Server**
- Under *Home* and *Networking*, create DNS zone
  - Using [xip.io](http://xip.io/), the DNS or URL for my public IP address is **18.207.43.144.xip.io**

    ![1-pic](/pics/1_DNS.png)

**1.3 SSH into Linux Server**
- Download the SSH Key or default private key, and move it to ``~/.ssh`` and rename it ``lightsail_key.rsa``

  ![2-pic](/pics/2_SSH-key.png)

- In your local terminal, type ``chmod 600 ~/.ssh/lightsail_key.rsa``

- Connect using SSH:
``ssh -i ~/.ssh/lightsail_key.rsa ubuntu@18.207.43.144``

**2.1 Security Setup: Port Number and UFW **

``sudo nano /etc/ssh/sshd_config``

- Change ``22`` to ``2200``
- Restart SSH: ``sudo service ssh restart``

```
sudo ufw status

sudo ufw default deny incoming  
sudo ufw default allow outgoing
sudo ufw allow 2200/tcp          
sudo ufw allow www               
sudo ufw allow 123/udp           
sudo ufw deny 22               

sudo ufw enable

```

**2.2 Security Setup: Firewalls on AWS Lightsail Instance**

- In your instance, go to *Manage*, *Networking*
- Under *Firewall* section, change to the following options:

  ![3-pic](/pics/3_Firewall.png)

**3.1 User Management: Give ``grader`` Access**

``sudo adduser grader``

- Create password and enter the information for ``grader``

``sudo visudo``

- Add the following line to give *sudo privilege* to ``grader``

- ``grader ALL=(ALL:ALL) ALL``

- Check if it works: ``sudo -l``

**3.2: User Management: Create SSH Key Login for ``grader``**

- On your local machine:
  - Type ``ssh-keygen``
  - Save and name the file: ``~/.ssh/grader_key``
  - Two files will be generated: ``grader_key`` and ``grader_key.pub``
  - ``cat ~/.ssh/grader_key.pub`` and copy the content


- On ``grader``'s virtual machine:
  - Type ``mkdir .ssh``
  - ``sudo nano ~/.ssh/authorized_keys`` and paste the content from ``grader_key.pub`` into this file
  - ``chmod 700 .ssh``
  - ``chmod 644 .ssh/authorized_keys``
  - ``nano /etc/ssh/sshd_config`` to check if ``PasswordAuthentication = NO``
  - Restart SSH: ``sudo service ssh restart``

- On your local machine:
  - ``ssh -i ~/.ssh/grader_key -p 2200 grader@18.207.43.144``


**4.1 App Deployment: Configure Apache2 for Python mod_wsgi**

``sudo apt-get install apache2``

- Check if Apache2 is working by visiting http://18.207.43.144; you should see the following:

  ![4-pic](/pics/4_Apache2.png)

``sudo apt-get install libapache2-mod-wsgi-py3``

- Note: this package has to match the Python version of your project

- ``sudo a2enmod wsgi`` to enable ``mod_wsgi``

**4.2 App Deployment: Configure PostgreSQL**

``sudo apt-get install postgresql``

- PostgreSQL should not allow remote connections. You should see the following by opening ``/etc/postgresql/9.5/main/pg_hba.conf``:
  ```
  local   all             postgres                                peer
  local   all             all                                     peer
  host    all             all             127.0.0.1/32            md5
  host    all             all             ::1/128                 md5
  ```

``sudo su - postgres``
- Create a PostgreSQL session in terminal: ``psql``

  ``
  postgres=# CREATE ROLE catalog WITH LOGIN PASSWORD 'catalog';
  postgres=# ALTER ROLE catalog CREATEDB;
  ``
  - Note the password for ``catalog`` is now 'catalog'

- Exit the PostgreSQL session: ``\q``

``sudo adduser catalog``
- Enter the same password created above 'catalog'

- ``sudo visudo`` and add the sudo privilege to this user:
  - ``catalog ALL=(ALL:ALL) ALL``

- Create a database named ``catalog``
  - ``createdb catalog``

- Exit the PostgreSQL session: ``\q``

**4.3 App Deployment: Configure Git**

- Login the virtual machine as ``grader``

```
mkdir /var/www/catalog

sudo git clone _your_item_catalog_project_.git catalog

sudo chown -R grader:grader catalog/

cd /var/www/catalog/catalog

```

- I made the following changes to my [Item Catalog Project](https://github.com/zhou0360/web-development/tree/master/1_item-catalog-project) in the local git repository:

  - Rename the ``project.py`` to ``__init__.py``, and at the bottom of the file:

    ```
    #app.debug = True
    #app.run(host="0.0.0.0", port=8000)
    app.run()
    ```
  - Replace the commented line with the following in related files:
    ```
    #engine = create_engine('sqlite:///PlatformAdProductwithusers.db')
    engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
    ```
  - Change the syntax to Python 3 in every ``.py`` file
  - Add the ``#!/usr/bin/env python3`` in the beginning of each ``.py`` file

**4.4 App Deployment: Google OAuth2.0 Authentication**

- Change the existing project credentials from ``localhost`` to the following:

  ![5-pic](/pics/5_GoogleOAuth2.png)

- Download and save the new JSON file in the ``/catalog`` folder and update the client ID and client secret key in the following files:
  - ``__init__.py``
  - ``templates/login.html``

**4.5 App Deployment: Python 3 Virtual Environment**

- Install the Python 3 virtual environment

```
sudo apt-get install python3-pip
sudo apt-get install python-virtualenv

cd /var/www/catalog/catalog/
sudo virtualenv -p python3 venv3

sudo chown -R grader:grader venv3/

. venv3/bin/activate

pip install httplib2
pip install requests
pip install --upgrade oauth2client
pip install sqlalchemy
pip install flask
sudo apt-get install libpq-dev
pip install psycopg2

python3 __init__.py

deactivate
```

- Enable a virtual host

```
sudo nano /etc/apache2/mods-enabled/wsgi.conf

# Add the following line
WSGIPythonPath /var/www/catalog/catalog/venv3/lib/python3.5/site-packages

------------------------------------------------------------

sudo nano /etc/apache2/sites-available/catalog.conf

# Add the following lines

``<VirtualHost *:80>
    ServerName 13.59.39.163
  ServerAlias ec2-13-59-39-163.us-west-2.compute.amazonaws.com
    WSGIScriptAlias / /var/www/catalog/catalog.wsgi
    <Directory /var/www/catalog/catalog/>
    	Order allow,deny
  	  Allow from all
    </Directory>
    Alias /static /var/www/catalog/catalog/static
    <Directory /var/www/catalog/catalog/static/>
  	  Order allow, deny
  	  Allow from all
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

------------------------------------------------------------
# Enable virtual host
sudo a2ensite catalog

# Reload Apache2
sudo service apache2 reload

```

**4.6 App Deployment: Set up Flask App**

```
sudo nano /var/www/catalog/catalog.wsgi

# Add the following lines:

activate_this = '/var/www/catalog/catalog/venv3/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/catalog/catalog/")
sys.path.insert(1, "/var/www/catalog/")

from catalog import app as application
application.secret_key = "Your_secret_key"

------------------------------------------------------------

# Restart Apache2
sudo service apache2 restart
```

**4.6 App Deployment: Set up database for the App**

```
sudo nano /var/www/catalog/catalog/AdProducts.py

# Add the following lines in the beginning
import sys
sys.path.insert(0, "/var/www/catalog/catalog/venv3/lib/python3.5/site-packages")
```

- Populate the database

```
# Activate python virtual environment
. venv3/bin/activate

# Populate the database
python database_setup.py
python AdProducts.py

deactivate
```

**4.7 App Deployment: Disable the default Apache site**

```
sudo a2dissite 000-default.conf
sudo service apache2 reload
```

**4.8 App Deployment: Launch the Web App**

```
sudo chown -R www-data:www-data catalog/
sudo service apache2 restart
```
- Now the web site is available at http://18.207.43.144 and http://18.207.43.144.xip.io.

- Home page:

  ![6-pic](/pics/6_HomePage.png)

**Resources**:

- [boisalai/udacity-linux-server-configuration](https://github.com/boisalai/udacity-linux-server-configuration)

- [Get Started on Lightsail](https://classroom.udacity.com/nanodegrees/nd004/parts/b2de4bd4-ef07-45b1-9f49-0e51e8f1336e/modules/56cf3482-b006-455c-8acd-26b37b6458d2/lessons/046c35ef-5bd2-4b56-83ba-a8143876165e/concepts/c4cbd3f2-9adb-45d4-8eaf-b5fc89cc606e)

- [Configuring Linux Web Servers](https://classroom.udacity.com/courses/ud299)


- [Python3 + venv + wsgi Implementation](https://github.com/jungleBadger/-nanodegree-linux-server-troubleshoot/tree/master/python3%2Bvenv%2Bwsgi)
