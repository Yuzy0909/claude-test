---
name: char-count
description: テキストの文字数を4パターンでカウントするスキル。「文字数を数えて」「文字数カウント」「何文字？」「字数を教えて」「改行含む・含まない」「スペース含む・含まない」など、文字数・字数の計測を求める場面では必ずこのスキルを使うこと。テキストが提供されたとき、あるいはこれからテキストを入力すると言われたときも積極的に使用すること。
---

# 文字数カウントスキル

ユーザーが提供したテキストの文字数を、以下の4パターンで計測して報告する。

## カウントするパターン

| パターン | 改行 | スペース類 |
|---------|------|-----------|
| 1 | 含む | 含む（全文字カウント） |
| 2 | 含む | 除く |
| 3 | 除く | 含む |
| 4 | 除く | 除く |

**スペース類の定義：**
- 半角スペース（` `）
- 全角スペース（`　`）
- タブ文字（`\t`）

**改行の定義：**
- `\n`（LF）
- `\r\n`（CRLF）→ 2文字ではなく1文字として扱う
- `\r`（CR）

## 手順

1. ユーザーのテキストを受け取る（提供されていなければ入力を促す）
2. 以下のPythonスクリプトを実行してカウントする

```python
text = """ここにテキストを入れる"""

import re

# スペース類の正規表現（半角・全角・タブ）
space_pattern = r'[ \t　]'
# 改行の正規表現（\r\n を先にマッチさせて1文字扱いにする）
newline_pattern = r'\r\n|\r|\n'

def count_chars(t, remove_newlines=False, remove_spaces=False):
    if remove_newlines:
        t = re.sub(newline_pattern, '', t)
    if remove_spaces:
        t = re.sub(space_pattern, '', t)
    return len(t)

p1 = count_chars(text)
p2 = count_chars(text, remove_spaces=True)
p3 = count_chars(text, remove_newlines=True)
p4 = count_chars(text, remove_newlines=True, remove_spaces=True)

print(f"パターン1（改行含む・スペース含む）: {p1} 文字")
print(f"パターン2（改行含む・スペース除く）: {p2} 文字")
print(f"パターン3（改行除く・スペース含む）: {p3} 文字")
print(f"パターン4（改行除く・スペース除く）: {p4} 文字")

# 関数カウント（言語ごとのパターン）
func_patterns = [
    r'^\s*def\s+\w+\s*\(',          # Python
    r'^\s*function\s+\w+\s*\(',     # JavaScript/PHP (function宣言)
    r'^\s*(async\s+)?function\s+\w+\s*\(',  # JavaScript async
    r'^\s*(public|private|protected|static|async)[\s\w]*\s+\w+\s*\([^)]*\)\s*[\{]',  # Java/C#/Go
    r'^\s*func\s+\w+\s*\(',         # Go/Swift
    r'^\s*(fn|pub fn)\s+\w+\s*\(',  # Rust
    r'^\s*sub\s+\w+\s*[\(\{]',      # Ruby/Perl
]
combined = re.compile('|'.join(func_patterns), re.MULTILINE)
func_count = len(combined.findall(text))
if func_count > 0:
    print(f"関数の数: {func_count} 個")
```

3. 結果を以下のフォーマットで出力する

## 出力フォーマット

```
## 文字数カウント結果

| パターン | 条件 | 文字数 |
|---------|------|--------|
| 1 | 改行含む・スペース含む | X 文字 |
| 2 | 改行含む・スペース除く | X 文字 |
| 3 | 改行除く・スペース含む | X 文字 |
| 4 | 改行除く・スペース除く | X 文字 |

関数の数: X 個  ← 関数が1つ以上検出された場合のみ表示

※ スペースは半角・全角・タブを含みます
```

関数が0個の場合は「関数の数」行を出力しない。

## 注意事項

- `\r\n`（Windowsの改行）は2バイトだが**1文字**として数える。Pythonの `len()` はこれを2文字と数えるため、正規表現で `\r\n` を先にまとめて除去してから処理する。
- テキストが長い場合でもスクリプトで処理するので問題ない。
- ユーザーがテキストを貼り付けるまえに「どんな条件でカウントしますか？」などと聞く必要はない。テキストを受け取ったらすぐに4パターン全部を出力する。
