#!/usr/bin/env bash

# Check what kind of file it is:
file serial

# Give execution permission and execute (only on linux system)
chmod +x serial
./serial

# Get a look inside
strings serial