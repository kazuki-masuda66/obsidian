# Eagle-X-ONE-Quote-onboarding-session-機能とEcom登録

## 概要
ONE Quote onboarding sessionに関するメモ。Portpair list、Commodityベースの価格設定、Price Transparency、T&C表示、Value addサービス、D&D、Prepurchase割引、OPUS連携、Tiger MRG連携、Space info、Ecom登録プロセスについて記録されています。

## 内容

### Portpair list
- **OQでカバーしているすべてのポートペアが見える**
- **Get Quoteに戻ってくる**

### Commodityベースの価格設定
- **Avocado->2000, Other->1000みたいなことができるようになる。Commodityによって変わる**
- **本番環境はまだComodityはFAKで固定されている**

### Price Transparency
- **Price Tranperancyがいいところ**

### T&C表示
- **T&Cが表示される**

### Value addサービス
- **Premiumu cargo service，例えばスペースEquipment Gurantee**

### D&D
- **D&Dなどは先に決めてしまうのがいいところ、交渉の余地なし**

### Prepurchase割引
- **Prepurchaseしたら20%Discountしますみたいな**

### Booking連携
- **Bookingの画面はLegacyのものだが、そこにQuoteした情報が入っている**
- **OPUSにBooking infoが即座に登録される**

### Tiger MRG連携
- **TigerからMRG（Guideline rate）を持ってきている**
  - **Daily basis（Monday to Firday）**
    - TPが木曜日にUpdateしたらONE Quoteに反映されるのは金曜日

### Space info
- **Space infoがあるのもOQの特徴**
  - すべてのスペースがない場合、Sold outが表示される
  - これはかなりリアルタイムBasis
  - Master Constraint Table -> sold out logicに影響

### Ecom登録プロセス

#### How to register new ID

##### In case of brand new csutomer
- **E-com registration（Landing pageからここに飛ばす必要がある）**
- **Customer code creation（OPUS）**
- **CusoterがSubmitしたらVerifyをマニュアルでしている**
- **その足跡にCustomer codeを作っている**
- **GST, Tax id等を確実に確認しないといけない。これらはEcom登録では出てこない。**
- **NAの場合はVerifierがSalesに登録をお願いしているし、他の国ではCSが担当していたりする**
- **現在は数日かかっている**
- **ほとんどの場合Customer infoがmissingだから。**
- **インドやベトナムでの固有情報もある**
- **EcomチームがOpusにデータがあるか確認してからCountry Verifierにメールを転送している**

##### LOA（TP trade）
- **EcomIDをつくったあとにやる**
- **別のVerfierがいる（LOA verfier）**
- **Country veriferと同じかも？**

#### FMCの場合
- **Additionalの確認が必要**

#### TP laneの場合
- **EsignatureやLOA(Letter）を出さないといけない**

## 次アクション
- [ ] 関連ノートにリンク（[[Eagle X]]、[[ONE Quote onboarding session]]など）
- [ ] 必要に応じてMemory Noteに変換

-quote`n#memory #work/one #work/one/eagle-x #work/one/dx