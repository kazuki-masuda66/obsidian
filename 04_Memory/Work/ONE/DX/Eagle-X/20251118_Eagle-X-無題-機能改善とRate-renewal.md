# Eagle X-無題-機能改善とRate renewal

## 概要
Eagle Xプロジェクトの機能改善とRate renewalに関するメモ。顧客コードの修正、TTマッピング、複数シートの処理、Pricerへのメール転送自動化、OPUSコードが存在しないPortの処理、大きいTenderの対象化、Rate renewalのプロセスについて記録しています。

## 内容

### 顧客のコード自体が間違っている場合があるので、それの修正としてすべてのコードを参考として表示するようにする

### TTのマッピングがあるのにうまくマッピングがされていない場合はどうすればいいか

### 複数シートがある場合に、チェックシートを埋めるのが難しい（例えばすべてのシートでGroup customerを埋めないといけないのか）

### Pricerへのメール転送は将来的に自動化されないのか

### Opusコードが存在しないPortがEUAでは多く存在する→Inlandとして取り扱わないといけない

### 大きいTenderを対象にいれたい
- →オフショアでEuropeに閉じれるものも対象にいれる
- EUA trade related
- RHQ controlled offshore account

### Last year nominationをConvertしてAwardにいれたい

### Route portfolio sumilationとPricingのAccount
- ー＞すべて同じにしたい

### End of Juneに新ITSができるがその後にチェックが必要

### Referはまだだが、これからEagle Xに加えることもできる
- ITSはTransit timeはもっていないがWishlistにはある
- Co2 emissionも
- EuropeではCo2 commissionの関心が非常に高まっている

### City nameで検索して、Zip codeがあればZip codeも見ている
- Zip codeがないときはCity nameだけ
- OPUS codeがない場合はSalesにCity name/Zip codeを訪ねてもらう方がいい
  - →本当にこれができるかは懐疑的だ（Kasia）

### Verge1、Rail2、Truck3
- ロールアウト完了

### デジタルマーケ
- インド・台湾・ベトナムのロールアウト完成
- Each countryで50TEUを増やす
- Start date
- SNOW
- ロールアウトを完遂
- コーラスの部分は消す

### TusharのR&R6週間のQuality改善
- 改善SRでアクセスライトあげて改善ポイントあげてもらう
- 10個
- 慣れている通常のセッションにも出てもらう　OC non-domi手伝おう

### Desired Positioningは何かあるか（Prodigy）
- →Most easier to useみたいないキーワードが欲しい
- →長期目線では考える必要がある

### Prodigyとの共有フォルダを作る

### Campaign Monitorは新しいアカウントを使ってもデジタルマーケのAPIは大丈夫か？

### Email addressと言語は関係ない気が。。。

### E-mailのトライアルはDPとも一緒にやったほうがいい

### Qone Quoteのログインアカウントをみんなもらえないか

### Turn time PWC確認

### Rate renewal
- OPUSからダウンロードするとVerticalかHorizontalがあるが、基本的にはHorizontalを使う
- SCtoRFAと形式が若干違う
  - RFAのほうがレートのところにカレンシーを持っている
  - SCはカレンシーが同じ
- ほとんどが貼り付けでいける
- SCRFA noとお客さんの情報が抜けている
  - これは手で入れる
- NVOで複数NACのケースはActual customerコードは持っている
  - 今シーケンスでわっていないActual cusomerは一緒に見ている
  - それ以外はSeqを分ける必要がある
- リマーク以外はデータが取れる
- SCとRFAをの分岐をいれないといけないといけない
- いろんなサービスを載せるときのPFについてMTIが相談に載ってくれる
  - 7月頭までに固める
  - ONE2030のため
  - ロジスティクスとは言わずプレミアムサービス
  - じんぎりが今年の10月
  - ONE Quoteの域をでる、Eコマースをどうするか
- イベントデータハブやIOT等もビジネスマターになっている
  - そこにデータの見える化や予測データを見せれるようにする
- CoP
  - Cのところでやっている（長谷川さん？）
  - COPに関わっていないといけない
  - BPM側に1名増員
  - Yeelarのところ
  - Product Catalogの延長
- イベントデータハブをもってきたい
- NEW Product CatalogにあわせてNEW COPを作らせる
  - そこにイベントデータハブを持ってくる

## 次アクション
- [ ] 関連ノートにリンク（[[Eagle X]]、[[機能改善]]、[[Rate renewal]]など）
- [ ] 必要に応じてMemory Noteに変換

#feature-improvement #rate-renewal`n#memory #work/one #work/one/eagle-x #work/one/dx
