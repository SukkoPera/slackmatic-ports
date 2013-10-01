#!/bin/sh

function create_user_group () {
	local user group comment home shell

	user=$1
	group=$2
	comment=${3:-"User added for a daemon"}
	home=${4:-/tmp}
	shell=${5:-/bin/false}

	# Creare group, if needed
	if ! grep -q ^$group /etc/group
	then
		echo "Creating group $group"
		if ! groupadd $group
		then
                	echo "Error running groupadd, please do it manually!"
			exit 6
	        else
        	        echo "OK, done!"
	        fi
	else
        	echo "Group already exists"
	fi

	# Create user
	if ! grep -q $user /etc/passwd
	then
        	echo "Adding user $user"
	        if ! useradd -c "$comment" -g $group -d $home -s $shell $user
        	then
                	echo "Error running useradd, please do it manually!"
			exit 7
	        else
        	        echo "OK, done!"
	        fi
	else
        	echo "User already exists"
	fi
}

create_user_group privoxy privoxy "Privoxy daemon"
