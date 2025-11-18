# ONE Quote onboarding session

- Portpair list
    - OQでカバーしているすべてのポートペアが見える
    - Get Quoteに戻ってくる
- Avocado->2000, Other->1000みたいなことができるようになる。Commodityによって変わる
- 本番環境はまだComodityはFAKで固定されている
- Price Tranperancyがいいところ
- T&Cが表示される
- Value addサービス
    - Premiumu cargo service，例えばスペースEquipment Gurantee
- D&Dなどは先に決めてしまうのがいいところ、交渉の余地なし
- Prepurchaseしたら20%Discountしますみたいな
- Bookingの画面はLegacyのものだが、そこにQuoteした情報が入っている
- OPUSにBooking infoが即座に登録される
- TigerからMRG（Guideline rate）を持ってきている
    - Daily basis（Monday to Firday）
        - TPが木曜日にUpdateしたらONE Quoteに反映されるのは金曜日
- Space infoがあるのもOQの特徴
    - すべてのスペースがない場合、Sold outが表示される
    - これはかなりリアルタイムBasis
    - Master Constraint Table -> sold out logicに影響
- 

![Untitled](ONE%20Quote%20onboarding%20session/Untitled.png)

![Untitled](ONE%20Quote%20onboarding%20session/Untitled%201.png)

- Ecom
    - FMCの場合Additionalの確認が必要
    - TP laneの場合EsignatureやLOA(Letter）を出さないといけない
    - How to register new ID
        - In case of brand new csutomer
            - E-com registration（Landing pageからここに飛ばす必要がある）
            - Customer code creation（OPUS）
        - CusoterがSubmitしたらVerifyをマニュアルでしている
        - その足跡にCustomer codeを作っている
        - GST, Tax id等を確実に確認しないといけない。これらはEcom登録では出てこない。
        - NAの場合はVerifierがSalesに登録をお願いしているし、他の国ではCSが担当していたりする
        - 現在は数日かかっている
        - ほとんどの場合Customer infoがmissingだから。
        
        - インドやベトナムでの固有情報もある
        - EcomチームがOpusにデータがあるか確認してからCountry Verifierにメールを転送している
        - LOA（TP trade）
            - EcomIDをつくったあとにやる
            - 別のVerfierがいる（LOA verfier）
            - Country veriferと同じかも？
            -