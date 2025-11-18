# 毎日のSpaceデータ更新作業-OPUSデータ取得と処理

## 概要
毎日のSpaceデータ更新作業の手順。OPUSからデータを取得し、Excelで処理する方法について詳細に記録しています。

## 内容

### バックアップ
- 3つのファイルをバックアップ

### OPUSからデータを取ってくる
- Inquiry by Customized Condition
- OPUS > Sales management＞CNTR BIZ
- 6週間分を取るので、To側に＋5した値を入れる
- TradeをLWT、DirectionをEにする
- カラムの順番を並び替えてテンプレート登録する

### データ処理
- ダウンロードしてEveryday OPUS updateフォルダーに格納
- ファイル名を日付に変更して保存
- 1st POLがTarget。カントリーコードを2桁で分割
- 隣にGW列を追加して、計算式をいれる
- Column AEに列追加する、名前をGW
- GW（Gross weight）を計算する: （Cargo weight ＋ Tare weight）/1000
- Pivotする、このシートをTrunkという名前にする
- Trunkシートをコピーして、名前をPIVOTとする
  - PIVOTからTrunk POLを除く
  - ピポットテーブルを丸ごとコピーしてカラムJに貼り付ける
  - コピー先のほうからT POLを除く

### AX3フォルダの処理
- AX3フォルダにあるB1_ONEMIS Space Controller Offline File (MAIN) - newを開く
- シートの日付を今日に変える
- 日付の横のシートのデータをヘッダ以外すべて削除
- Sheet１は残す
- G:\Shared drives\Latin West Coast\Space Control\Looker\1. Daily space update
- このフォルダから最新データを持ってくる
  - SPC(ALC)
  - カラムIで列をInsert
  - VlookupでSheet１からデータを持ってくる

### バックアップ
- バックアップを自分のLocal driveに保存する
- AX1-AX4のすべてのファイルを
- AX3は2つのファイル

## 次アクション
- [ ] 関連ノートにリンク（[[OPUS]]、[[Space Control]]、[[データ処理]]など）
- [ ] 必要に応じてMemory Noteに変換

#inbox #one #afla #space-control #opus #data-processing

