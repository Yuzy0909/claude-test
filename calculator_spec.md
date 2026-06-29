# calculator.py

## 概要

基本的な四則演算および累乗計算を提供するシンプルな計算モジュール。個別の演算関数と、演算子文字列を使って統一的に計算を呼び出せるディスパッチ関数 `calculate` を備える。

## 対象ファイル

`/Users/you_mac/Documents/claude-test/calculator.py`

---

## 機能一覧

| 関数名 | 概要 |
|---|---|
| `add(a, b)` | 加算 |
| `subtract(a, b)` | 減算 |
| `multiply(a, b)` | 乗算 |
| `divide(a, b)` | 除算（ゼロ除算チェックあり） |
| `power(base, exp)` | 累乗 |
| `calculate(a, operator, b)` | 演算子文字列を受け取り対応する関数へディスパッチ |

---

## 詳細仕様

### add(a, b)

- **概要**: `a` と `b` の和を返す。
- **引数**:
  - `a` (数値): 左辺の値
  - `b` (数値): 右辺の値
- **戻り値**: (数値) `a + b` の結果
- **例外**: なし
- **使用例**:
  ```python
  add(3, 5)   # => 8
  add(1.5, 2) # => 3.5
  ```

---

### subtract(a, b)

- **概要**: `a` から `b` を引いた差を返す。
- **引数**:
  - `a` (数値): 左辺の値（被減数）
  - `b` (数値): 右辺の値（減数）
- **戻り値**: (数値) `a - b` の結果
- **例外**: なし
- **使用例**:
  ```python
  subtract(10, 3)  # => 7
  subtract(0, 5)   # => -5
  ```

---

### multiply(a, b)

- **概要**: `a` と `b` の積を返す。
- **引数**:
  - `a` (数値): 左辺の値
  - `b` (数値): 右辺の値
- **戻り値**: (数値) `a * b` の結果
- **例外**: なし
- **使用例**:
  ```python
  multiply(4, 7)   # => 28
  multiply(3, 0.5) # => 1.5
  ```

---

### divide(a, b)

- **概要**: `a` を `b` で割った商を返す。`b` がゼロの場合は例外を発生させる。
- **引数**:
  - `a` (数値): 被除数
  - `b` (数値): 除数
- **戻り値**: (float) `a / b` の結果
- **例外**:
  - `ValueError("Cannot divide by zero")` : `b == 0` のとき
- **使用例**:
  ```python
  divide(20, 4)  # => 5.0
  divide(7, 2)   # => 3.5
  divide(1, 0)   # => ValueError: Cannot divide by zero
  ```

---

### power(base, exp)

- **概要**: `base` の `exp` 乗を返す。
- **引数**:
  - `base` (数値): 底
  - `exp` (数値): 指数
- **戻り値**: (数値) `base ** exp` の結果
- **例外**: なし
- **注意**: 負の指数や小数の指数も Python の `**` 演算子の仕様に従い動作する。
- **使用例**:
  ```python
  power(2, 8)   # => 256
  power(3, 0)   # => 1
  power(4, 0.5) # => 2.0
  ```

---

### calculate(a, operator, b)

- **概要**: 演算子を表す文字列を受け取り、対応する演算関数へディスパッチして結果を返す。サポートされていない演算子が渡された場合は例外を発生させる。
- **引数**:
  - `a` (数値): 左辺の値
  - `operator` (str): 演算子を表す文字列。使用可能な値は下表を参照。
  - `b` (数値): 右辺の値
- **戻り値**: (数値) 演算結果
- **例外**:
  - `ValueError("Unsupported operator: <operator>")` : サポート外の演算子が渡されたとき
  - `ValueError("Cannot divide by zero")` : `operator == "/"` かつ `b == 0` のとき（`divide` 内で発生）

#### サポートされている演算子

| operator 文字列 | 対応する演算 | 対応関数 |
|---|---|---|
| `"+"` | 加算 | `add` |
| `"-"` | 減算 | `subtract` |
| `"*"` | 乗算 | `multiply` |
| `"/"` | 除算 | `divide` |
| `"**"` | 累乗 | `power` |

- **使用例**:
  ```python
  calculate(10, "+", 5)   # => 15
  calculate(10, "-", 3)   # => 7
  calculate(4,  "*", 7)   # => 28
  calculate(20, "/", 4)   # => 5.0
  calculate(2,  "**", 8)  # => 256
  calculate(5,  "%", 2)   # => ValueError: Unsupported operator: %
  ```

---

## スクリプトとして直接実行した場合の動作

`python calculator.py` として実行すると、以下の5件のサンプル計算結果を標準出力へ表示する。

```
10 + 5 = 15
10 - 3 = 7
4 * 7 = 28
20 / 4 = 5.0
2 ** 8 = 256
```

---

## 注意事項

- 各関数の引数 `a`, `b` に型チェックは実装されていない。数値型（`int` / `float`）以外を渡した場合の動作は Python の演算子仕様に依存する。
- `divide` のゼロ除算チェックは `b == 0` の厳密等価のみ。浮動小数点演算の精度によって `b` が極めて 0 に近い値でも例外は発生しない点に注意する。
- `power` 関数は `calculate` から `"**"` 演算子で呼び出す際、`base` と `exp` の順に引数が渡される。

---

## 使用例（モジュールとしてインポートする場合）

```python
from calculator import add, divide, calculate

# 個別関数を直接呼び出す
result = add(100, 200)        # 300

# calculate 経由で統一的に呼び出す
result = calculate(9, "**", 2)  # 81
```
