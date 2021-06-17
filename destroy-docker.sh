#!/bin/bash

# VERSION
version='1.0'

# OUTPUT VARS
TERM=xterm
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
bold=`tput bold`
reset=`tput sgr0`

# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "${red}Please run as root: ${reset}${bold}sudo ./destroy-docker.sh${reset}"
  exit
fi

echo ""
echo "When proceeding, the explorer-api docker container and image ${red}will be deleted.${reset}"
echo ""

read -r -p "Continue? [y/N] " response
response=${response,,} # tolower
if [[ $response =~ ^(yes|y) ]]; then
  echo "Stopping Container..."
  docker container stop explorer-api

  echo "Removing Container..."
  docker container rm explorer-api

  echo "Removing image..."
  docker image rm blocklattice.org/explorer-api

  # Check errors
  if [ $? -ne 0 ]; then
    echo "${red}It seems errors were encountered. ${reset}"
    exit 2
  else
    echo "Done, destroyed."
  fi
  
else
  echo "Cancelled."
fi


