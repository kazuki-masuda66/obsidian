---
title: Eagle-X DENSO レート不一致問題 - 実例と対策
tags: [eagle-x, denso, rate-discrepancy, consolidation-error, pricing-tool, ommc]
created: 2025-11-22
---

# Eagle-X DENSO レート不一致問題 - 実例と対策

## 概要
DENSO Round 2テンダーにおけるレート不一致問題の実例。Pricing ToolとConsolidated Sheetの間でレートが異なり、600TEU/年のビジネスを失った重大なインシデント。

## 問題の概要

### インシデント情報
- **顧客**: DENSO (G-JP100734)
- **Sequence**: seq01
- **Round**: R2
- **影響**: 600TEU/年のビジネス損失
- **発見日**: 2025年2月5日

### レート不一致の詳細

**Lane**: Nagoya - Mt Juliet, TN Door (DRY)

**Pricing Tool表示（OMMCがSalesに送信）**:
- USD 5,995/40ft + OBS

**Consolidated Sheet（Salesが確認）**:
- USD 7,395/40ft + OBS

**Pricer Submission File（実際の入力）**:
- USD 6,700/7,395/7,395 per 20'/40'/40'

**差異**: USD 1,400/40ft（約23%の差異）

## 問題の原因分析

### 調査結果
1. **Pricing Toolからのエクスポート**: 正しいデータ（USD 6,700/7,395/7,395）をエクスポート可能
2. **Consolidation段階でのエラー**: Consolidation段階で誤ったデータが使用された可能性

### 根本原因
- **Consolidationプロセスの問題**: Pricing ToolからConsolidated Sheetへのデータ転送時にエラーが発生
- **検証不足**: Consolidation後のデータ検証が不十分

## 対応プロセス

### 2025年2月5日 - 問題発見

**発見者**: Takumi Suzuki (JP Sales Chubu)

**報告内容**:
- OMMCとSalesの間でレート不一致を発見
- Consolidated SheetのColumn AZ lane#20で確認
- 600TEU/年のビジネス損失

### 2025年2月5日 - 緊急対応

**対応者**:
- Yang Elton Zhang (TP Marketing) - 2月6日にDENSOとのミーティング予定
- Koji Nakai (Eagle X Project) - BenとNikkoに調査依頼
- Flourance Tan (Eagle X Project) - データ確認

**対応内容**:
1. **即座の調査**: BenとNikkoに調査依頼
2. **他のレーンの確認**: Mt Juliet以外のレーンも確認が必要
3. **緊急ミーティング**: OMMC、EagleX、Sales、TP Marketingの合同ミーティングを設定

### 2025年2月5日 - データ確認

**Flourance Tanの確認結果**:
- **Customer Lane ID**: J020
- **ONE Lane ID**: 44
- **TP Domi-JP R2 Pricer Submission**: USD 6,700/7,395/7,395
- **TP Domi-JP R2 Pricing Tool working file**: USD 6,700/7,395/7,395

**問題点**:
- OMMCが参照している"USD 5,495/5,995/5,995"のPricing Toolが不明
- このPricing Toolの特定が必要

### 2025年2月5日 - OMMCからの情報

**Ada Buenaventura (OMMC TPEB Pricing Team)の報告**:
- **参照ファイル**: v18（最新版）
- **場所**: G:\Shared drives\GHQ TP Team Drive\Direct Tender Bid (CIF)\2025\JPN\ADA\EAGLE X\DENSO\R2
- **Pricing Tool rates**: USD 5,495/5,995/5,995 per 20'/40'/40'
- **Customer sheet rates**: USD 6,700/7,395/7,395 per 20'/40'/40'

## 対策と改善

### 即座の対策
1. **合同ミーティング**: OMMC、EagleX、Sales、TP Marketingの合同ミーティングで問題を特定
2. **他のレーンの確認**: 同様の問題がないか全レーンを確認
3. **データ検証プロセスの強化**: Consolidation後のデータ検証を強化

### 根本対策
1. **Consolidationプロセスの改善**: 
   - Pricing ToolからConsolidated Sheetへのデータ転送プロセスの見直し
   - 自動検証機能の追加

2. **検証プロセスの標準化**:
   - Consolidation後の必須検証項目の明確化
   - Sales、OMMC、Eagle Xの3者での検証

3. **データ整合性の確保**:
   - Pricing Tool working fileとConsolidated Sheetの100%整合性を確保
   - Pricer submission fileとConsolidated fileの整合性を確保

### 重要な原則
- **Consolidated fileは100% Pricer submission fileと一致する必要がある**
- **PricerがConsolidated fileで提供するオファーが100%正確でない限り、Salesは正しいオファーを提供できない**

## 実務ノウハウ

### レート不一致の防止策
1. **Pricing Toolの確認**: 
   - Pricer submission fileとPricing Tool working fileの整合性を確認
   - 最新版のファイルを参照

2. **Consolidation後の検証**:
   - Consolidated SheetとPricing Toolのデータを照合
   - 特に重要なレーン（高ボリューム、高価値）は重点的に確認

3. **3者検証**:
   - Sales、OMMC、Eagle Xの3者でデータを確認
   - 不一致が発見された場合、即座に報告

### 問題発見時の対応
1. **即座の報告**: 問題を発見したら即座に報告
2. **影響範囲の確認**: 同様の問題がないか全レーンを確認
3. **根本原因の調査**: データ転送プロセス全体を調査
4. **顧客への説明**: 必要に応じて顧客に説明・対応

## 関連リンク
- [[Eagle-X Consolidation Process]]
- [[Pricing Tool Workflow]]
- [[Tender Quality Control]]

## 次アクション
- [ ] 04_Memory/Work/ONE/DX/Eagle-X/に移動を検討
- [ ] Consolidation検証プロセスの標準化を検討
- [ ] レート不一致防止チェックリストの作成を検討

#inbox #eagle-x #denso #rate-discrepancy #quality-control #consolidation-error

