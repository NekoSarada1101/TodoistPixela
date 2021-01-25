# todoist-pixela

## 概要
昨日に完了したTodoistのタスク数をPixelaに登録する。

## 開発環境
* Python 3.8
* [Todoist Sync API](https://developer.todoist.com/sync/v8/)
* [Pixela API](https://pixe.la/ja)

## 使用方法
```
git clone https://github.com/NekoSarada1101/todoist-pixela.git
```
[settings.py](https://github.com/NekoSarada1101/todoist-pixela/blob/main/settings.py) の`TODOIST_TOKEN`、`PIXELA_TOKEN`、`PIXELA_URL`を自分のトークン、URLに書き換える

ディレクトリを移動し、実行する。
```
cd todoist-pixela
python main.py
```

## ライセンス
[MIT](https://github.com/NekoSarada1101/todoist-pixela/blob/main/LICENSE)
