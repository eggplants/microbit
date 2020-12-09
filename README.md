# これは何

- micro:bitを[`bbcmicrobit/micropython`](https://github.com/bbcmicrobit/micropython)で触る

## ハジメに

```bash
# On ubuntu
$ sudo usermod -a -G dialout eggplants
$ sudo chmod a+rw /dev/ttyACM0
# OR,
$ chmod +x allow_dev.sh
$ ./allow_dev.sh
```

## 便利なリンク

- BBC micro:bit MicroPython ドキュメンテーション
  - <https://microbit-micropython.readthedocs.io/ja/latest/index.html>
  - 本質情報

## 便利なコマンド

```bash
$ python -m pip install ufs yotta pipenv
$ pipenv --python 3.8
$ pipenv install mu-editor
$ LANG=C pipenv run mu-editor
```

## ufs

- microfs

```bash
# micro:bitを接続した状態で

# 現在のmicrofs内ファイル確認
$ ufs ls
# 削除
$ ufs rm sth.py
# ローカルファイルをアップロード
$ ufs put path/sth.py
# デバイス内ファイルをダウンロード
$ ufs get sth.py
```
