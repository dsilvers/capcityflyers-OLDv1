upstream ccf_server {
    # server unix:/home/ccf/gunicorn.sock fail_timeout=5;
    server 127.0.0.1:9002 fail_timeout=0;
}
server {
    listen 80;
    server_name capcityflyers.com www.capcityflyers.com;
    return 301 https://capcityflyers.com$request_uri;
}


server {
    listen 443 ssl;
    server_name capcityflyers.com www.capcityflyers.com;

        client_max_body_size 4G;

    access_log /var/log/nginx/capcityflyers.com.ssl.access.log;
    error_log /var/log/nginx/capcityflyers.com.ssl.error.log;

        ssl                  on;
        ssl_certificate      /etc/letsencrypt/live/capcityflyers.com/fullchain.pem;
        ssl_certificate_key  /etc/letsencrypt/live/capcityflyers.com/privkey.pem;
        keepalive_timeout    70;
        add_header           Front-End-Https    on;

    # path for static files
        root /home/ccf/capcityflyers.com/static/;


    location /static/ {
        alias   /webapps/hello_django/static/;
    }

    location /media/ {
        alias   /webapps/hello_django/media/;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        if (!-f $request_filename) {
            proxy_pass http://ccf_server;
            break;
        }
    }
}