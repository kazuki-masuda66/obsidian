# Quick Memo-Eagle XとSNOW PMO-各種メモ

## 概要
Quick Memoに関するメモ。R2のTenderシート対応、Conversion Mapping、Pricing tool、TTツール、Eagle X memo（LA、WNS India Hands-on、JP、EUA、NA）、Eagle X NAの注意点、SNOW PMO、OPUS Storageの性能改善、EAGLE X内部打ち合わせ、CST meeting、SNOW Imai san 1on1、Space design workshop、Spaceグランドデザイン、Wayportの可視化、JP Pricerセッション、デジタルマーケティング、CVA、PRDメモなどについて記録しています。

## 内容

### R2のTenderシートは下記のパターンに対応
- レーンの削除
- レーンの追加
- 列の追加
- Conversion MappingはR1でやったものがRetreiveできる
- 追加列はCustomer Intention FlagとしてPricerに送る
- 顧客フォーマットに列追加がない場合、Initial check inでSalesが国語で記入して、それをベースにCSTが列追加（Customer Intention Flag）を行う
- Pricing toolでR1のデータがRetreiveできる
- すぐ顧客に返さないといけない場合などは直接Pricing toolをR2用に更新して送ることも許容

### TTツールのデータはPricing toolでRetreiveできない？
- 例えばConsoliのあとにSalesがTTを更新した場合それはどこにも保持されていない

### WNS Indiaの関わらせ方はGCSM含めて検討予定

### Eagle X memo
- **LA**:
  - 5つのConversionをBenに依頼中
  - 4つのTenderをStatus listにUploadを依頼中（PwC）
  - Cassandaraは3つ追加で依頼してくる、PwCがStatus listにUpload
- **WNS India Hands-on**:
  - Pedroにむこうの予定を確認してもらっている
  - 候補は9月11日週
  - Yuesheng＋増田で9月11日に行くか
  - Benに14－15日に行ってもらうか（この場合はVisaが問題ないことを確認しないといけない）
- **JP**:
  - リストの最新版を確認する（Release monthの情報も欲しい）
  - Nikkoから指摘があったTenderの確認
  - Daicelを確認
- **仲井さん確認**:
  - OMMC End to Endの件
  - NEXEN IOPのConsoliの件
  - 来週のNAの時間変更
- **Nikko確認**:
  - NAをいつから始めるか
    - 週次で確認するタイミングがあるから並行して始めてほしい
  - 日本のAmbasaddorのものを先にやってもらう
- **YS確認**:
  - SASのConversionをJayとJoに依頼できているか
- **EUA**:
  - 新規アカウントを追加する必要あり
  - SodiallのIOP部分のテスト
  - DanoeをFlouranceにやってもらう
- **NA**:
  - Dollar generalを確認

### Eagle X NAの注意点 from Kugohさん
- Salesは全然できない。Pricerが主体となる
- 今年は確実にできるものだけをやるほうがよい
- 事前にPricerとの確認を含めた検証を終わらせる
- NAだけPricerとCSTがやり取りを行うFlowができてくるかも

### SNOW PMO
- EAはKellyがJoin
- LAはリモートか、日程調整
- 19th Feb以降だったら参加できる
- AEはまだFBしてきていない、AEの返信によっては日程変更
- Workshop2についてWAとOCはPICをアサインしたが、TPとAFかはまだReplyがない
- しかしPJスケジュールの関係でそんなに先には伸ばせない
- Workshop2を先に行うのが良いかもしれない

### OPUS Storageの性能改善
- 2022年1月以降の条件でデータをとっていた
  - 2ヶ月（60日）でデータの期間を少なくする→最終的に2週間に
- ファイル分割
  - Gozuさんの毎回の負担を軽減する策を考える（RPAなど）

### EAGLE X 内部打ち合わせ
- CSTには2人夜間シフトにしてもらう
  - Eagle Xも近江さん、森さんがシフト
- 8時間×2で途中引き継ぎをしてもらう
  - US側にはやり取りは午前中に実施してもらう
- Surcharge
  - Subject, Fixed, Include

### CST meeting
- CSTには2人夜間シフトにしてもらう
  - Eagle Xも近江さん、森さんがシフト
- 8時間×2で途中引き継ぎをしてもらう
  - US側にはやり取りは午前中に実施してもらう
- Change request？
- 24時間で返すことが目標
- 今後はEagle Xの何人かのメンバーも参加して貰う予定

### SNOW Imai san 1on1
- Trip: LAはきびしい、2月19日以降、EAはKelly、AEはRachel、HoDの承認が必要
  - 遅らせた方がいい
  - WA,Oceaniaは返事あり、Af,とTPはリマインドあり
- NA（TP:Nondomi）
  - 2月にカムバック
- BSAモジュールにLoad officeのアロケーションにBreakdown（Control by HOのモジュール）
  - Service Nowにも連携される。ラテンはControl HOはやっていない
  - BreakdownをもとにUtilizationを確認しているからやらないといけない
- CMの最大化
- SNOWとBOMS
- Standbyの話も来る？GD4、AP
- ウェイポートの可視化をしたい（道田さんからの宿題）
  - 超えた部分はサードパーティを買うか、ロールオーバー
  - 来年のネットワークを考えるときに使える
  - 香港へのAllocationが正しかったかどうか

### 要員の件
- 4月1日がTarget
- 誰がどのように評価して各Localの評価につなげるかクリアにしている
- 各国と打ち合わせする

### Space design workshop
- Grand designなのか今の話なのかがわかりにくい
- どこをスコープにするか
  - ある程度周辺の議論を含めるか
    - Grand designで周辺も含めてSpace control
      - APはつながっています。制約されるのを認識した上で議論を進める
      - どういう順番でものごととが起こっているかはA to Zがあるということを
  - Spaceコントロールにフォーカス
- IPCやWayport、MTなどが図に出ていない
- 何をやったら100点なのか、ロングホールで埋めるのは当たり前
- すべて網羅した形で最適化する
- スティッキーノートで課題や問題点を載せてもらう
- Space controlのグランドデザインの前に乗せる
- GHQ全体としては異論がない形にしておく
- スペースコントローラの上のレベルと握っておく
- 後々に活かせるように、標準化まではPrincipalに違反しているよねくらいが言えたらOK
- Grantだけ個別にIndividual session、Grant特別セッションを設ける
- 石川さんと日本語セッションを30分

### Spaceグランドデザイン
- Awardを機動的にすることへの抵抗感
- Budget
  - NAは過去実績から積み上げ
  - それ以外はトップダウン？
- TP（Bucket）
  - 俺たちのサービスの線はここだ（600はFOBで使う）みたいな領域争い
- VietnamのBooking office
  - 地場のNVOCが優先されて、Walmartが優先されていない？
  - BookingのAcceptanceがFairか？
- Salesの責任はAward通りにお客さんに積んできてもらう
- APをころころ変えている→Awardは変えていない
- Awardは年間何百TEU
- APは週間何TEU
- 毎週同じTEUをだしてくれるのは世界に1社くらいToyota
- 短期的なコミットメントを変えてる
- APの年間計画
  - Awardから季節性を考慮して作られる＝年間AP
  - 50で単体で割るわけではない
  - 年間APとは比べないといけない
- 長期的APはなんのためにいるか、どう作るかは考えないといけない
- 釜山で荷物が滞っている
- MQCはサービスコントラクトに対して1つ
  - APはサービスレーン、オリジンでいれる
  - MQCはWalmartというSCに1つ
  - APと粒度が違う
- 年度終わりでコストコがこのままだとMQC達成しなそう。MQCを守るためにONEに今まで20TEUだったところ、100TEU乗せるはみたいなことを言われることがある
- そうなったら困る。。。だからAPは実績の20TEUではなく50TEUでいく。そうすると突然100TEUと言われたときに50TEUでと言われたりする
- Short termの契約は契約期間が1ヶ月未満。Bookingが入るのが2週間あって、その1ヶ月前にContractを結ぶというプロセスがある。ほとんどのお客さんはNVOCC。APを作るタイミングにはその契約はなかったが、その後にできる
- APの概念が希薄
  - 市況が悪くてスペースどこも開いている
    - とにかく量をとればいい
    - どうせ開いてるでしょ
  - GD1はすぐにFirm（F）
  - GD4は少し待ちWaiting（W）
  - GD6は受けません
  - Firmになったら受けませんはない
  - GD4のあとにもう一回Standbyが回ることはない
    - 受けるならマニュアルでFirm
    - 受けないならマニュアルでCancel
  - APで埋まらなうものをNON APで埋める
    - ShortやSpot
  - TPはバケットはどう考えるのかと聞かれるかも
    - Space controlの話ではないと持っていく

### Wayportの可視化
- 寄港数が見れるといい
- 何回寄港があるか見れるといい
- Draftの影響があってここはDraftじゃない
- BSAに達していないものがすべて
- Port pair間のWeight listがあるといい
- 100と線グラフの間のスペースを埋めたい
- Eagle plusのAverage trend reportに似ている
- Terminalの出港時にどうだったかはGVOに聞かないとない
- POL week（WayportのLoading week）：SYMが同じタイミングだよねって見る
- Eagle plusのWayport dashboardで作ろうとしている
- Sales weekはBooking officeが見る
- Eagle plusは見方がコツがあって、よく問い合わせが来てしまう
- Wayport余ってるのにThird party feederを買うのはよくない
- Fixedで買っていて使い漏れているのがないか
- ワースト、トップ10が欲しい
- WayportのUtilizationをTradeの評価の対象にするべき

### JP Pricerセッション
- TP: R1MRG等を指示して、OMMCが実施、R2以降はGHQ Pricderが直接
- AEもTPと同じ、2月の後半からOMMCで2人作業を渡して同じ形になる。最初は伊東さんが実施される
- EA（くろすさん）：Key accountはGHQ、それ以外はOMMC。OMMCのWorkloadを見ながらGHQと分担
- WAはEAと同じ
- AFLAはGHQで対応
- Simplified format：AE1st roundはMRGをそのまま投げるみたいなことがよくあるが、大量のNACがあるからMRGを渡しちゃう
- TPも近鉄とかにはやっていた。営業から今のMRGがあるからこれを使って以下等聞かれる。そもそもMRGは高めに設定しているからそれでOK
- EAとWAはとくにそういうことはやっていない。AFLAも使っていない
- 今、よしなにやっているところなので営業の反発はあるかも？
- TPのNon-domiはNA
- 欧州以外はNon-domiは向こうで見ている。LWのNon-dimiはチリ、LEはサンパウロ
- AEはNondomiも見てる。FOBだけGHQで。FOB以外、日系以外はLondonでやっている

### デジタルマーケティング
- Email Marketingに乗るのか乗らないのか
- Bookingまでいたったお客さんをNew
- 全世界ではなく限定数カ国で
- こういうAssumption
- 彼らの強みはSolutionはいくつか試したい
- コスト感、Budget感がわからない
- New One
- One Quoteへのアクセスをベンチマークを10％増やしたい
- それを達成するにはどこにどう手を打つか
- ソリューションはBudgetは度外視して、いくつかのソリューション
- 6ヶ月後
- SEOやEmarketingの合せ技か、Email Marketingに一本で行くのか
- 条件を設定したら、Comと話してみる
- こういう条件でこう話している
- 似たようなサービスでいい手筋があるか
- Logisitic industryにツテがあるか

### CVA
- GCSMが提唱する考え方、Salesforce。Sales Performanceをモニタリングする考え方
- LT＝6ヶ月以上
- MT＝3－6ヶ月
- ST=1－3ヶ月

### PRDメモ
- PRDはP1-P9までカバーされている
- TenderとPRISMはP1-P3のみ
- PRISMとTT toolはTIME GAPがある
- PRISMは週次で反映?だがTTは月次ベース
- TTでも5million route

## 次アクション
- [ ] 関連ノートにリンク（[[Eagle X]]、[[SNOW PMO]]、[[Space design]]、[[Wayport]]など）
- [ ] 必要に応じてMemory Noteに変換

#snow-pmo #space-design #wayport #digital-marketing`n#memory #work/one #work/one/eagle-x #work/one/dx