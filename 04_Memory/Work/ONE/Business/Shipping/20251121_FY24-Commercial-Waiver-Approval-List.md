# Commercial Waiver Approval Route - 承認ルートと閾値

## 概要
Commercial Waiver（商業的な料金免除）とNon-DEMDET（Demurrage/Detention以外）の承認ルートと承認閾値のリストです。各Trade、Service Scope Group、Leg、Service Scope Codeごとに、承認レベルの閾値と承認者のメールアドレスが記載されています。

## 内容

### ファイル情報
- **元ファイル**: `FY24 Commercial Waiver Approval List.xlsx`
- **形式**: Excelスプレッドシート
- **年度**: FY24（2024年度）
- **場所**: 00_Memo内に保存されていた資料

### 承認レベルの閾値

#### Level 1: Pricing supervisor
- **DAR (COM)**: < $1K（1,000ドル未満）
- **Non-DEMDET**: < $2K（2,000ドル未満）

#### Level 2: MKTG Manager
- **DAR (COM)**: >=$1K ~ <$5K（1,000ドル以上5,000ドル未満）
- **Non-DEMDET**: >=$2K ~ <$10K（2,000ドル以上10,000ドル未満）

#### Level 3: SM/DGM/GM
- **DAR (COM)**: >=$5K ~ <$10K（5,000ドル以上10,000ドル未満）
- **Non-DEMDET**: >=$10K ~ <$100K（10,000ドル以上100,000ドル未満）

#### Level 4: GHQ/RHQ Head
- **DAR (COM)**: >=$10K（10,000ドル以上）
- **Non-DEMDET**: >=$100K（100,000ドル以上）

### 承認ルートの構造

#### データ構造
各承認ルートは以下の情報を含みます：
- **Trade**: 取引ルート（AE、ASOC、TPTA、AFLAなど）
- **Service Scope Group**: サービススコープグループ
- **Leg**: Leg（Domi、Non-domi）
- **Service Scope Code**: サービススコープコード
- **Level 1**: Pricing supervisorのメールアドレスと閾値
- **Level 2**: MKTG Managerのメールアドレスと閾値
- **Level 3**: SM/DGM/GMのメールアドレスと閾値
- **Level 4**: GHQ/RHQ Headのメールアドレスと閾値
- **Japan local PIC**: 日本ローカルの承認者（該当する場合）
- **Remark**: 備考

### 主要Trade別の承認ルート

#### AE (Asia-Europe)
- **NE Domi**: WEW;OEW;AEW
  - Level 1: huiteen.soh@one-line.com; ghq.ae.mktg.pri@one-line.com; wayne.hunt@one-line.com; eua.mktg.aewb.pri.neu@one-line.com
  - Level 2: george.yeung@one-line.com; phillip.howell@one-line.com
  - Level 3: christina.tan@one-line.com; mary.cowan@one-line.com
  - Level 4: mike.hanson@one-line.com; genki.yasuda@one-line.com
  - Japan local PIC: mihoko.ito@one-line.com（Level 3まで承認可能、Level 4はMike Hanson、Yasuda-san）

- **ME Domi**: WMW;OMW;AMW
  - 承認ルートはNE Domiと同様

- **NE Non-domi**: WEE;OEE;AEE
  - Level 1: florian.brinkmann@one-line.com; eua.mktg.aeeb.pri.neur@one-line.com
  - Level 2: trish.clarke@one-line.com
  - Level 3: mary.cowan@one-line.com
  - Level 4: mike.hanson@one-line.com; genki.yasuda@one-line.com
  - Japan local PIC: なし

#### ASOC (Asia-Oceania)
- **EA Domi**: IAA
  - Level 1: peterson.so@one-line.com, florianne.sanchez@one-line.com
  - Level 2: krystle.onn@one-line.com; esther.tan@one-line.com
  - Level 3: amy.chan@one-line.com; krystle.onn@one-line.com
  - Level 4: tianhong.wee@one-line.com; noritaka.kurosu@one-line.com
  - Japan local PIC: lemuel.serrano@one-line.com, florianne.sanchez@one-line.com（ex JP only、Lemuel/FlorianneはLevel 1まで、Tanishima-sanはLevel 3まで）

- **OC Domi**: AUS;NZS
  - Level 1: hk.mktg.oc.pri@one-line.com; benny.chan@one-line.com
  - Level 2: yuki.yau@one-line.com
  - Level 3: sarah.man@one-line.com; irene.chan@one-line.com
  - Level 4: tianhong.wee@one-line.com; noritaka.kurosu@one-line.com

- **OC Non-domi**: AUN
  - Level 1: au.pri.national@one-line.com; daniel.hill@one-line.com; katie.gorman@one-line.com; jeff.li@one-line.com
  - Level 2: greg.tate@one-line.com; john.hughes@one-line.com
  - Level 3: sarah.man@one-line.com; irene.chan@one-line.com
  - Level 4: tianhong.wee@one-line.com; noritaka.kurosu@one-line.com

- **OC Non-domi**: NZN
  - Level 1: daniel.adamson@one-line.com
  - Level 2: russel.tully@one-line.com; mike.cate@one-line.com
  - Level 3: sarah.man@one-line.com; irene.chan@one-line.com
  - Level 4: tianhong.wee@one-line.com; noritaka.kurosu@one-line.com

#### TPTA (Trans-Pacific)
- **TP Domi**: TPE;WPE;AHE;AHW
  - CIF:ASEAN, Oceania, ISC, Middle East, and East Africa
    - Level 1: marygrace.sayson@one-line.com
    - Level 2: yu.araki@one-line.com;philip.tan@one-line.com;hueymian.woon@one-line.com
    - Level 3: takaaki.takahashi@one-line.com
    - Level 4: kohei.sawai@one-line.com; adeline.tang@one-line.com
  
  - CIF: China, Hong Kong, Taiwan, Korea and Vietnam
    - Level 1: carla.borja@one-line.com
    - Level 2: kelvin.c.lin@one-line.com;adele.wong@one-line.com;hueymian.woon@one-line.com
    - Level 3: takaaki.takahashi@one-line.com
    - Level 4: kohei.sawai@one-line.com; adeline.tang@one-line.com
  
  - CIF:JOA
    - Level 1: jerika.senales@one-line.com
    - Level 2: hueymian.woon@one-line.com; jasmine.lim@one-line.com
    - Level 3: takaaki.takahashi@one-line.com
    - Level 4: kohei.sawai@one-line.com; adeline.tang@one-line.com
  
  - CIF:Japan
    - Level 1: jinky.muralla@one-line.com
    - Level 2: jasmine.lim@one-line.com; kanae.kondo@one-line.com;hueymian.woon@one-line.com
    - Level 3: takaaki.takahashi@one-line.com
    - Level 4: kohei.sawai@one-line.com; adeline.tang@one-line.com
  
  - FOB:BCO
    - Level 1: kosuke.omori@one-line.com; yang.zhang@one-line.com
    - Level 2: kosuke.omori@one-line.com; yang.zhang@one-line.com; michael.wray@one-line.com
    - Level 3: tim.walsh@one-line.com; makoto.kodera@one-line.com
    - Level 4: kohei.sawai@one-line.com; adeline.tang@one-line.com
  
  - FOB:BCO - Japan
    - Level 1: michelle.pickens@one-line.com
    - Level 2: christina.abersold@one-line.com; michael.wray@one-line.com
    - Level 3: tim.walsh@one-line.com; makoto.kodera@one-line.com
    - Level 4: kohei.sawai@one-line.com; adeline.tang@one-line.com
    - Japan local PIC: あり
  
  - FOB:NVO
    - Level 1: christina.abersold@one-line.com; michael.wray@one-line.com
    - Level 2: christina.abersold@one-line.com; michael.wray@one-line.com
    - Level 3: tim.walsh@one-line.com; makoto.kodera@one-line.com
    - Level 4: kohei.sawai@one-line.com; adeline.tang@one-line.com
  
  - FOB:NVO - Japan
    - Level 1: christina.abersold@one-line.com; michael.wray@one-line.com
    - Level 2: christina.abersold@one-line.com; michael.wray@one-line.com
    - Level 3: tim.walsh@one-line.com; makoto.kodera@one-line.com
    - Level 4: kohei.sawai@one-line.com; adeline.tang@one-line.com
    - Japan local PIC: あり

#### AFLA (Asia-Latin America)
- **LE Domi**: LEW; CSE (excl ex JP)
  - Level 1: hk.mktg.laec.pri@one-line.com
  - Level 2: winky.ng@one-line.com; jenny.tsai@one-line.com
  - Level 3: wansan.tan@one-line.com; jenny.tsai@one-line.com
  - Level 4: benghin.lim@one-line.com; hiroki.yamakoshi@one-line.com
  - Japan local PIC: matsuru.shimamoto@one-line.com（Excl ex JP、Level 2まで）

- **LE Domi**: LEW; CSE (ex JP only)
  - Level 1: ziyu.au@one-line.com; GHQ.AFLA.MKTG.JP@one-line.com
  - Level 2: matsuru.shimamoto@one-line.com
  - Level 3: wansan.tan@one-line.com; jenny.tsai@one-line.com
  - Level 4: benghin.lim@one-line.com; hiroki.yamakoshi@one-line.com
  - Japan local PIC: matsuru.shimamoto@one-line.com（Ex JPN to Latam、Level 2まで）

- **LW Domi**: LWE (excl ex JP)
  - Level 1: ghq.lawc.mktg@one-line.com
  - Level 2: soonang.chong@one-line.com; ronny.yap@one-line.com
  - Level 3: wansan.tan@one-line.com; peisan.ong@one-line.com
  - Level 4: benghin.lim@one-line.com; hiroki.yamakoshi@one-line.com
  - Japan local PIC: matsuru.shimamoto@one-line.com（Excl ex JP、Level 2まで）

- **LW Domi**: LWE (ex JP only)
  - Level 1: ziyu.au@one-line.com; GHQ.AFLA.MKTG.JP@one-line.com
  - Level 2: matsuru.shimamoto@one-line.com
  - Level 3: wansan.tan@one-line.com; peisan.ong@one-line.com
  - Level 4: benghin.lim@one-line.com; hiroki.yamakoshi@one-line.com
  - Japan local PIC: matsuru.shimamoto@one-line.com（Ex JPN to Latam、Level 2まで）

- **LW Non-domi**: LWN; LWW; ILW
  - Level 1: nicolas.medina@one-line.com; cristobal.ferron@one-line.com; alessandro.napoli@one-line.com
  - Level 2: helga.timmermann@one-line.com
  - Level 3: mauricio.campello@one-line.com
  - Level 4: benghin.lim@one-line.com; hiroki.yamakoshi@one-line.com

- **LW Non-domi**: LWS
  - Level 1: caleb.carroll@one-line.com; adam.matthijs@one-line.com; michael.merlino@one-line.com
  - Level 2: elizabeth.small@one-line.com
  - Level 3: tim.walsh@one-line.com
  - Level 4: benghin.lim@one-line.com; hiroki.yamakoshi@one-line.com

### 日本ローカル承認者の特別ルール

#### 日本ローカル承認者がいる場合
- **AE (NE/ME Domi)**: mihoko.ito@one-line.com
  - Level 3まで承認可能
  - Level 4はMike Hanson、Yasuda-sanが承認

- **ASOC (EA Domi, WA Domi)**: lemuel.serrano@one-line.com, florianne.sanchez@one-line.com
  - ex JP only
  - Lemuel、FlorianneはLevel 1まで
  - Tanishima-sanはLevel 3まで

- **TPTA (FOB:BCO/NVO - Japan)**: 日本ローカル承認者あり

- **AFLA (LE/LW Domi)**: matsuru.shimamoto@one-line.com
  - Level 2まで承認可能
  - Excl ex JPまたはEx JPN to Latamの条件あり

### 承認プロセスの使用方法

#### 入力方法（HowToInput）
1. **Trade**: 必須項目、ドロップダウンリストから選択
2. **Service Scope Group**: 必須項目、ドロップダウンリストから選択
3. **Leg**: 必須項目、ドロップダウンリストから選択
4. **Service Scope Code**: 自動入力されるが、必要に応じて手動入力可能
5. **Level 1**: 必須項目、手動入力。Name1,Name2,etc. ; threshold amount(USD) to follow latest guideline
6. **Level 2**: 必須項目、手動入力。Name1,Name2,etc. ; threshold amount(USD) to follow latest guideline
7. **Level 3**: 必須項目、手動入力。Name1,Name2,etc. ; threshold amount(USD) to follow latest guideline
8. **Level 4**: 必須項目、手動入力。Name1,Name2,etc. ; threshold amount(USD) to follow latest guideline
9. **Do you have a separate approver for Japan local (exp/imp)?**: 必須項目、"Yes/No"を選択
10. **Japan local PIC**: オプション項目、必要に応じてコメント

### 関連情報
- **Commercial Waiver**: 商業的な配慮としての料金免除
- **DAR処理**: Demurrage and Detentionの処理と関連
- **承認プロセス**: Tigerシステムを使用した承認プロセス
- **AODOC**: Approval Routeが記載されているシステム

### 確認事項
- [ ] 実際のExcelファイルを開いて詳細な構造を確認
- [ ] 各Tradeごとの承認ルートを確認
- [ ] 日本ローカル承認者の権限を確認

## 次アクション
- [ ] 承認ルートの詳細をMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）
- [ ] FY25の承認ルートリストと比較
- [ ] Tigerシステムでの承認プロセスと統合

#commercial-waiver #approval-route #approval-threshold #dar #non-demdet #inbox #tiger-system

