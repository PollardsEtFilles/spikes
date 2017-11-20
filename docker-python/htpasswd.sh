
mkdir -p ~/pypi
htpasswd -cb  ~/pypi/.htpasswd ${USER} docker
htpasswd -cb  ~/pypi/.htpasswd root docker
