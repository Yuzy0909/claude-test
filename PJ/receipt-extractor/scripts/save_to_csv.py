#!/usr/bin/env python3
"""
領収書情報をCSVファイルに保存するスクリプト

ファイル名は「日付_取引先名_合計金額.csv」の形式で自動生成される。
例: 20260609_セブン-イレブン_671.csv

--output でディレクトリを指定できる（デフォルト: ~/Documents）。

使い方:
  python3 save_to_csv.py \
    --output ~/Documents \
    --date "2026年06月09日" \
    --supplier "セブン-イレブン" \
    --store "長泉中土狩店" \
    --address "静岡県駿東郡長泉町中土狩258-1" \
    --invoice "T9080102003059" \
    --tax8-excl 618 --tax8-tax 49 --tax8-incl 667 \
    --tax10-excl 4 --tax10-tax 0 --tax10-incl 4 \
    --total 671 \
    --note "冷しぶっかけとろろそば / ハジメ レモングラスティー 600ml" \
    --payment "PayPay（電子マネー）"
"""

import argparse
import csv
import os
import re
from datetime import datetime

HEADERS = [
    "日付",
    "取引先名",
    "店舗名",
    "住所",
    "インボイス登録番号",
    "8%対象_税抜金額",
    "8%対象_消費税額",
    "8%対象_税込金額",
    "10%対象_税抜金額",
    "10%対象_消費税額",
    "10%対象_税込金額",
    "合計税込金額",
    "備考",
    "支払い方法",
    "取込日時",
]


def parse_date(date_str):
    """「2026年06月09日」→「20260609」に変換する。変換できなければそのまま返す。"""
    m = re.search(r"(\d{4})年(\d{1,2})月(\d{1,2})日", date_str)
    if m:
        return f"{m.group(1)}{int(m.group(2)):02d}{int(m.group(3)):02d}"
    # 数字のみの場合はそのまま
    digits = re.sub(r"[^\d]", "", date_str)
    return digits if digits else date_str


def safe_filename(text):
    """ファイル名に使えない文字を除去する。"""
    return re.sub(r'[\\/:*?"<>|]', "", text)


def build_filename(date_str, supplier, total):
    date_part = parse_date(date_str) if date_str else "日付不明"
    supplier_part = safe_filename(supplier) if supplier else "取引先不明"
    total_part = safe_filename(total) if total else "金額不明"
    return f"{date_part}_{supplier_part}_{total_part}.csv"


def main():
    parser = argparse.ArgumentParser(description="領収書情報をCSVに保存する")
    parser.add_argument(
        "--output",
        default="~/Documents",
        help="保存先ディレクトリ（デフォルト: ~/Documents）",
    )
    parser.add_argument("--date", default="", help="日付")
    parser.add_argument("--supplier", default="", help="取引先名")
    parser.add_argument("--store", default="記載なし", help="店舗名")
    parser.add_argument("--address", default="記載なし", help="住所")
    parser.add_argument("--invoice", default="未登録業者", help="インボイス登録番号")
    parser.add_argument("--tax8-excl", default="", help="8pct対象 税抜金額")
    parser.add_argument("--tax8-tax", default="", help="8pct対象 消費税額")
    parser.add_argument("--tax8-incl", default="", help="8pct対象 税込金額")
    parser.add_argument("--tax10-excl", default="", help="10pct対象 税抜金額")
    parser.add_argument("--tax10-tax", default="", help="10pct対象 消費税額")
    parser.add_argument("--tax10-incl", default="", help="10pct対象 税込金額")
    parser.add_argument("--total", default="", help="合計税込金額")
    parser.add_argument("--note", default="", help="備考")
    parser.add_argument("--payment", default="", help="支払い方法")
    args = parser.parse_args()

    output_dir = os.path.expanduser(args.output)
    os.makedirs(output_dir, exist_ok=True)

    filename = build_filename(args.date, args.supplier, args.total)
    output_path = os.path.join(output_dir, filename)
    file_exists = os.path.isfile(output_path)

    row = [
        args.date,
        args.supplier,
        args.store,
        args.address,
        args.invoice,
        args.tax8_excl,
        args.tax8_tax,
        args.tax8_incl,
        args.tax10_excl,
        args.tax10_tax,
        args.tax10_incl,
        args.total,
        args.note,
        args.payment,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    ]

    with open(output_path, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(HEADERS)
        writer.writerow(row)

    print(f"✓ 書き込み完了: {output_path}")
    print(f"  {args.date} / {args.supplier} {args.store} / 合計¥{args.total}")


if __name__ == "__main__":
    main()
