# EagleX Pricing Tool - FY25 SOP

## 概要
EagleX Pricing ToolのFY25（2025年度）SOP（Standard Operating Procedure）に関する資料です。Pricing Toolの使用方法、手順、注意点について詳細にまとめました。

## 内容

### ファイル情報
- **元ファイル**: `EagleX Pricing Tool FY25 SOP (240819).pptx.pdf`
- **形式**: PDF（元はPowerPointプレゼンテーション）
- **作成日**: 2024年8月19日（240819）
- **更新日**: 2024年8月27日
- **場所**: 00_Memo内に保存されていた資料

### Tool Overview（ツール概要）

#### 4つの主要要素
1. **Input ONE Format**: 顧客のTender Sheetから情報を取得し、標準的なONE Formatに変換
2. **Refer to each data set**: OPUS、Eagle PlusなどからPricingに必要な重要なデータを取得
3. **Re-Convert to Customer Format**: 計算と入力を行い、顧客フォーマットに再変換
4. **Export and submit**: Pricing情報をエクスポートし、顧客フォーマットに再変換して提出

#### データソース
- **Tender DB**: Converted Tender Data、Routing Cost、Lifting/WGT/CM
- **Contract**: DMT、DMT Tariff、Surcharge
- **Master Contract Data**: OFT/Surcharge、MRG、Target CM/TEU
- **PRISM**: COA、Contract、DMT、LT MRG/Surcharge

### Column Overview（1-7列の概要）

#### 1.1 Customer and Routing Info（顧客情報とルーティング情報）
- **データソース**: 顧客のTenderからONE形式に変換されたデータ
- **デフォルトデータ**: Pricerの利便性のため自動的に事前入力されるが、Cream色のハイライトエリアで修正可能
- **クイックナビゲーション**: ドロップダウンオプションでPricing Tool全体へのクイックアクセス
- **追加情報**: Group Location、Cargo Type/Termなどは(+)をクリックして確認可能

#### 1.2 IOP info and Tender Volume Proposal（IOP情報とTender Volume提案）
- **データソース**: IOP Pricersが提出したデータ
- **デフォルトデータ**: 顧客のTenderにCommodity/Tender Volumeが記載されている場合、自動的に事前入力
- **Inland Routing情報**: IOPチームが提出したInland Routing情報
- **Tender Volume and Commodity Info**: Tender VolumeとCommodity情報

#### 1.3 Rate Structure Benchmark / Customer Remarks（レート構造ベンチマーク/顧客備考）
- **データソース**: システム情報から生成されたデータ
- **Rate structure benchmark**: Pricerの参照のため事前入力されるが、Pricerが適宜修正可能
- **Rate structure**: Pricerが選択したベンチマークに基づいて変更される
- **Customer remark columns**: 顧客がTender Sheetで特別な要件を指定する場合の列

#### 1.4 Current Performance/Game Plan/Pricer's MRG（現在のパフォーマンス/ゲームプラン/PricerのMRG）
- **Customer's performance**: OPUS/Lookerから抽出された顧客のパフォーマンス
- **Game Plan**: Route Portfolio Simulationデータ
- **MRG Mandates**: Trade Managersが設定したMRG Mandatesから抽出されたデータ
- **Target CM and LT MRG Rate**: EA/WAの場合、LT MRG列は非表示になり、Target CM (EA/WA)が表示される

#### 1.5 FRT Control Panel and Pricer's Comments（FRT Control PanelとPricerのコメント）
- **Offer rate and surcharge structure**: All-in rate計算のためのOffer rateとsurcharge structure
- **All in rate and expected CM Section**: All in rateとexpected CMセクション
- **Required FRT**: EA/WAの場合、選択したroute/costでTarget CMから計算されたRequired FRT
- **Pricer's comment boxes**: 各レーンを拒否または備考を入力するためのコメントボックス

#### 1.6 Base Rate and Surcharges Breakdown（Base RateとSurcharges Breakdown）
- **Base rate**: 顧客に提示するオファーレート
- **Rate structure breakdown**: "Applicable rate structure"（LT MRGまたは顧客のリクエスト構造）に応じたレート構造の内訳
- **Subtotal visibility**: Include/subject+fixed surchargesの小計、選択したroutingに基づくcost/boxの可視性

#### 1.7 DMT Section and Other Columns for Pricers input（DMTセクションとその他のPricer入力列）
- **Customer remarks**: DMTに関連する顧客備考がDMT tariff/offerセクションの隣に表示
- **DMT types**: Pricerがオファーする必要があるDMTタイプのみ表示、その他は非表示
- **Other columns**: DMTセクションの後、Pricerの入力が必要な他の列（space commitment、uncommon surchargesなど）

### Data Retrieval（データ取得）

#### 2.1 Routing（ルーティング設定）
**Set E2E Routeボタンの使用方法**:
1. **適用方法の選択**:
   - All Rows: Tender内のすべての行
   - Selected Rows: 列AにYが付いている行
   - Filtered Rows: ドロップダウンでフィルタリングされた行

2. **オプション基準の選択**:
   - MIN cost / Shortest TT
   - Ocean Priority: 例：P1のみを使用する場合はP1にチェック
   - Respect POL/POD/TS Port: POL/POD/TS Portを含める
   - Respect IOP's transmode: IOP transmodeを含める

3. **Refresh E2E Database**: PricerがPOR/DELをカウンターオファーする場合は、このボタンをクリックしてroutingデータを更新

**Trunk Service Lane**:
- [Set E2E Route]ボタンを実行する前に、Trunk Service Lane列で使用するService Laneを指定可能
- [Set E2E Route]ボタン実行中、Trunk Service Laneは自動的に尊重される
- Trunk Service Laneが入力されていない場合、ルート設定後に赤色でハイライトされる

**ルーティングの手動更新**:
- データ取得後も、各行のドロップダウンリストから希望のルーティングを手動で更新可能
- リスト内のルーティングはPriority 1、2、3に基づく
- E2Eルーティングが選択されると、Expected CM、Required FRT列の近くにcost per boxが利用可能
- EPP A、EPP Bを選択してCMレベルを計算可能

**ルーティングが利用できない場合**:
- PRDにルートが欠けている場合、一部のレーンでルーティングが表示されない場合がある
- この場合、Pricerは「Trunk Service Lane」のみを入力可能
- この場合、Expected CMを計算するためのコストはない
- 後でPRDのルーティングを更新し、Pricing Toolで利用可能にする必要がある

**Blank POL or POD**:
- Blank POL/PODは[Set E2E Route]ボタン実行中に自動入力される
- PricerのPOL/PODがE2Eルートと異なる場合、Pricerの手動入力は上書きされない
- このような違いはオレンジ色でハイライトされる

#### 2.2 Surcharge Structure（サーチャージ構造）
**Rate Structure Benchmarkの選択**:
- Pricerはドロップダウンリストから「Rate Structure Benchmark」を選択可能
- **Customer's Request**: 次の契約期間の顧客リクエスト
- **Current Contract**: 既存/アクティブな契約のレート構造に基づく
- **LT MRG**: PricerのMRGレート構造に基づく

**Contract dataの利用**:
- Contract data、long term rate structure infoが利用可能な場合、データが取得され、「Applicable surcharges from PRISM」と比較され、「Possible applicable surcharges」に表示される

#### 2.3 Surcharge Structure - Customer's Request（サーチャージ構造 - 顧客リクエスト）
- Customer's requestが選択された場合、PricerはT&C summaryを読む必要がある
- T&C summaryには、顧客のリクエストまたはsales intentionによって示されるsurcharge structureが記載されている
- その後、Pricerは[Set Surcharge]ボタンを使用してapplicable surchargeを設定可能

#### 2.4 Set Surcharge（サーチャージ設定）
**適用行の選択**:
- [Set Surcharge]では、このsurcharge structureを適用する行を選択する最初のセクションがある
- 「All Rows」「Service Scope Code」「Origin」など、複数のオプションがある
- 一部のオプションでは、適用行をさらにフィルタリング可能
- 例：GB destinationsのみにこのレート構造を適用する場合は、「Destination」を選択し、下部ボックスでDELコードを選択

**サーチャージの設定**:
- サーチャージを設定するには、Pricerは以下を実行可能：
  - 各サーチャージを1つずつチェック
  - Origin、Ocean、Destinationセクションの各セクションの上部にあるボックスをチェックすると、そのセクション内のすべてのサーチャージが選択される
- 左下に3桁のサーチャージコードを入力可能（リストにないサーチャージコードの場合、1回に1つのサーチャージのみ）
- [Subject]をクリックすると、選択したサーチャージが「Customer Rate Structure」に移動

**注意事項**:
- Pricing Toolは、選択されていないサーチャージを「Inclusive」サーチャージと見なす
- 「Free in/Free out」料金を追加するには、左下の「Enter Surcharge」ボックスにF-IまたはF-Oを入力

**サーチャージの削除**:
- サーチャージが誤って選択された場合、Pricerは以下で削除可能：
  1. 削除したいサーチャージをクリック
  2. [Remove]をクリック
- サーチャージは「2.PriSM Surcharges」セクションにリストバックされる
- 注意：「Select All」は、一度にすべてのサーチャージを削除するオプションでもある

**Fixed Surchargeの設定**:
1. 固定するサーチャージを選択
2. [Fixed]をクリック
3. この固定サーチャージに適用する行を選択
4. 各サーチャージの通貨と金額を入力
5. [Set Fixed Amt]をクリック
- [Update Condition]ボタンをクリックすると、固定数量がサーチャージセクションに表示される

**Populate & Overwrite / Add on to existing**:
- Subject/fixed surchargeが設定された後：
  1. [Populate & Overwrite]ボタン: サーチャージを「Possible applicable surcharges」に入力。セルに情報がある場合、このボタンをクリックするとデータが上書きされる
  2. [Add on to existing]: 既存の設定の上にさらにサーチャージを追加したい場合に便利

**Update Condition**:
- [Update Condition]は、サーチャージ条件と数量をサーチャージセクションに更新する機能
- このステップには読み込みに時間がかかる場合があるが、Pricing Toolには進行状況を示すステータスバーがある

#### 2.5 Target CM/TEU Retrieval（EA/WA用）（Target CM/TEU取得）
- **East and West Asia Trades**: Target CM/TEUはE2E routingに関連するコストごとに設定されている
- **取得方法**: Target CM列の上部にある[Target CM(EA)]または[Target CM(WA)]をクリック
- **計算式**: E2E Route Cost + Target CM = Required FRT
- **仕組み**: 各port pairで考慮すべきE2E routeを指定することで、システムはTarget CM submissionをE2E routing costと比較してRequired Freightを生成

#### 2.6 LT MRG Retrieval（LT MRG取得）
**取得手順**:
1. LT MRG列の上部にある[MRG]ボタンをクリック
2. 希望するLT MRGのバージョンを選択
3. [Refresh MRG Data]をクリック
   - その後、LT MRGデータが入力される

**注意事項**:
- Pricing Toolは、関連するTradeのMRGのみを表示（trade code/domi、non-domi選択は不要）
- 必要な選択はMRGのバージョンのみ
- 最新のものが一番上に表示される
- **Date = MRG registration date**

#### 2.7 LT MRG Retrieval - Missing Data（LT MRG取得 - データ欠落）
- **データがない場合**: サービスがない可能性のあるport pairs（サービスがないport pairsに関連する可能性がある）では、MRG行が空白で表示される
- **カウンターオファー**: Pricerは、黄色のエリアでPOR/DELを操作することで、LT MRGがあるport pairsでカウンターオファー可能
- **自動入力**: MRGが一度取得されていれば、LT MRGデータが自動入力される

#### 2.8 Route Counteroffer（ルートカウンターオファー）
**手順**:
1. Pricerが提供したいPOR/DELを黄色の列エリアで更新
2. [Set E2E Route]をクリック
3. [Refresh E2E Database]をクリック
4. ルーティングの基準を設定
5. [Set Route]をクリック
- **注意**: 特定のレーンのみにルートを設定する場合は、列AにYを付けて行を選択することを忘れない

**ハイライト**:
- Pricerによってカウンターオファーされたレーンは黄色でハイライトされ、顧客シートにエクスポートされ、salesの可視性のために表示される

#### 2.9 Retrieve Inland Route（内陸ルート取得）
**取得方法**:
- IOPチームからの内陸オファリングをインポートするには、Inland Routeセクションの上部にある[Retrieve Inland Route]ボタンを使用

**適用行の選択**:
- Retrieve Inland Routesでは、Pricerは適用行を選択可能：
  - All Rows、Selected Rows、Filtered Rows

**インポートオプション**:
- **A) Import IOP Offer**: IOP PricersのOffer > Import IOP Offerを選択
- **B) Import ITS Tender Mandate**: ITS logic、most used route、またはMIN Cost routeに従うオプション
- **Optional**: 顧客の希望するtransmodeに従うかどうかのオプション選択
- **注意**: EUA内陸ルートの場合、デフォルトで顧客のPOL/PODを尊重する

**結果**:
- プロセスが完了すると、Inland Route情報がInland Route Sectionに表示される
- OIH/DIHはPricerの操作エリア列に反映される
- OIH/DIH pricesはここに反映される
- Pricerは、ドロップダウンをクリックして「USD」を選択することで、OIH/DIHをローカル通貨ではなくUSD通貨でエクスポートするオプションがある
- [Eagle-X backend will calculate and input in customer's sheet]

### Referred Condition（参照条件）

#### 3.1 Referred Condition - Exactly Related（参照条件 - 完全に関連）
**Exact Matchの定義**:
- PRISM snapshotデータが、上記の5つのキー（Origin、Destination、Terms、CGO Type）と完全に一致するサーチャージ情報を持っていることを意味する
- **例**: Tender routing request ex.BRNVT to AEAUH CY/CY (RF)、PRISM data available ex.BRNVT to AEAUH CY/CY (RF)

**Column Referred Condition**:
- 顧客の要件はPrism Snapshotデータ（EagleXデータベースの基礎を形成）と比較・照合され、両方の情報セットが完全に関連（Exact Match）または密接に関連しているかどうかが決定される
- Column Referred Conditionは、Pricerの参照のための重要なガイドで、顧客の5つの主要要件（origin and destination locations、receiving and delivery terms、cargo types）に関するサーチャージ情報の正確性を検証する

#### 3.2 Referred Condition - Closely Related（参照条件 - 密接に関連）
**Closely Relatedの3つのカテゴリー**:

1. **By "Pair"（ペア別）**:
   - EagleXがport pairsに関する堅牢なサーチャージ情報を持っているが、delivery termsまたはcargo typesについては完全ではないことを意味する
   - **例**: Tender routing request ex.BRNVT to CNCKG CY/CY (RF)、PRISM data to utilize ex.BRNVT to CNCKG CY/CY (DR)（おそらくdry surcharge structureのみが利用可能）

2. **By "Country"（国別）**:
   - EagleXが要求された情報を国レベルで処理していることを意味する
   - **例**: Tender routing request ex.BRNVT to AEAJM CY/CY (RF)、PRISM data to utilize ex.BRNVT to AE XXX CY/CY (RF)（NVT to AJMがないため、国「AE」からサーチャージを適用）

3. **By "Combination"（組み合わせ別）**:
   - EagleXがデータの組み合わせで処理していることを意味する（国レベルでもルートがないため、ツールはservice scopeの共通サーチャージとPOR、DELの共通サーチャージ（国レベルである可能性がある）に基づいてサーチャージを取得）
   - **例**: Tender routing request ex.BRNVT to YEADE CY/CY (RF)、PRISM data doesn't have BR to YE -> to use common surcharges from LEE scope + common origin BR surcharges as well as common destination YE surcharges

### Comparison Inclusive Surcharges（比較包含サーチャージ）

#### 4.1 Eagle-X backend logic - Comparison Inclusive Surcharges
**サーチャージの重要性**:
- サーチャージは、各ルーティングのコストに関連する収益を生み出す鍵
- Service scopeレベルでは、各レーンで考慮される可能性のある約50のサーチャージがあるが、顧客とPricerは主に主要なものに焦点を当てる

**EagleXの処理方法**:
- EagleXはEagle-Eye-Viewで、port pairレベルですべての自動評価サーチャージを考慮する
- これが利用できない場合、Service scopeレベルのサーチャージを考慮し、収益機会が見落とされないようにする

**サーチャージの変動要因**:
- 各port pairは、Service scopeに応じて、Origin point、ocean transit中、destination pointで異なるサーチャージセットを持つ
- これらは、port-pairs、receiving / delivery terms、cargo type、extra requirements（HAZ、HEA）などによって異なる

**Comparison Include列**:
- これらはComparison Include列にアルファベット順にリストされ、EagleX backend計算に考慮される
- ただし、50のサーチャージすべてが必ずしも各レーンに適用されるわけではない（一度にすべて）

#### 4.2 Applicable Surcharges from Prism
- **定義**: 顧客の/Pricingの主要要件（origin and destination port pairs、delivery terms、cargo type）に適用される主要サーチャージを指す
- **データソース**: Pricing Simulation (PriSim)に基づく

### FRT Control Panel / Pricing Operation（FRT Control Panel / Pricing操作）

#### 5.1 FRT Control Panel - Button Overview（FRT Control Panel - ボタン概要）
**使用方法**:
- 各port pairにOffer Rateを設定するには、[Offer Rate]列の上部にある[FRT Control Panel]をクリック

**Benchmark（ベンチマーク）**:
以下の5つの条件を選択可能：
1. **LT MRG**
2. **Current FRT**
3. **Target CM/TEU**
4. **Formula**: 希望する式をそれに応じて作成可能
5. **Offer Rate**: さらに調整したい場合は、このオファーレートを選択可能

**Adjustment Type（調整タイプ）**:
以下の2つの条件を選択可能：
1. **Amount**
2. **Ratio**

**Filter Condition（フィルタ条件）**:
以下の7つの条件を選択可能。選択した条件に基づいて、リストボックス内の候補が更新される：
1. **Service Scope Code**
2. **Origin**
3. **Destination**
4. **Port Pair**
5. **Blank Row**: Blank RowのみにOffer Rate Calculationを適用可能
6. **Selected Row**: Selected Rowのみに適用可能（列AにYがマークされている場合）
7. **Filtered Row**: ドロップダウンでフィルタリングされたレーンに適用可能

**Adjustment Amount（調整金額）**:
- 計算に追加できる値（+/-値）

**Apply Same Rate to All in Rate（All in Rateに同じレートを適用）**:
- このチェックボックスにチェックを入れ、Runボタンをクリックすると、Offer Rate列に入力するレートがAll in Rate列にも反映される

#### 5.2 Offer Rate with Benchmark: Formula（ベンチマークによるオファーレート: 式）
**計算式**:
- **LT MRG + OIH + DIH + Add on + Hidden Cost = Offer Rate**
- **O.ARB + MRG + D.ARB = LT MRG**

**自動入力**:
- LT MRG列の値は、PricerがLT MRGを取得すると自動入力される
- 「Door」delivery termを要求するレーンのInland Haulage値は、IOPの提出に従って自動入力される
- ただし、Pricerは必要に応じて、ハイライトされた黄色のエリアでこの自動入力データを修正可能

**式の構築**:
- オファーレートを構築するには、LT MRG、OIH、DIH、Add on、Hidden Cost列内の任意の値セットを合計可能
- BenchmarkをFormulaに設定し、Formula Sectionの下で合計したい列ヘッダーにチェックを入れる > Runをクリック
- このページの例では、FRT control panelの5つのヘッダーすべてがクリックされている。これは、5つの列すべての値が合計され、Offer rate列の値になることを意味する

#### 5.3 Offer Rate with Adjustment Amount（調整金額によるオファーレート）
**使用方法**:
- Adjustment Amountは、FRT Control Panelでオファーレートを設定する迅速な代替方法
- **例**: BenchmarkがLT MRGに設定され、値100、200、300で調整されている場合、これらの増加により、以下の画像のようにオファーレートがそれぞれ増加する

**注意事項**:
- PricerがFRT Control Panelで調整金額を修正すると、この金額はFRT Control Panel (Add On)列に反映される
- Pricerは、FRT Control Panel (Add On)に手動で値を入力しないことを推奨（手動入力は、PricerがFRT Control Panel調整金額を再度実行すると上書きされる可能性がある）
- Benchmark Offer RateはLT MRGと同じように機能する。オファーレートの値は調整金額に応じて修正される

#### 5.4 Offer Rate with Benchmark: Current FRT（ベンチマークによるオファーレート: 現在のFRT）
- **使用方法**: BenchmarkをCurrent FRT（Current FRT = Current contract rate）に設定すると、調整金額ボックスの値が現在のレートの上に追加され（該当する場合）、新しいオファーレートが作成される
- **例**: このスライドの例では、顧客は現在40ft High Cubeのみを予約している。これは唯一の適用可能なcargo typeであるため、オファーレートは40ft HC Current OFTの上に2000の調整金額のみを考慮する

#### 5.5 All in Rate - Expected CM（All in Rate - Expected CM）
**一般的な状況**:
- 一般的に、顧客はTarget ratesなしでRound1 Tendersを送信する
- オファー（rates and surcharges）と顧客のリクエスト（surcharges）を比較することは定量化が困難
- オファーレートとApplicable SurchargesをAll-In Rate（Expected CMを提供）に追加するのが最善

**All-In Rateの生成**:
- Reference Base列で選択されたsurcharge structureに応じて、異なるレベルのAll-In ratesを生成可能
- この選択の後、[Surcharge Update]をクリック > その後、[All In Rate Calculation]をクリック

**Reference Baseのオプション**:
- **Customer's Request**: Pricerが「Possible applicable surcharge」で設定したsurcharge structureに基づく
- **Current Contract**: 顧客の現在の契約に基づくsurcharge structure
- **LT MRG**: Trade marketingが提出したLT MRG structureに基づくsurcharge structure
- **All-In**: PRISMで適用可能なすべてのサーチャージを含むsurcharge structure
- **Subject all**: PRISMで適用可能なすべてのサーチャージにsubject toのsurcharge structure

**計算式**:
- [Offer Rate] + [Offer Rate - Subject/Fixed] = [All In Rate]
- **注意**: このレート構造は、all-in rate、expected CMを計算するためにのみ使用される（オファーされたsurcharge structureは「Possible Applicable Surcharge」で設定されているため）

#### 5.6 Base Rate Calculation（Base Rate計算）
**Base Rateの定義**:
- Base Rateは、顧客に提示する最終レートオファーが配置される列
- Base Rateを計算するには、Pricerは[Base Rate Calculation]をクリックし、適用行を選択し、[Calculate]をクリックするだけ

**計算式**:
- [All In Rate] - [Possible Applicable Surcharges] = [Base Rate]

**オプションステップ**:
1. **Round up to nearest**: Pricerの希望に応じて計算を最も近い数字（例：5、10）に丸めるのに役立つ
2. **Surcharges to be included**: 選択したサーチャージ数量をbase rateに含める（ただし、レート構造は変更されない）

#### 5.7 Rate Breakdown Area（レート内訳エリア）
**内訳の表示**:
- All in Rateは、rates breakdown sectionで個別の部分に分解される
- Surcharge conditions（subject toまたはfixed）は「Applicable Rate Structure」列に自動設定される
- 顧客のTenderにエクスポートする必要がある列情報には、行1に番号タグが付いている
- [Y/M means Yes, it is a mandatory column pricers need to input // Y means Yes, but it is an optional for pricer to input]

**確認事項**:
- a. Base Rateとsurcharge figuresに満足しているかどうかを決定。そうでない場合は、値またはsurcharge conditionを自由に調整
- b. レートがsurcharge conditionなしで表示される場合、またはsurcharge conditionが数量なしで表示される場合、またはconditionまたは数量がない場合、そのサーチャージはそのport-pairリクエストに適用されないことを意味する

**注意**:
- 見積内訳に満足している場合は、エクスポートセクションに直接進んでオファーを提出可能（DMTやその他の情報を入力する必要がない場合）
- 欠落情報に関する詳細情報が必要な場合は、Eagle-X Team (ghq.eaglex.pricing.support@one-line.com)に連絡

**行2の番号**: 顧客シートの列番号を示す

#### 5.8 All-In Rate - Manually amending surcharges（All-In Rate - サーチャージの手動修正）
**手動調整**:
- Pricerは黄色のエリアで個別のサーチャージ（サーチャージの追加または削除）を手動で調整可能
- これは、固定サーチャージセットのみを提供するreference baseと混同しないこと

**手動調整時の注意事項**:
1. サーチャージの文字間にスペースがないこと
2. 複数のサーチャージはカンマのみで区切られる
3. セル内の最後のサーチャージの後にカンマが続かないこと
- [All In Rate Calculation]をクリックして、更新されたAll In Rateを確認

**注意**:
- サーチャージを手動で調整する場合、[Surcharge Update]ボタンを再度クリックする必要はない（[Surcharge Update]は手動調整を上書きするため）

**例**:
1. Offer Rate - SubjectはOBSとTHDを表示（fix Reference Base = Customer's Requestに従って）。OBSとTHDが削除されなかった場合よりもAll-In rateが高い（オファーレートにsubject to surchargesが含まれるため）
2. Offer Rate - SubjectはOBSとTHDを表示しない（両方が手動で削除された）。OBSとTHDがinclusiveと見なされるため、All-In rate値が低い

#### 5.9 Copying amended surcharges to multiple cells（修正されたサーチャージを複数のセルにコピー）
**手順**:
1. 転送したい情報を持つ単一のセルをコピー
2. 情報を貼り付けたいターゲットエリアをハイライト
3a. **オプション1**: "Home"タブの下 > "Find & Select"をクリック > "Go To Special"を選択 > "Visible cells only"を選択
3b. **オプション2**: キーボードショートカットを使用。Alt + ;（Altとセミコロンを一緒にクリック）で、表示されているセルのみを選択
- **代替**: このビデオを参照: https://www.youtube.com/watch?v=AITgQcxFfJI&t=77s

#### 5.10 Pricing Operation as per Target CM（Target CMに基づくPricing操作）
**前提条件**:
- このプロセスは、すでにrouting costを取得していることを前提とする

**手順**:
1. Target CM（per Unit）を入力 - 最終的に持つCMレベル（約）
2. Target CMはrouting costに対して逆計算され、提供を検討すべきrequired Freight levelを提供する（ただし、surcharge structureなしのオファーレートのみ）
3. ルーティングがない場合（コストなし）、その行はゼロのままになる
4. Target CMは最終CMと同じではない。Expected CM（per TEU）が最終CM（オファーレートと提供を検討すべきsurcharge structureを考慮するため）

**Target CMの利用方法**:
1. [FRT Control Panel]をクリック
2. Benchmarkを「Formula」として選択
3. Formulaで「Target CM +E2E Cost」をクリック
4. [RUN]をクリック
- **注意**: CM after included subject to surcharges into calculation

#### 5.11 Other columns that needs filling out（入力が必要なその他の列）
- 顧客のTenderに従って入力が必要だが、標準的なEagle-X pricing列の一部ではない列は、右端に表示される
- 顧客のT&C notesに従って、これらの要件を考慮すること

**Summarize Surcharge Tariff**:
- [Set Surcharge]と[Update Condition]ボタンの下で選択して適用したものを確認できるボタン
- 列CIの下にある
1. [Summarize]をクリック
2. 要約サーチャージtariffを入力したい列ヘッダーをクリック
3. [OK]をクリック

#### 5.12 Customize OBS Tariff per different Quarters（四半期ごとのOBS Tariffのカスタマイズ）
- Pricerは、ドロップダウンから各四半期の異なるOBS Quantumを選択可能。これにより、OBS tariffがすぐに変更される
- Pricerは、以下のいずれかの方法で独自のカスタム数量を作成するオプションがある：
  1. Pricing Toolの値を直接変更
  2. OBS Masterワークシートに移動 > 最後の行までスクロール > 新しいカスタムOBSを追加。これにより、カスタムOBSが保存され、簡単に取得可能

#### 5.13 DMT data retrieval / DMT offering（DMTデータ取得/DMTオファリング）
**Set DMTボタン**:
- [Set DMT]ボタンをクリックして、free timeオファーを設定し、Tariff DMT情報を取得

**手順**:
1. **適用行の選択**: All Rows、Selected Rows、またはFiltered Rowsのみに適用するかどうか
2. **D&D Itemの選択**: 提供したいD&D Item（複数選択可能）
3. **ベンチマークの選択**: 使用したいベンチマーク：
   - > offered based on current "Contract DMT"
   - > offered based on ONE "Tariff"
   - > offered by matching "Customer's Request"
4. **DMT Tariff populationのTierを選択**: either lowest tier、highest tierなど
5. [Apply]をクリック

**重要事項**:
- Customer's Request Data Source MUST be in a numeric type so that the information can be copied over to DMT offering column

**Customer's Requestが選択された場合**:
6. ポップアップが、DMT infoをオファーとして利用したい列を選択するよう要求
7. [OK]をクリック

**DMT情報の表示**:
- Customer's remarkからのDMTがDMT offer列にコピーされる
- "Contract DMT"が選択された場合、「Contractual Free time」列が利用される
- "Tariff"の場合、「DMT Tariff FT days」列が利用される

**Average Stay Days**: 顧客が一般的に必要とする/過去に使用した日数（freetime）
**Contractual FT**: 顧客が権利を持つ日数（freetime）
**DMT Charge**: 選択したtierに基づいて表示される

**注意**: Manual free time input in numeric type can be done as well

#### 5.14 Pricer's Remark - Decline Offer（Pricerの備考 - オファー拒否）
**確認事項**:
- この段階で、Pricerは確保を意図しているすべてのレーンに価格を設定したことを再確認可能
- レーンに見積もりが付けられていない場合、Pricerはそのレーンに見積もりを付けないことを明示的に述べる必要がある
- 見積もりが付けられておらず、declineとしてマークされていないすべてのレーンは、提出段階でエラーとして表示される

**手順**:
1. Decline Offer列にマーカー（Y）を付ける - 必須
2. ドロップダウンリストからdecline理由を選択 - 必須
3. 内部備考を入力 - オプション

#### 5.15 Other Than OFT information fill up（OFT以外の情報入力）
**変更点**:
- 過去、顧客から別のシートに情報を入力する追加リクエストがあった場合、Eagle-XはPricerに「0-2_OtherThanOFT」フォルダからファイルを見つけるよう要求していたが、Pricerにとって不便だった可能性がある
- 現在、Eagle-XはPricing Toolに別のタブを追加し、Pricerがファイルを見つける必要がなくなり、レートオファリングと同時に入力して提出しやすくなった
- 情報が取得され、CSTチームが各Tradeの提出を結合し、salesに送信するのを支援する

**注意**: 別のシートの代わりに、Pricing Toolに組み込まれる

### Export Data（データエクスポート）

#### 6.1 Export Data to Customer Sheet（顧客シートへのデータエクスポート）
**エクスポート手順**:
- PricerがPricing、DEM/DET、Decline、またはInternal Remarksなどをすべて入力し終えた後、顧客シートにデータをエクスポートするには、ツールの左上にある[Export]をクリックするだけで、データがエクスポートされる

**重要事項**:
- 一部の欠落情報が必要な入力である場合、Pricerはデータを正常にエクスポートできない可能性がある
- **例**: Not decline、but doesn't have "Base Rate" information
- Offer Lane、but no routing、and pricers didn't input "Trunk Service Lane" info
- ポップアップメッセージが表示され、入力が必要なセルが黄色でハイライトされる

**エクスポート後の確認**:
- データが正常にエクスポートされたら、データが適切にエクスポートされたかどうかを再確認することを推奨
- **ヒント**: Pricerは、[view] > [New Window]に移動してウィンドウを分割することで、簡単に確認可能

**データ確認方法**:
- データを確認するには、PricerはPricing Toolの行1-2にインジケーターがある列を確認する必要がある
- **行1**: Pricerの入力の必須（Y/M）またはオプション（Y）
- **行2**: Customer Sheet行番号

**意図的にスキップする列**:
- サーチャージが特定のTradeに適用されない場合、または入力する他の要件がTradeに関連しない場合がある
- Eagle-XチームにPricerが意図的にこの列をスキップしたことを知らせるには、2つのオプションがある：
  1. エクスポート前にPricing Toolの行1のインジケーターを「Y/M」から「N.A」に変更。その後、顧客シートの「Pricer」入力インジケーターが赤いテキストに変更される
  2. 「Pricer」入力インジケーターを直接赤いテキストに変更（顧客シートの行3-4）

#### 6.2 Export Surcharges in Local vs USD Currency（ローカル通貨とUSD通貨でのサーチャージエクスポート）
**デフォルト表示**:
- Pricing Toolのサーチャージは、デフォルトでローカルtariff通貨で表示される

**エクスポートオプション**:
- Pricerは、サーチャージをローカル通貨またはUSD通貨でエクスポートするかどうかを選択するオプションがある
- Export as local currency = サーチャージの上部のインジケーターは「A」として表示される必要がある
- Export as USD currency = Pricerはインジケーターをexport (USD)から「B」に変更する必要がある

**注意**: Eagle-Xチームは、計算に最新の3ヶ月平均為替レートを使用

#### 6.3 Export Base Rate in a Different Currency（異なる通貨でのBase Rateエクスポート）
**使用方法**:
- Base Rateは、一般的にUSDで提供されるが、他の通貨でも顧客シートにエクスポート可能
1. Export by Non USDを「Y」として選択
2. Pricerが使用したい通貨を選択
3. 選択した通貨に基づいて為替レートが自動更新される

**注意**: Eagle-Xチームは、計算に最新の3ヶ月平均為替レートを使用

### Pricer Submission（Pricer提出）

#### 7. Pricer Submission
**提出手順**:
- 顧客シートの情報に満足したら、[Submit]をクリックしてPricingをCSTに提出して統合
- これにより、Tradeの提出が他のTradeのPricingとsales提出と結合され、顧客に送信される
- [Submit]をクリックする前に、顧客シート情報に100%満足していることを確認

**提出後の処理**:
- クリックすると、更新されたCustomer SheetのファイルがPricer Submissionフォルダにアップロードされる
- 再提出の場合、以前の提出ファイルは「old」フォルダに移動され、常に最新ファイルがPricer submissionフォルダに残る

**メッセージ入力**:
- Salesに含まれる無料テキストメッセージを入力できるポップアップボックスがある（Pricer提出メールに含まれる）

### Subsequent Rounds Pricing Tool（後続ラウンドPricing Tool）

#### 8. Subsequent Rounds Pricing Tool
**R1からの作成**:
- 後続ラウンドのPricing Toolは、R1 Pricing Toolファイルから作成される
- R1を終了した後、元のフォルダに保存して保管することを忘れない
- **注意**: R1 rate structure is captured from R1 surcharge section

**新しいセクション**:
- ライトブルーの色で、いくつかの情報を表示する新しいセクションが表示される：
  - R1 Offer Rate and Structure
  - Customer Target Rate（該当する場合）
  - オファーと顧客のターゲット間のレートギャップ（該当する場合）
  - 顧客からのその他のフィードバック（該当する場合）

**Pricing操作**:
- Pricing操作に関しては、FRT Control Panelボタンを使用してR1と同様に実行可能
- LINK: HOW FRT CONTROL PANEL WORKS? (P.44)
- Pricerは行1-2にinput requirement indicatorも表示される。一部のTenderでは、salesがR2レートのみの入力を要求する場合があるが、一部のTenderでは、サーチャージ、free time、その他の情報も入力が必要な場合があるため、これらの2行を確認

**削除/追加されたレーン**:
- 後続ラウンドでは、このラウンドに合格できなかったため削除されたレーン、または新しく追加されたレーンがある場合がある
- この場合、Pricerは「Remarks」にインジケーターを表示可能
- **新しく追加されたレーンの場合**: Customer remarkにこの新しく追加されたレーンインジケーターがある
- **削除されたレーンの場合**: Pricerの入力は不要で、入力は統合ファイルにsalesに取得されないことに注意

### Extra Buttons Functions（追加ボタン機能）

#### 9. Extra Buttons Functions

##### 9.1 Add On - Add
**使用方法**:
- PricerがOFT計算に追加料金/要因を追加したい場合に使用可能
- Pricerは項目名を入力し、これがHidden Costかどうかを示す必要がある
  - Hidden Costとして識別された場合、E2E Costの上に追加される
  - Hidden Costでない場合、E2E Costに追加されない

**手順**:
1. [Add On-Add]をクリック
2. Item Nameを入力
3. これがhidden costかどうかを選択
4. [Insert Item]をクリック
- その後、Pricing Toolはこのadd onの新しい列を自動生成

##### 9.2 Surcharge - Add
**使用方法**:
- Pricerがサーチャージセクションにサーチャージを追加したい場合に使用可能（サーチャージが既存のものである場合、通知するポップアップメッセージが表示される）

**手順**:
1. [Surcharge-Add]をクリック
2. サーチャージコードを入力
3. [OK]をクリック
- その後、Pricing Toolはこのサーチャージの新しい列を自動生成

##### 9.3 New Lane
**使用方法**:
- Pricerが任意のTenderに「New Lane」を提供したい場合に使用可能

**手順**:
1. [New Lane]をクリック
2. Mandatory Fieldsに情報を入力
3. [Done]をクリック
- その後、Pricing Toolはこの新しいレーンの新しい行を自動生成
- Lane ID命名規則は「New_Trade_no.」となり、顧客シートにページの下部にエクスポートされる

**注意**: This is just for only display purpose, it doesn't involve the surcharge condition setup

### Troubleshooting（トラブルシューティング）

#### 10. Troubleshooting

##### 10.1 Button not showing/working/running/Calculating（ボタンが表示されない/動作しない/実行されない/計算されない）
**原因1: 拡張画面**:
- Macro（ボタン）が適切に動作しない理由の1つは、拡張画面である可能性がある
- これを修正するには、HDMIを抜いてラップトップ画面のみで作業するか、「Extended」の代わりに「Duplicate」を使用することで、この問題を緩和可能
- 画面シフトのホットキーは、キーボードで + Pを押すこと。その後、「Duplicate」を選択
- または、タスクバーのWindowsボタン > Settings > Systemを使用可能
- その後、display setting > multiple displays >

**原因2: 非表示の行/列**:
1. エラーポップアップメッセージで[End]をクリック
2. Excelで任意のセルをクリック > 「Ctrl-A」をクリックしてExcelのすべてのセルを選択
3. 任意の列を右クリック > Unhideをクリックしてすべての行と列を非表示解除
4. 計算オプションを再度試す

##### 10.2 Page or Page Columns not Scrolling（ページまたはページ列がスクロールしない）
**解決方法**:
- Pricing Toolでページを左右にスクロールできない場合、以下の2つのオプションでpaneをunfreeze可能：
  1. view sectionの下のFreeze Panesアイコンを使用 > Unfreeze Panes
  2. 「Search」を使用してfreeze panesと入力。そこからpaneをunfreeze可能

##### 10.3 Button cannot be clicked（ボタンをクリックできない）
**原因: Google Sheetでの直接作業**:
- この問題を引き起こす理由の1つは、Pricerがファイルをダウンロードする方法である可能性がある
- したがって、Google Sheetで直接開いて作業しないこと
- Google SheetでPricing Toolを開いた後、download functionを使用

**問題**:
- Google Sheetは.xlsmファイルを.xlsxに変更し、このファイルタイプではmacroが動作しない
- Google Sheetが開かれた後、ここからダウンロードすることはオプションではない（ファイルは.xlsxになるため）

**推奨方法**:
1. File explorerから開く
2. G-Driveでファイルを開かずにダウンロード

**クイック修正**:
- ボタンが適切に動作しない場合のクイック修正：
  1. 現在開いているすべてのExcelファイルを閉じる
  2. File explorerを使用するか、タスクバーの検索を使用
  3. 以下のパスを入力：
     - C:\users\username\AppData\Local\Temp\Excel8.0\
     - C:\users\username\AppData\Local\Temp\VBE\
     - 注意：一般的に、usernameはfirstname.lastname（それぞれ最大8文字）
  4. MSFormed.exdファイル（キャッシュファイル）を削除
  5. その後、Pricing Toolファイルのボタンが動作するはずなので、Pricing Toolファイルで再度試す
- 「username」を自分のものに変更して動作させる
- Windowsバージョンによって異なるアプローチがある場合がある（例：キーボードのボタンを使用/タスクバーで検索機能を表示）

##### 10.4 Macro errors / How to remove restrictions（Macroエラー/制限の削除方法）
**問題**:
- Macroに関する問題を経験する場合がある
- REDでハイライトされた通知で「Microsoft has blocked macros」と記載されている場合

**解決方法1: ファイルのプロパティからUnblock**:
- このセキュリティを解除するには、File explorerでファイルの場所を開く
- > Pricing Toolファイルを右クリックし、「Properties」を選択
- > Propertiesウィンドウの下部で、「Unblock」にチェックを入れて、ファイルでmacroが動作するように許可

**解決方法2: Trust Center Settings（信頼センター設定）**
**STEP 1: TRUST CENTER SETTINGSに移動**:
- Excelファイルのスクリーンショットに従って手順を実行

**STEP 2: TRUSTED LOCATIONS（信頼された場所）**:
- 以下の手順で新しい信頼場所を追加：
- Pathはここからコピー可能: G:\Shared drives\Eagle-X-FY24ForPricer

**STEP 3: ActiveX Settings（ActiveX設定）**:
- 「Enable all controls without restrictions…」を選択

**STEP 4: MACRO SETTINGS（Macro設定）**:
- スクリーンショットに従って3つのポイントすべてにチェックを入れ、OKをクリック

### 関連資料
- [[20251121_EagleX-Pricing-Tool-Calculation-Logic]]: EagleX Pricing Toolの計算ロジック
- [[04_Memory/Work/ONE/DX/Eagle-X/20251118_Eagle-X-Pricing-tool説明-機能と使い方詳細.md]]: Eagle-X Pricing toolの詳細説明
- [[04_Memory/Work/ONE/Business/Shipping/20250113_Pricingのプロセス-運賃設定の方法と手順.md]]: Pricingのプロセス全体

### 確認事項
- [ ] 実際のPDFファイルを開いて詳細な図表を確認
- [ ] 各セクションの詳細な手順を確認
- [ ] トラブルシューティングの実際の画面を確認

## 次アクション
- [ ] SOPの詳細な手順をMemory Noteに変換（[[04_Memory/Work/ONE/DX/EagleX/]]）
- [ ] 関連する計算ロジック資料と統合
- [ ] 実際のPricing業務で使用する際の参考資料として活用

#eaglex #pricing-tool #sop #fy25 #dx #inbox #tool-overview #data-retrieval #frt-control-panel #export-data #troubleshooting

