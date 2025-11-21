# Peru-Pricing-特殊貨物とAP処理

## 概要
Peruにおける特殊貨物（NOR、Reefer、OOG、Flat Rackなど）のレート設定とAP（Allocation Plan）処理方法をまとめたノート。

## 内容

### NOR (Non-Operating Reefer)
- **定義**: 冷凍機能を使わない冷凍コンテナ（Dry cargo用）
- **需要**: 11月-1月のfresh cargo campaignで需要が高い
- **制約**: 
  - Week 44時点で800 TEUのPECLL NOR backlogがAsiaに存在
  - backlog解消までPECLL NOR bookingを停止
  - AP顧客でも週50ユニットにキャップ
- **レート例**:
  - BP-PECLL: USD 1,100/40NOR, USD 1,900/40NOR, USD 2,000/40NOR, USD 2,100/40NOR, USD 2,300/40NOR, USD 2,700/40NOR, USD 3,000/40NOR
  - CNROQ-PECLL: USD 1,800/40NOR, USD 2,400/40NOR
- **Free Time**: 14 days free line detention at POD
- **BP定義**: Ningbo/Shanghai/Yantian/Shekou/Hong Kong/Pusan/Qingdao/Xiamen/Keelung
- **制約理由**: Golden Week休暇中の過積載により、CallaoにNOR equipmentの大量サプライスが発生

### Reefer (RH)
- **用途**: 冷凍貨物
- **レート例**:
  - CNSHA-PEPAI: USD 1,800/D2
  - KRPUS-PEPAI: USD 3,000/40RH, USD 2,400/20RH
  - CNSHA-PECLL: USD 2,500/40RH
  - INNSA-PECLL: USD 3,900/40RH
- **Free Time**: 7 days free line detention at POD
- **ターゲット**: PE RH targetを達成しているため、追加のaggressive rateは設定しない

### OOG (Out of Gauge)
- **定義**: 標準コンテナサイズを超える貨物
- **種類**:
  - **OWOH**: Over Width & Over Height
  - **OH**: Over Height only
- **実例**: Infinity Logistic - 9 packages (6 OWOH, 3 OH)
- **レート**: FAK MRGを参照
- **VVD**: ターゲットVVDの確認が必要

### Flat Rack (FR)
- **用途**: 大型貨物、機械類
- **レート例**:
  - JPYOK-PECLL: USD 7,000/40FR(OH)
  - INNSA-PECLL: USD 12,950/40FR(OWOH)
- **Free Time**: 7 days DET F/T at POD; other Free time as per standard tariff

### Open Top (OT)
- **用途**: 上部から積み込む貨物
- **実例**: ONBOARD LOGISTICS - 1x20' OPEN TOP / TOKYO - CALLAO

### AP (Allocation Plan) 処理
- **目的**: 顧客にスペースを保証し、ボリュームを確保
- **AP顧客例**:
  - LUMICENTER S.A. (PE100756)
  - その他主要顧客
- **制約**: AP顧客でもNORは週50ユニットにキャップ
- **管理**: BSA (Booking Space Allocation) またはAP allocation内で管理

### 特殊貨物のレート設定基準
1. **市場競争力**: 競合他社のレートを考慮
2. **スペース制約**: equipment availability、backlog状況
3. **貨物タイプ**: NOR、Reefer、OOGなど貨物タイプに応じたレート設定
4. **季節要因**: fresh cargo campaignなど季節的な需要変動

### 特殊貨物の制約管理
- **NOR Backlog**: 800 TEUのbacklog解消までbooking停止
- **Equipment Imbalance**: Golden Week後のequipment surplusを解消
- **Draft Issues**: 重量貨物でdraft issuesが発生する場合、レート設定を調整

### 特殊貨物のFree Time設定
- **NOR**: 14 days free line detention at POD
- **Reefer**: 7 days free line detention at POD
- **OOG/Flat Rack**: 標準tariffに従う

## 次アクション
- [ ] NOR backlogの解消状況をモニタリング
- [ ] 特殊貨物のレート実績を更新
- [ ] AP顧客のパフォーマンスを追跡

#inbox #peru #pricing #special-cargo #NOR #reefer #OOG #AP

