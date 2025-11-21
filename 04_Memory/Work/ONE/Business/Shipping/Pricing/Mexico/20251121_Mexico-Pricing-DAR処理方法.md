# Mexico Pricing - DAR処理方法

## 概要
Mexico PricingにおけるDAR（Demurrage and Detention）の処理方法、Waiverの判断基準、実際のケーススタディをまとめました。

## 内容

### DARとは
- **Demurrage**: コンテナがCY（コンテナヤード）に滞留している期間の料金
- **Detention**: コンテナが顧客の管理下にある期間の料金
- **DAR**: Demurrage and Detention Request（料金免除・調整リクエスト）

### DAR処理の基本フロー

#### 1. DARリクエストの受信
- **Jacqueline Estrada** (`jacqueline.estrada@one-line.com`): Demurrages Coordinator
- **Sandra Hernandez** (`sandra.hernandez@one-line.com`): Demurrages Coordinator
- **Andrea Lomeli** (`andrea.lomeli@one-line.com`): Sales Executive、DARリクエスト
- **Angeles Olivares** (`angeles.olivares@one-line.com`): Sales Executive、Commercial Support

#### 2. リクエスト内容の確認
- **請求金額**: いくらのDARが発生しているか
- **RFA番号**: どの契約のDARか
- **理由**: なぜDARが発生したか（顧客のミス、ONEのミス、不可抗力など）
- **割引要求**: 何%の割引を求めているか
- **BL番号**: どのB/LのDARか

#### 3. 判断基準

**承認するケース**:
- ONEのミスが原因の場合
- 顧客が年間を通じて良好な実績を維持している場合
- 商業的な配慮（commercial gesture）が必要な場合
- 明確な理由があり、顧客のミスではない場合
- メキシコ税関（Mexican Customs）の手続きが原因の場合（例: dumping accusation）

**却下するケース**:
- 顧客の計画ミスが原因の場合
- 顧客のミスが明確な場合（例: 規制・税関関連の問題）
- 根拠が不十分な場合
- メキシコ税関の手続き上の問題が顧客側にある場合

#### 4. 承認・却下の判断
- **Kazuki Masuda**: 最終判断者
- **Soon Ang Chong**: 判断者
- **Ron Yap**: 判断者
- 判断後、メキシコチームに返答

### DAR処理の実際のケース

#### ケース1: TL PACIFICO - メキシコ税関による差し押さえ
**状況**:
- **B/L**: NB4ID9533300
- **コンテナ**: TLLU5441704, TLLU5725167, TRHU4017910
- **金額**: USD 22,624（うちTRHU4017910がUSD 16,000以上）
- **理由**: メキシコ税関によるdumping accusation（3ヶ月以上差し押さえ）
- **タイムライン**:
  - ETA: June 10
  - June 17: コンテナが差し押さえられた日
  - Sept 23: リリース日（税関がdumpingなしと認めた）
  - Sept 26: 港を出た日
  - October 03: 顧客に配送された日
  - October 03: 空コンテナ返却日
- **要求**: 割引

**判断**:
- メキシコ税関の手続きが原因
- ただし、顧客側にも手続き上の問題があった
- **却下**: メキシコ税関の手続きは顧客と税関当局の間の問題であり、ONEの責任ではない

**ポイント**:
- メキシコ税関の手続きは顧客と税関当局の間の問題
- ONEの責任ではない場合は却下
- ただし、商業的な配慮を検討する場合もある

#### ケース2: SPARX INTERNATIONAL FREIGHT - Commercial Support
**状況**:
- **金額**: USD 28,215
- **理由**: 規制・税関関連の問題による遅延
- **要求**: 15%割引

**判断**:
- 顧客の規制・税関関連の問題が原因
- ただし、2025年に120+ TEUの実績がある
- **承認**: 商業的な配慮として10%割引（最大レベル）

**ポイント**:
- 顧客の実績を考慮
- 商業的な配慮として最大10%まで
- 顧客のミスが原因でも、実績があれば検討

#### ケース3: コンテナ盗難（Stolen Container）
**状況**:
- **B/L**: XMNF59004600
- **コンテナ**: TCLU8486366
- **金額**: USD 6,930
- **理由**: コンテナが盗難された（Free Time終了12日前）

**実例: 詳細なコンテナ盗難ケース**
- **総額**: USD 8,910.00
- **部分支払い**: USD 3,330.00（August 20thまで）
- **盗難日**: October 20th
- **残額**: USD 4,455.00（detention charges）
- **DVコスト**: USD 3,700（USD 3,400 + USD 300 Admin fee）
- **処理**: 顧客が30日以内にコンテナを回収または空コンテナを返却した場合、警察報告書の日付でdetentionをカット

**処理ルール**:
- **警察報告書（Police report）**: 確認が必要
- **DV（Depreciation Value）**: 支払い確認
- **処理**: 
  - 顧客が30日以内にコンテナを回収または空コンテナを返却した場合、警察報告書の日付でdetentionをカット
  - コンテナが空で返却されない場合、顧客がDVを支払い、警察報告書の日付でdetentionを停止

**ポイント**:
- メキシコではコンテナ盗難が多発（カルテルによる内陸輸送中の盗難）
- 警察報告書の日付でdetentionをカット
- DV支払い確認が必要

#### ケース4: MABE - Free Time延長
**状況**:
- **B/L**: ONEY CANF74086400, ONEY CANF74087500, ONEY CANF74088600, ONEY CANF74085300
- **理由**: Golden Week前に積み込み、最初の利用可能なMNで出荷したい
- **要求**: Free Time延長（14 days → 17 days、3日追加）

#### ケース5: STARMARK - 税関問題によるDAR
**状況**:
- **B/L**: SH5AA1175300
- **Vessel**: HYUNDAI VOYAGER V.0156E
- **コンテナ**: 1X40'HQ
- **ルート**: SHANGHAI - LAZARO CARDENAS, MEXICO
- **ETD**: Jun 3
- **金額**: USD 13,365.00 detention charges
- **理由**: 税関問題による遅延
- **実績**: 2025年にregular support
- **要求**: 割引

**判断**:
- 税関問題は顧客と税関当局の間の問題
- ただし、顧客の実績を考慮して検討

#### ケース6: BEIERSDORF - 大規模DAR処理
**状況**:
- **金額**: USD 64,640.00 generated（100%）
- **回収額**: USD 47,660.00（74%）
- **要求**: 26% discount
- **保証金**: USD 2,000.00（Customs Broker支払い、総額の10%）
- **Write Off**: USD 18,664.39承認要求
- **DV**: USD 6,700.00（キャンセル済み）
- **処理**: 26%割引をシステムに登録

**判断**:
- 重要な顧客（MABE）
- Golden Week前の特別なケース
- **承認**: 一度限り（once off）として承認

**ポイント**:
- 重要な顧客の特別なケースは検討
- 一度限り（once off）として承認
- Free Time延長は慎重に判断

### DAR Waiverの権限範囲
- **Adele**: USD 1,000まで
- **Sun Ang・Kazuki**: USD 5,000まで（見込み）
- それ以上の場合は上位承認が必要

### DAR割引率の実例
- **10%**: SPARX（最大レベル）、一般的な商業的配慮の上限
- **15%**: 一部のケースで検討（例: STARMARK要求）
- **25%**: 大規模DARで検討（例: USD 96,775のDARで25%承認、USD 24,193.75）
- **26%**: BEIERSDORF（USD 64,640 generated、USD 47,660 recovered）
- **50%**: 特別なケースで検討（例: コンテナ盗難、長期滞在）
- **60%**: 極めて特別なケース（例: 一部の長期滞在コンテナ）
- **85%**: 顧客要求（例: DELMAR、UPS）だが通常は却下または大幅に削減

### DAR処理の注意点

#### 1. 顧客の実績を確認
- 年間を通じて良好な実績がある場合は、商業的な配慮を検討
- 頻繁にDARが発生する顧客は、厳格に判断

#### 2. 原因の明確化
- ONEのミスか、顧客のミスかを明確にする
- メキシコ税関の手続きは顧客と税関当局の間の問題
- 不可抗力の場合は個別に判断

#### 3. 商業的な配慮
- 重要な顧客（例: SPARX、MABE）の場合は、商業的な配慮を検討
- ただし、根拠が明確であることが前提
- 最大10%まで（例: SPARX）

#### 4. メキシコ特有のケース
- **コンテナ盗難**: 警察報告書の日付でdetentionをカット
- **メキシコ税関の手続き**: 顧客と税関当局の間の問題、ONEの責任ではない

### Free Timeの標準
- **標準**: 14 days（例: MABE契約）
- **延長要望**: 個別に判断
- **特別なケース**: Golden Week前など、3日延長を検討
- **MABE**: 21 days import（特別な契約条件）
- **STARMARK**: 12 days（DG貨物の場合）
- **到着通知**: 15 days in advance（リリース通知を送るため）
- **レート有効期限**: 14 days（例: CNTAO-MXZLO）

### DAR処理の連携

#### メキシコチームとの連携
- **Jacqueline Estrada**: Demurrages Coordinator
- **Sandra Hernandez**: Demurrages Coordinator
- **Andrea Lomeli**: Sales Executive、DARリクエスト
- **Angeles Olivares**: Sales Executive、Commercial Support

#### シンガポールチームとの連携
- **Kazuki Masuda**: 最終判断者
- **Soon Ang Chong**: 判断者
- **Ron Yap**: 判断者
- **Adele Chia**: DAR Waiver権限（USD 1,000まで）

### DAR処理のベストプラクティス

#### 1. 迅速な対応
- DARリクエストは迅速に対応
- 顧客の信頼を維持するため、遅延を避ける

#### 2. 明確な説明
- 承認・却下の理由を明確に説明
- 数字・テーブルでの反証が有効

#### 3. 記録の保持
- DAR処理の記録を保持
- 将来の判断の参考にする

#### 4. 顧客との関係維持
- 重要な顧客とは良好な関係を維持
- 商業的な配慮と厳格な判断のバランスを取る

## 次アクション
- [ ] [[20251121_Mexico-Pricing-基本ルールとTigerシステム]]にリンク
- [ ] [[20251121_Mexico-Pricing-主要顧客別ルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#mexico #pricing #dar #demurrage #detention #waiver #inbox

