# Chile Pricing - DAR処理方法

## 概要
Chile PricingにおけるDAR（Demurrage and Detention）の処理方法、Waiverの判断基準、実際のケーススタディをまとめました。

## 内容

### DARとは
- **Demurrage**: コンテナがCY（コンテナヤード）に滞留している期間の料金
- **Detention**: コンテナが顧客の管理下にある期間の料金
- **DAR**: Demurrage and Detention Request（料金免除・調整リクエスト）

### DAR処理の基本フロー

#### 1. DARリクエストの受信
- **Sebastian Mosqueira** (`sebastian.mosqueira@one-line.com`) がDAR Coordinator
- チリチーム（Loreto, Esmeraldaなど）からリクエストが来る
- 顧客からの要望をチリチームが代行してリクエスト

#### 2. リクエスト内容の確認
- **請求金額**: いくらのDARが発生しているか
- **RFA番号**: どの契約のDARか
- **理由**: なぜDARが発生したか（顧客のミス、ONEのミス、不可抗力など）
- **割引要求**: 何%の割引を求めているか
- **BL番号**: どのB/LのDARか

#### 3. 判断基準

**承認するケース**:
- ONEのミスが原因の場合
- 顧客が年間を通じて良好な実績を維持している場合（例: Falabella）
- 商業的な配慮（commercial gesture）が必要な場合
- 明確な理由があり、顧客のミスではない場合

**却下するケース**:
- 顧客の計画ミス（vendor planification issues）が原因の場合
- 顧客のミスが明確な場合
- 根拠が不十分な場合

#### 4. 承認・却下の判断
- **Simon Wong**: 最終判断者
- **Adele Chia**: RFA確認のためCCに入れる
- 判断後、チリチームに返答

### DAR処理の実際のケース

#### ケース1: Falabella - 2日間のCTIC延長
**状況**:
- **B/L**: NB5BCY690500
- **Invoice**: CLT043226
- **金額**: USD 480.00
- **理由**: NOR貨物の誤解による2日間の超過
- **要求**: 2日間のCTIC延長（DAR）

**判断**:
- 年間を通じてDARが発生していない（良好な実績）
- 顧客の誤解によるものだが、商業的な配慮が必要
- **承認**: 2日間のCTIC延長を承認

**ポイント**:
- Falabellaは非常に厳格なKPI管理をしている
- 年間を通じて良好な実績がある場合は、商業的な配慮を検討
- DAR番号: SCLBB25110027A

#### ケース2: Nutreco Cargo - 40%割引要求
**状況**:
- **請求金額**: USD 16,400
- **RFA**: TCANN00354A, TNBON00557A
- **理由**: ベンダーの計画ミスによる出荷集中（vendor planification issues）
- **要求**: 40%割引

**判断**:
- ONEのミスではない
- ベンダーの計画ミスが原因
- **却下**: 丁寧に却下

**ポイント**:
- 顧客側の計画ミスはONEの責任ではない
- 明確な理由がない場合は却下
- **詳細**: 
  - TCANN00354A: CANF26911500 - USD 16,080.00
  - TNBON00557A: NB5JJA419900 - USD 320.00
  - Total: USD 16,400.00

#### ケース3: Nutreco Cargo - 35%→40%割引の交渉
**状況**:
- **請求金額**: USD 249,120.00
- **要求**: 35%割引（USD 87,000）→ 42.5%割引要求 → 40%割引（USD 98,480）で最終決定
- **理由**: ベンダーの計画ミスによる出荷集中
- **条件**: USD 5,000/BL cap per BL

**判断**:
- 最初は35%割引を提案（USD 87,000）
- 顧客が42.5%を要求
- **最終決定**: 40%割引（USD 98,480）でcap、これ以上の交渉なし

**ポイント**:
- USD 5,000/BL cap per BLを設定
- 40%が上限、これ以上の交渉は不可
- 残額の支払いを確認
- **詳細**: 24件のInvoice、各BLにUSD 5,000 capを適用

#### ケース4: 50%割引 - 1回限りのケース
**状況**:
- **B/L**: SHAFD4280700
- **貨物**: 1x40'NOR ex CNSHA to CLSAI
- **請求金額**: USD 960
- **要求**: 50%割引（1回限り）

**判断**:
- 1回限りのケースとして承認
- **承認**: 50%割引を承認

**ポイント**:
- 1回限りのケースとして特別に承認
- 通常はこのような高率の割引は承認されない

### DAR Waiverの権限範囲
- **Adele**: USD 1,000まで
- **Sun Ang・Kazuki**: USD 5,000まで（見込み）
- それ以上の場合は上位承認が必要

### DAR処理の注意点

#### 1. 顧客の実績を確認
- 年間を通じて良好な実績がある場合は、商業的な配慮を検討
- 頻繁にDARが発生する顧客は、厳格に判断

#### 2. 原因の明確化
- ONEのミスか、顧客のミスかを明確にする
- 不可抗力の場合は個別に判断

#### 3. 商業的な配慮
- 重要な顧客（例: Falabella）の場合は、商業的な配慮を検討
- ただし、根拠が明確であることが前提

#### 4. DAR番号の管理
- DAR承認後は、DAR番号を記録
- チリチームがDARを作成するので、番号を確認

### Free Timeの標準
- **標準**: 21 days
- **Falabella**: 14 days（特別）
- **NOR**: 14 days（例: Expeditors Chile）
- **DAR処理**: 10 days（例: Capital Logistics）
- **Dorel**: 21 days（DRY）、15 days（40'NOR）
- **Empresas Demaria**: 14 days（DG）、21 days（dry）
- **延長要望**: 原則押し返す
- **特別なケース**: 個別に判断

### DAR処理の連携

#### チリチームとの連携
- **Sebastian Mosqueira**: DAR Coordinator
- **Loreto Aravena**: KA Sales、DARリクエスト
- **Esmeralda Hernandez**: DAR処理、承認依頼

#### シンガポールチームとの連携
- **Simon Wong**: 最終判断者
- **Adele Chia**: RFA確認
- **Sun Ang**: DAR Waiver権限（USD 5,000まで）

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
- [ ] [[20251121_Chile-Pricing-基本ルールとTigerシステム]]にリンク
- [ ] [[20251121_Chile-Pricing-主要顧客別ルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#chile #pricing #dar #demurrage #detention #waiver #inbox

