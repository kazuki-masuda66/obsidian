# Chile Pricing - 基本ルールとTigerシステム

## 概要
Chile Pricingにおける基本ルールとTigerシステムを使ったレート修正リクエストの処理方法についてまとめました。チリ特有のルールや運用方法を含みます。

## 内容

### Tigerシステム - レート修正リクエストの処理

#### 基本的な流れ
1. **Tiger通知の受信**
   - `tigeradmin@one-line.com` からレート修正リクエストの通知が届く
   - チリチーム（Paula, Esmeralda, Belen, Loreto, Macarena, Carolina, Leandroなど）からのリクエスト
   - 通知には顧客名、RFA番号、理由、詳細が含まれる

2. **リクエスト内容の確認**
   - Tigerのリンクから詳細を確認
   - 顧客の要望内容を理解
   - 既存契約との整合性を確認

3. **承認・却下の判断**
   - Game Plan比率（70% FAK / 30% NAC）を確認
   - 採算性（CM/TEU）を確認
   - チリ特有のルールを考慮

#### よくあるリクエストパターン

**パターン1: レート修正（Rate Amendment）**
- 顧客からの値下げ要求
- ボリューム増加に伴うレート調整
- 期間延長のリクエスト

**パターン2: DMT Exception（運賃表例外）**
- 標準運賃表から外れた特別レート
- 新規顧客向けの特別条件

**パターン3: サーチャージ追加・修正**
- CVCサーチャージの追加・修正
- EPH、VJPなどの追加
- 特別サーチャージの設定

### Chile Pricingの基本ルール

#### Game Plan比率
- **基本指針**: **70% FAK / 30% NAC**
- 超過例: Sparx（55%/45%）- これは例外として許容済み
- 追加NAC要求時の牽制材料として使用

#### レート設定のベンチマーク
- Little Oceanよりは高めに設定
- NPRC N・Ecuador NIRを併用ベンチマーク
- スペース逼迫時のアドホック依頼は原則FAK水準で回答

#### Free Time（無料期間）
- **標準**: 21 days
- **Falabella**: 14 days（特別）
- **NOR**: 14 days（例: Expeditors Chile）
- **DAR処理**: 10 days（例: Capital Logistics）
- **Dorel**: 21 days（DRY）、15 days（40'NOR）
- **Empresas Demaria**: 14 days（DG）、21 days（dry）
- **延長要望**: 原則押し返す
- **特別なケース**: 個別対応

#### DND割引権限
- **Adele**: USD 1,000まで
- **Sun Ang・Kazuki**: USD 5,000まで（見込み）
- **実例**: Nutreco Cargo - USD 16,400請求に対して40%割引（USD 9,840）を承認
- **実例**: Falabella - USD 480請求に対して2日間のCTIC延長を承認
- **実例**: 50%割引 - 1回限りのケース（例: BL SHAFD4280700、USD 960請求）
- 充分な根拠無しの場合は拒否

### チリチームとの連携

#### 主要メンバーと役割
- **Paula Benito** (`paula.benito@one-line.com`): レート修正リクエスト
- **Esmeralda Hernandez** (`esmeralda.hernandez@one-line.com`): レート修正、DAR処理
- **Belen Cruz** (`belen.cruz@one-line.com`): レート修正、NOR対応
- **Loreto Aravena** (`loreto.aravena@one-line.com`): KA Sales、DAR処理
- **Macarena Tramon** (`macarena.tramon@one-line.com`): Sparx関連
- **Carolina Chapa** (`carolina.chapa@one-line.com`): DMT Exception
- **Leandro Silva** (`leandro.silva@one-line.com`): Sparx関連
- **Julio Rondanelli** (`julio.rondanelli@one-line.com`): 管理職
- **Claudia Valenzuela** (`claudia.valenzuela@one-line.com`): 管理職
- **Sebastian Mosqueira** (`sebastian.mosqueira@one-line.com`): DAR Coordinator

#### 連携のポイント
- **Pushy PIC（チリ側）**: 数字・テーブルでの反証が有効
- 明確な根拠を示すことが重要
- メールでのやり取りが多いが、必要に応じて直接連絡

### チリ特有の注意点

#### Valparaíso港の制限
- 大型船・重量貨制限中
- Shanghai omit（AX2）継続中
- **SHA→San Antonioの新規オファー不可**

#### 港コード
- **CLSAI**: San Antonio
- **CLVAP**: Valparaíso
- **CLPUQ**: Punta Arenas
- **CLCNL**: Iquique
- **CLIQQ**: Iquique（別表記）

#### サーチャージの扱い
- **CVC**: チリ特有のサーチャージ。固定額で設定されることが多い
- **EPH**: 特定のPOL（例: THLCH）で必要
- **VJP**: 特定のPOLで必要
- **THD/CSS**: 標準的なサーチャージ

### レート修正リクエストの処理例

#### 例1: Sumitomo Rubber Latin America
- **RFA**: TSCLB00345A
- **特徴**: 四半期契約
- **特殊ルール**: 
  - POL THLCHの場合、EPHとVJPを必須で含める
  - 契約はOFT + THD + fixed CVC only
  - CVC for Chilean PODは固定額で、BL内で支払い可能

#### 例2: Sparx Logistics Chile
- **RFA**: SCLN00545A
- **NAC**: "Tricot"専用
- **特徴**: Game Plan違反（55%/45%）
- **CVCサーチャージ**: USD 95/100（特別設定）

#### 例3: Expeditors Chile
- **RFA**: SCLN00282A
- **NOR対応**: CNDLC - CLSAI, CLCNL USD 1,100/40NOR
- **Counter Offer**: CNDLC - CLSAI, CLCNL USD 1,300/40NOR
- **条件**: All in subject to THD/CSS only
- **Free Time**: 14 days at POD
- **Valid**: 15 Oct - 21 Oct（短期）

## 次アクション
- [ ] [[20251121_Chile-Pricing-主要顧客別ルール]]にリンク
- [ ] [[20251121_Chile-Pricing-DAR処理方法]]にリンク
- [ ] [[20251121_Chile-Pricing-チリ特有の港とルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#chile #pricing #tiger-system #rate-amendment #inbox

