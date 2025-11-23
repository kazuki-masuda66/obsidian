# Eagle-X Calculation Logic Formula - 計算ロジックノウハウ

---
title: Eagle-X Calculation Logic Formula - 計算ロジックノウハウ
tags: [eagle-x, calculation-logic, formula, pricing, surcharges, base-freight]
created: 2025-11-22
---

## 概要
Eagle-X Pricing Toolにおける計算ロジックとフォーミュラに関するノウハウ。Base Freight、All In Calculation、Surchargeの扱い、6つのケーススタディを含む計算式をまとめた。

## ファイル情報
- **元ファイル**: `Calculation Logic (Eagle-X) Formula.xlsx`
- **形式**: Excelスプレッドシート（5シート）
- **シート名**: Image, Sheet1, Logic, Dummy Amount, Sheet2

## 計算式の基本構造

### 基本計算式
```
C (LT MRG or CUSTOMER) = PRISIM - LT MRG or CUSTOMER
F (ALL IN CALCULATION) = OFT + ARO + ARD + APPLICABLE SURCHARGES
H (BASE FREIGHT) = ALL IN CALCULATION - CUSTOMER APPLICABLE TO SURCHARGES
```

### 計算式の説明
- **C**: LT MRGまたはCUSTOMERのサーチャージ
- **F**: All In計算（OFT + ARO + ARD + 適用サーチャージ）
- **H**: Base Freight（All In計算から顧客適用サーチャージを差し引いたもの）

## ケーススタディ（Sheet1）

### Case 1: LT MRG = Subject to OBS, THL, THD
- **A (Base LT MRG)**: 20': 500, 40': 1000, HC': 1000
- **B (Surcharges)**:
  - OBS: 20': 60, 40': 120, HC': 120
  - THL: 20': 100, 40': 200, HC': 200
  - THD: 20': 80, 40': 160, HC': 160
- **D (All In)**: 20': 740, 40': 1480, HC': 1480
- **E (Base Rate)**: 20': 680, 40': 1360, HC': 1360
- **計算式**: D = A + B, E = D - C

### Case 2: Customer Request = Subject to OBS Only
- **A (Base LT MRG)**: 20': 500, 40': 1000, HC': 1000
- **B (Surcharges)**:
  - OBS: 20': 60, 40': 120, HC': 120
- **D (All In)**: 20': 560, 40': 1120, HC': 1120
- **E (Base Rate)**: 20': 500, 40': 1000, HC': 1000

### Case 3: Current Contract = Subject to OBS and THL Only
- **A (Base LT MRG)**: 20': 500, 40': 1000, HC': 1000
- **B (Surcharges)**:
  - OBS: 20': 60, 40': 120, HC': 120
  - THL: 20': 100, 40': 200, HC': 200
- **D (All In)**: 20': 660, 40': 1320, HC': 1320
- **E (Base Rate)**: 20': 600, 40': 1200, HC': 1200

### Case 4: Subject All = OBS, THL, THD, EES
- **A (Base LT MRG)**: 20': 500, 40': 1000, HC': 1000
- **B (Surcharges)**:
  - OBS: 20': 60, 40': 120, HC': 120
  - THL: 20': 100, 40': 200, HC': 200
  - THD: 20': 80, 40': 160, HC': 160
  - EES: 20': 65, 40': 130, HC': 130
- **D (All In)**: 20': 805, 40': 1610, HC': 1610
- **E (Base Rate)**: 20': 745, 40': 1490, HC': 1490

### Case 5: Customer Request = All In
- **A (Base LT MRG)**: 20': 500, 40': 1000, HC': 1000
- **B**: なし（All Inのため）
- **D (All In)**: 20': 500, 40': 1000, HC': 1000
- **E (Base Rate)**: 20': 440, 40': 880, HC': 880

### Case 6: Manual Input By Pricer
- **A (Base Manual Input)**: 20': 450, 40': 900, HC': 900
- **B (Surcharges)**:
  - OBS: 20': 60, 40': 120, HC': 120
  - THL: 20': 100, 40': 200, HC': 200
- **D (All In)**: 20': 690, 40': 1380, HC': 1380
- **E (Base Rate)**: 20': 530, 40': 1060, HC': 1060

## Logic Sheet - サーチャージロジック

### サービススコープ
- **Service Scope**: WEE
- **Surcharge**: All Auto Rating Surcharges
- **Sample Port Pair**: BEANR/SAJED
- **LT MRG OFT**: USD 800

### サーチャージの扱い

#### Subject/Fixedサーチャージ
- **OBS**: Subject/Fixed, 77
- **DOC**: Subject/Fixed, 50
- **XAF**: Subject/Fixed, 50
- **XDD**: Subject/Fixed, 50

#### Inclusiveサーチャージ
- **AMS**: Inclusive, 50
- **CMD**: Inclusive, 50
- **CML**: Inclusive, 50
- **CSC**: Inclusive, 50
- **CSS**: Inclusive, 50
- **CYR**: Inclusive, 50
- **DOF**: Inclusive, 50
- **DRP**: Inclusive, 50
- **ECA**: Inclusive, 50
- **FI**: Inclusive, 50
- **FO**: Inclusive, 50
- **HAZ**: Inclusive, 50
- **HEA**: Inclusive, 50
- **NEO**: Inclusive, 50
- **PCT**: Inclusive, 50
- **PSA**: Inclusive, 50
- **PSS**: Inclusive, 50
- **PUC**: Inclusive, 50
- **SCT**: Inclusive, 50
- **SLF**: Inclusive, 50
- **THD**: Inclusive, 50
- **THL**: Inclusive, 50

#### その他のサーチャージ
- **GAT**: 33
- **LLO**: 44
- **MBF**: 66
- **OCR**: 88

### All In Calculationのロジック
- **Default Displayed Surcharges**: Pricing Toolで表示されるデフォルトサーチャージ
- **Update Condition**: サーチャージの更新条件
- **Right Hand Side Surcharges**: All In計算に含まれるサーチャージ
- **New Column Inserted**: 新しい列が挿入されるかどうか
- **Benchmark Rate Offers**: ベンチマークレートオファーに使用されるかどうか
- **All In Calculation**: All In計算に含まれるかどうか

## Dummy Amount Sheet - ダミー金額

### サーチャージ別ダミー金額（USD）
- **標準サーチャージ**: 50 USD
- **GAT**: 33 USD
- **LLO**: 44 USD
- **MBF**: 66 USD
- **OBS**: 77 USD
- **OCR**: 88 USD

### サーチャージ一覧（65種類）
ADC, ADD, AHA, AMS, BSC, CAF, CCC, CCU, CFD, CGD, CMC, CMD, CML, CSC, CSS, CVC, CYR, DGS, DOC, DOF, DRP, ECA, EEC, EHL, EIS, ESD, FED, FGP, FI, FO, GAT, GOH, HAU, HAZ, HEA, HHA, IFL, INP, INS, LID, LLO, LOG, LOT, MBF, NEO, OCR, PCT, PSA, PSS, PUC, RMF, SCT, SLF, THD, THL, TSL, WHF, WHO, WRC, XAF, XCA, XDD, XDL

## Sheet2 - サーチャージグループ

### グループ1
CAF, THL, TSL, SCT, OBS, ECA, NEO

### グループ2
CSS, DOC, ECA, GAT, LLO, MBF, OBS, OCR, SCT, THL, TSL, XAF, XDD

### グループ3
OBS, AMS, DOF, THD

### グループ4
FGP, DOC

## 実務上のポイント

### Base Freight計算
- All In計算から顧客適用サーチャージを差し引いてBase Freightを計算
- 顧客のT&Cに応じて、Subject/FixedサーチャージとInclusiveサーチャージを適切に扱う

### All In Calculation
- OFT + ARO + ARD + 適用サーチャージで計算
- Pricing Toolで表示されるデフォルトサーチャージを基準に計算
- サーチャージの更新条件に応じて、All In計算に含めるかどうかを判断

### サーチャージの扱い
- **Subject/Fixed**: Base Rate計算に含まれる
- **Inclusive**: All In計算に含まれるが、Base Rate計算には含まれない
- **その他**: 個別のロジックに従って処理

### ケース別の計算方法
- Case 1-3: LT MRGベースの計算
- Case 4: Subject Allサーチャージを含む計算
- Case 5: All Inリクエストの場合
- Case 6: 手動入力の場合

## 次アクション
- [ ] 04_Memory/Work/ONE/DX/Eagle-X/に移動を検討
- [ ] 実際の計算例を追加
- [ ] サーチャージの詳細ロジックを確認

#inbox #eagle-x #calculation-logic #formula #pricing #surcharges #base-freight

