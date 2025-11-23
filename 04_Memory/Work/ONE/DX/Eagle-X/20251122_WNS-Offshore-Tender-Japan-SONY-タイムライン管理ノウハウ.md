---
title: WNS Offshore Tender - Japan SONY タイムライン管理ノウハウ
tags: [wns, offshore-tender, japan, sony, timeline-management, eagle-x, as-is-process]
created: 2025-11-22
---

# WNS Offshore Tender - Japan SONY タイムライン管理ノウハウ

## 概要
日本向けWNS Offshore Tender処理におけるタイムライン管理の実務ノウハウ。SONYテンダーを中心とした歴史的データと、Eagle-X vs AS-ISプロセスの比較。

## 背景情報

### SONYテンダーのタイムライン要件
- **受領日**: 2024年12月2日（月）
- **内部Pricing Deadline**: 2024年12月6日（金） - 4営業日後
- **顧客提出期限**: 2024年12月11日（水） - 7営業日後
- **要求**: SONY形式での統合ファイル提出

### タイムライン（N+0からN+7）
```
N+0: Dec 2 (Mon) - Tender Release Date = Package receive from customer
N+1: Dec 3 (Tue) - Initial Checkin → WNS replies Eagle X T&C file to sales, Sales check contents
N+2~3: Dec 4 (Wed) ~ Dec 5 (Thu) - Conversion can be completed by WNS?
N+?: Dec - WNS sends Sales Review Request, Sales replies
N+?: Dec - Sales sends Return of Sales Review, WNS completes the Conversion, RFQ is sent to Pricers finally
N+4: Dec 6 (Fri) - Internal Pricing Deadline Date → Please send consolidated file to Sales, with SONY format
N+5~6: Dec 9 ~ Dec 10 - Sales needs to check the contents and amend
N+7: Dec 11 (Wed) - Customer Offer Deadline Date
```

## 歴史的データ分析

### SONYテンダー実績
| 受領日 | 担当者 | テンダー名 | Round | 受領からPricer Deadlineまでのカレンダー日数 | 国 | レーン数 | Pricer Deadline | Bid Deadline |
|--------|--------|------------|-------|--------------------------------------------|----|---------|----------------|--------------|
| 2022/12/20 14:31 | Ayano Arai | SONY | 1 | 6.1日 | Japan | 300 | 2022/12/26 17:00 | 2023/1/6 17:00 |
| 2023/12/1 18:50 | Eri Ohnishi | SONY | 1 | 6.9日 | Japan | 384 | 2023/12/8 17:00 | 2023/12/14 22:00 |

### その他日本テンダー実績
- **SUMITOMO CHEMICAL CO., LTD.**: 6.5日（Round 1, 1234 lanes）、3.1日（Round 2, 27 lanes）、5.4日（Round 3, 114 lanes）
- **TORAY INDUSTRIES**: 6.5日（TP, 128 lanes）、6.3日（Non TP, 194 lanes）
- **Yokohama Rubber**: 6.4日（1746 lanes）、5.1日（609 lanes）、8.1日（1047 lanes）

### 平均タイムライン
- **平均**: 受領からPricer Deadlineまで約6カレンダー日（約4営業日）
- **傾向**: レーン数が多いほどタイムラインが長くなる傾向

## Eagle-Xプロセス vs AS-ISプロセス

### Eagle-Xプロセス（推奨）
- **Conversion期間**: 約2日（複雑でない場合）
- **全体プロセス**: Sales + Offshore + Eagle X support + Pricersの連携
- **目標**: 10営業日（受領からPricer Deadlineまで）

### AS-ISプロセス（SONY用）
- **Draft Bid release準備**: 1営業日（最大2日、Salesからの確認が必要な場合）
- **Pricing期間**: 5営業日
- **Consolidation**: 1営業日（全てのPricing response + Remarks + Service情報の統合）
- **合計**: 約7営業日

### AS-ISプロセスの詳細
1. **Draft Bid release準備、Clarification or Confirmation from Sales & Bid Release to Pricers**
   - 1営業日（最大2日、Salesからの確認が必要な場合）

2. **Pricing teamsの対応時間**
   - 5営業日

3. **Consolidation**
   - 1営業日
   - 全てのPricing response + Remarks + Service情報の統合
   - Deadline後に遅れたPricer responseも、SalesにF2F discussionの時間が残っている場合は統合

## 実務ノウハウ

### 事前計画の重要性
- **推奨**: WNSとSalesの間で**事前計画**を実施
- **目的**: タイムラインの最適化と精度向上
- **実施**: TSTとSalesの間で実施（GHQ Eagle X teamの承認不要）

### タイムライン管理のポイント
1. **Conversion期間の短縮**
   - 複雑でないBidは2日で完了可能
   - Salesからの確認が必要な場合は最大2日

2. **Pricing期間の確保**
   - 最低5営業日を確保
   - レーン数が多い場合は余裕を持たせる

3. **Consolidationの効率化**
   - 1営業日で完了可能
   - 遅れたPricer responseも柔軟に対応

### エスカレーション基準
- **条件**: Eagle-Xを使用することでSalesが期限までに提出できない場合
- **対応**: GHQ Eagle X teamにエスカレーション

## 関連情報

### 担当者
- **WNS India**: Siva Rama Krishna Buddha (Siva)
- **WNS Philippines**: Pedro Retes
- **Japan SYM**: Yugo Fukai

### 参考資料
- SONY BID for FY25 Prechecking process
- Historical tender data (2022-2024)

## 次アクション
- [ ] SONYテンダーの事前計画プロセスを確立
- [ ] 他の日本テンダー（SUMITOMO、TORAY、Yokohama Rubber）のタイムラインも分析
- [ ] Eagle-XプロセスとAS-ISプロセスの使い分け基準を明確化

