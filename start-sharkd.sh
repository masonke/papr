#!/usr/bin/env bash
#
#######################################
## Make sure things run consistently ##
#######################################
export LANGUAGE=C
export LANG=C
export LC_MESSAGES=C
export LC_TIME=C

########################
## Script starts here ##
########################

if pgrep [s]harkd
then
  echo "Sharkd is already running"
else
  echo "sharkd is not running."
  echo 
  echo " "
  echo "Deleting the old socket file"
  if [[ -e /private/tmp/sharkd.sock ]] ; then
    rm /private/tmp/sharkd.sock
  fi
  echo "Starting sharkd"
  sharkd unix:/private/tmp/sharkd.sock
  pgrep [s]harkd
fi
 