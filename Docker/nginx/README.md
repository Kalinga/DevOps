Docker image stored at Docker hub (https://hub.docker.com/)
kalinga/nginx

Configuration used for nginx
	--prefix=/usr/share/nginx
	--conf-path=/etc/nginx/nginx.conf
	--http-log-path=/var/log/nginx/access.log
	--error-log-path=/var/log/nginx/error.log
	--lock-path=/var/lock/nginx.lock
	--pid-path=/run/nginx.pid
	--http-client-body-temp-path=/var/lib/nginx/body
	--http-fastcgi-temp-path=/var/lib/nginx/fastcgi
	--http-proxy-temp-path=/var/lib/nginx/proxy
	--http-scgi-temp-path=/var/lib/nginx/scgi
	--http-uwsgi-temp-path=/var/lib/nginx/uwsgi