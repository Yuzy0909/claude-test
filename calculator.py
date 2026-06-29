"""
calculator.py - シンプルな電卓モジュール

四則演算・累乗・剰余・整数除算をサポートし、
ディスパッチテーブルを通じて統一的なインタフェースを提供する。
"""

from __future__ import annotations

Number = int | float


def _validate(a: object, b: object) -> tuple[Number, Number]:
    """a, b が数値型であることを検証し、(a, b) を返す。"""
    for name, val in (("a", a), ("b", b)):
        if not isinstance(val, (int, float)):
            raise TypeError(
                f"引数 '{name}' は int または float である必要があります。"
                f" (受け取った型: {type(val).__name__})"
            )
    return a, b  # type: ignore[return-value]


def add(a: Number, b: Number) -> Number:
    """a と b の和を返す。

    Args:
        a: 被加算数
        b: 加算数

    Returns:
        a + b の結果

    Raises:
        TypeError: a または b が数値型でない場合
    """
    a, b = _validate(a, b)
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """a から b を引いた差を返す。

    Args:
        a: 被減算数
        b: 減算数

    Returns:
        a - b の結果

    Raises:
        TypeError: a または b が数値型でない場合
    """
    a, b = _validate(a, b)
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """a と b の積を返す。

    Args:
        a: 被乗数
        b: 乗数

    Returns:
        a * b の結果

    Raises:
        TypeError: a または b が数値型でない場合
    """
    a, b = _validate(a, b)
    return a * b


def divide(a: Number, b: Number) -> float:
    """a を b で割った商を返す（浮動小数点除算）。

    Args:
        a: 被除数
        b: 除数（0 は不可）

    Returns:
        a / b の結果（float）

    Raises:
        TypeError: a または b が数値型でない場合
        ValueError: b が 0 の場合
    """
    a, b = _validate(a, b)
    if b == 0:
        raise ValueError("ゼロ除算はできません。")
    return a / b


def floor_divide(a: Number, b: Number) -> int:
    """a を b で割った整数商を返す（切り捨て除算）。

    Args:
        a: 被除数
        b: 除数（0 は不可）

    Returns:
        a // b の結果（int）

    Raises:
        TypeError: a または b が数値型でない場合
        ValueError: b が 0 の場合
    """
    a, b = _validate(a, b)
    if b == 0:
        raise ValueError("ゼロ除算はできません。")
    return int(a // b)


def modulo(a: Number, b: Number) -> Number:
    """a を b で割った余りを返す。

    Args:
        a: 被除数
        b: 除数（0 は不可）

    Returns:
        a % b の結果

    Raises:
        TypeError: a または b が数値型でない場合
        ValueError: b が 0 の場合
    """
    a, b = _validate(a, b)
    if b == 0:
        raise ValueError("ゼロ除算はできません。")
    return a % b


def power(base: Number, exp: Number) -> Number:
    """base の exp 乗を返す。

    Args:
        base: 底
        exp: 指数

    Returns:
        base ** exp の結果

    Raises:
        TypeError: base または exp が数値型でない場合
    """
    base, exp = _validate(base, exp)
    return base ** exp


# 演算子文字列 → 関数のディスパッチテーブル
_OPS: dict[str, object] = {
    "+":  add,
    "-":  subtract,
    "*":  multiply,
    "/":  divide,
    "//": floor_divide,
    "%":  modulo,
    "**": power,
}

SUPPORTED_OPERATORS: frozenset[str] = frozenset(_OPS)


def calculate(a: Number, operator: str, b: Number) -> Number:
    """演算子文字列を使って a と b を演算する統一インタフェース。

    Args:
        a: 左辺の数値
        operator: 演算子文字列。対応演算子: +, -, *, /, //, %, **
        b: 右辺の数値

    Returns:
        演算結果

    Raises:
        TypeError: a または b が数値型でない場合
        ValueError: operator が未対応、またはゼロ除算が発生した場合
    """
    if not isinstance(operator, str):
        raise TypeError(f"operator は str である必要があります。(受け取った型: {type(operator).__name__})")
    if operator not in _OPS:
        raise ValueError(
            f"未対応の演算子: '{operator}'. "
            f"対応演算子: {sorted(SUPPORTED_OPERATORS)}"
        )
    func = _OPS[operator]
    return func(a, b)  # type: ignore[operator]


if __name__ == "__main__":
    examples: list[tuple[Number, str, Number]] = [
        (10,  "+",  5),
        (10,  "-",  3),
        (4,   "*",  7),
        (20,  "/",  4),
        (20,  "//", 3),
        (20,  "%",  3),
        (2,   "**", 8),
    ]
    for a, op, b in examples:
        print(f"{a} {op} {b} = {calculate(a, op, b)}")
