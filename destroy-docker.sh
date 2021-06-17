# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "${red}Please run as root: ${reset}${bold}sudo ./destroy-docker.sh${reset}"
  exit
fi

docker container stop explorer-api
docker container rm explorer-api
docker image rm blocklattice.org/explorer-api
