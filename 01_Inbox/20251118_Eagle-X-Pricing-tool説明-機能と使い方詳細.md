# Eagle-X-Pricing-tool説明-機能と使い方詳細

## 概要
Pricing tool説明に関するメモ。共通フォーマットのインポート、データソース、Search Data、Get data、運賃、All in rate、Expected CM/TEU、Export to Customer sheet、D&D、Route、Surcharge / MRGの比較、Filing、Pricing Logicの説明動画、2026 Pricing toolの説明について詳細に記録されています。

## 内容

### 共通フォーマットをインポート
- **PRISM**: Pricing Sumilation
- **COA**: Lifting等の実績
- **DMT**: Tariff
- **Contractの情報**: TenderDBから引っ張ってきている

### 実例：Murata

#### Search Data
- **NVOを選ぶと横にNACが出てくる**
- **下にどのTradeか出てくる**
- **Link finnalというところで30_2のリンクもシートに持っており、そうでないとサーチに時間がかかってしまう**
- **ここといずれステータスリストをリンクさせていきたい**
- **それぞれでPricing toolでそれぞれExcelを格納してあげていたのはなぜか？**
  - ファイルを事前に作ってあげている
  - データインポートまで
  - 別にスクリプトを作っている
  - Tradeごとにテンプレートがある
  - MRGとかサーチャージとかがTradeごとにファイルが違くて重さが違う
  - ファイルをサーチして取り込み、COA,プラスリフティングがあるかどうかLiftingを走らせる
  - Routeの候補も事前にリトリーブしている→PSファイル

#### Get dataでRetrieveする
**Lifting**
- BCOはContract no
- NACはNVとNACの組み合わせ
- だからボタンが２つに分かれている
- Lifting resultのマスタを参照して条件にあったものだけを持ってきている
- LT MRGの全部バージョンは別シートで持っている、ここにドミだけでなくNon domiも持っている
- ゲートポートが有る場合は黒い列で指定
  - MRG Serach conditionにYをつけるとゲートポートも含まれる
- 同じPORとPODでも揚げ地、積地でレートは変わってくる
- 該当Port pairのRouteをすべて持ってきている、かつこのコストも裏で持っている
- 文字列をすべて連結している
- 各タイプ・サイズごとのコストも持っている
- デフォルトはDefault settingで選んだものがデフォルトでセットされる
- サービスと各ロケーションはぶつ切りになってHiddenされているが、これは最終的にSubmissionしたファイルに送られる

**運賃**
- MRGはこうだがお客さんにどう実際にだすか
- 頻出アイテムはデフォルトで用意していてここはマニュアルでいれる
- FRTコントロールパネルで簡易入力できる
  - Benchmarkにフォーミュラを選ぶ
    - 選択した値をSUMする式が入る
  - お客さんごとに追加が必要だったらAd on insertする
    - 例えばDMT等が追加できる
  - MRGがうまっていないところはDecline offerにYをいれてDecline reasonが入れられる
- フィールドマッピングでどのPricerがSurchargeいれているから、そこからPricing toolのSurchargeに紐づけている
- Y/MはYは返してね、MはMandatory
- Base rateはどれをいれるかはFRTコントロールパネルの右側
  - 差し引きたいSurchargeを選択できる
  - Banker関連のSurchargeが引かれてBase rateが出てくる
- サーチャージは各トレードではなｋ，クロストレードで出している
- サーチャージは23個裏では持っている、フィールドマッピングで指定された５つだけを持っている
- OBSはSYM
- ローカルサーチャージは各国のSYMがやっていたりする
- 四半期に一回洗いがえる
- Pricing toolで読めるようにシートを作っている
- サーチャージをきれいにしたい
- オートレートまではいっていない
- 実際そこまではいっていない
- 近江さんがデータを作っている、12月くらいにデータを集めてきている
- 直接的なLook upは可能か？
  - 何かキーが足りない、パフォーマンス？

#### All in rate
- **All in rateはFRTコントロールパネルの右下**
  - DOC等をいれるケース、いれないケース

#### Expected CM/TEU
- **Expected CM/TEUはコストを元に計算されている、このあたりがシュミレーション**
- **MRGがないレーンやIntra AsiaやNondomiで使う**
  - PSのカバレッジがないところはコストの情報がない
- **重要なコンポーネントだけを指定するFlexibilityを持たせている**
  - ただ、TTの情報がうまく取れないからパッチ宛が必要

### Export to Customer sheet
- **Routeの場所を変えた場合は黄色でハイライトされている**

### 提出はSubnitボタン
- **このシートだけ出力**
- **File infoに出力先等のデータを持っている**
- **今後メールもできる（Gフォーム経由）**

### D&D
- **DMT tariffのデータを持ってきて中間テーブルを作っている**
- **Nodeで分かれている？**
- **PwがContractのデータベースにAverageのfree timeとTariffの日数がある**

### Route
- **選択肢にゴミデータが入ってしまっている**
- **いらないのが混じっている、Pricerからすると候補が多すぎる**

### Surcharge / MRGのApple to Appleの比較が課題

### Filing
- **Filingの対象はBase rate**
  - OPUSの？？になるから
- **MRGのStructureがFilingのStructureもでない**

### Pricing Logicの説明動画
- [https://drive.google.com/file/d/1UKHDvE9mfEir44_cNyS6dw0BnqNHTtTQ/view?usp=sharing](https://drive.google.com/file/d/1UKHDvE9mfEir44_cNyS6dw0BnqNHTtTQ/view?usp=sharing)
- **いろんなマカロンがあるときにどれが安いか、どう比較するか？**
  - すべて足したものを比較する
  - **ALL in calculation**はすべてを足したものを表示する

### Customer's request
- **Set Surcharge →Update Surcharge**

### Set END to ENDが最初に押下
- **ミニマムコストのルートをセット**
- **End to End costが出てくる**

### T&Cを読む
- **Rate Structureの解釈**

### Set Surchargeを押下
- **All rowsにPopulate**

### Update Conditionボタンを押下
- **右側のサーチャージカラムが反映される（InclusiveがSubject toか）**

### Retrieve MRGを押す
- **MRGカラムが埋められる**
- **Long Term MRGのRate Structureも埋められる**

### FRT Control Panel
- **Benchmarkを選ぶ**
  - MRGを選ぶと
  - MRGで計算したものが加算される
- **Surcharge Updateを押す**
  - サーチャージの方もLong Term MRGのRate Structureが反映される

### All in Caluculationを押す
- **すべてのサーチャージをたされた総額がでる**

### Base Rateの計算
- **All inカラムーSubjectサーチャージが計算される**

### 重要なポイント
- **顧客がAll Inしか求めていないときも常に最後のBase Rateまでオペレーションすることが求められる**
- **顧客のレートストラクチャーの前提で全部足しこんだものと、LTMRG前提で全部足したものを比較して、最終的にBase Rateを算出している**
- **Base Rateが最終的にCustomer Sheetに反映される**
- **All in rateはApple to Apple比較のため**

### Subject to allのSurchargeはPricing toolはどこから持ってくるか
- **Applicable Surcharge from PRISM**

### どうやってPricerはSubject to allを選ぶのか
- **Pricerによる。Pricerが高いレートを出したいならこっちを使ってもいい**
- **ベンチマークサイドは完全にPricer, Tradeによる**
- **ただし、Customer's requestはPricerがCustomerのリクエストを再現するべき**

### Custimuzed OBS
- **別シートを変えて対応する**

### 用語定義
- **Customer's Request** = Marketing/Pricer-Defined Rate Structure based on their interpretation of Customer's T&C; Executed Using Set Surcharge and Update Condition
- **LT MRG** = Long Term Minimum Rate Guideline; Minimum Rate Level Set by Trade Management to Offer for Long Term Customers
- **Target CM** = Target Contribution Margin; Minimum CM Level Set by Trade Management where Rate Offer To Long Term Customers Should be Based On.
- **Current Contract** = Agreed Rate Levels between Customer and ONE for Specified Port Pairs
- **Benchmark Rates** = Baseline/Basis of Marketing/Pricing Offer; Can be based on LT MRG, Target CM, Current Contract.
- **Reference Base (Benchmark Rate Structure)** = Surcharge Condition of Benchmark Rates
- **All In Calculation** = Benchmark Rates + Benchmark Rate Structure (Subject)
- **Base Rate** = Rate Level Marketing/Pricing intends to offer/export to customer/customer sheet; It is calculated using All In Rates (Minus) Customer's Request Rate Structure

### 2026 Pricing toolの説明
- **AK列を展開すると顧客テンダーシートのその他の情報が見れる**
- **Decline Laneに直接飛べるようになった**
- **First CYとLst CYが追加された、これはMRGの取得のため**
- **Cargo NatureとEquipment Typeも追加された**
- **オレンジの部分はEUA IOP Pricer関連**
- **Applicable SurchargeのキーはReferredカラムによって制御可能**
  - POR DEL, Cargo type
  - Pair=Port Pairベース
- **Add on CostとHidden Costの違い**
  - Hidden CostはCYCYコストとして認識される
- **今期からDeclineを入れないとExportできないようになっている**
- **Base Rateのクリームの色の部分が顧客が求めている部分のレート**
  - Offerしたくない場合はNo Offerを選択する
- **必須かどうかの判断**
  - Y = Optional
  - Y/M = Mandatory
- **End to End routeを設定するときに最初に常にRefresh E2E databaseを最初に行う**
- **SurchargeはデフォルトでInclusiveとなっている**
  - Tigerと同じ
  - Subject toにしたいのだけ選ぶ

## 次アクション
- [ ] 関連ノートにリンク（[[Eagle X]]、[[Pricing tool説明]]など）
- [ ] 必要に応じてMemory Noteに変換

#inbox #one #eagle-x #pricing-tool
