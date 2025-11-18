# APのUpdate方法-Master Constraint Table更新

## 概要
AP（Account Plan）のUpdate方法について記録したメモ。最新のVVD確認、Sales Targetの準備、AP期間の定義、Master Constraint TableのUpdate方法、AX4 ENSENADA studyについて詳細に記載されています。

## 内容

### 最新のVVDをここから確認する
- G:\Shared drives\LW AP\11. Data for Prepare AP
- 対象のWk, Service, Domiで絞る

### 各月のSales Targetフォルダをつくる
- G:\Shared drives\Latin West Coast\Account plan Year 2024\New AP process\Sales target\2025
- CimonからSales Targetのデータをもらう
- 月末、でも20日くらいにもらう（？）

### いつからいつまでのAPかということを定義する
- https://docs.google.com/spreadsheets/d/1HWEaV1JMEAq7nk6byFTROOgDZnExphcvFEH_G0-PTkU/edit?gid=1448216665#gid=1448216665
- OPUSカレンダーのISO Weekを使ってる
- CimonのSales TargetとBSAを比較する

### 最終結果はここにConsoliされて各サービスのExcelシートに転記される
- G:\Shared drives\Latin West Coast\Account plan Year 2024\Account Plan to sales with no back end data\Account plan 2025

### Master Constrain TableのUpdate方法について
- BKがデータを固めたらここからデータをコピーする
  - **G:\Shared drives\LW AP\4_Convert_AP**
- ここに対象月を作る
  - G:\Shared drives\Latin West Coast\Space Control\AX4\Standby\2025
- 1ファイルずつ開いてAX1-3のデータを削除してAX4だけを残す
- VVDと対象WKを正しいことを確認する
- JPは翌月分を作る
  - どれか1つを選んでSubmission OfficeをTYO以外を削除する
  - 対象月を翌月、翌月のVVDをコンマつなぎでいれる（スペースは不要）
- OQの翌月分を前月からコピーして、対象WKとVVDをUpdateする
- Master Constrainで各WKのデータを1つずつUploadして、Saveする
- 翌月のVVDで検索して、JPの分とOQの分を削除する
- JP+1をアップロードする
- 翌月のVVDで検索して、OQをアップロードする
- 翌月VVDで正しくJP+1とOQが入っているか確認する

### AX4 ENSENADA study
- 6vessel 7wks
- MarketingとしてはOption2の方が良い
  - MXZLOのMinも400－500から変わる？
  - AX3を全て持ってくる
  - ENSENADAを追加するのはすぐにはEast boundをHelpしない、WestboundはHelpする
  - MSCがEnsenadaを除いたときの話
  - AX3は最初のCallがENSENADA
  - 今週中にStudyしてTMに話さないといけない
  - どれくらいVolumeをGenerateできるかStudyする
  - Port coverage AX3 VS AX4
    - TT time comparison→どれくらい増えるか
      - Competitor servicesがどれくらい
    - Past performance
      - Volume we can forseee
    - AX4のMXLZOとMX
    - もっとも大きなインパクトはSPRC、なぜならAX4はSPRCによっていないから
    - FOにそんなにDiscloseしないように
      - どのサービスからENSENADAが移動するかは言わないように
    - Market Competitorの状況

### APのSOP
- https://docs.google.com/presentation/d/1J26nHSXDbuaFYnYnpC6RxtGGSi9Ehv4N/edit?slide=id.p52#slide=id.p52

## 次アクション
- [ ] 関連ノートにリンク（[[AP]]、[[Master Constraint Table]]、[[ENSENADA study]]など）
- [ ] 必要に応じてMemory Noteに変換

#inbox #one #afla #ap #master-constraint-table #account-plan

