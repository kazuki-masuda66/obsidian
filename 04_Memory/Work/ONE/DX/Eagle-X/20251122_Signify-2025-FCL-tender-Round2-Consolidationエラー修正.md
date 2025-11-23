---
title: Signify 2025 FCL tender Round 2 - Consolidationエラー修正
tags: [signify, consolidation-error, pricer-submission, wns-india, tpeb-na]
created: 2025-11-22
---

# Signify 2025 FCL tender Round 2 - Consolidationエラー修正

## 概要
Signify 2025 FCL tender Round 2におけるConsolidationエラーの原因分析と修正プロセス。Pricer SubmissionとConsolidated Sheetの間でのデータ不一致問題。

## 背景情報

### 顧客情報
- **顧客名**: Signify (Philips Lighting)
- **FY**: 2025
- **Tender Type**: FCL tender
- **Round**: Round 2
- **Sales Region**: TPEB NA

### 問題の概要
- **発見日**: 2024年11月7日
- **問題**: Consolidated fileにPricer Submissionと異なるデータが含まれていた
- **影響**: 顧客から複数の問題点を指摘

## エラー詳細

### 問題のあるレーン例
- **APAC_NAM_1406_A**
- **APAC_NAM_1407_A**
- **APAC_NAM_1409_A**

### エラー内容
- **セクション**: "(e) Destination Haulage" (column AY through BB)
- **問題**: 数値が欠落し、大幅に低いレートを提示してしまった

### データ不一致の詳細
- **Pricer Submission**: Pricing toolから正しくエクスポートされたデータ
- **Consolidated Sheet**: WNS INが手動で操作した可能性があるデータ
- **差異**: Pricer Submissionのデータが正しく反映されていない

## 原因分析

### 調査結果
1. **Pricer Submission File**: 正しくデータがキャプチャされている
   - APAC_NAM_1406_A、APAC_NAM_1407_A、APAC_NAM_1409_AのDIHCが正しくCH-CI列に記録
   - 50-1と60-1も正しくDIHCがキャプチャされている

2. **Consolidation Tool**: ツール自体に問題はない
   - Consolidation toolは正しくデータをキャプチャ
   - ツールのエラーではない

3. **WNS INの手動操作**: 問題の原因
   - WNS INがCopy & Pasteの際に手動でデータを操作した可能性
   - 時間的制約（deadlineがタイト）により、正しいデータを使用しなかった

### 根本原因
- **Consolidation段階での手動操作**: WNS INがConsolidation toolからOriginal fileへのCopy & Pasteの際に、独自の判断でデータを変更
- **時間的制約**: Deadlineがタイトで、正しいデータを使用する時間がなかった

## 修正プロセス

### 対応方針
- **基本方針**: Pricer Submissionの純粋なコピーをConsolidated fileに反映
- **プロセス改善**: Consolidation processの適切な実施を確保

### 修正手順
1. **Pricer Submission Fileの確認**
   - 正しいデータが含まれていることを確認
   - DIHCなどの特殊項目も確認

2. **Consolidation Toolの再実行**
   - Consolidation toolを使用して正しいデータを生成
   - 手動操作を避ける

3. **最終確認**
   - Consolidated fileとPricer Submission fileの一致を確認
   - 顧客提出前に最終チェック

## 実務ノウハウ

### Consolidationプロセスの重要性
- **原則**: Pricer Submissionの純粋なコピーを使用
- **禁止**: 手動でのデータ操作や独自の判断による変更
- **確認**: Consolidated fileとPricer Submission fileの一致を必ず確認

### タイムライン管理
- **問題**: Deadlineがタイトな場合でも、正しいデータを使用する
- **対応**: 時間的制約がある場合は、事前にエスカレーション
- **改善**: Consolidation processに十分な時間を確保

### エラー防止策
1. **自動化の推進**: 手動操作を最小限に
2. **ダブルチェック**: Consolidated fileとPricer Submission fileの一致確認
3. **プロセス遵守**: Consolidation processの適切な実施

## 担当者連携

### TPEB NA側
- **担当者**: Kosuke Omori (Sr. Manager, Import Execution Marketing BCO)
- **役割**: 問題の発見とエスカレーション

### WNS IN側
- **担当者**: Feroz (IN TenderSC)
- **役割**: Consolidation処理の実施と修正

### GHQ Eagle X側
- **担当者**: Flourance Tan、Benhur Dalumpines、Kazuki Masuda
- **役割**: 問題の調査とプロセス改善

## 関連情報

### 参考資料
- Pricer Submission File
- Consolidated Customer Tender File
- Consolidation Tool documentation

## 次アクション
- [ ] Consolidation processの改善
- [ ] WNS INへのプロセス教育
- [ ] 自動化の推進
- [ ] エラー防止策の実施

