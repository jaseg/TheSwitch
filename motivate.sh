#!/bin/bash
export MPD_HOST=hyperblast.cbrp3.c-base.org
status=$(mpc|grep play)
mpc pause
ssh alien@hyperblast.cbrp3.c-base.org 'mplayer "/var/lib/mpd/music/audio/music/Charts ab 1956/1987/10 05. W03 Rick Astley - Never Gonna Give You Up.mp3"'
if [ -n "$status" ]
then
	mpc play
fi
