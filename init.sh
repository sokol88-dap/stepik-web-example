# start nginx server
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# run gunicorn application server
gunicorn -b 0.0.0.0:8080 hello:app