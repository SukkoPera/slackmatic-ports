if ! getent passwd nm-openvpn >/dev/null; then
    useradd -r -U -d / -c 'NetworkManager OpenVPN' -s /usr/bin/nologin nm-openvpn
fi
