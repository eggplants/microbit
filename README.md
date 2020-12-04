# これは何

- micro:bitを[`bbcmicrobit/micropython`](https://github.com/bbcmicrobit/micropython)で触る

## ハジメに

```bash
# On ubuntu
$ sudo usermod -a -G dialout eggplants
$ sudo chmod a+rw /dev/ttyACM0
```

## 便利なリンク

- BBC micro:bit MicroPython ドキュメンテーション
  - <https://microbit-micropython.readthedocs.io/ja/latest/index.html>
  - 本質情報

## 便利なコマンド

```bash
$ python -m pip install ufs yotta pipenv
$ ufs ls
$ pipenv --python 3.8
$ pipenv install mu-editor
$ LANG=C pipenv run mu-editor
```
