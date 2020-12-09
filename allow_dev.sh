#!/bin/bash

sudo usermod -a -G dialout "$(whoami)"
sudo chmod a+rw /dev/ttyACM0
