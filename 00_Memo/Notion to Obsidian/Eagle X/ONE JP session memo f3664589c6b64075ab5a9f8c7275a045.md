# ONE JP session memo

## ONE Japan session宿題事項

- Eagle XのScope定義を最新化してONE Jに送る（GHQ）
- FY24に向けたリストの再整理（ONE J）
- プロセスの見直し案・機能追加の検討（GHQ）
    - プロセス
        - Sales ReviewのSkip
        - Pricer転送のSkip
    - 機能
        - TT toolの情報の明確化
        - Simplifiedのカラム追加(Sales Target)
        - Emailのタイトル
        - PiplineとSimplifiedフォーマットの接続（将来的なエンハンスメント）
        - Request Addのシート
        - Simplified formatにあるFreetimeのチェックリスト
- ONE JのSalesとのPreconvesion準備・7月（GHQ）
- NAC-NVO Conflict Caseの具体例の検討（ONE J）
    - GHQ側と継続協議事項
- Eagle X portalのTrainig Videoの改善（GHQ）
- 

![Untitled](ONE%20JP%20session%20memo/Untitled.png)

### Agenda

[https://docs.google.com/spreadsheets/d/1GIKW1CQLhWZXI8DktoS1fRgKSCpaxSBN/edit#gid=943901080](https://docs.google.com/spreadsheets/d/1GIKW1CQLhWZXI8DktoS1fRgKSCpaxSBN/edit#gid=943901080)

### Session Memo

### FY23 BID Activity and review

- Tigerとの違いを明確にしてほしい、Filingも同じプロセスに
- Potential service laneを見えるようにして欲しい
    - 韓国向けのWin lostが見えていない、データを集めるのに時間がかかってしまっていて他船社との勝負にならない
    - 営業がレーンを削ってからPricerに見積もりを出してしまっている
        - どうせサービスないし、いつも断っているし、時間ないし
        - 営業のマインドセットをかえる必要がある、お客さんのシートを変えずに出してもらう
- By Nakai san : Missingのルートをつくる（Inlandを含めて）、そうでないとEnd to EndでCMが見れない
    - 今バッチで作っているが、MAXの20万ルートに来てしまっている
    - 海上だめでも内陸儲かってるとかもありうる、それをEnd to Endでみたい
- Rate Structure
    - どのSurchargeがSub toでどれがIncludeなのか
    - どれだけSurchargeとれるからOceanこれだなみたいなことを考えれるように
- Filing
    - TSTにそのまま投げると間違いがいつも発生している
    - だからいつも自分でFiling用にマニュアルでConversionをかけている営業がいる
    - 丸投げしている営業のものをミスでいれてしまっている
- 最終的にEmailなどSimplifiedフォーマットをお客さんに投げてそれを埋めてもらうようにしたい
    - シーズン前から準備してお客さんに持っていきたい
    - OPUSからダウンロードしたものがベースとなるものがONE formatとしたい(Rate renewal)

### Fukai-san Feedback

- Japan全体では600以上のTenderがある
    - この対象は6ヶ月以上のLong termのもの
    - 北米とNon FMCはそれぞれでカウントしている
- FY23の反省点
    - As IsはあいにくTenderもう始まってました、もう3日間で出さないといけない等
    - 営業の交渉は止められない
    - 清水は48個あるうち8個Eagle Xに乗せてくれた、とてもSupportive
    - 始まりが2月になってしまったので、準備ができていなかった
    - 営業の一人ひとりがEagle Xとはというところの理解ができていなかった
- JOA->Japan Offshore, Intra Asia，営業が各地に訪問、Tenderの結果や来年に向けた情報収集をしている
- 10月頭、11月Tenderのキックオフ
    - 支店ごとにXXTEU取りに行くみたいなStrategyを立てる
- NAC のBusiness ownerの定義
    - 誰がPricing,取りまとめをするのか、戦略的なところを考える
- それぞれの課からEagle X Ambassador・Superuserを立てる
    - 20課、200人の営業がいる
- 大手のBCOは都度マネジメントからの要請で営業はそのProgressを確認しないといけない
    - Pipelineを使っている、予算をつくるためにNominationを使ってくれとお願いしている
        - 簡単にCVAに登録できる
        - TenderのProgress、どこまでいきましたかというところまで、RPSやPricing toolを使ってProgressを把握する情報に使えないか
        - PIPELINEをちゃんと作るから他を削ってほしいという声が営業から上がっている
        - 予算作成にPiplineを使った
        - 期中のPiplineのフォーマットも作っていて、Oppurunitiyの見える化をしようとしている
        - 日々使うものとして来週リリース予定
        - GCSMのBenとやり取りしている
- 営業の声についてアンケートとった
    - 

![Untitled](ONE%20JP%20session%20memo/Untitled%201.png)

![Untitled](ONE%20JP%20session%20memo/Untitled%202.png)

![Untitled](ONE%20JP%20session%20memo/Untitled%203.png)

![Untitled](ONE%20JP%20session%20memo/Untitled%204.png)

![Untitled](ONE%20JP%20session%20memo/Untitled%205.png)

- 

![Untitled](ONE%20JP%20session%20memo/Untitled%206.png)

- Pipeline
    - Data studioでVisualizeしている
    - 元データのシートは課別に
    - 去年はCVAから作成
    - サービスなくてもOppurunitiyとしてすべていれてもらう方針
    - Lostしたものもダッシュボードで見えるように
    - RPSの元データをこれを参照させる
    - PiplineからSimplifiedの元を作らせる
        - Simplifiedをイチから入力させるのを避けさせる

### FY24 BID Target

- Tender definition discussion
    - NAC-NVO conflict case
    - Biz owner
        - レーン数の多い人がBiz ownerになる
        - 関係者全員を集めてPricing
        - 調整はメール
    - 同じNACでも
        - Customer formatでくる場合と
        - NVOフォーマットでくるケースがある
        - 日通は全航路1担当
        - フォーマットがないものは沖縄の部隊を通して日通フォーマットにする
    - Fanuc
        - YUSEN logi
    - 40-50社
    - UNIQLOのSC以外
- [https://docs.google.com/presentation/d/17uAwCQY_NmNu9KctWRSS-ckFgY95RRkxA4kjqTPHTm8/edit#slide=id.g253ae714aa2_2_0](https://docs.google.com/presentation/d/17uAwCQY_NmNu9KctWRSS-ckFgY95RRkxA4kjqTPHTm8/edit#slide=id.g253ae714aa2_2_0)
- Number of Account
    - 全体で２９６件（これは2月からのみなので実態はもっと多い）
        - Simplified→206件
        - Simplified以外→90件
            - 59件はConversion study済み
            - 31件未実施もOffshoreやSeq2等があるので実際はもっと少ない
    - 定義の見直し後にこの件数の再チェックが必要★JP側へのお願い事項

### Scope wise possible change

- Conversion
    
    **＝＝V43 Updated Point＝＝**
    
    [**[Initial Checkin]**](https://docs.google.com/forms/d/e/1FAIpQLSeFgGxoE_TzCj7rS-z3KbMlgDCiYxsivxNzIru2e3rVYRUdDQ/viewform)
    
    **✓ Group Customer Code search made easy**
    
    > -Separate sections for each Region to split pull-downs
    > 
    > - Enabled initial search of Country.
    
    **✓ Updated Validity related question**
    
    **✓ Implemented round 2 process**
    
    > -Add Customer FeedBack field description
    > 
    > - Addition of questions for Simplified Format accounts starting the EagleX process from R2
    
    [**[Conversion Tool]**](https://docs.google.com/spreadsheets/d/1NdIEWAz5pH9kebLV1PHp-2fTDbtjKznlEz-LS30-mX4/edit#gid=1608454728)
    
    **✓ Raised upper limitation of number of Rows/Columns**
    
    > - Rows & Column in Customer Sheet & ONE Format can be variable
    > 
    > 
    > (If Both of Row number & Column number are huge, tool is even unworkable).
    > 
    
    **✓ Implemented the latest price assign logic and Pricer Tool Assistant Data (Need to analyze overall assigned results)**
    
    > - Updated Customer Sheet & ONE Format to present Eagle X Pricing Assign.
    > 
    > - Added some information (version info, additional blank column etc.)
    
    **✓ Implemented Round 2 process**
    
    > - New/Delete lanes from the previous round can be identified in the new version.
    > 
    
    **✓ Field Mapping Master**
    
    > -Master registration and retrieve functions for Field Mapping have been implemented
    > 
    
    **✓ Addition of columns describing Rate Structure**
    
    > -Rate Structure columns have been added to the Customer Sheet, where the structure of the Surcharge can be input.
    > 
    > - We are planning to make it possible to fill it in automatically from Checklist and T&C Summary in v44 or later,
    > - However, at this time, it is assumed that you will enter the information manually based on the Checklist.
    
    **✓ Updated Detail function**
    
    [**[Sales Review]**](https://docs.google.com/spreadsheets/d/1I4aOpmxkYzPIRi01PtmxnGJ5mRMj_erZr_r_8qjjk-8/edit#gid=1758262462)
    
    **✓ Updated Field Mapping Review Sheet**
    
    > -Created Remark column
    > 
    
    [**[Status List]**](https://docs.google.com/spreadsheets/d/1aqOVSDqDj5OzAt-ZcaqldfCtBTf30kZuBIrO1zwbk4E/edit#gid=1142938611)
    
    **✓ Add columns for each round Status**
    
    > -Add progress have been listed in Col.K to Col.N
    > 
    
- V44を開発中
    - スケジュール
        - 今週末で開発完了、来週前半でEagle Xチームテスト、後半でCST向けにテスト環境としてリリース、End to Endでテスト完了後、Regionへ開放予定（7月2～3週目辺り？）
        - [https://docs.google.com/presentation/d/1ndhAeqqHQUbJFvUL9E0w5nQe3EOjYFqwhr3k6NSRNFw/edit#slide=id.g254459ece98_0_57](https://docs.google.com/presentation/d/1ndhAeqqHQUbJFvUL9E0w5nQe3EOjYFqwhr3k6NSRNFw/edit#slide=id.g254459ece98_0_57)
    - 開発項目
        - V43の不具合解消
        - EUA要件
        - ChecklistのRetrieve function
        - [https://docs.google.com/spreadsheets/d/1BaQmFAfYgrcEdGAQGUkvIs85RNSo4Fym56Ju5VDtTEA/edit#gid=1685512760](https://docs.google.com/spreadsheets/d/1BaQmFAfYgrcEdGAQGUkvIs85RNSo4Fym56Ju5VDtTEA/edit#gid=1685512760)

### JPN dedicated case/solution

- BCO/NVO Conflict case
- NAC-NVO Conflict Case

### Required Process review

- Simplified format case, omit review process
    - Simplifiedの場合、基本はSales ReviewはSkipでよいか？
        - 極力キャッチボールを減らしたい
            - 事前にFY23でSales Reviewを終えている場合はReviewをSkipしたい
                - Status listにReview済みかのフラグを追加して、それで判定できないか★PwC確認
    - 運用を始めるのはV44の本番リリース辺りから？ー＞FY24から
- Assistance for Copy & Paste Process
    - Consoli後のCopy&PasteはCSTで実施するで確定でよいか？
        - 営業はCSTが作業を終えるよりも、早く見たい
            - AsIsから変更しない,コピー＆ペイストは営業にお願いする
- Assistance function for Rate renewal case
    - Simplified Format creation→OPUSからダウンロードしたデータをSimplifiedフォーマットに貼り付け→一部カラムが埋まり切っていないものがあれば手で追加→Initial check in
    - PipelineよりもOPUSのほうが今は見やすい、運賃情報もある
        - 将来的なエンハンスメント事項とする
    - V44でリリース予定
- TT tool
    - ReconversionしたときにTT toolのバージョンを記載する
        - Consolidationした後の結果にバージョン情報を記載できないか★PwC確認
    - Eagle Xで使っているTT toolをEagle X Portalに載せるようにする
- SimplifiedのときはSend to Pricerを省略できないか
    - Pricer asing masterの精度を確認。TSTのような大きなTenderファイルでなければ問題ないのではないか★内部確認
    - CSTから自動Pricerに送るものの、Salesは特殊な宛先が必要な場合はちゃんとチェックして、宛先間違いを指摘するよう周知する
    - TSTの指摘事項の具体例を確認する
    - Simplifiedのターンタイムを短くしたい
- JapanのPreconversion
    - Tender Q&A＋Checklist draft→第一弾Review
    - Reviewシート（Location/TT tool mapping）→第二弾Review
        - このReviewが済んでいる場合はSales ReviewをSkip
        - 不明な新規レーンがある場合のみReview依頼
- NVOは2,3日で出してくれというパターンが多い
    - 去年のものをベースに先にRateをもらっておくというWorkaroundを作っておく
    - 差分だけを動くみたいな（10レーンは先にやっておく、2,3レーンだけ）
        - ただしその場合Pricerがファイルがわかれていて認識しづらい
    - MRGを返す場合は現在承認が必要だが、それを包括的にとっておく
    - 急ぎのときどう対応するか、NVOは時間勝負、とにかく裁かないといけない
- オフラインでどうしてもやらないと行けない場合もSimplifiedを使ってください
    - オフピークにPricing toolを通すことでFilingまでもっていけるか確認する
- Simplifiedにカラム追加して欲しい
    - Sales Target
    - 先にないと書かない。あまり列を追加するという感覚がない
- Mailのタイトルをもっと明確化して欲しい
    - 結構流れて言ってしまう
    - ★とか[Eagle X]みたいな文言を頭につける等
- PIPELINEとOPUSの違いは、とれなかったPotential laneも入っている

### 佐久間さん個別セッション

JPのPortalサイト

[https://sites.google.com/one-line.com/eaglexconversionpricing](https://sites.google.com/one-line.com/eaglexconversionpricing)

Eagle X のTraining videoについて

- **Additional Sales Functionalitiesがベースの説明なので、上に合ったほうがわかりやすい**
- GdriveへのアクセスはStatus listから飛ぶにかえる
- c. How to Save Tender Bid File and Documents?
    - Customer formatのときは事前にファイルとT&Cを保存するという目的を先に伝える
- d. How to Check the Status List?
    - b. How to Find a Folder in ONE Shared Drive?とセット
    - Pricerの提出状況も見えるということも伝える
- 逆に短すぎる、5分くらいでも大丈夫
- e. How to Contact Eagle X Support Team and CST?
    - どういうときに連絡する
        - Reviewまでいっていたらこっちみたいな例を
        - どうPricerに送るか
        - チェックリストの内容についてはこちらに
- **Initial Check-in**
    - それぞれのツールの用途がわかっていない人向けに
        - どういうときにこれを使うか
        - この単語がなにかわからない人がいる
        - 概要の説明を記載、または動画
        - イメージ図を乗せたほうがわかりやすい
    - ページごとでもいいのでは、細かく別れすぎている
    - チェックインの前に格納というのを強調する
- Request ADD
    - Simplifiedだったらというのがない
    - すべてのツールに対してなんの目的で伝えるのか
    - Seqの追加と新しいアカウントの追加
    - 1シートで回答させたほうがわかりやすい★PwC
- Simplified Format
    - ページごとでいいのでは
    - Seqを選ぶ時はダッシュボードと比較して選んでくださいと強調する
    - 説明の順番が逆（１．３）
    - 考えるものではなく該当のものを選ぶ
- Simplified format file
    - 上で生成されたものですよと書いてあげる
    - ファイルの全体像をお見せします、導入
    - シートの構成
    - 黄色はMnadatory
    - Rate
        - Target rate
    - このあと細かい説明をします
    - POR,DELはセット
    - Doorのパターン追加説明
        - プルダウンにない
        - PODに港
        - 必須の部分は手入力できる
    - Emailサンプルを提供してもらう★佐久間さん
    - FreetimeはSimplified formatにあるからチェックリストと被っているから消す★PwC
    - Other remarkの例がFree timeのがおかしい
    - なにかいい例があれば★佐久間さん
        - カラムとして設定はないがPricerにいいたい
    - Remark
        - 欧州向けIncludeXXでだしてください
    - カラムカスタマイズの件について動画があったほうがいい
    - 
- Sales checklist
    - Customer formatであることを書いておく
    - ベースはカスタマーフォーマットと突き合わせてみてください
        - 右と左でつきあわせて
    - PORうちいれてません、なぜなら名古屋なのが明確だから
    - Freetime
        - 全部にチェックにはいってしまっている
        - DEmaは４０days Nagoya DetentionはAs per tariff等
    - Arbitrary/Inland
        - 例がおかしい、Subject to Fuel charge
    - Surhargeの用途がよくわからなくなる
        - 使い方を説明
        - そもそもの仕組みがわからなくなる
        - DICではカラムがなかったから足した
        - クラレはいい感じにやった
    - Review
        - Conversionがまだ完了していないからその精度を高めるためのConversionであること、最初に全体像を伝える
            - シート構成
                - このシートは
        - レビューした結果の選択は動画を分けない方がいい
        - 曜日が迷子になることがある、Day of Weekを例にしてあげる
        - Customer formatのこれがこうなんですとしてほしい
        - カスタマーフォーマットをもとに説明してほしい
        - SBS TOSHIBA
        -