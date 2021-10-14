# 課題

## 禁則事項
`test_main.py` を修正した場合、不正行為があったと見なされ本講義を含む今学期の全ての単位を失う可能性があります。

## 内容

1. `input_list` を入力とし、それを `numpy.ndarray` に変換して出力する関数 `list2ndarray` を実装せよ
   - `input_list` はリスト型のオブジェクトで、各要素は `int` または `float` 型と仮定する
1. `x_array`, `y_array` という二つの `numpy.ndarray` を入力とし、 `x_array` と `y_array` の差のl2ノルムを出力する関数 `dist` を実装せよ
   - `x_array`, `y_array` は `numpy.ndarray` 型のオブジェクトで、同じ系列長であると仮定する
1. `x_array` を入力とし、その一番はじめの要素と最後の要素を取り除いた `numpy.ndarray` を出力する関数 `extract` を実装せよ
   - `x_array` は `numpy.ndarray` 型のオブジェクトで系列長は3以上だと仮定する
1. `x_array` と `idx` を入力とし、`x_array` の `idx` 番目の要素を 0 に書き換える関数 `drop` を実装せよ
   - `x_array` は `numpy.ndarray` 型のオブジェクトであると仮定し、 `x_array` の系列長を L とする
   - `idx` は `int` 型のオブジェクトでかつ 0 以上 L - 1 以下の値をとると仮定する

## 実行環境の作り方
`pip3 install -r requirements.txt`

## 実行コマンド
`python3 test_main.py`
