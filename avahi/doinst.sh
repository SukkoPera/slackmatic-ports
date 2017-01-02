if [ -x /usr/bin/update-desktop-database ]; then
  /usr/bin/update-desktop-database -q usr/share/applications >/dev/null 2>&1
fi

# Reload messagebus service
if [ -x etc/rc.d/rc.messagebus ]; then
  chroot . /etc/rc.d/rc.messagebus reload
fi

