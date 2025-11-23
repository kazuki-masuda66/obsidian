---
title: ARCH CHEMICAL FY25 Pricing tool - レートフィルタリング処理
tags: [arch-chemical, pricing-tool, rate-filtering, lane-filtering, na-sales, wns-india]
created: 2025-11-22
---

# ARCH CHEMICAL FY25 Pricing tool - レートフィルタリング処理

## 概要
ARCH CHEMICAL FY25 Pricing toolにおけるレートフィルタリング処理。NAが興味のないレーンの除外と、4つのタブ（Quote Summary、Origin、Ocean、Destination）での一貫したフィルタリング。

## 背景情報

### 顧客情報
- **顧客名**: ARCH CHEMICAL
- **FY**: 2025
- **Sales Region**: North America (NA)
- **担当者**: Amanda Moskos (ONE Care Sales - Southern Region)

### フィルタリング要件
- **除外条件**: North Americaに触れないレーンを除外
- **対象タブ**: 4つのタブ全て（Quote Summary、Origin、Ocean、Destination）
- **フィルタリング方法**: "Please quote"と"Do not quote"で明示

## プロセス詳細

### 初回リクエスト（2024年11月11日）
- **リクエスト内容**: North Americaに触れないレーンを除外
- **問題**: Originタブのみフィルタリングされていた（78 lanes filtered）

### 修正リクエスト（2024年11月12日）
- **要求**: 4つのタブ全てでフィルタリング
- **対応**: WNS INチームが4つのタブ全てでフィルタリングを実施

### 最終確認（2024年11月13日）
- **確認内容**: 各タブのレーン数
  - Quote Summary: 77 Lanes
  - Origin: 76 Lanes
  - Ocean: 78 Lanes
  - Destination: 80 Lanes
- **確認者**: Sharon Tang (EAS Commercial, Service & Yield Management)
- **承認**: Amanda Moskosが確認・承認

## 実務ノウハウ

### フィルタリングの重要性
- **目的**: 不要なレーンのPricing tool作成を回避
- **効果**: 作業効率の向上とエラーの削減
- **注意点**: 全てのタブで一貫したフィルタリングが必要

### フィルタリング方法
1. **"Please quote"と"Do not quote"で明示**
   - 各レーンに明確な指示を付与
   - 4つのタブ全てで統一

2. **タブ間の整合性確認**
   - Quote Summary、Origin、Ocean、Destinationのレーン数を確認
   - 不一致がある場合は調整

### タイムライン管理
- **初回リクエスト**: 2024年11月11日 22:43
- **修正リクエスト**: 2024年11月12日 09:30
- **最終確認**: 2024年11月13日 01:54
- **処理期間**: 約2日

## 担当者連携

### Sales側
- **担当者**: Amanda Moskos
- **役割**: フィルタリング要件の明確化と最終確認

### WNS IN側
- **担当者**: Mahender (IN TenderSC)
- **役割**: 4つのタブ全てでのフィルタリング実施

### GHQ Eagle X側
- **担当者**: Sharon Tang、Cornelio Yuson、Benhur Dalumpines
- **役割**: プロセス確認とサポート

## 関連情報

### グループメールアドレス
- **IN TenderSC**: in.tendersc@one-line.com
- **GHQ EAGLEX PRICING SUPPORT**: ghq.eaglex.pricing.support@one-line.com
- **CST EAGLEX SUPPORT**: cst.eaglex.support@one-line.com
- **HK.GCSM.Tender**: hk.gcsm.tender@one-line.com

### 参考資料
- ARCH CHEMICAL 2025 (import) bid sheet
- フィルタリング済みファイル（4タブ全て）

## 次アクション
- [ ] フィルタリング済みファイルの最終確認
- [ ] Pricing tool作成プロセスの開始
- [ ] 他のテンダーでも同様のフィルタリングプロセスを適用

