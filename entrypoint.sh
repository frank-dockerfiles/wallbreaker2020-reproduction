#!/bin/sh
service apache2 start
tail -F /var/log/apache2/access.log /var/log/apache2/error.log
