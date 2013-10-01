#!/bin/sh

if [ ! -x /usr/sbin/upsdrvctl ] || [ ! -x /usr/sbin/upsd ]
then
	echo "NUT binaries not executable!"
	exit 1
fi

case "$1" in
start)
	/usr/sbin/upsdrvctl start
	/usr/sbin/upsd
	/usr/sbin/upsmon
	;;
stop)
	/usr/sbin/upsmon -c stop
	/usr/sbin/upsd -c stop
	/usr/sbin/upsdrvctl stop
	;;
*)
	echo "Usage: $0 [start|stop]"
	exit 1
	;;
esac

exit 0
