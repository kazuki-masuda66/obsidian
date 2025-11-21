# Chile Pricing - サーチャージと特殊ルール

## 概要
Chile Pricingにおけるサーチャージ（CVC、EPH、VJP、THD、CSSなど）の扱い方、特殊なルール、NOR対応などをまとめました。

## 内容

### サーチャージの種類

#### CVC (Chilean Port Surcharge)
- **特徴**: チリ特有のサーチャージ
- **設定方法**: 固定額で設定されることが多い
- **支払い**: BL内で支払い可能な場合がある
- **例**: 
  - Sparx: USD 95/100（特別設定）
  - Sparx: USD 80からUSD 100に更新（wrong cvc, was updated from 80usd to 100usd）
  - Sumitomo: Chilean PODは固定額で、BL内で支払い可能
  - 固定額として契約に含める

**注意点**:
- チリPODの場合は固定額で設定
- BL内で支払い可能な場合がある
- 顧客によって異なる設定

#### EPH (Equipment Positioning Surcharge)
- **適用条件**: 特定のPOL（例: THLCH）で必要
- **例**: Sumitomo Rubber Latin America
  - POL THLCHの場合、EPHとVJPを必須で含める
  - 契約はOFT + THD + fixed CVC only

#### VJP (Vessel Positioning Surcharge)
- **適用条件**: 特定のPOL（例: THLCH）で必要
- **例**: Sumitomo Rubber Latin America
  - POL THLCHの場合、EPHとVJPを必須で含める

#### THD (Terminal Handling Charge - Destination)
- **特徴**: 標準的なサーチャージ
- **用途**: ほとんどの契約に含まれる
- **例**: "All in subject to THD/CSS only"

#### CSS (Carrier Security Surcharge)
- **特徴**: 標準的なサーチャージ
- **用途**: ほとんどの契約に含まれる
- **例**: "All in subject to THD/CSS only"

#### OFT (Ocean Freight)
- **特徴**: 基本海上運賃
- **用途**: 契約の基本部分
- **例**: Sumitomo契約はOFT + THD + fixed CVC only

### サーチャージの設定ルール

#### 標準的なサーチャージ
- **THD/CSS**: 標準的なサーチャージ、ほとんどの契約に含まれる
- **設定方法**: "All in subject to THD/CSS only"と記載

#### チリ特有のサーチャージ
- **CVC**: チリ特有、固定額で設定
- **EPH/VJP**: 特定のPOLで必要

#### 特別なサーチャージ
- **Sparx**: CVC USD 95/100（特別設定）
- **顧客別**: 顧客によって異なる設定

### 特殊なルール

#### NOR (Not Otherwise Rated) 対応
- **特徴**: 標準レート表にない特殊なレート
- **用途**: 新規ルート、特殊な貨物
- **例**: Expeditors Chile
  - CNDLC - CLSAI, CLCNL USD 1,100/40NOR
  - CNDLC - CLSAI, CLCNL USD 1,300/40NOR（counter offer）
  - All in subject to THD/CSS only
  - Local charges not manifested by ONE
  - Valid: 15 Oct - 21 Oct（短期）
- **例**: Sparx Logistics Chile
  - USD 750/NOR（10-20 containers weekly、80% Chile / 20% Peru）
  - POL: BP ASIA、POD: CALLAO & SAN ANTONIO/VALPARAISO
  - Free time: 14 days at destination
  - 競合: Yang Ming USD 700/NOR
  - Valid: 26 Sep - 14 Oct 2025（短期）
- **例**: Industrias Cleaner
  - CNTAO & CNDLC - CLSAI USD 2,000/40NOR
  - Valid: 1/9/25 - 30/9/25
  - POD Free line detention days: 14 days
- **例**: Dorel Tender
  - NOR volume: 60% of 1,900 TEU = 1,140 TEU
  - Free time: 15 days for 40'NOR
- **例**: Eternity / NAC Emu
  - 17 NOR equipment
  - 18 daysから24 daysへの延長要求（6 additional free detention days）

**NOR対応のポイント**:
- 標準レート表にない特殊なレート
- 短期間の有効期限（例: 15 November to 31 November 2025）
- Free Timeは標準より短い場合がある（例: 14 days）

#### Free Timeの設定
- **標準**: 21 days
- **Falabella**: 14 days（特別）
- **NOR**: 14 days（例）
- **延長要望**: 原則押し返す

#### Local Charges
- **設定方法**: "Local charges not manifested by ONE, customers are to pay to the local offices accordingly"
- **用途**: 現地で発生する費用を顧客が直接支払う
- **例**: NOR対応、特殊なルート

### 契約構造の例

#### 標準的な契約
- **OFT**: 基本海上運賃
- **THD/CSS**: 標準的なサーチャージ
- **CVC**: チリ特有のサーチャージ（固定額）

#### 特殊な契約（Sumitomo）
- **OFT**: 基本海上運賃
- **THD**: Terminal Handling Charge
- **CVC**: 固定額
- **EPH/VJP**: POL THLCHの場合、必須で含める

#### NOR対応
- **基本レート**: NORレート
- **THD/CSS**: 標準的なサーチャージ
- **Local Charges**: 顧客が直接支払い

### サーチャージ設定のベストプラクティス

#### 1. 標準的なサーチャージを確認
- THD/CSSは標準的なサーチャージ
- ほとんどの契約に含まれる

#### 2. チリ特有のサーチャージを考慮
- CVCはチリ特有、固定額で設定
- 顧客によって異なる設定

#### 3. 特殊なPOLのサーチャージを確認
- EPH/VJPは特定のPOLで必要
- 契約条件を確認

#### 4. NOR対応の注意点
- 短期間の有効期限を設定
- Local Chargesを明記
- Free Timeを標準より短く設定する場合がある

### サーチャージ更新の処理

#### 更新リクエストの処理
- **Tigerシステム**: サーチャージ更新のリクエスト
- **承認・却下**: 契約条件を確認して判断
- **例**: SparxのCVCサーチャージ更新依頼が頻発

#### 更新時の注意点
- 契約条件を確認
- 固定額として設定されている場合は変更が困難
- 顧客との交渉が必要

## 次アクション
- [ ] [[20251121_Chile-Pricing-基本ルールとTigerシステム]]にリンク
- [ ] [[20251121_Chile-Pricing-主要顧客別ルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#chile #pricing #surcharges #cvc #eph #vjp #thd #css #nor #inbox

