# install base libraries
sudo apt update
sudo apt install python3.5
sudo apt-get install -y python3.5-dev
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install --upgrade pip
# sudo -H pip3 install --upgrade django==2.1
sudo -H pip3 install --upgrade gunicorn
# sudo python3 -m pip install mysqlclient

# for work with database
# sudo /etc/init.d/mysql start
# mysql -uroot -e "create database stepic_web;"
# mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate