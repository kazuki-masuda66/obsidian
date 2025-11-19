# WK30-AX4 Space Control-週次業務メモ

## 概要
WK30（Week 30）のAX4 Space Control業務に関する週次メモ。HYVT0157E、NLVT0007E、HIIT0111E、TGBT0021Eなどの各VVDのスペース状況、Roll Listの作成方法、CLLのUpdate方法、EC Pricingの更新について記録しています。

## 内容

### AX4のSpace状況
- **HYVT0157E**: Dharshinishreeから追加TEUを求められているが、すでにClose済み。Close済みだとどうにもならない。追加のMisconnection分を次の船でと言われることはあるが、基本はBSA遵守
- **NLVT0007E**: マレーシアから追加で34 teuを載せられないか、最終Loadingは36teus。Rollリストを作る。Control by HOを使って最新の状況に更新。ONE Quoteの数のUpdateの仕方: Control by HOでBooking firmはゼロ。マイナスの人たちにRollリスト送ることを依頼（ただしダイレクトポートは送らない）
- **HIIT0111E**: MALAYSIA MARKETINGから追加スペース要求
  - AX1 IMET2531E: BSA 12 vs Loading 34 teus（6 teus AP bookings、22 teus additional space required）
  - AX2 KDDT0530E: BSA 27 vs Loading 54 teus（17 teus AP bookings、27 teus additional space required）
  - AX3 OSET2531E: BSA 26 TEUS vs loading 72 teus（30 teus AP bookings、46 teus additional space required）
  - AX4 HIIT0111E: additional 23 teus - to transfer 13 TEUS MXZLO bookings from AX2 ORIT2530E & 10 TEUS MXZLO bookings from AX2 OSET2531E
- **TGBT0021E**: AX4 TGBT0021E (additional 55 teus) - to transfer 40 TEUS MXZLO bookings from AX2 VTDT2533E & 15 TEUS MXZLO bookings from AX2 TKHT2534E

### SummaryファイルのUpdate
- WK29, HYVT0157E: Vessel expected to depart full in weight first. Estimated around 100 teus of roll with 5TEUs of misconnection
- WK30: No service
- WK31, NLVT0007E: ONE vessel. Estimated to be full in weight with around 200 teus of Roll, subjected to no misconnection and shortfall
- WK32, HIIT0111E: Current sales projection 57% current booking 43%. I will push the Front Office to input the forecast as usual
- WK33: No service

### CLLのUpdate方法
- DELでMXを除く
- NGBとPUSも同様に行う
- T2は1でカウントしていい（SOC）
- F5はBooking NoをBooking Inquiryでいれる（2本のコンテナと10本のVoid）×２
- Elynに精緻な数を聞く、PUSはCatharine
- Final figure tableを聞く

### EC Pricing
- 今回LOFFが1900だからStar Cargoに1900-2000
- **Starcargo only**: POL: Ningbo/Shanghai/Yantian/Shekou/Hong Kong/Pusan/Qingdao/Xiamen/Keelung/Taoyuan/Taichung/Kaohsiung to ECGYE: USD 1900/40NOR
- **Tier 2**: POL: Ningbo/Shanghai/Yantian/Shekou/Hong Kong/Pusan/Qingdao/Xiamen/Keelung/Taoyuan/Taichung/Kaohsiung to ECGYE: USD 2000/40NOR
- Validity: 1-15 August 2025

### その他の業務メモ
- IsaacはXIAMENの報告をしている。その後SCRC
- HKのことをこないだ聞いた
- Billyは2人いる（Billy Wu: Xiamenから現在のマーケットPriceの報告）
- ECM Space sharing by Roberto
- PUS Backlogの反対はFresh
- NingboマーケットはMichelle
- TingTaoはJason
- NLVT0007E: CN-SHANGHAIのスケジュールが9日（？）そうするとPusanが12日？HIIT0111Eとスケジュールがかわらなくなる。An chengにスケジュールを聞く
- Billyにアドバンスリストをとって30TEU900トンを選ぶ
- Owner's meritが50TEUと500tonあるからもう少し乗せるべき？HIIT0111Eから前に持ってこれる？
- Rollリストをどう作って、どのタイミングで送るか
- Crossborder(Monarch) coordination AX4(TPE) China - Lazaro Cardenas - Chicago / Sparx Logistics / ETA Lazaro Cardenas September 2nd, Hyundai Prestige 0111
- 台風などで遅れる場合はGVOに実際の時間を確認する（Elynも教えてくれるが）
- ONE船の場合、オーナーズメリットを可能な限りとりたい。特にTonは自然減で減った分取れる可能性が高い。正確なオーナーズメリットを知りたい場合はプランナーに確認する
- ElynにFinal Figureを確認してUpdateする
- 船に余裕があるときはAdvance Listをつくって、後ろの船から前の船に持ってくる
- Advance Listは多めに作ってOK、これをRollしても下に戻るだけだからなんの影響もないから
- Closing dateにRoll List（Standby list）を送るが、これは最優先にいれてOK
- DNR=Do Not Roll
- 主にVNの貨物かと思いますが、上海でロールする場合は、SHA ETAの３日前ならPOL側のOPUISデータ変更でOK、それ以降であれば、こちら側でロールの連絡をするルールになっているようですので、ご注意ください

## 次アクション
- [ ] 関連ノートにリンク（[[AX4]]、[[Space Control]]、[[EC Pricing]]、[[Roll List]]など）
- [ ] 必要に応じてMemory Noteに変換

#afla #ax4 #space-control #wk30 #roll-list #ec-pricing`n#memory #work/one #work/one/dx