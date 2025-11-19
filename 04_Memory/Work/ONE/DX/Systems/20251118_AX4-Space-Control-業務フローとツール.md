# AX4 Space Control-業務フローとツール

## 概要
AX4 Space Control業務の詳細なフローとツールの使い方について記録したメモ。Wayport、CLL（Container Loading List）、Closing、APのアップロード、Misconnection発生時の対応などについて詳細に記載されています。

## 内容

### Wayportについて
- HK,YTN,KEL,NGB,SHA,PUS→MX
  - PUSに行く前までで、空コンを運びたいなどが来る
  - CL→HK前後でVVDの名前が変わる
    - CL: TDR（Terminal Departure Report）→2700
      - ROB：2700
      - HK：-500
      - 南米からの貨物はYTNでドカンと落ちる
      - NGBで今度はドカンと積む
      - 上記を考慮して、余ってるスペースをPusan前で活用する
      - カラコン移動だけでなくCODもWayportを使う
  - いろいろ問い合わせがあるが、このWayportはいろんな航路が通っているため、自分じゃなくてもいいやの精神で航路によっては断りまくってる
  - AX4は基本的にWayportのリクエストはない（2港しかよらない）。AX1はある

### Pusan入港4日前のClosingに向けて
- AX4のファイルにControl by HOの数値をBooking OPUSに貼り付けていく
- AX4のファイルにマニュアルでベタ打ちするときは緑にする（暗黙のルール）

### CLL（Container Loading List）
- Control by HOの数値とは違う
- コンテナを基軸に見ている
- Bookingを受けただけだと認識されない
  - 空ブッキングもいる
  - 空コンを取りにきたときにBooking NumberとContainer Numberが紐づく
  - 2本しか空コンをピックしていないということがわかる
  - Container Numberが入っていないためCLLには認識されない
- Pusanは10日以上おいておくとお金かかる
  - 2回ロールすると我々のCostにもなる、だから基本は１回まで
  - 基本RFとOOGはロールしない

### Closing
- Pusan入港4日前
  - 24日の昼の1時入港だと24時間前までに全船積み情報をしめないといけない
  - Docの3時間前にといわれても直しようがない
  - 24日の4か前の場合は1
    - その日を含める→だから21日のCOBがClosing

### Long Range SKD Inquiry
- Vessel Operation：Vessel Schedule
- これは毎日見る（船の遅延がないか）

### LocalとTS
- TSのほうが早く固まる
- RoughにLocalがどれくらい積まれるかPusanやNingboに聞く

### TEUの列を追加する
- いったん全部２をいれる
- D2は１に変更
- OTはBooking NumberをOPUSにいれて、念の為VOIDを確認する、VOIDがゼロ（何もはいっていない）であれば１としてカウントしてOK
- Pivotして、それを大本のAX4のファイルに戻す

### 釜山バックログとは
- PUS Backlogは他のWeight portや前週などですでに中国からPusanにもってきているもの
- Localの部分はLast minutesの作業
- もし超えてしまった場合は他のAXサービスと交換する（MXZLCのTS以外のものと）

### Show up Ratioについて
- 「Show up（実際の搬入量）」は、中国オフィスやフロントオフィスによる予測値
- 例えば、100TEUのFirm Bookingがあったとしても、Show up Ratioが50%と予測されていれば、実際には50TEUが搬入される想定
- この場合、BSAも50TEUであれば、ロールオーバー（積み残し）は発生しない
- ただし、もし、アグレッシブな運賃調整などでShow up期待値が60%に上がれば、10TEU分のロールオーバーが発生する可能性が出てくる
- マーケットによっては、RRがあると、その前に予約が急増することがあり、その場合はShow up率が非常に高くなる傾向にある

### カンボジアの貨物について
- カンボジア発の貨物も14TEUあって、もし足りない場合はそれはロールOKとAdeleに前に聞きました
- sineat.yuan@one-line.comが担当のようです
- カンボジアとは普段接点ないのですが、CLLからBKG#を確認して、Billyにロール貨物として連絡するもOKのようです

### AP
- July18のファイル（最新のAPのファイル）
- Loading office別のデータを見る
- BSAにデータを持ってくる
  - AP&ALCシートを使う
  - AX1-3を消してAX4だけのものをコピペ
  - Controll by HOでBSAを確認する
- WayportシートのBSAに貼り付ける
- Alocationを入れる
- →Control by HOの値をマニュアルでいれる
- 韓国にはすごい少なめにしたほうがいいい、最後に開放するのほうがいい

### Misconnectionが発生したとき
- Rollのリスト一覧への影響を確認する
- 振り先をチームに相談する
  - PUS到着＋通常2日間のトランシップ時間を考慮して、どのサービスにのせるべきか
  - 調整がついたらその結果をBillyに報告する
  - 関連するLoading OfficeのSalesもCCにいれる

### APのアップロード
- Converted AP
  - 5つのファイルをコピー
    - AX4フォルダのStandby配下に月ごとのフォルダを作って
    - Biweeklyだから5つのうち2つを削除
    - 3つのファイルをOPUSにUpdateする
    - T.LaneでフィルターかけてAX4以外にする
    - AX4以外を行削除する
    - 保存する
- Master Table Constrain creation
  - GHQしかUpdateできない
    - VVDだけうつ
    - 日本のだけデータが入っている
    - 日本は2ヶ月分入っている、8月に9月のAPが入っている
    - ONE Quoteも翌月分がある
    - DELフラグをすべて✓いれる（ただし、ONE Quoteは残す）
    - Saveする
    - UPLOAD EXCELでデータを入れ直す
    - Saveする
    - Weekごとあるから、これを3週分やる（今月は）
  - ONEQuoteと日本は翌月分も登録しておく
    - 2回分（Biweekly）をまとめてできるけど、前回は1週分ずつやった
    - UploadしたファイルをLocalにコピー
    - 日本だけにする
      - Submission OfficeをTYOBBでフィルター
      - TYOBB以外でフィルターをかけて全部消す（TYOBBだけに）
      - VVD名を変更する。カンマで複数のVVDをいれることが可能
    - ONE Quoteも過去のファイルをコピー
      - VVDだけを変更する
      - ONE Quoteに300TEUあげている
    - 7月23日に8月分をやっている
  - AX4のファイル→AP&alocationのシートを開く
    - ONE Quoteに50TEU分をAlocation
    - BSAにはこのシートから値を持ってくる

### 確認ポイント
- AFLA projectionは事前に見れないのか？
- Show upとはFresh show upとは？
- LA Forcast: Roberto from Shanghai
- Elyn from Sha
- Wanさんが見ているPowerBIはなに？

### A.POLとB.POLの違い
- Roll listは１BL=1BKみたいなのが多いと嬉しい（調整しやすいから）
- ダイレクトポートは基本Rolloverしない（ダイレクトポートとは実際に船がよるところ）
- Fresh＝Rolloverではないもの

### Control by HOで
- LWT、AX4、OriginをALL
- HYVTなどの頭は船の名前なので変わらない
- ４週間ごとに動いているから４週前を打てば前のVoyageを見れる

## 次アクション
- [ ] 関連ノートにリンク（[[AX4]]、[[Space Control]]、[[Wayport]]、[[CLL]]など）
- [ ] 必要に応じてMemory Noteに変換

#afla #ax4 #space-control #wayport #cll #ap`n#memory #work/one #work/one/dx
