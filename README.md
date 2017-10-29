# capcityflyers.com

Yet another simple website powered by an over-engineered Django web applicalication.

# Requirements

- Python 3.6

# Setup

```
# Install python 3.6 on Ubuntu (Xenial does not have native packages)
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6


# Yeah... we're using MySQL for now.
> CREATE DATABASE ccf;
> GRANT ALL PRIVILEGES ON ccf.* TO 'ccf'@'localhost' IDENTIFIED BY 'somepassword';


# Add these to your .bashrc or .bash_profile
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='-p python3.6'
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv ccf

git clone https://github.com/dsilvers/capcityflyers.git capcityflyers.com
cd capcityflyers.com
pip install -r requirements.txt
./manage.py migrate
./manage.py collectstatic

# Nginx setup
cp etc/nginx_capcityflyers.com /etc/nginx/
/etc/init.d/nginx stop
letsencrypt certonly --cert-path /etc/letsencrypt/live --key-path /etc/letsencrypt/keys -d capcityflyers.com -d www.capcityflyers.com
/etc/init.d/nginx start

# Gunicorn setup
cp etc/ccf-gunicorn.service /etc/systemd/system/
systemctl enable ccf-gunicorn
systemctl start ccf-gunicorn
```