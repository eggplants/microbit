# What is this

- handle micro:bit with [`bbcmicrobit/micropython`](https://github.com/bbcmicrobit/micropython)

## First

```bash
# On ubuntu
$ sudo usermod -a -G dialout eggplants
$ sudo chmod a+rw /dev/ttyACM0
```

## Useful links

- BBC micro:bit MicroPython documentation
  - <https://microbit-micropython.readthedocs.io>
- ...

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
$ pipenv --python 3.9
$ pipenv install mu-editor
$ LANG=C pipenv run mu-editor
```
