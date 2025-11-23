---
title: Costco Bid Launch FY25 - 複数ファイル処理と特殊要件
tags: [costco, bid-launch, multiple-files, round1-filtering, freetime, ommc]
created: 2025-11-22
---

# Costco Bid Launch FY25 - 複数ファイル処理と特殊要件

## 概要
Costco FY25 Bid Launchにおける複数ファイル処理と特殊要件の管理。11,631レーンのうち2,857レーンのみをQuote対象とするフィルタリングと、Round 1処理の特殊要件。

## 背景情報

### 顧客情報
- **顧客名**: Costco
- **FY**: 2025
- **Sales Region**: North America
- **担当者**: Heidi Grabski (Sr. Key Account Executive, Global Customer Management)

### ファイル構成
- **総ファイル数**: 10ファイル
- **統合後**: 1つのワークシートに統合
- **総レーン数**: 11,631 lanes
- **Quote対象レーン数**: 2,857 lanes（CKAM指示に基づく）

## 特殊要件

### Round 1フィルタリング
- **条件**: "Round 1"列が"YES"の場合のみQuote
- **処理**: "Round 1"列がBLANKの場合はR1で提出しない（R2で提出）
- **影響**: 2,857 lanesのみがQuote対象

### 複数ファイル処理
- **統合方法**: 10ファイルを1つのワークシートに統合
- **追加列**: "ATTENTION TO PRICERS (REGIONAL REQUIREMENT)"列を追加
- **目的**: 特定の地域/ポートペアの特別指示をPricerに伝達

### Free Time処理
- **形式**: AS IS形式でリリース
- **配布**: Lead tradeに送信後、全Pricerに配布
- **Lead Trade割り当て**:
  - US/CA: TPEB
  - MX: LAWC EB
  - JP/KR/TW/CN: TPWB Dry/Reefer
  - AU/NZ: OCE SB
  - UK: AETWB / TAEB

## プロセス詳細

### Initial Check-in
- **提出日**: 2024年10月30日
- **処理**: OMMCがInitial Check-inを実施
- **確認事項**: 複数ファイルの統合可能性、Free Time処理方法

### T&C Summary
- **提出日**: 2024年11月2日
- **形式**: Eagle-X標準形式
- **制約**: 行数の追加不可（各要件の行数が固定）
- **対応**: 地域ごとの要件が異なる場合の処理方法を検討

### Conversion処理
- **提出予定日**: 2024年11月6日
- **処理内容**: 2,857 lanesのみをConversion
- **確認事項**: 
  1. 2,857 lanesのみのConversionが可能か
  2. Free TimeのAS IS形式でのリリースが可能か
  3. R1進行中の追加レーンリクエストへの対応
  4. Location確認待ちの処理方法

## 実務ノウハウ

### 複数ファイル統合
- **方法**: 10ファイルを1つのワークシートに統合
- **追加列**: "ATTENTION TO PRICERS (REGIONAL REQUIREMENT)"列を追加
- **メリット**: 1つのファイルで管理可能、Pricerへの指示が明確

### Round 1フィルタリング
- **条件**: "Round 1"列が"YES"の場合のみQuote
- **処理**: BLANKの場合はR1で提出しない
- **注意**: 全てのタブで一貫したフィルタリングが必要

### Free Time処理
- **形式**: AS IS形式でリリース
- **配布**: Lead tradeに送信後、全Pricerに配布
- **形式**: Heidi提供のWorking file形式を使用

### 追加レーンリクエスト対応
- **問題**: R1進行中にCostcoが追加レーンをリクエスト
- **対応**: PricerがPricing toolで新しいレーンを追加可能
- **処理**: TSTがConsolidation時に追加レーンを処理

### Location確認待ち対応
- **問題**: Location確認待ちのリストがある
- **対応**: 確認後にLocationとTrade mappingを調整
- **処理**: Re-conversionが必要な場合は、Pricerが再提出が必要

## 特殊指示

### Location Mapping
- **US/CA Place of Receipt**: SHENZHEN PORTS = Yantian
- **US Place of Delivery**: BELLEVILLE = VAN BUREN, MI
- **US Place of Delivery**: GOULDSBORO = Covington Township, PA
- **UK/TW/MX Place of Receipt**: SHENZHEN PORTS = ONE's direct South china port of call
- **CA/MX**: "REQUESTED DISCHARGE PORT"をPricer discharge port entryにコピー
- **AU**: Place of DeliveryがDOOR locationだが、PORT destination quoteを要求

### Transit Time
- **US/CA**: "Inland Transit Time (3) Port Of Discharge To Final Destination"にHeidiが指示するTransitを入力

### Counter対応
- **原則**: Counter不可
- **例外**: TAWBのみ許可（例: FelixstoweをSOUまたはLondon GatewayとしてQuote）

## タイムライン

### 主要マイルストーン
- **Initial Check-in**: 2024年10月30日
- **T&C Summary提出**: 2024年11月2日
- **Conversion提出予定**: 2024年11月6日
- **Merge file提出予定**: 2024年11月22日

### 処理期間
- **Conversion期間**: 約1週間
- **Pricing期間**: 約2週間
- **Consolidation期間**: 約1週間

## 担当者連携

### Sales側
- **担当者**: Heidi Grabski
- **役割**: 要件の明確化と最終確認

### OMMC側
- **担当者**: Analynne Garcia、Mychaela Denise Verches
- **役割**: Conversion処理とPricer連携

### GHQ Eagle X側
- **担当者**: Kazuki Masuda、Benhur Dalumpines
- **役割**: プロセス確認とサポート

## 関連情報

### 参考資料
- Costco Bid Launch Initial Check-in
- T&C Summary template
- Free Time Working file

## 次アクション
- [ ] 2,857 lanesのみのConversion確認
- [ ] Free TimeのAS IS形式でのリリース確認
- [ ] 追加レーンリクエスト対応プロセスの確立
- [ ] Location確認待ち対応プロセスの確立

