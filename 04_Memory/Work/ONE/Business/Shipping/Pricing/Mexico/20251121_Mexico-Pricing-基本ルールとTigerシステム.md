# Mexico Pricing - 基本ルールとTigerシステム

## 概要
Mexico Pricingにおける基本ルールとTigerシステムを使ったレート修正リクエストの処理方法についてまとめました。メキシコ特有のルールや運用方法を含みます。

## 内容

### Tigerシステム - レート修正リクエストの処理

#### 基本的な流れ
1. **Tiger通知の受信**
   - `tigeradmin@one-line.com` からレート修正リクエストの通知が届く
   - メキシコチーム（Ricardo Saldana, Jeimy Guerrero, Andrea Lomeli, Angeles Olivaresなど）からのリクエスト
   - 通知には顧客名、RFA番号、理由、詳細が含まれる

2. **リクエスト内容の確認**
   - Tigerのリンクから詳細を確認
   - 顧客の要望内容を理解
   - 既存契約との整合性を確認

3. **承認・却下の判断**
   - Game Plan比率を確認
   - 採算性（CM/TEU）を確認
   - メキシコ特有のルールを考慮

#### よくあるリクエストパターン

**パターン1: レート修正（Rate Amendment）**
- 顧客からの値下げ要求
- ボリューム増加に伴うレート調整
- 期間延長のリクエスト

**パターン2: Arbitrary Request（任意レート）**
- 標準レート表にない特殊なレート
- 新規ルート、特殊な貨物

**パターン3: DMT Exception（運賃表例外）**
- 標準運賃表から外れた特別レート
- 新規顧客向けの特別条件

### Mexico Pricingの基本ルール

#### レート設定のベンチマーク
- 市場動向と会社方針を踏まえて設定
- Elmaなどの競合他社の提示に対し、適切なカウンターを提示

#### Free Time（無料期間）
- 標準: 14 days（例: MABE契約）
- 延長要望は個別に判断
- 特別なケース（Golden Week前など）は3日延長を検討

#### レート有効期限
- **標準**: 5日間
- **短期**: 7日間（例: OOGレート、nominationなしの場合null and void）
- **中期**: 14日間（例: CNTAO-MXZLO）
- **長期**: 15-30日間（例: 15/11/25 - 30/11/25）
- **超長期**: 月次、四半期など

#### レート設定の実例
**Lazaro Cardenas (MXZLO)向け**:
- CNNSA→MXZLO: USD 7,700/40FR (OOG)
- CNTAO→MXZLO: USD 1,600/20', USD 2,000/40'
- CNNGB→MXZLO: USD 1,750/40HC
- CNSHA→MXZLO: USD 1,750/40HC
- CNTAO→MXZLO: USD 1,000/40HC（別ルート）
- CNTAO→MXZLO: USD 1,200/40HC（別ルート）
- TWTXG→MXZLO: USD 8,400/40FR (OOG)
- KRPUS→MXZLO: USD 1,750/40HC, USD 1,000/40HC, USD 1,200/40HC
- VNSGN/VNHPH→MXZLO: USD 1,900/40HC, USD 1,200/40HC, USD 1,500/40HC
- Tuticorin→MXZLO: USD 1,700/40HC, USD 1,900/40HC, USD 1,300/40HC, USD 1,600/40HC
- Qingdao→MXZLO: USD 1,750/40HC, USD 1,000/40HC, USD 1,200/40HC
- Cochin→MXZLO: USD 1,600/40HC, USD 1,300/40HC

**特殊貨物レート**:
- HAZ (Class 2.1, UN 1950): USD 700/TEU
- Flexibag Add-on: USD 100/unit（IDSUB-MXZLO例）
- Reefer Origin Plug-in: USD 300/unit（3 days）
- Restow: USD 500/unit x no. of restow

### メキシコチームとの連携

#### 主要メンバーと役割
- **Ricardo Saldana** (`ricardo.saldana@one-line.com`): Sales Support Coordinator、レート修正リクエスト
- **Jeimy Guerrero** (`jeimy.guerrero@one-line.com`): Sales Executive、レート修正、HAZ対応
- **Andrea Lomeli** (`andrea.lomeli@one-line.com`): Sales Executive、DAR処理
- **Angeles Olivares** (`angeles.olivares@one-line.com`): Sales Executive、Commercial Support
- **Israel Flores** (`israel.flores@one-line.com`): Sales & Service Manager、Container Deposit対応
- **Alejandra Olmedo** (`alejandra.olmedo@one-line.com`): Sales Executive、MABE対応
- **Jacqueline Estrada** (`jacqueline.estrada@one-line.com`): Demurrages Coordinator、DAR処理
- **Sandra Hernandez** (`sandra.hernandez@one-line.com`): Demurrages Coordinator
- **Josue Sanchez** (`josue.sanchez@one-line.com`): Commercial Steering Expert Analyst、AP処理
- **Beatriz Ceja** (`beatriz.ceja@one-line.com`): Customer Service Supervisor、Container Deposit対応
- **Gerardo Resendiz** (`gerardo.resendiz@one-line.com`): Sales Support Coordinator

#### 連携のポイント
- **グループメール**: `ghq.lawc.mktg@one-line.com` を必ずCCに入れる
- **迅速な対応**: レートリクエストは迅速に対応
- **明確な説明**: 承認・却下の理由を明確に説明

### メキシコ特有の注意点

#### 港コード
- **MXZLO**: Lazaro Cardenas（主要港）
- **MXMAN**: Manzanillo
- **MXVER**: Veracruz
- **MXENS**: Ensenada

#### サーチャージの扱い
- **CDD/CVC (MX)**: メキシコ特有のサーチャージ
- **BRS/PSS/BAF/OBS**: 標準的なサーチャージ
- **LSF, CSS, SLF, THCS**: 標準的なサーチャージ
- **Local charges**: ONEがmanifestしない場合、顧客が現地オフィスに直接支払い

#### レート設定の標準フォーマット
```
Rates are inclusive of BRS/PSS/BAF/OBS subj LSF, CSS, SLF, THCS both end, 
Doc fees both end, CDD/CVC (MX) prevailing surcharges in Opus and local charges

Local charges not manifested by ONE, customers are to pay to the local offices accordingly.

CY/CY, Non-DG
Rates are subj to equipment and space availability
```

### レート修正リクエストの処理例

#### 例1: DACHSER DE MEXICO
- **RFA**: TMEXN00275A
- **特徴**: レート修正リクエスト頻発
- **処理**: Adele Chiaが処理

#### 例2: AIRMAR TRANSPORTES INTERNACIONALES
- **RFA**: TGDLN00019A, GDLN00067A, TMEXN00737A
- **特徴**: Tier 1顧客、週92TEU
- **Arbitrary Request**: 頻繁にリクエスト

#### 例3: SPARX INTERNATIONAL FREIGHT
- **特徴**: 2025年に120+ TEU実績
- **Commercial Support**: DAR割引リクエスト（10%まで検討可能）

### レートリクエストのベストプラクティス

#### 1. グループメールを必ずCCに入れる
- `ghq.lawc.mktg@one-line.com` を必ずCCに入れる
- 迅速な対応のため

#### 2. 正確な情報を提供
- POL、POD、コンテナタイプ、数量を明確に
- 貨物の詳細（OOG、HAZ、Reeferなど）を明記

#### 3. 有効期限を明確に
- レートの有効期限を明確に設定
- 短期間の有効期限（5-7日）を推奨

#### 4. 条件を明確に
- CY/CY、Local charges、サーチャージの扱いを明確に
- 特殊な条件（OOG、HAZなど）を明記

## 次アクション
- [ ] [[20251121_Mexico-Pricing-主要顧客別ルール]]にリンク
- [ ] [[20251121_Mexico-Pricing-DAR処理方法]]にリンク
- [ ] [[20251121_Mexico-Pricing-メキシコ特有の港とルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#mexico #pricing #tiger-system #rate-amendment #inbox

