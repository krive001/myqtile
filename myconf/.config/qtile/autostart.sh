#!/bin/sh

#pasystray &
#xcompmgr &
 
#pkill compton  &
pkill polkit-gnome-au &
pkill dunst &
pkill xcompmgr & 
pkill mpd &
# pkill gcsf &
# fusermount -u mount point

sleep 1
#compton -b -f  &
dunst &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
feh --bg-scale ~/.config/qtile/12.jpg &
(sleep 1 && xcompmgr) &
nm-applet &
mpd &
# gcsf mount mount point -ssome_session. &

