---
title: CM (Contribution Margin) 計算について - OPUS COA
tags: [cm, contribution-margin, opus, coa, pricing, calculation, variable-cost, fixed-cost]
created: 2025-11-22
source: 00_Memo/CM計算について　（営業本部共有用） (1).pptx
---

# CM (Contribution Margin) 計算について - OPUS COA

## 📚 概要

Contribution Margin（貢献利益）の計算方法について、OPUS COAモジュールを使用した実務的な説明資料（14スライド）。営業本部向けの共有資料。

## 🎯 CM計算の基本

### CMの定義
```
CM (Contribution Margin) = Revenue - Variable Cost
```

### Gross CMとFixed Cost
- **Gross CM**: Revenue - Variable Cost
- **Fixed Cost**: 変動しない固定費
- **Net Profit**: Gross CM - Fixed Cost

## 💰 Revenue（収益）の計算

### OPUS COAでのRevenue
- **OPUS**: BKG InquiryのCharge Tabに表示されるすべてのCharge
- **CM計算に含まれるもの**:
  - Base freight（基本運賃）
  - Inland haulage（内陸輸送費）
  - Manifested surcharge（マニフェスト記載のサーチャージ）

### CM計算に含まれないもの
- Non-manifested local charges（マニフェスト未記載のローカルチャージ）
- Demurrage Detention Charge（デマレッジ・デテンション料金）

## 📊 Variable Cost（変動費）の計算

### OPUS COAでのVariable Cost
- **Pricing Simulation**: 各BookingのRoutingに基づいて自動計算される
- **CM計算に含まれるもの**:
  - **TES**: Terminal cost（ターミナルコスト）
  - **TRS**: Transport cost（輸送コスト）
  - **EPP**: Empty Positioning Cost（空コンテナポジショニングコスト）
  - **Reefer Bunker consumption Cost**: 冷凍コンテナのバンカー消費コスト
  - **CM**: Agency Commission（エージェント手数料）

### その他のVariable Cost
- **Admin cost**: Office cost（オフィスコスト）
- **Container Capital cost**: コンテナ資本コスト
- **Vessel cost**: 船舶コスト
- **Voyage cost**: 航海コスト（Bunker、Port Charge、Canal Transit Charge）

## 🚢 COA（Contract of Affreightment）のCM計算

### COAの特徴
- **COAのCM計算**: コンテナ単位ではなく、全体のRevenueとVariable Costを計算
- **Fixed Cost**: COAのCM計算ではFixed Costは含まれない
- **Reefer**: Reefer Bunker consumption Cost（Frozen/Chilled）がVariable Costとして含まれる
- **Demurrage Detention**: CM計算には含まれない（Variable Costではない）
- **Storage cost**: Locationによって異なるが、AP UnitのCM計算には含まれない
- **Bunker**: Bunker costの変動はCMに影響するが、OBS（On Board）は含まれない

## 📈 P/L構造とUtilization

### CMとUtilizationの関係
- **CM = Freight Revenue - Variable Cost**
- **Utilization**: 船舶の稼働率
- **RevenueとVariable Cost**: Utilizationに比例して変動する
- **Fixed Cost**: Utilizationに関係なく固定

### グラフ表示
- **Utilization**: 0%から100%まで
- **Revenue**: Utilizationに比例して増加
- **Variable Cost**: Utilizationに比例して増加
- **CM**: Revenue - Variable Cost
- **Fixed Cost**: 一定

## 🔍 OPUS - Inquiry By Booking

### 機能概要
- **OPUS Inquiry by BKG**: 各Booking（Post shipment）のCM計算が可能
- **RevenueとVariable Cost**: 詳細な内訳を確認できる
- **Negative CM / Low CM cargo**: 詳細な内訳を確認して原因を分析
- **Pre shipmentとPost shipment**: 比較してPricing simulationで事前にCM levelとUtilizationを確認

### 使用方法
1. **Booking Number**: ブッキング番号を入力
2. **Route**: ルートを選択
3. **Cost Details**: コスト詳細を確認
4. **Remarks**: 各項目のRemarksを確認して詳細を把握

### 実例
- **BKG Number**: TYOCH6829700 (R5x1)
- **BKG Number**: TYOCF0141700 (D5x4 - D5x4のTTL Cost)

## 🎯 重要なポイント

### CM計算の原則
1. **Revenue**: Base freight、Inland haulage、Manifested surchargeを含む
2. **Variable Cost**: TES、TRS、EPP、Reefer Bunker consumption Cost、CMを含む
3. **Fixed Cost**: CM計算には含まれない（COAの場合）
4. **Utilization**: RevenueとVariable Costに影響する

### 実務での活用
- **Pre shipment**: Pricing simulationでCM levelを事前確認
- **Post shipment**: Inquiry by Bookingで実際のCMを確認
- **Negative CM / Low CM cargo**: 詳細な内訳を確認して原因を分析
- **Revenue向上**: Base freight、Inland haulage、Manifested surchargeの最適化
- **Variable Cost削減**: TES、TRS、EPP、Reefer Bunker consumption Costの最適化

## 🔗 関連リンク

- [[Eagle-X-Calculation-Logic-Formula-計算ロジックノウハウ]]
- [[OPUS-SPC-Standby-SOP-標準作業手順書]]
- [[Pricing-Management]]
- [[Contribution-Margin-Management]]

## 📝 備考

- この資料は営業本部向けのCM計算の共有資料
- OPUS COAモジュールを使用した実務的な説明
- Gross CMの最大化を目指すための重要な資料

