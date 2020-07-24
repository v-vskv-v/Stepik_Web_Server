if [ -e /etc/nginx/sites-enabled/test.conf ]
then
	sudo rm /etc/nginx/sites-enabled/test.conf
fi

if [ -e /etc/nginx/sites-enabled/default ]
then 
	sudo rm /etc/nginx/sites-enabled/default
fi

sudo ln -s ~/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

if [ -e /etc/gunicorn.d/test ]
then
	sudo rm /etc/gunicorn.d/test
fi

if [ -e /etc/gunicorn.d/ask ]
then
	sudo rm /etc/gunicorn.d/ask
fi

sudo ln -s ~/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/ask.conf   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start

mysql -uroot -e "create database if not exists qa"

sudo python3 ~/web/ask/manage.py syncdb
sudo python3 ~/web/ask/manage.py makemigrations
sudo python3 ~/web/ask/manage.py migrate
