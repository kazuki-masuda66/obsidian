# Ecuador Pricing - 特殊貨物とFree Time設定

## 概要
Ecuador Pricingにおける特殊貨物（NOR、Reefer、FR、OOG、Returning Shipmentなど）の対応方法、Free Time設定のルールをまとめました。

## 内容

### 特殊貨物の対応

#### 1. NOR（Not Otherwise Rated）
**重要性**:
- **EC NOR比率**: EC（エクアドル支店）の契約貨物の70%がNOR利用
- **目標**: 150 TEU/週を取るためにはNORを落とせない
- **主要顧客**: STARCARGOがNOR取扱全体の約60%

**ケース1: STARCARGO - 月次NORレート**
- **RFA**: GYEN00151A
- **レート設定**: 月次レート、市場動向を考慮
- **Base Port**: USD 800/40NOR（例: 11月最後の週）
- **例外レート**: 特定のbookingに例外レートを適用（例: IMPORTADORA ALVARADO）

**ケース2: MAVIJU - 月次NORレート**
- **RFA**: GYEB00130A
- **レート設定**: 月次レート、Rate Backdateリクエスト
- **Qingdao to ECGYE**: USD 1,100/40NOR

**NOR Free Time設定**:
- **標準**: CTOC 14 days / CTIC 21 days
- **延長**: 個別に判断（例: STARCARGOの19コンテナに対して5日間の追加Free Time）

#### 2. Reefer（冷凍コンテナ）
**ケース1: FARLETZA - Returning Shipment**
- **POL**: CNZHA（Zhanjiang）
- **POD**: ECGYE
- **コンテナ**: 40RH
- **貨物**: 冷凍エビ（Frozen shrimps）
- **レート設定**: Returning shipmentのレート設定
- **処理**: Ginger Rodriguez、Karen Camachoが担当

**ケース2: FARLETZA - Space Release**
- **Vessel**: ONE SPIRIT OITT2547E
- **B/L**: ONEYSZPFAH940300, ONEYTAOFL7207400
- **コンテナ**: 1x40RH
- **S/C**: GYE00176
- **処理**: Karen Camachoが担当、Isaac Yan、Maggie XieがSpace Release

**Reefer Free Time設定**:
- **標準**: CTOC 14 days / CTIC 21 days
- **延長**: 個別に判断

#### 3. FR（Flat Rack）
**ケース: LOGUNSA - HAKATA to ECGYE**
- **POL**: HAKATA
- **POD**: ECGYE
- **コンテナ**: 1x40 FR
- **貨物**: USED CONSTRUCTION MACHINE、USED CAT EXCAVATOR
- **寸法**: 9,460×2,800×3,010 mm
- **重量**: 20,300 KGS
- **レート設定**: OOG/FR貨物のレート設定
- **処理**: Yadira Morenoが担当

**FR対応**:
- OOG/FR貨物のため、適切なレート設定が必要
- Target VVDの確認が必要

#### 4. OOG（Out of Gauge - 重量超過・寸法超過）
**ケース: LOGUNSA - HAKATA to ECGYE**
- **コンテナ**: 1x40 FR
- **貨物**: USED CONSTRUCTION MACHINE、USED CAT EXCAVATOR
- **寸法**: 9,460×2,800×3,010 mm
- **重量**: 20,300 KGS
- **レート設定**: OOG/FR貨物のレート設定
- **処理**: Yadira Morenoが担当

**OOG対応**:
- OOG/FR貨物のため、適切なレート設定が必要
- Target VVDの確認が必要

#### 5. Returning Shipment（返送貨物）
**ケース: FARLETZA - CNZHA to ECGYE**
- **POL**: CNZHA（Zhanjiang）
- **POD**: ECGYE
- **コンテナ**: 40RH
- **貨物**: 冷凍エビ（Frozen shrimps）
- **レート設定**: Returning shipmentのレート設定
- **RFA**: GYE00176
- **処理**: Ginger Rodriguez、Karen Camachoが担当

**Returning Shipment対応**:
- 返送貨物のため、特別なレート設定が必要
- 冷凍エビなどの特殊貨物の場合は、適切なレート設定が必要

### Free Time設定のルール

#### 標準Free Time
- **CTOC（Container Terminal Out Charge）**: 14 days（Origin）
- **CTIC（Container Terminal In Charge）**: 21 days（Destination）
- **NOR**: 標準Free Timeと同じ
- **Reefer**: 標準Free Timeと同じ

#### Free Time延長のリクエスト

**STARCARGO - 19コンテナに対して5日間の追加Free Time**:
- **B/L**: TPEF68645500, TPEF62814400, TPEF72577400, TPEF73924800など、合計19コンテナ
- **RFA**: GYEN00151A
- **理由**: 税関手続きの遅延により、追加のFree Timeが必要
- **要求**: 5日間の追加Free Time
- **承認**: 理由が明確な場合、5日間の追加Free Timeを承認
- **DAR準備**: DARを準備して承認

**承認基準**:
- 税関手続きの遅延は顧客の責任ではない場合がある
- 理由が明確な場合は承認を検討
- Tier 1顧客として優先的に対応

#### Free Time設定の例

**STARCARGO**:
- **標準**: CTOC 14 days / CTIC 21 days
- **延長**: 19コンテナに対して5日間の追加Free Time（税関手続きの遅延）

**その他の顧客**:
- **標準**: CTOC 14 days / CTIC 21 days
- **延長**: 個別に判断

### 特殊貨物のベストプラクティス

#### 1. NOR貨物
- EC NOR比率70%を維持するため、NOR貨物を優先
- STARCARGOがNOR取扱全体の約60%を占める
- 月次レートを要求する顧客が多い

#### 2. Reefer貨物
- Returning shipmentの場合は、特別なレート設定が必要
- Space Releaseリクエストが多い
- 温度設定などを確認

#### 3. FR/OOG貨物
- OOG/FR貨物のため、適切なレート設定が必要
- Target VVDの確認が必要
- 寸法・重量を確認

#### 4. Returning Shipment
- 返送貨物のため、特別なレート設定が必要
- 冷凍エビなどの特殊貨物の場合は、適切なレート設定が必要

### Free Time設定のベストプラクティス

#### 1. 標準Free Timeを確認
- CTOC: 14 days（Origin）
- CTIC: 21 days（Destination）

#### 2. Free Time延長のリクエスト
- 理由が明確な場合は承認を検討
- 税関手続きの遅延は顧客の責任ではない場合がある
- Tier 1顧客として優先的に対応

#### 3. 特殊貨物のFree Time
- NOR、Reefer、FR/OOGとも標準Free Timeと同じ
- 延長が必要な場合は個別に判断

#### 4. DAR準備
- Free Time延長を承認した場合は、DARを準備して承認

## 次アクション
- [ ] [[20251121_Ecuador-Pricing-基本ルールとTigerシステム]]にリンク
- [ ] [[20251121_Ecuador-Pricing-主要顧客別ルール]]にリンク
- [ ] [[20251121_Ecuador-Pricing-DAR処理方法]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#ecuador #pricing #nor #reefer #fr #oog #returning-shipment #free-time #ctic #ctoc #inbox

