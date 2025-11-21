# Space Control 業務ガイド

## 概要
Space Control業務の包括的なガイド。日次・週次・月次のタスク、主要な業務フロー、ツールの使い方などをまとめています。

## 📅 日次タスク

### 朝のルーティン（10時まで）

#### 1. スペース更新
- **対象**: AX1/2/3/4（Opus + ONEMIS + PAITA: AX2,3）
- **期限**: 10時までに更新
- **手順**:
  1. OPUSで最新のBooking状況を確認
  2. Control by HOで数値を取得
  3. ONEMISファイルを更新
  4. PAITAメールを送信（AX2,3のみ）
     - **件名**: `<MIS REPORT>5.1.2_BKG_Space Control Analysis Report(Schedule)-GPX Revenue Lane is available`
     - **宛先**: ONEMIS: onemis@one-line.com (SYM: Groupmail)

#### 2. 船の遅延確認
- **ツール**: OPUS > Vessel Operation > Vessel Schedule > Long Range SKD Inquiry
- **確認事項**: 船の遅延がないか、スケジュール変更がないか
- **頻度**: 毎日確認

### 午後のルーティン（13:30まで）

#### 3. 日次サマリー更新
- **対象**: AX3, CLIQQ, RFs
- **期限**: 13:30に更新
- **内容**: Summaryファイルに最新のスペース状況を反映

#### 4. RF, CLIQQ更新
- **頻度**: 月/水にSummaryファイルで更新

---

## 📆 週次タスク

### Pusan入港4日前のClosing作業

#### Closingのタイミング
- **ルール**: Pusan入港4日前
- **例**: 24日の昼の1時入港の場合
  - 24時間前までに全船積み情報を提示
  - 24日の4日前 = 21日のCOBがClosing（その日を含める）

#### Closing前の作業フロー

##### Step 1: Control by HOで数値を取得
- **場所**: OPUS > Sales Management > Space Control > Control by HO
- **設定**:
  - LWT、AX4、OriginをALL
  - VVDを指定（HYVTなどの頭は船の名前なので変わらない）
  - 4週間ごとに動いているから4週前を打てば前のVoyageを見れる

##### Step 2: AX4ファイルに数値を貼り付け
- AX4のファイルにControl by HOの数値をBooking OPUSに貼り付けていく
- **重要**: マニュアルでベタ打ちするときは緑にする（暗黙のルール）

##### Step 3: CLL（Container Loading List）の確認
- **場所**: OPUS > Service Management > Booking/Documentation > Operation > Loading/Discharging List > Container Loading List (CLL)
- **注意点**:
  - Control by HOの数値とは違う
  - コンテナを基軸に見ている
  - Bookingを受けただけだと認識されない
    - 空ブッキングもいる
    - 空コンを取りにきたときにBooking NumberとContainer Numberが紐づく
    - Container Numberが入っていないためCLLには認識されない

##### Step 4: TEUの列を追加する
1. いったん全部2を入れる
2. D2は1に変更
3. OTはBooking NumberをOPUSに入れて、念の為VOIDを確認
   - VOIDがゼロ（何も入っていない）であれば1としてカウントしてOK
4. Pivotして、それを大本のAX4のファイルに戻す

##### Step 5: CLLのUpdate方法（詳細）
- DELでMXを除く
- NGBとPUSも同様に行う
- T2は1でカウントしていい（SOC）
- F5はBooking NoをBooking Inquiryで入れる（2本のコンテナと10本のVoid）×2
- Elynに精緻な数を聞く、PUSはCatharine
- Final figure tableを聞く

##### Step 6: VSLクローズ
1. BILLYにコンテナリストをリクエスト
2. OPUS CLLをダウンロードして数値を集計
3. Baseportで最終積載数を集計
4. 集計後、BILLYにVSLクローズを伝える
5. PUS TS積載 - KRPUS TS @'CB Song' Loading（CLLを集計）

---

## 📋 Roll List作成フロー

### Roll Listとは
- 積み残し（Rollover）が必要な貨物のリスト
- BSA（Booking Space Allocation）を超えた場合に作成

### Roll List作成のタイミング
- **Closing date**: Roll List（Standby list）を送る
- **最優先**: これを最優先に入れてOK

### Roll List作成手順

#### Step 1: Control by HOで最新状況を確認
- Control by HOを使って最新の状況に更新
- ONE Quoteの数のUpdateの仕方:
  - Control by HOでBooking firmはゼロ
  - マイナスの人たちにRollリスト送ることを依頼（ただしダイレクトポートは送らない）

#### Step 2: Roll Listの作成
- **対象**: BSAを超えた貨物
- **除外**: ダイレクトポートは基本Rolloverしない（ダイレクトポートとは実際に船がよるところ）
- **注意**: RFとOOGはロールしない（基本ルール）

#### Step 3: POLに送信
- POLにロールリスト提出のメールを送信
- スペースコントローラーがPOL提出に基づいてロール/オーバーを決定

#### Step 4: Advance Listの作成（余裕がある場合）
- **目的**: 後ろの船から前の船に持ってくる
- **ルール**: Advance Listは多めに作ってOK、これをRollしても下に戻るだけだからなんの影響もない
- **例**: Billyにアドバンスリストをとって30TEU900トンを選ぶ

### Roll Listの判定基準

#### Show up Ratioについて

##### Show up Ratioとは
- **Show up（実際の搬入量）**: 中国オフィスやフロントオフィスによる予測値
- **定義**: Firm Bookingに対して、実際にゲートイン（コンテナヤードに搬入）される割合
- **計算式**: Show up Ratio = 実際の搬入量（TEU）÷ Firm Booking（TEU）× 100

##### 基本的な考え方

**例1: 標準的なケース**
- Firm Booking: 100TEU
- Show up Ratio: 50%（予測）
- **実際の搬入量**: 50TEU
- **BSA**: 50TEU
- **結果**: ロールオーバー（積み残し）は発生しない ✅

**例2: Show up Ratioが上がった場合**
- Firm Booking: 100TEU
- Show up Ratio: 60%（予測、アグレッシブな運賃調整などで上昇）
- **実際の搬入量**: 60TEU
- **BSA**: 50TEU
- **結果**: 10TEU分のロールオーバーが発生する可能性 ⚠️

##### Show up Ratioの標準値

**一般的なShow up Ratio（LAWC貿易）**
- **標準**: 50%が一般的
  - 特にNVO（Non-Vessel Operating）顧客の場合、先にBookingを入れる傾向がある
  - Name Accountがある場合は、比率に基づいて先にBookingを入れる
- **South PRC（華南）**: 50%が標準
- **North China（華北）**: 
  - AX1: 40-45%
  - AX2: 50-55%
  - AX3: 60-70%
- **Central China（華中）**: 
  - AX1: 50-55%
  - AX2: 55-60%（レート調整後は62%の実績あり）
  - AX3: 60-70%

**季節・市場状況による変動**
- **Winter time slack season（冬季閑散期）**: 50-60% max
- **通常時**: 50-55%
- **レート調整後**: 約10%増加
  - マーケットに合致: 45-50%または55%
  - マーケットに合致しない: 35-40%

**特別なケース**
- **GRI（General Rate Increase）前**: Show up率が非常に高くなる傾向
  - 例: 華南・厦門・汕頭でGRI前駆け込みでShow-up 80%以上
- **RR（Rate Reduction）前**: その前に予約が急増し、Show up率が非常に高くなる傾向

##### 予測の精度とタイミング

**予測の性質**
- **将来分は予測値**: 「今週＋1週＋2週＋3週」といった将来分はあくまで予測値
- **ピックアップ率ベース**: ピックアップ率やShow up比率に基づいた推測
- **出航週が近づくまで仮定**: このすべては、出航週が近づくまで、あくまで仮定に基づいています

**精度が上がるタイミング**
- **CYゲートオープン**: 通常、CYゲートは本船到着の3～5日前に開く
- **空コンテナのピックアップ状況**: 空コンテナのピックアップ状況などにより、より正確な予測が可能になる
- **ゲートイン数**: ゲートイン数に基づいて、実際にその週の本船をクローズする際には、彼らに確認すればその時点の数字がわかる

##### Fresh show upとは

**Fresh vs Rollover**
- **Fresh**: Rolloverではないもの（新規Bookingから実際に搬入されたもの）
- **Rollover**: 前の船から積み残されたもの

**Fresh show upの重要性**
- Fresh BookingのShow up率を正確に把握することで、将来のスペース需要を予測できる
- 例: NingboでFresh booking 1,048TEU、Show up率40%と予測 → Forecast 450TEU

##### Show up Ratioに影響する要因

**1. レート競争力**
- **マーケットに合致**: Show up率が向上（45-50%または55%）
- **マーケットに合致しない**: Show up率が低下（35-40%）
- **レート調整後**: 約10%の増加が期待できる

**2. マーケット状況**
- **GRI前**: Show up率が急上昇（80%以上になることも）
- **RR前**: 予約が急増し、Show up率が高くなる
- **閑散期**: Show up率が低下（50-60% max）

**3. 顧客タイプ**
- **NVO**: 先にBookingを入れる傾向があり、Show up率が低め
- **Name Account**: 比率に基づいて先にBookingを入れる
- **Direct Account**: Show up率が比較的高い傾向

**4. 地域・サービス**
- **AX1**: 一般的にShow up率が低め（40-50%）
- **AX2**: 中程度（50-60%）
- **AX3**: 比較的高め（60-70%）
- **AX4**: サービスによって異なる

##### Show up Ratioの活用方法

**スペース計画への活用**
1. **BSA設定**: Show up Ratioを考慮してBSAを設定
   - Firm Booking × Show up Ratio = 予想搬入量
   - 予想搬入量 ≤ BSA であれば、ロールオーバーは発生しない

2. **Forecast作成**: Show up Ratioを基にForecastを作成
   - 例: Fresh booking 1,048TEU、Show up率40% → Forecast 450TEU

3. **Roll List作成**: Show up Ratioが予想より高い場合に備えてRoll Listを準備

**注意点**
- Show up Ratioは常に変動する
- マーケット状況、レート競争力、季節要因などを総合的に判断する必要がある
- 過去の実績データを参考にしつつ、最新のマーケット情報を反映させる

### Roll Listの特別ルール

#### CN/HKGトランジット貨物
- 1週間前にチェック
- BL番号で選択（スプリットブッキングを避ける）

#### 木曜日のVSLクローズ
- 週16 VSLをクローズ後、午後に週17 VSLのロールリストリクエストを送信

#### DNR（Do Not Roll）
- DNR = Do Not Roll
- 主にVNの貨物
- 上海でロールする場合:
  - SHA ETAの3日前ならPOL側のOPUSデータ変更でOK
  - それ以降であれば、こちら側でロールの連絡をする

---

## 🔄 Wayport処理

### Wayportとは
- 複数港を経由する航路で、中間港でのスペース活用
- 空コン移動だけでなくCODもWayportを使う

### Wayportの主要ルート
- **HK,YTN,KEL,NGB,SHA,PUS→MX**
  - PUSに行く前までで、空コンを運びたいなどが来る
  - CL→HK前後でVVDの名前が変わる
    - CL: TDR（Terminal Departure Report）→2700
      - ROB：2700
      - HK：-500
      - 南米からの貨物はYTNでドカンと落ちる
      - NGBで今度はドカンと積む
      - 上記を考慮して、余ってるスペースをPusan前で活用する

### Wayportの処理パターン

#### SCENARIO 1: Short-haul space
- CNNGB/CNSHA TO KRPUS WAYPORT (DUMMY WAYPORT TO CATER ORIGIN ROLLOVER) | 50/500

#### SCENARIO 2: PEAK SEASON
- ORIGIN WILL COME TO US FOR MORE WAYPORT SPACE FOR THEIR ROLLOVER

#### SCENARIO 3: RESCUE PLAN
- AS A RESCUE PLAN, IN THE EVENT OF PORT OMISSION

### Wayportの注意事項
- **AX4**: 基本的にWayportのリクエストはない（2港しかよらない）。AX1はある
- **EX SEA, ISC T/S CARGO VIA CN (CHINA) PORTS**: を考慮に入れる
- いろいろ問い合わせがあるが、このWayportはいろんな航路が通っているため、自分じゃなくてもいいやの精神で航路によっては断りまくってる

---

## 📊 Master Constraint Table更新

### 更新の全体フロー
```
1. BKがデータを固める
2. データのコピー
3. 対象月フォルダの作成
4. データの編集（AX1-3の削除、AX4のみ残す）
5. VVDと対象WKの確認
6. JP（翌月分）の作成
7. OQ（翌月分）の作成
8. Master ConstraintへのUpload
9. 保存と確認
```

### 詳細手順

#### Step 1: データのコピー
- **コピー元**: `G:\Shared drives\LW AP\4_Convert_AP`
- **内容**: BKが固めたデータ

#### Step 2: 対象月フォルダの作成
- **場所**: `G:\Shared drives\Latin West Coast\Space Control\AX4\Standby\2025`
- **構造**: 各月ごとのフォルダを作成

#### Step 3: データの編集
- AX1、AX2、AX3のデータを削除
- AX4のデータのみを残す

#### Step 4: JP（翌月分）の作成
- どれか1つを選ぶ
- Submission OfficeをTYO以外を削除
- 対象月を翌月に変更
- 翌月のVVDをコンマつなぎで入れる（スペースは不要）

#### Step 5: OQ（翌月分）の作成
- 前月からOQの翌月分をコピー
- 対象WKとVVDをUpdate
- ONE Quoteに300TEUあげている

#### Step 6: Master ConstraintへのUpload
- **場所**: OPUS > Sales Management > Space Control > Standby Management > Master Constraint Table Creation
- 各WKのデータを1つずつUpload
- Upload後は必ずSave

#### Step 7: 確認
- 翌月のVVDで検索して、JPの分とOQの分を削除
- JP+1をアップロード
- 翌月のVVDで検索して、OQをアップロード
- 翌月VVDで正しくJP+1とOQが入っているか確認

---

## 🚨 緊急時対応

### Misconnection発生時

#### 対応フロー
1. Rollのリスト一覧への影響を確認
2. 振り先をチームに相談
   - PUS到着＋通常2日間のトランシップ時間を考慮して、どのサービスにのせるべきか
3. 調整がついたらその結果をBillyに報告
4. 関連するLoading OfficeのSalesもCCに入れる

### 貨物緊急時計画（Omission / gap filling）

#### SWAP
- POL間のスペース交換
- オリジンからCOVコストをアドバイス

#### FIFOロジック
- 最大1週間ロールオーバー

#### Advance load
- 前積み

#### ROB
- コスト分析、コスト考慮
- 運営コスト（restow）

---

## 🛠️ 主要ツールとシステム

### OPUS
- **URL**: http://10.65.224.11/opuscntr/SignOn.do
- **主要機能**:
  - Control by HO
  - CLL（Container Loading List）
  - Booking Inquiry
  - Master Constraint Table Creation

### ONEMIS
- **メール**: onemis@one-line.com (SYM: Groupmail)
- **用途**: 日次スペース更新

### 共有フォルダ
- **ASM**: `G:\Shared drives\Latin West Coast\Space Control\ASM`
- **BaplieVw**: `G:\Shared drives\Latin West Coast\Space Control\BaplieVw.zip`
- **AP**: `G:\Shared drives\LW AP\4_Convert_AP`
- **Standby**: `G:\Shared drives\Latin West Coast\Space Control\AX4\Standby\2025`

### Google Drive
- **EDI**: https://drive.google.com/drive/folders/1DbCuZlcib4aJ_BIFxAQauDeeutQ2_uXA
- **LTS & BSA共有**: https://drive.google.com/drive/folders/1P1i699tAGMalt8hxxPtY4UgYtv_So5RN (@ GOOGLE DRIVE STARRED)

---

## 📈 スペース管理の基本ロジック

### スペースリリース vs APロジック
```
CGM Sales target to sales office 
> Account Plan by sales office (to be within sales target) 
> Service lanes: AX1,2,3,4 
> SPACE 
> Ratio up/down depends on BSA + OQ
```

### スペースリリースのタイミング
- **t/s CN/HK**: 1週間前（VN/ID/MY）
- **BSAベース**: 最初にリリース
- **予測調整**: 営業予測をレビュー後に調整（POLに疑問がある場合/予測がない場合はフォローアップ）
- **BSA/調整配分**: SPCモジュールに更新（変更がある場合はレビュー&調整）

---

## 💡 重要なポイント

### Pusan Backlog
- **定義**: PUS Backlogは他のWeight portや前週などですでに中国からPusanにもってきているもの
- **Local**: Localの部分はLast minutesの作業
- **超過時**: もし超えてしまった場合は他のAXサービスと交換する（MXZLCのTS以外のものと）

### Fresh vs Rollover
- **Fresh**: Rolloverではないもの
- **A.POLとB.POLの違い**: Roll listは1BL=1BKみたいなのが多いと嬉しい（調整しやすいから）

### Owner's Merit
- **定義**: ONE船の場合、オーナーズメリットを可能な限りとりたい
- **特にTon**: 自然減で減った分取れる可能性が高い
- **確認方法**: 正確なオーナーズメリットを知りたい場合はプランナーに確認する

### 台風などで遅れる場合
- GVOに実際の時間を確認する（Elynも教えてくれるが）

---

## 📞 主要連絡先

### スペースコントロール関連
- **Elyn**: Final Figure確認、精緻な数値確認
- **Catharine**: PUS関連の精緻な数値確認
- **Billy**: KRPUS TS、コンテナリストリクエスト、VSLクローズ連絡
- **An cheng**: スケジュール確認

### マーケット関連
- **Michelle**: Ningboマーケット
- **Jason**: TingTao
- **Isaac**: XIAMENの報告、その後SCRC
- **Billy Wu**: Xiamenから現在のマーケットPriceの報告

### その他
- **Roberto**: ECM Space sharing
- **プランナー**: Owner's Merit確認

---

## 📚 関連ノート
- [[20251118_AX4-Space-Control-業務フローとツール]]
- [[20250113_Master-Constraint-Tableの更新方法-詳細手順]]
- [[20251121_Soon-Ang-Takeover-List-詳細版]]
- [[20251118_WK30-AX4-Space-Control-週次業務メモ]]

---

**最終更新**: 2025-01-13  
**作成者**: Space Control Team

#space-control #ax4 #work/one #work/one/dx #guide

