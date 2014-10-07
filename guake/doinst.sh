#!/bin/sh

if [ -f /etc/gconf/schemas/guake.schemas ]; then
	export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
	gconftool-2 --makefile-install-rule /etc/gconf/schemas/guake.schemas > /dev/null
fi
