
```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6



pip install -r requirements.txt

cp etc/nginx_capcityflyers.com /etc/nginx/

systemctl load etc/ccf-gunicorn.service

/etc/init.d/nginx stop
letsencrypt certonly --cert-path /etc/letsencrypt/live --key-path /etc/letsencrypt/keys -d capcityflyers.com -d www.capcityflyers.com
/etc/init.d/nginx start

systemctl start ccf-gunicorn
```