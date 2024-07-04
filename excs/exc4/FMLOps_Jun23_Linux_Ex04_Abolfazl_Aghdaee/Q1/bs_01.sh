#!/bin/bash


if [ -e /etc/shadow ]

 then
    echo "Shadow passwords are enabled."


    if [ -w /etc/shadow ]; then
        echo "You have permission to edit /etc/shadow."
    else
        echo "You do NOT have permission to edit /etc/shadow."
    fi
else
    echo "The file /etc/shadow does not exist."
fi

