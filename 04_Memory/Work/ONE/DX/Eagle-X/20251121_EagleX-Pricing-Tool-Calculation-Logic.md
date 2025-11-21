# EagleX Pricing Tool - Calculation Logic

## 概要
EagleX Pricing Toolの計算ロジックに関する資料です。Pricing Toolの計算方法、ロジック、用語集、計算式について詳細にまとめました。

## 内容

### ファイル情報
- **元ファイル**: `Eagle X - Pricing Tool Calculation Logic.pptx`
- **形式**: PowerPointプレゼンテーション
- **作成日**: 2025年5月29日
- **場所**: 00_Memo内に保存されていた資料

### 計算ロジックの基本概念

#### 問題設定の例
**例題**: Macaronを販売する際、市場で最も安い価格に合わせたい場合、どのように計算・比較するか？

**比較例1: A or B?**
- Macaron A = SGD 12.75 subject to 12% GST, 5% Service Charge, SGD 2 Take Out Box
- Macaron B = SGD 17.00 Total

**比較例2: A or C?**
- Macaron A = SGD 12.75 subject to VAT, Service Charge, Platform Fee
- Macaron C = SGD 12.75 subject to GST, Service Charge, Take Out Box

### 用語集（Terminologies）

#### 基本用語
- **Customer's Request = Marketing/Pricer**
  - 顧客のT&C（Terms and Conditions）に基づいて定義されたレート構造
  - Set SurchargeとUpdate Conditionを使用して実行

- **LT MRG = Long Term Minimum Rate Guideline**
  - Trade Managementが設定した長期顧客向けの最小レートレベル

- **Target CM = Target Contribution Margin**
  - Trade Managementが設定した最小CMレベル
  - 長期顧客へのレートオファーはこのレベルに基づく

- **Current Contract = Agreed Rate Levels**
  - 顧客とONEの間で合意された特定の港ペアのレートレベル

- **Benchmark Rates = Baseline/Basis of Marketing/Pricing Offer**
  - Marketing/Pricingオファーの基準となるレート
  - LT MRG、Target CM、Current Contractに基づくことができる

- **Reference Base (Benchmark Rate Structure) = Surcharge Condition of Benchmark Rates**
  - Benchmark Ratesのサーチャージ条件

- **All In Calculation = Benchmark Rates + Benchmark Rate Structure (Subject)**
  - Benchmark RatesとBenchmark Rate Structureを合計したもの

- **Base Rate = Rate Level Marketing/Pricing intends to offer/export to customer/customer sheet**
  - Marketing/Pricingが顧客に提示・エクスポートするレートレベル
  - All In RatesからCustomer's Request Rate Structureを差し引いて計算

### 計算式

#### 基本計算式
- **A**: 基準値（Benchmark Rate）
- **B**: サーチャージ（Surcharge）
- **C**: 顧客リクエスト（Customer's Request）
- **D = A + B**: All In Calculation（基準レート + サーチャージ）
- **E = D - C**: Base Rate（All In Calculation - Customer's Request）

#### 計算の流れ
1. **A（Benchmark Rate）を設定**
   - LT MRG、Target CM、Current Contractから選択

2. **B（Surcharge）を追加**
   - Reference Base（Benchmark Rate Structure）を適用

3. **D = A + B（All In Calculation）を計算**
   - Apple to Apple比較のための総額

4. **C（Customer's Request）を確認**
   - 顧客のT&Cに基づくレート構造

5. **E = D - C（Base Rate）を計算**
   - 顧客に提示するレートレベル

### 計算ロジックの詳細

#### All In Calculationの重要性
- **目的**: Apple to Apple比較
- **方法**: Benchmark Rates + Benchmark Rate Structure（Subject）
- **用途**: 異なるレート構造を持つオファーを比較する際の基準

#### Base Rateの計算
- **目的**: 顧客に提示するレートレベル
- **方法**: All In Rates - Customer's Request Rate Structure
- **注意**: 顧客がAll Inしか求めていない場合でも、常にBase Rateまで計算する

### 関連資料
- [[20251121_EagleX-Pricing-Tool-FY25-SOP]]: EagleX Pricing ToolのSOP（Standard Operating Procedure）
- [[04_Memory/Work/ONE/DX/Eagle-X/20251118_Eagle-X-Pricing-tool説明-機能と使い方詳細.md]]: Eagle-X Pricing toolの詳細説明
- [[04_Memory/Work/ONE/Business/Shipping/20250113_Pricingのプロセス-運賃設定の方法と手順.md]]: Pricingのプロセス全体

### 確認事項
- [ ] 実際のPPTファイルを開いて詳細な図表を確認
- [ ] 計算例の詳細を確認
- [ ] 各TradeごとのBenchmark Rate設定方法を確認

## 次アクション
- [ ] 計算ロジックの詳細をMemory Noteに変換（[[04_Memory/Work/ONE/DX/EagleX/]]）
- [ ] 関連するSOP資料と統合
- [ ] 実際のPricing業務で使用する際の参考資料として活用

#eaglex #pricing-tool #calculation-logic #dx #inbox #cm #benchmark-rate #base-rate

