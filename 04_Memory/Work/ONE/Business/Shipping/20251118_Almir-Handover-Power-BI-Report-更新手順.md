# Almir Handover-Power BI Report-更新手順

## 概要
Almir Handover（Power BI report）の更新手順について記録したメモ。Supply Demand reportとBudget & Projection reportの更新方法、eeSeaへのアクセス方法、Tableauの使い方、AlphalinerでのVessel情報確認について詳細に記載されています。

## 内容

### 2つのレポート
- Supply Demand report
- Budget & Projection report

### Supply Demand reportの手順
1. eeSeaにアクセスする（GSEからシェア）
2. Tableauにログインする（GSEのアカウント＋Authenticaterでワンタイムパスワード）
3. ONEフォルダ→Weeky roundtrips explanation→ONE - voy v3
4. G:\Shared drives\GHQ AFLA\Business Intelligence\Looker Reports - Transition Folder
5. AFLA Supply DBというExcelファイルを開く
6. 1列目のService - master nameの列を全コピー
7. 違う新しいシートに全貼り付け
8. Remove Duplicateをして対象のAFLAに関連するサービスを取得する
9. Tableauに戻り、右上のService - master nameからまず全文の選択肢を外し、そのあと一つずつ対象を選択する
10. 選択できたらApplyを押す
11. Service Versionで3つを選択しApply
12. 右上のダウンロードからデータをダウンロード
13. ONE - voy v3_data (2)みたいなデータがダウンロードできる
14. ダウンロードをしたファイルからカラムAだけをコピーしてDuplicationをRemoveする
15. もとのやつと比較してなにか抜けていないか確認する
16. ダウンロードしたデータのA列からL列までをAFLA Supply DBに貼り付ける
17. A列にMexicaで検索して、Vessel NameがNullのものがないかチェック（これは不要かも）
18. SaveしてExcelを閉じる
19. Power BIを開く
20. G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan
21. AFLA Supply & Demand
22. Dataをリフレッシュする
23. Vessel Nameタブにいき、データがうまっていないものがあるか確認する
24. データが埋まっていないものがある場合はそのVesselをAlphalinerで検索して、TEUとWeightを調べて、データに追加する
25. Publishする

### DBを用意する必要がある
- Supplyのみ準備している
- ECC ration

### ON TIME Report
- Service Qualityをるのによい
- BlankはOmission

### Budget & Projection
- SYM→MarketingチームがProjectionのデータを確定させる
- ProjectionのファイルをGシートからExcelでダウンロードする
- Budget & Projectionを開く
- G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan
- 毎月行う
- 大本のPower BIとは別にそのもとのデータソースのPower BIが存在する
- G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan\Budget Segments\FY25 BP 1Half AFLA\Jun-Sep Proj
- 上から順にPower BIファイルを開く
- BSA & Liftings FY25 1H Jun-Sep Proj
- Transform data
- 個別ファイルをここに吐き出す
- G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan\Budget Segments\FY25 BP 1Half AFLA\Jun-Sep Proj\DB Output
- 対象のSales Weekだけを選ぶ
- Sepの場合はWK39まで
- My workspaceにPublishして、My workspaceからExcelでダウンロード→DB outputにフォルダ移動
- RevenueのBIからFAKとRevenueのデータを出力する

### どうやってデータをもってくるか
- eeSeaのにGSEのアドレスでサインインする
  - TableauのモバイルでVerification Codeを取得する
- ONEフォルダのWeeky roundtrips explnaation
- Voy Ver3
  - Serviceを選択する
- Everyweek updateしている
  - Duplicateをなくす
- Alphlinerから落としていたが、とても大変だった

## 次アクション
- [ ] 関連ノートにリンク（[[Power BI Report]]、[[eeSea]]、[[Tableau]]、[[Alphaliner]]など）
- [ ] 必要に応じてMemory Noteに変換

#power-bi #eeSea #tableau #alphaliner #work/one #work/one/afla

