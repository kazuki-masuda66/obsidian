# Chile Pricing - AP処理と特殊ケース

## 概要
Chile PricingにおけるAP（Allocation Plan）の処理方法、特殊なケース（太陽光パネル、Reefer、NORなど）の対応方法をまとめました。

## 内容

### AP (Allocation Plan) 処理

#### APとは
- **Allocation Plan**: 船腹配分計画
- **目的**: 各オフィスへの船腹配分を決定
- **期間**: 月次（例: December Week 49-01）

#### AP処理のフロー

**1. AP Inputの準備**
- **配布**: Marketingから各オフィスに配布
- **期間**: 8th November 2025 - MKTG to distribution to origins for input
- **フォーマット**: Google Sheets（共有ドライブ）

**2. AP Inputの提出**
- **期限**: 13th November 2025 - Sales to return AP Submission
- **確認**: PIC Check columnに"Done"を記入
- **完了**: "Complete"チェックボックスをチェック

**3. AP最終化**
- **期限**: 17th November 2025 - MKTG to finalize the AP and distribute to all offices
- **変更不可**: AP配布後は変更不可

#### AP処理のポイント

**ボリュームの調整**:
- **Pan South**: 中国旧正月前の需要増加に対応
- **例**: December APで253 TEUsに増加
- **理由**: 顧客の需要増加、パフォーマンス改善のコミットメント
- **AP実績**: 53 TEU/week（AX1: 64 TEU、AX2: 12 TEU、AX3: 24 TEU）
- **損失**: Octoberで127 TEUを失った（平均42 TEU/week in FAK rates）
- **120% AP honored**: AX3で120%のAPをhonor（例: ORIT2543E ONE ORINOCO）

**Walmart Chile AP実例**:
- **Nov AP**: 166 TEU per week
- **SPRC**: HKG + XMN BB = 60 TEU + 20% buffer maximum
- **Rolling Forecast**: 72 TEU for SPRC bookings（60 TEU + 20% buffer）
- **注意**: 72 TEUのrolling forecastを受け入れるわけではない。APは60 TEU to upload + 20% additional threshold
- **Booking実績**: 
  - MJUT0541E-AX2: 41 TEU（Firmed BKG 22 TEU、3 TEU production issue、final: 19 TEU）
  - 40 TEU booking cancelled and shifted to competitor
  - VRIT0542E-AX2: 22 TEU

**Falabella AP実例**:
- **AP**: 100 TEU/week + 20% buffer（最大120 TEU/week）
- **配分**: 同一ループ内で港配分自由（AP Flex）
- **Do-Not-Roll**: 厳守
- **AP by Loop**: AX1: 64 TEU、AX2: 12 TEU、AX3: 24 TEU
- **Mexico POD追加**: Nov-Decで10 TEU/week（Manzanillo and Lázaro Cárdenas）
- **レート**: CNBP/MXZLO & MXLZCはCNBP/CLVAPと同じレートを適用

**A. Hartrodt AP実例**:
- **目標**: 2,500 TEU（2025年）
- **実績**: 2024年1,368 TEU、2025 Q1+Q2 692 TEU、2025年見込み1,384 TEU
- **Gap**: 目標2,500 TEUに対して大幅に未達
- **Allocation**: 20 TEU/week（現在）、目標50 TEU/week
- **パフォーマンス**: 16-20 TEU with 70-87.50% performance
- **レートGap**: ONEは競合よりUSD 50-100高い

**サービス別の配分**:
- **AX1**: MONTEVIDEO EXPRESS
- **AX2**: ONE SPIRIT
- **AX3**: SEASPAN BRAVO
- **AX4**: HYUNDAI PREMIUM

**BSA (Basic Space Allocation)**:
- DecemberのBSAは船のサイズに応じて配分
- 大型船の到着により配分が増加する可能性

#### AP処理の注意点

**1. 期限厳守**
- AP Inputの提出期限を厳守
- 遅延は全体のスケジュールに影響

**2. 正確な情報**
- ボリューム、サービス、期間を正確に入力
- 誤りがあるとAP全体に影響

**3. 変更不可**
- AP配布後は変更不可
- 提出前に十分に確認

**4. チリチームとの連携**
- **Lisa Sanchez**: Commercial Steering Supervisor
- **Marco Aguero**: AP処理
- **Claudia Valenzuela**: AP処理
- **Paula Benito**: AP処理
- **Julio Rondanelli**: AP処理

### 特殊なケース

#### 1. 太陽光パネル（Solar Panels）
**ケース**: Altius / REQUEST QUOTATION FOR LOADING OF SOLAR PANELS FROM Shanghai
- **数量**: 533x40HC
- **期間**: Dic25 + Ene 26
- **POL**: Shanghai
- **POD**: Chile

**対応方法**:
- 新規NVO/NACアカウントか既存アカウントかを確認
- レート設定: CNSHA→CLSAI/CLVAP
- 例: USD 2,000/40HC

**注意点**:
- 大型貨物のため、スペース確保が必要
- 期間が長いため、複数の船に分ける可能性
- 特別な取り扱いが必要な場合がある

**注意点**:
- 大型貨物のため、スペース確保が必要
- 期間が長いため、複数の船に分ける可能性
- 特別な取り扱いが必要な場合がある

#### 2. Reefer（冷凍コンテナ）
**ケース**: BL NBOFF8554600 // EMPRESAS DEMARIA S.A. // From Ningbo to Valparaiso / Reefer
- **POL**: Ningbo
- **POD**: Valparaiso
- **タイプ**: Reefer

**対応方法**:
- Reeferレートを設定
- 電源確保が必要
- 温度管理が必要

**注意点**:
- Reeferは通常のコンテナより高額
- 電源確保のため、スペース制限がある
- 温度管理が重要

**Reefer/NOR実績**:
- **Chile向けR5**: 週平均443 TEU（Week 40-47）
- **目標**: 220 units or 440 TEU（目標達成）
- **Week 42**: Golden Week holidaysで低調
- **PECLL**: surplus stockとhigh roll poolのためcap中
- **Reefer campaign**: 11月から3月末まで
- **NOR需要**: 週平均360 boxes（16,000 TEU ÷ 22 weeks）が必要
- **現状**: 週平均200 boxes未満（10月実績）
- **August実績**: 300 reefer boxes/week未達
- **Industrias Cleaner**: 100% achievement（August）

#### 3. NOR（Not Otherwise Rated）
**ケース**: Expeditors Chile / NOR rates
- **POL**: CNDLC
- **POD**: CLSAI, CLCNL
- **レート**: USD 1,100/40NOR

**対応方法**:
- NORレートを設定
- 短期間の有効期限（例: 15 November to 31 November 2025）
- Free Time: 14 days at POD

**注意点**:
- 標準レート表にない特殊なレート
- 短期間の有効期限
- Local Chargesを明記

**NORボリュームの実績**:
- **Chile向け**: 週平均443 TEU（Week 40-47、R5）
- **目標**: 220 units or 440 TEU（目標達成）
- **NOR需要**: 週平均360 boxes（16,000 TEU ÷ 22 weeks）が必要
- **現状**: 週平均200 boxes未満（10月実績）
- **Reefer campaign**: 11月から3月末まで
- **Dorel Tender**: NOR volumeは60% of 1,900 TEU = 1,140 TEU

#### 4. 日本からの輸入（Return Cargoes）
**ケース**: rate request import from Japan to Chile a/c Hillebrand Gori (return cargoes)
- **POL**: JPYOK/JPKUB
- **POD**: CLSAI/CLVAP
- **レート例**: USD 7,700/40HC または USD 4,000/40HC

**対応方法**:
- Return Cargoesのレートを設定
- 日本からの輸入は特殊なルート
- レートは個別に確認

**注意点**:
- Return Cargoesは特殊なルート
- レートは個別に確認が必要
- 期間や条件を確認

**Maritrans - 日本からの輸入**:
- **POL**: JPNGO
- **POD**: CLVAP
- **DG貨物（80%）**: USD 5,500/40'st & hc、USD 5,400/20'st
- **NON-DG貨物（20%）**: USD 5,200/40'st & hc、USD 5,100/20'st
- **Free Time**: 21 days at POD
- **Valid**: 01/09 - 31/12
- **Commodity**: UN3166/CLASS9 FORKLIFTS（DG）、FORK LIFT TRUCKS, N.O.S.（NON-DG）

#### 5. タイからの特殊ルート
**ケース**: THBKK→CLPUQ
- **POL**: THBKK
- **POD**: CLPUQ
- **Add-on**: CLSAI FAK + USD 1,700/3,200/3,200

**対応方法**:
- Base Port（CLSAI）のFAKにAdd-onを追加
- サービス（Trasmares経由）を明記

**注意点**:
- Punta Arenasは特殊なルート
- Add-onを正確に計算
- サービス経由を明記

**タイからのReefer**:
- **THBKK→CLVAP/CLCNL/CLSVE/CLCNL/CLLQN**: USD 3,600/40RH
- **Valid**: 17 Sep - 30 Sep
- **Free Time**: 7 days free line detention at POD
- **Commodity**: Pharma productsは別途確認が必要

### 特殊ケースの対応ベストプラクティス

#### 1. 新規NVO/NACアカウントの確認
- 新規アカウントか既存アカウントかを確認
- 既存アカウントの場合は契約条件を確認

#### 2. 特殊な貨物の対応
- 太陽光パネル、Reeferなど特殊な貨物は個別対応
- スペース確保、特別な取り扱いが必要

#### 3. NOR対応
- 標準レート表にない特殊なレート
- 短期間の有効期限を設定
- Local Chargesを明記

#### 4. 特殊なルートの対応
- Punta Arenas、日本からの輸入など特殊なルート
- Add-onを正確に計算
- サービス経由を明記

## 次アクション
- [ ] [[20251121_Chile-Pricing-基本ルールとTigerシステム]]にリンク
- [ ] [[20251121_Chile-Pricing-主要顧客別ルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#chile #pricing #ap #allocation-plan #special-cases #solar-panels #reefer #nor #inbox

