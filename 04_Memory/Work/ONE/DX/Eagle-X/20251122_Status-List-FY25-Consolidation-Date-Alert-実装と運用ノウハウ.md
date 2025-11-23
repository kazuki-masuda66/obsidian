---
title: Status List FY25 - Consolidation Date Alert実装と運用ノウハウ
tags: [eagle-x, status-list, consolidation-date, alert, pricing-finalized]
created: 2025-11-22
source: ★スター付きメール抽出_Part4.md
---

# Status List FY25 - Consolidation Date Alert実装と運用ノウハウ

## 概要

FY25 Status Listにおいて、Consolidation dateが最後のOFT更新日（Pricing Finalized date）より早い場合のアラート表示機能について。

## 背景

- **日付**: 2024年6月28日 - 7月3日
- **発信者**: Haruka Kawata TPV (Conversion Team)
- **受信者**: Flourance Tan, Kazuki Masuda, Benhur Dalumpines
- **目的**: Consolidation dateとPricing Finalized dateの不一致を検知するアラート機能の実装

## 主要ポイント

### 1. アラートの目的

- **検知内容**: Consolidation dateが最後のOFT更新日（Pricing Finalized date）より早い場合
- **重要性**: Pricingが完了する前にConsolidationが設定されることを防止
- **運用上の課題**: Pricing完了前にConsolidationが設定されると、データの整合性に問題が生じる可能性

### 2. アラート表示の提案

#### Option 1: 詳細表示
- **Header Label**: "Pricers Late Submission"
- **Flag表示**: 
  - TP - Single Submission
  - TP/AE/EA - Multiple Submission
- **特徴**: どのPricerが遅れているかを詳細に表示

#### Option 2: シンプル表示
- **Header Label**: "Pricers Late Submission"
- **Flag表示**: Yes/No
- **特徴**: シンプルで分かりやすい表示

### 3. 実装の経緯

- **要望元**: Conversion Team（Benhur Dalumpines）
- **実装者**: Haruka Kawata TPV
- **確認者**: Flourance Tan, Kazuki Masuda
- **目的**: Pricing完了前にConsolidationが設定されることを防止

## 実務上の注意点

### 1. アラートの確認タイミング

- **Status List更新時**: Status Listを更新する際に、アラートを確認
- **Pricing完了時**: Pricingが完了した時点で、Consolidation dateとの整合性を確認
- **Consolidation設定時**: Consolidation dateを設定する際に、Pricing Finalized dateを確認

### 2. 対応フロー

1. **アラート検知**: Consolidation dateがPricing Finalized dateより早い場合、アラートが表示
2. **原因確認**: どのPricerが遅れているかを確認
3. **対応**: Pricing完了を待つか、Consolidation dateを調整
4. **再確認**: 対応後、アラートが解消されたことを確認

### 3. データ整合性の確保

- **Pricing完了の確認**: Pricing Finalized dateが設定されていることを確認
- **Consolidation設定**: Pricing完了後にConsolidation dateを設定
- **整合性チェック**: 定期的にConsolidation dateとPricing Finalized dateの整合性を確認

## 関連情報

- **システム**: Status List FY25 (v47)
- **対象**: 全Eagle Xアカウント
- **アラート表示**: "For Pricing check"列に表示
- **担当者**: 
  - Haruka Kawata TPV (実装)
  - Flourance Tan (確認)
  - Kazuki Masuda (確認)
  - Benhur Dalumpines (要望元)

## 今後の展開

1. **アラート表示の改善**: Option 1またはOption 2の選択、または両方の実装
2. **運用ルールの明確化**: アラートが表示された場合の対応ルールを明確化
3. **自動化の検討**: 将来的に自動的にConsolidation dateを調整する機能の検討

## 関連ファイル

- [[Eagle-X-Status-List-Management]]
- [[Pricing-Finalized-Date-Management]]
- [[Consolidation-Date-Management]]

