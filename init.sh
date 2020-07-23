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

sudo ln -s ~/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/ask.py   /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart
