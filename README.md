# What is this

- handle micro:bit with [`bbcmicrobit/micropython`](https://github.com/bbcmicrobit/micropython)

## First

```bash
# On ubuntu
$ sudo usermod -a -G dialout eggplants
$ sudo chmod a+rw /dev/ttyACM0
# OR,
$ chmod +x allow_dev.sh
$ ./allow_dev.sh
```

## Useful links

- BBC micro:bit MicroPython documentation
  - <https://microbit-micropython.readthedocs.io>
- Python Editor for micro:bit
  - <https://python.microbit.org/v/2.0>

## Useful commands

### ufs

- A command for handling microfs

```bash
# Install
$ pip install ufs

# With micro:bit connected to pc:

# Check files in micro:bit's microfs
$ ufs ls
# Remove a file in microfs
$ ufs rm sth.py
# Write local file into microfs
$ ufs put path/sth.py
# Download file from microfs
$ ufs get sth.py
```

### mu-editor

- GUI code editor for micropython

```bash
$ pip install pipenv
$ pipenv --python 3.7
$ pipenv install mu-editor
# not japanese but english
$ LANG=C pipenv run mu-editor
```

### picocom

- Connect to REPL through serial communication

```bash
$ sudo apt install picocom
$ picocom /dev/ttyACM0 -b 115200
```

### fritzing

- Designing Circuits IDE

```bash
$ sudo apt install fritzing
$ fritzing
```
