#!/usr/bin/env bash
# For MacOs make sure gcc is installed
brew install gcc

# Have a virtual env for it
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv angr

# Install dependencies
CC=/usr/local/bin/gcc-8 UNICORN_QEMU_FLAGS="--python=/usr/bin/python " pip install unicorn  # Python 2 is probably /usr/bin/python on your macOS system
pip install angr

# Fix some stuff https://docs.angr.io/introductory-errata/install
PYVEX=`python3 -c 'import pyvex; print(pyvex.__path__[0])'`
UNICORN=`python3 -c 'import unicorn; print(unicorn.__path__[0])'`
ANGR=`python3 -c 'import angr; print(angr.__path__[0])'`

install_name_tool -change libunicorn.1.dylib "$UNICORN"/lib/libunicorn.dylib "$ANGR"/lib/angr_native.dylib
install_name_tool -change libpyvex.dylib "$PYVEX"/lib/libpyvex.dylib "$ANGR"/lib/angr_native.dylib