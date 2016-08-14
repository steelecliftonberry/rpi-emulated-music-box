#!/bin/sh

# call via cron:
# $ crontab -e
# @reboot /path/to/runbox.sh

sleep 15

cd /home/pi/git/rpi-emulated-music-box/

/home/pi/git/rpi-emulated-music-box/EmulatedMusicBox.py
