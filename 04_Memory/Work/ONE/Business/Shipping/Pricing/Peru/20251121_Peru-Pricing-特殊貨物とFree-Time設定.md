# Peru Pricing - 特殊貨物とFree Time設定

## 概要
Peru Pricingにおける特殊貨物（Reefer、NOR、OOG、Fishmealなど）の対応方法、Free Time設定のルールをまとめました。

## 内容

### 特殊貨物の対応

#### 1. Reefer（冷凍コンテナ）
**ケース1: MARINASOL S.A. - KRPUS to PEPAI**
- **POL**: KRPUS
- **POD**: PEPAI
- **コンテナ**: 20RH
- **レート**: USD 2,400/20RH
- **Free Time**: 7 days free line detention at POD

**ケース2: NOATUM LOGISTICS - INNSA to PECLL**
- **POL**: INNSA
- **POD**: PECLL
- **コンテナ**: 40RH
- **レート**: USD 3,900/40RH
- **Free Time**: 7 days free line detention at POD

**Reefer Free Time設定**:
- **標準**: 7 days free line detention at POD
- **MRG freetimeに合わせる**: DMT ExceptionでFree Time延長を設定
- **注意点**: ペルー税関の手続き（ocean freight manifest必須）を考慮

#### 2. NOR（Not Otherwise Rated）
**ケース: LUMICENTER S.A.**
- **POL**: BP（Ningbo/Shanghai/Yantian/Shekou/Hong Kong/Pusan/Qingdao/Xiamen/Keelung）
- **POD**: PECLL
- **コンテナ**: 40NOR
- **レート**: USD 2,700/40NOR（例）、USD 3,000/40NOR（例）
- **Free Time**: 14 days free line detention at POD for NOR

**NOR Free Time設定**:
- **標準**: 14 days free line detention at POD for NOR
- **制限**: PE NORを抑制する必要がある
- **注意点**: ドラフト問題がある場合は慎重に判断

#### 3. OOG（Out of Gauge - 重量超過・寸法超過）
**ケース: ONBOARD LOGISTICS - Tokyo to Callao**
- **POL**: Tokyo（Chiba推奨）
- **POD**: Callao
- **コンテナ**: 1x20' OPEN TOP
- **貨物**: Conveyor belt（コンベアベルト）
- **寸法**: 2.06x1.85x2.06 M
- **重量**: 6,800 Kg
- **容積**: 7.851 M3

**OOG対応**:
- OPEN TOPコンテナを使用
- 適切なPOLを推奨（Chiba or Tokyo）
- レート設定は個別に確認

#### 4. Fishmeal（魚粉）
**ケース: PERU BROKER S.A.**
- **POL**: Callao
- **POD**: Shibushi（日本）
- **コンテナ**: 8x40'
- **特徴**: ペルーで2番目に重要なfishmeal顧客
- **レート**: Target USD 700/40'
- **期間**: 11月出荷

**Fishmeal対応**:
- 特殊貨物として扱う
- 日本からのレート動向を考慮
- キャンペーン残りの貨物に対応

#### 5. Frozen Cargo（冷凍貨物）
**ケース: FROZEN CARGO / ASIA - PAITA**
- **POL**: CNSHA
- **POD**: PEPAI
- **コンテナ**: D2
- **レート**: USD 1,800/D2

**Frozen Cargo対応**:
- PaitaへのAdd-onを考慮
- 冷凍コンテナが必要

### Free Time設定のルール

#### 標準Free Time
- **CTOC（Container Terminal Out Charge）**: 14 days（Origin）
- **CTIC（Container Terminal In Charge）**: 21 days（Destination）
- **NOR**: 14 days free line detention at POD
- **Reefer**: 7 days free line detention at POD

#### Free Time延長のリクエスト

**DMT Exception（運賃表例外）**:
- **目的**: MRG freetimeに合わせる
- **例**: MARINASOL S.A. - Reefer貨物のFree Time延長
- **処理**: TigerシステムでDMT Exceptionリクエストを作成

**承認基準**:
- 契約で合意されたFree Timeに合わせる
- 特殊貨物（Reeferなど）の場合は検討
- 個別に判断

#### Free Time設定の例

**GEODIS FORWARDING**:
- **CTOC**: 14 days（Origin）
- **CTIC**: 21 days（Destination）
- **契約**: 1年契約（1,000 TEUコミット）

**MARINASOL S.A.**:
- **Reefer**: 7 days free line detention at POD
- **延長**: DMT ExceptionでMRG freetimeに合わせる

**LUMICENTER S.A.**:
- **NOR**: 14 days free line detention at POD for NOR

### 特殊貨物のベストプラクティス

#### 1. Reefer貨物
- Free Timeは7 daysが標準
- MRG freetimeに合わせる場合はDMT Exceptionで設定
- ペルー税関の手続き（ocean freight manifest必須）を考慮

#### 2. NOR貨物
- Free Timeは14 daysが標準
- PE NORを抑制する必要がある
- ドラフト問題がある場合は慎重に判断

#### 3. OOG貨物
- OPEN TOPコンテナを使用
- 適切なPOLを推奨
- レート設定は個別に確認

#### 4. Fishmeal貨物
- 特殊貨物として扱う
- 日本からのレート動向を考慮
- キャンペーン残りの貨物に対応

### Free Time設定のベストプラクティス

#### 1. 標準Free Timeを確認
- CTOC: 14 days（Origin）
- CTIC: 21 days（Destination）
- NOR: 14 days
- Reefer: 7 days

#### 2. Free Time延長のリクエスト
- DMT ExceptionでMRG freetimeに合わせる
- 契約で合意されたFree Timeに合わせる
- 個別に判断

#### 3. 特殊貨物のFree Time
- Reefer: 7 daysが標準
- NOR: 14 daysが標準
- 延長が必要な場合はDMT Exceptionで設定

#### 4. ペルー税関の手続きを考慮
- BLにOFT（Ocean Freight）を含める必要がある
- manifestしない場合は税関から罰金が課される

## 次アクション
- [ ] [[20251121_Peru-Pricing-基本ルールとTigerシステム]]にリンク
- [ ] [[20251121_Peru-Pricing-主要顧客別ルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#peru #pricing #reefer #nor #oog #fishmeal #free-time #ctic #ctoc #inbox

