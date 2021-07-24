#!/usr/bin/env bash
# This only works in Bash 4.0 and above
# If you're using other shells or using Bash lower than 4.0, don't use the manager
# Instead, type out the commands one by one yourself
# Sorry for the inconvenience

error () {
  printf "\x1b[01;31merror\x1b[0m: $1\n"
}

info () {
  printf "\x1b[01;34minfo\x1b[0m: $1\n"
}

case "${1,,}" in
  serve)
    clear
    info "Locating Python..."
    export FLASK_ENV="development"
    command -v python >/dev/null 2>&1 && python server.py || error "Couldn't locate Python. Aborting..." ; exit 1
    ;;

  logo)
    clear
    info "Locating NodeJS..."
    command -v node >/dev/null 2>&1 && node png.js || error "Couldn't locate NodeJS. Aborting..." ; exit 1
    ;;

  *)
    error "Invalid option. Aborting..." ; exit 1
    ;;
esac