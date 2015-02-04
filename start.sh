cd /zreal/zrealty
bash start.sh
cd /geo/geo
uwsgi --socket :8009 --module geo.wsgi --emperor /etc/uwsgi/vassals --uid root --gid root --master --processes 4 --threads 2 --stats 127.0.0.1:9292 --daemonize=/var/www/vhosts/geo.zrealtycorp.com/logs/uwsg.log
