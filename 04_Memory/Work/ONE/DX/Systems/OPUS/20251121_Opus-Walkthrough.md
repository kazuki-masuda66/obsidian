# Opus Walkthrough - OMMC TP Pricers向け操作ガイド

## 概要
Opus（ONEの業務システム）の使い方に関する詳細なガイドです。OMMC（ONE Manila Marketing Center）TP（Transpacific）Pricersが日常的なPricing業務で使用するOpusシステムの機能について、具体的な操作手順と実例を含めて詳細にまとめました。

## 内容

### ファイル情報
- **元ファイル**: `Opus_Walkthrough.pptx`
- **形式**: PowerPointプレゼンテーション
- **作成者**: Aira Benitez
- **作成日**: MAY 2025
- **対象**: OMMC TP Pricers
- **目的**: OMMC TP Pricersが日常的なPricing業務で使用するOpusシステムの機能の使い方を示す
- **場所**: 00_Memo内に保存されていた資料

### S/C Proposal & Amendment Inquiry（サービス契約提案・修正照会）

#### パス（Path）
```
Sales Management > Pricing > Service Contract > S/C Inquiry > S/C Proposal & Amendment Inquiry
```

#### 検索方法
- **10桁のS/C番号**で検索
- **Customer Name**（顧客名）で検索
- **Customer Code**（顧客コード）で検索
- **S/C Effective Date**（サービス契約有効日）で検索

#### Boiler Plate（ボイラープレート）
- **内容**: 契約がCIFまたはFOB契約かどうかを判断可能
- **情報**: Pricerの名前と契約有効期間も表示される

#### Origin & Destination Route（Origin & Destination Route）
- **内容**: WPE scope下に表示される国
- **Location Group**: Tiger location group codeがOpusシステムでも使用されている

#### WPE Location Group（WPE Location Group）
- **内容**: WPE Location Groupの情報が表示される

#### Origin & Destination Arbitrary Rates（Origin & Destination Arbitrary Rates）
- **内容**: Origin & DestinationのArbitrary Ratesが表示される

#### Rate Tab（レートタブ）
**General Rate（一般レート）**:
- **内容**: FAK ratesがファイルされている場所
- **用途**: FAK（Freight All Kinds）レートの確認

**Special Rate（特別レート）**:
- **内容**: Special NAC / LT NAC ratesがNamed Accountsと共にファイルされている場所
- **用途**: 特別なNAC（Named Account）レートやLT NAC（Long Term Named Account）レートの確認

#### Commodity Note（商品備考）
- **表示方法**: spy glass（虫眼鏡アイコン）をクリックすると表示される
- **用途**: 
  - Rate's validity（レートの有効性）を入力
  - Rate structure（レート構造）を入力
  - Specific service/vessel（特定のサービス/船舶、該当する場合）を入力
- **重要性**: Commodity Notes機能は常にファイル時に使用される

#### Conversion Column（変換列）
- **表示方法**: Conversion列のspy glassをクリックすると表示される
- **内容**: APP dateとcharges（該当する場合）が表示される

**APP Date（Application Date）の重要性**:
- **定義**: APP Dateはレートの実際の有効日
- **決定方法**: 顧客のesign（電子署名）がNA CAPに送信され、同時に契約がFiledされた日付
- **実例シナリオ**: 
  - Rate validityがまだeff 1 May 2025と表示されている場合でも、顧客のsign pageが遅れて送信され、契約が2 May 2025にFiledされた場合、APP dateは2 May 2025と表示される
  - このシナリオにより、1 May 2025にgate-inした影響を受けるbookingsは、late filingによりNROF（No Rate on File）となる
- **影響**: このため、OMMCは遅延（backdate）filing、VID refund、NROF bookingをレートするためのmanual ratingのリクエストを頻繁に受け取る

#### Special Note（特別備考）

**Inclusive Surcharges Notes（包含サーチャージ備考）**:
- **内容**: 特別なレート構造が契約にファイルされている場所
- **用途**: 特別なレート構造の確認

**Fixed Surcharges（固定サーチャージ）**:
- **内容**: 固定サーチャージが契約にファイルされている場所
- **例**: PSS（Peak Season Surcharge）が現在$0で固定されている場合

**Others > Hazardous Cargo Clause（その他 > 危険物貨物条項）**:
- **内容**: HAZ clauseが契約にファイルされている場所
- **用途**: 危険物貨物の条項の確認

**DEM/DET（Demurrage/Detention）**:
- **内容**: 特別なfree time conditionが契約にファイルされている場所
- **目的**: ADHOC DAR applicationsの使用を最小限に抑える
- **条件**: アカウントが特別なfree time conditionの承認を受けている限り

#### AMD History（修正履歴）
- **表示方法**: AMD Historyをクリックすると、契約のAMD履歴を表示する新しいウィンドウにリダイレクトされる
- **用途**: 
  - Filing AMD Dateを確認するために使用される
  - "Filed Date"列の下に表示される日付は、AMDが署名のためにfiledされた日付

### Booking Inquiry（Booking照会）

#### パス（Path）
```
Service Management > Booking/Documentation > Booking > Booking > Booking Inquiry
```

#### サンプルBooking Number
- **例**: MUMF42148800

#### BKG Creation（Booking作成）
- **内容**: Booking作成情報が表示される

#### Route Detail（ルート詳細）
- **内容**: Route情報をこのタブで確認可能
- **用途**: Vessel delaysをレビューする際にVVD detailsを取得するのにも有用

#### CNTR（コンテナ）
**CRD（Cargo Receiving Date）の重要性**:
- **定義**: CRD（Cargo Receiving Date）を知ることは重要
- **用途**: 特にNROF casesをレビューする際に重要

**その他の情報**:
- **Container number**: コンテナ番号
- **Weight**: 重量
- **Measure**: 容積
- **VGM（Verified Gross Mass）**: 検証済み総重量

#### Charge（料金）
- **内容**: Chargeタブには、Bookingにリンクされたratesとchargesが表示される
- **Application Date**: レートの適用日
- **IN**: I = Include（含む）/ N = Not Include（含まない）
- **Term**: P = Prepaid（前払い）/ C = Collect（後払い）
- **M**: M = Manual（手動）/ A = Automatic（自動）

#### S/C No.のSpyglass
- **動作**: S/C No.のspyglassをクリックすると、S/C Proposal and Amendment Inquiryにリダイレクトされる
- **用途**: Bookingにリンクされているレートを確認し、正しいレートが適切にリンクされているかどうかを確認する

### DEM/DET Adjustment Request - After Booking Approval（DEM/DET調整リクエスト - Booking承認後）

#### パス（Path）
```
Service Management > Demurrage/Detention > F/T Adjustment > DAR - After Booking > DAR - After Booking Approval
```

#### 入力項目
- **APVL Office**: 正しいAPVL Officeを指定する必要がある（OMMCの場合はSINHQ）
- **DAR No.**: Salesが提供するDAR番号（SalesがDARリクエストを準備するため）
- **S/C No.**: アカウントの10桁のサービス契約番号
- **BKG No.**: リンクされたBooking
- **Free Time**: 追加のfree timeリクエストの場合、「Add」列の下に入力し、日数を指定
- **F/T**: Tariff日数の列
- **Comment box**: 備考を入力するセクション

#### 操作手順
1. **DAR番号を入力**し、「Retrieve」をクリック
2. **選択されたリクエスト理由を確認**（リクエストと正確である必要がある）
3. **「Comment」ボックスをクリック**し、備考を入力
4. **すべての詳細を確認**し、すべてが正しい場合は、リクエストをApprove（承認）する

### Product Catalog Inquiry（プロダクトカタログ照会）

#### パス（Path）
```
Service Management > Product Catalog > Product Catalog Generation > Product Catalog Inquiry
```

#### 入力項目
- **POR / POL / POD / DEL**: 5文字のロケーションコードを入力
- **Cargo Nature**: 正しいCargo Natureを選択
- **Ocean Route Priority**: 
  - **P1/P2**: ONE websiteで利用可能なルートで、優先的に取られるべきルート
  - **All**: すべての利用可能なルートを表示するために選択可能
- **R & D Term**: C = CY（コンテナヤード）/ D = Door（ドア）
- **TP/SZ**: 
  - **Dry**: D2/D4/D5/D7
  - **Reefer**: R2/R5

#### 操作手順
1. 入力項目を入力
2. **「Retrieve」をクリック**して利用可能なルートを表示
3. **Product Catalog > Detail**で詳細を確認

### Pricing Simulation（Pricingシミュレーション）

#### パス（Path）
```
Sales Management > Pricing > Simulation > Pricing Simulation
```

#### 用途
- Pricingシミュレーションの実行
- レート計算の確認

### Location Inquiry（ロケーション照会）

#### パス（Path）
```
Sales Management > Pricing > Code > Inquiry > Location Inquiry
```

#### 用途
- ロケーションコードの確認
- ロケーション情報の照会

### Surcharge Inquiry（サーチャージ照会）

#### パス（Path）
```
Sales Management > Pricing > Surcharge > Surcharge Inquiry
```

#### 用途
- サーチャージ情報の確認
- サーチャージコードの照会

### RFA Proposal & Amendment Inquiry（RFA提案・修正照会）

#### パス（Path）
```
Sales Management > Pricing > RFA > Proposal & Amendment > RFA Proposal & Amendment Inquiry
```

#### サンプルRFA
- **例**: TCMBN01356A

#### 用途
- RFA（Rate Filing Agreement）の提案と修正の照会
- RFA情報の確認

### TRI Inquiry（TRI照会）

#### パス（Path）
```
Sales Management > Pricing > Tariff > Tariff Rate Item > TRI Inquiry
```

#### 用途
- Tariff Rate Item（TRI）の照会
- Tariff情報の確認

### Commodity Inquiry（商品照会）

#### パス（Path）
```
Sales Management > Pricing > Code > Inquiry > Commodity Inquiry
```

#### 用途
- 商品コードの照会
- 商品情報の確認

### Customer Inquiry（顧客照会）

#### パス（Path）
```
Sales Management > Pricing > Code > Inquiry > Customer Inquiry
```

#### 用途
- 顧客情報の照会
- 顧客コードの確認

### Long Range SKD Inquiry（長期スケジュール照会）

#### パス（Path）
```
Vessel Operation > Vessel Schedule > VSL SKD > VSL SKD Inquiry > Long Range SKD Inquiry
```

#### 入力方法
- **Vessel Code**: Booking Inquiryから取得可能なVessel Codeを入力

#### 用途
- 船舶スケジュールの確認
- 長期スケジュールの照会

### 重要な注意事項

#### APP DateとNROF
- **APP Date**: レートの実際の有効日は、顧客のesignがNA CAPに送信され、契約がFiledされた日付
- **NROF**: Late filingにより、APP Dateより前にgate-inしたbookingsはNROFとなる可能性がある
- **対応**: 遅延（backdate）filing、VID refund、manual ratingのリクエストが頻繁に発生

#### DAR処理
- **APVL Office**: OMMCの場合はSINHQを指定
- **DAR No.**: Salesが提供（SalesがDARリクエストを準備するため）
- **Free Time**: 「Add」列に日数を入力

#### Location Group
- **Tiger location group code**: Opusシステムでも使用されている
- **WPE Location Group**: WPE scope下のLocation Group情報

### 関連情報
- [[04_Memory/Work/ONE/DX/Opus/]]: Opusシステム関連のMemory Note
- [[20251121_Mexico-Pricing-基本ルールとTigerシステム]]: Tigerシステムとの連携
- **OMMC**: ONE Manila Marketing Center
- **TP**: Transpacific Trade

### 確認事項
- [ ] 各機能の操作手順を確認
- [ ] APP DateとNROFの関係を理解
- [ ] DAR処理の手順を確認

## 次アクション
- [ ] 操作手順をMemory Noteに変換（[[04_Memory/Work/ONE/DX/Opus/]]）
- [ ] 実際の業務で使用する際の参考資料として活用
- [ ] 各機能の詳細な操作手順を確認

#opus #system #walkthrough #dx #ommc #tp #pricing #s-c-inquiry #booking-inquiry #dar #product-catalog #inbox

