# u_random_dummy_data

これは様々なフィールドのランダムダミーデータを生成するためのPythonアプリケーションです。

このアプリケーションでは以下のダミーデータを生成します：

- 名字（漢字）
- 名前（漢字）
- 名字（カタカナ）
- 名前（カタカナ）
- 郵便番号
- 住所1
- 住所2
- 住所3
- 電話番号
- 生年月日

## 使い方

### How to Use (from Distoribution)

1. First, install distoribution package
```shell
pip install u_random_dummy_data
```
2. Next, run script
```shell
u_random
```

### How to Use (from Source file)

1. First, Install [Rye](https://rye-up.com/)
2. Next, run script
```shell
rye sync
rye run u_random
```

これにより、ランダムなダミーデータの配列が作成されます。

#### Options

- `-u N` N個のダミーデータを作成します。デフォルト:1
- `-f [csv|tsv|json|yaml|scala]` 出力フォーマットの指定。デフォルト:csv

## 連絡

何か疑問点がある場合は issue を作成してください。
気が向いたら見ます。
