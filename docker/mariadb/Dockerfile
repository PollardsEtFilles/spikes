FROM mariadb:5.5

MAINTAINER PEF <peter@pollardsetfilles.com>

WORKDIR /code/

#RUN ["/bin/bash", "-c", "set -o pipefail && mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root mysql"]

#RUN mysql -u root < "CREATE DATABASE "
RUN sed -i '/^\[mysqld\]/a\lower_case_table_names=1' /etc/mysql/my.cnf && \
    sed -i '/^\[mysqld\]/a\local-infile=1' /etc/mysql/my.cnf

