# 最高のPricing - CM最大化ガイド（Pricer視点）

## 📚 概要

Pricerの視点から、Contribution Margin（CM）を最大化するための包括的なガイド。営業ではなく、**いかにCMを最大化するか**に焦点を当てた実践的な戦略とノウハウをまとめています。

## 🎯 CM最大化の基本原則

### CMの定義と計算式

```
CM (Contribution Margin) = Revenue - Variable Cost
CM/TEU = 660 USD（または66 USD/t）を目安
```

### CM最大化の2つのアプローチ

1. **Revenue（収益）の最大化**
   - Base freight（基本運賃）の最適化
   - Inland haulage（内陸輸送費）の最大化
   - Manifested surcharge（マニフェスト記載のサーチャージ）の適切な設定

2. **Variable Cost（変動費）の最小化**
   - TES（Terminal cost）の最適化
   - TRS（Transport cost）の最適化
   - EPP（Empty Positioning Cost）の最小化
   - Reefer Bunker consumption Costの最適化
   - Agency Commissionの最適化

## 💰 Revenue最大化の戦略

### 1. Base Freight（基本運賃）の最適化

#### Benchmark Ratesの選択戦略

**選択肢**:
- **LT MRG（Long Term Minimum Rate Guideline）**: Trade Managementが設定した長期顧客向けの最小レートレベル
- **Target CM**: Trade Managementが設定した最小CMレベル
- **Current Contract**: 顧客とONEの間で合意された特定の港間ペアのレートレベル

**選択基準**:
```
1. 市場状況を確認
   - 需要が高い → Target CMまたはCurrent Contractを基準に上乗せ
   - 需要が低い → LT MRGを基準に、競争力のあるレートを設定

2. スペース状況を確認
   - スペース余裕（Roll Pool）がある → LT MRG基準で競争力重視
   - スペースがタイト → Target CM基準でCM最大化

3. 顧客の価値を評価
   - Tier1顧客（高ボリューム、長期契約） → Current Contract基準
   - スポット顧客 → Target CM基準でCM最大化
```

#### All In Calculationの活用

**目的**: Apple to Apple比較のため

```
All In Calculation = Benchmark Rates + Benchmark Rate Structure（Subject）
```

**戦略**:
- 顧客がAll Inしか求めていない場合でも、**常にBase Rateまで計算する**
- All In Calculationで比較することで、異なるレート構造を持つオファーを正確に評価
- Base Rate = All In Rates - Customer's Request Rate Structure

### 2. Surcharge（サーチャージ）の最適化

#### 必須サーチャージの設定

**標準サーチャージ**:
- **BRS/PSS/BAF/OBS**: 燃料関連サーチャージ
- **HEA**: Heavy Equipment Additional（重量貨物追加料金）
- **LSF**: Low Sulphur Fuel（低硫黄燃料）
- **CSS**: Currency Surcharge（通貨サーチャージ）
- **SLF**: Security Low Sulphur Fuel（セキュリティ低硫黄燃料）
- **THCS**: Terminal Handling Charge Surcharge（ターミナルハンドリングチャージサーチャージ）

**戦略**:
```
1. 可能な限り条件付きで付加
   - "subject to HEA" → 重量貨物の場合のみ追加
   - "subject to prevailing surcharges" → 市場状況に応じて追加

2. 顧客の要望を確認
   - 顧客がAll Inを求めている場合 → 全て含める
   - 顧客がBase Rateのみを求めている場合 → サーチャージを差し引く

3. 市場競争力を考慮
   - 競合がサーチャージを含めている → 含める
   - 競合がBase Rateのみ → サーチャージを差し引いて比較
```

#### Inland Haulage（内陸輸送費）の最大化

**戦略**:
- 内陸輸送が必要な場合、**必ずInland haulageを追加**
- 顧客が内陸輸送を求めている場合、**適切なレートを設定**
- 内陸輸送のコストを考慮し、**CMを確保できるレートを設定**

### 3. 市場状況に応じたレート設定

#### 市場分析の重要性

**確認すべき情報**:
- **競合他社のレート**: EMC、CMA、Evergreenなど
- **市場レートレベル**: FAK、Tier1、スポットレート
- **スペース状況**: Roll Pool、Backlog、Draft issues
- **季節要因**: Golden Week後、年末年始、シーズン貨物

**戦略**:
```
1. 市場が強い場合（需要 > 供給）
   - Target CM基準でレート設定
   - サーチャージを積極的に付加
   - スペースがタイトな場合は、さらに上乗せ

2. 市場が弱い場合（需要 < 供給）
   - LT MRG基準でレート設定
   - サーチャージを最小限に
   - スペース余裕がある場合は、競争力重視

3. 市場が均衡している場合
   - Current Contract基準でレート設定
   - 標準的なサーチャージを設定
   - 顧客の価値に応じて調整
```

## 📊 Variable Cost最小化の戦略

### 1. EPP（Empty Positioning Cost）の最小化

#### EPPの理解

**EPP = EPC（Empty Positioning Cost）**:
- **EPP A**: 標準的なEPP（基本全てEPP A）
- **EPP B**: 過去1年を計算（TP tradeなど、シーズナリティがある場合）

**EPPのSurplus/Deficit**:
- **上海**: Deficitになりがち（空コンテナが必要）
- **ロサンゼルス**: Surplusになりがち（空コンテナが余る）

**戦略**:
```
1. EPPの確認
   - Pricing SimulationでEPPを確認
   - EPPが高い場合は、レートに反映

2. 空ポジコストの考慮
   - LosでLadenで貨物を取ると、その分空Posiしなくてすむ → インセンティブ
   - EPCはTEU単位で計算
   - せめて空ポジコストがないととらせない

3. ネガティブCMの回避
   - ネガティブのCMはとっちゃだめ
   - 取らずに空ポジさせたほうが優位
   - 将来かかる空ポジコストはそのPricingで回収
```

#### TP（Trans-Pacific）の特殊性

**TPはEPP B**:
- 北米発はシーズナリティがある
  - 牧草、魚、カニ
  - 年に数回ドカンとくる
  - 北米の西岸から箱を持ってくる
    - 12月はReferをもってこないといけない
    - それ以外はめちゃくちゃSurplus
- **Pricingでもこういう点を考慮している**

### 2. TES（Terminal cost）の最適化

**戦略**:
- **ターミナルの選択**: コストが低いターミナルを選択
- **ルーティングの最適化**: ターミナルコストを最小化するルーティング
- **Pricing Simulationで確認**: 各BookingのRoutingに基づいて自動計算される

### 3. TRS（Transport cost）の最適化

**戦略**:
- **ルーティングの最適化**: 輸送コストを最小化するルーティング
- **内陸輸送の最適化**: 内陸輸送コストを最小化
- **Pricing Simulationで確認**: 各BookingのRoutingに基づいて自動計算される

### 4. Reefer Bunker consumption Costの最適化

**戦略**:
- **Reefer貨物の評価**: Reefer Bunker consumption Costを考慮
- **Frozen/Chilledの違い**: FrozenとChilledでコストが異なる
- **Pricing Simulationで確認**: 各BookingのRoutingに基づいて自動計算される

## 🎯 船腹配分とスペース管理

### 1. スペース状況の確認

**確認すべき情報**:
- **Roll Pool**: スペース余裕
- **Backlog**: 積み残し
- **Draft issues**: 吃水制約
- **Equipment availability**: コンテナの可用性

**戦略**:
```
1. スペースがタイトな場合
   - CM最大化を優先
   - 高CM貨物を優先
   - 低CM貨物はRollover

2. スペース余裕がある場合
   - 競争力重視
   - ボリューム確保
   - 長期顧客との関係維持
```

### 2. AP（Account Plan）との連携

**APの理解**:
- **BSA（Berth Space Allocation）**: 各顧客に保証する船腹量
- **Sales Target**: 営業目標
- **Actual Lifting**: 実際の船積み実績

**戦略**:
```
1. APの確認
   - 顧客のBSAを確認
   - Sales Targetを確認
   - Actual Liftingを確認

2. APに基づいたPricing
   - BSAを超える場合は、CM最大化を優先
   - BSA内の場合は、Current Contract基準
   - Sales Targetを達成するために、適切なレートを設定
```

### 3. Yield Managementの実践

**Yield Managementの目的**:
- **Contribution Marginの最大化**
- **正確なCMの評価基準の設定**
- **適切な目標設定**
- **ステークホルダーを巻き込んだ実行**

**戦略**:
```
1. 顧客の評価
   - Port Pair別のパフォーマンスを評価
   - CM/TEUで顧客をランク付け
   - 高CM顧客を優先

2. 貨物の評価
   - OCN（Ocean）: 100% Utilizationを目指す
   - IPC（Interport/Wayport）: CMを確保
   - T/S（Transshipment）: CMを確保
   - MT（Empty Container）: 動的な管理

3. Portfolio Strategy
   - Trade/Service PortfolioとCargo Portfolioの最適化
   - Pricing Management、Space Management、Route Managementの統合実行
```

## 📈 実践的なPricingプロセス

### ステップ1: データの準備と取得

**データソース**:
- **PRISM**: Pricing Simulation（運賃シミュレーション）
- **COA**: Lifting等の実績（過去の船積み実績）
- **DMT**: Tariff（運賃表）
- **TenderDB**: Contractの情報（契約データ）
- **Salesforce**: FAK・MRGレートの管理

**確認すべき情報**:
- **顧客情報**: BCO（Contract No）またはNVO（NVとNAC）
- **過去のLifting実績**: 過去の取引実績を確認
- **現在のContract**: 既存契約の内容を確認
- **市場状況**: 競合他社のレート、スペース状況、季節要因

### ステップ2: Eagle-X Pricing Toolの使用

#### Pricing Toolの起動

1. **共通フォーマットをインポート**
   - Tradeごとにテンプレートが用意されている
   - MRGやサーチャージがTradeごとに異なる

2. **Search Data**
   - 顧客を選択（NVOを選ぶと横にNACが出てくる）
   - 過去のLifting実績を確認
   - 現在のContractを確認

#### Benchmark Ratesの決定

**選択基準**:
```
1. 市場状況を確認
   - 需要が高い → Target CMまたはCurrent Contractを基準に上乗せ
   - 需要が低い → LT MRGを基準に、競争力のあるレートを設定

2. スペース状況を確認
   - スペース余裕（Roll Pool）がある → LT MRG基準で競争力重視
   - スペースがタイト → Target CM基準でCM最大化

3. 顧客の価値を評価
   - Tier1顧客（高ボリューム、長期契約） → Current Contract基準
   - スポット顧客 → Target CM基準でCM最大化
```

#### All In Calculation

**計算式**:
```
All In Calculation = Benchmark Rates + Benchmark Rate Structure（Subject）
```

**目的**: Apple to Apple比較のため

#### Base Rateの算出

**計算式**:
```
Base Rate = All In Rates - Customer's Request Rate Structure
```

**戦略**:
- 顧客がAll Inしか求めていない場合でも、**常にBase Rateまで計算する**
- Base Rateで顧客に提示するレートレベルを決定

### ステップ3: 採算性の確認

#### Expected CM/TEUの計算

**目標**: CM/TEU = 660 USD（または66 USD/t）を目安

**確認方法**:
- **Pricing Simulation**: 各BookingのRoutingに基づいて自動計算される
- **OPUS COA**: Post shipmentのCM計算が可能

**判断基準**:
```
1. CM/TEU ≥ 660 USD（または66 USD/t）
   → 承認可能

2. CM/TEU < 660 USD（または66 USD/t）
   → 以下の判断が必要：
   - スペースがタイト → Rollover
   - スペース余裕がある → 競争力重視で承認
   - ネガティブCM → 絶対に承認しない
```

#### Variable Costの確認

**確認すべき項目**:
- **TES**: Terminal cost
- **TRS**: Transport cost
- **EPP**: Empty Positioning Cost
- **Reefer Bunker consumption Cost**: 冷凍コンテナのバンカー消費コスト
- **CM**: Agency Commission

**最適化のポイント**:
- **ルーティングの最適化**: コストが低いルーティングを選択
- **EPPの最小化**: 空ポジコストを最小化
- **ターミナルの選択**: コストが低いターミナルを選択

### ステップ4: レート提示と承認

#### レート提示の準備

**必須条件（Remarks）**:
- **Offer Validity**: 7日以内にnominationがない場合、レートは無効
- **Rate Validity**: 具体的な期間を明記
- **Rates are inclusive of**: 運賃に含まれるサーチャージ
- **Local Charges**: 現地費用の取り扱い
- **貨物条件**: CY/CY, Non-DGなど
- **Equipment and Space Availability**: 設備・スペースの可用性
- **Free Time**: 無料期間

#### 承認判断

**承認基準**:
```
1. CM/TEU ≥ 660 USD（または66 USD/t）
   → 承認可能

2. CM/TEU < 660 USD（または66 USD/t）
   → 以下の判断が必要：
   - スペースがタイト → Rollover
   - スペース余裕がある → 競争力重視で承認
   - ネガティブCM → 絶対に承認しない

3. 特別なケース
   - Tier1顧客（高ボリューム、長期契約） → 柔軟に対応
   - 戦略的顧客 → 長期的な関係を考慮
   - 市場競争力 → 競合他社との比較を考慮
```

## 🔍 高度な戦略とテクニック

### 1. 顧客別の価値評価

#### 顧客の分類

**Tier1顧客**:
- 高ボリューム
- 長期契約
- 安定した取引実績
- **戦略**: Current Contract基準、柔軟に対応

**Tier2顧客**:
- 中ボリューム
- 短期契約またはスポット
- 変動する取引実績
- **戦略**: Target CM基準、CM最大化を優先

**スポット顧客**:
- 低ボリューム
- 単発案件
- 不規則な取引実績
- **戦略**: Target CM基準、CM最大化を最優先

#### 顧客の価値評価

**評価基準**:
- **ボリューム**: 年間TEU数
- **CM/TEU**: 平均CM/TEU
- **契約期間**: 長期契約か短期契約か
- **取引実績**: 過去のLifting実績
- **戦略的重要性**: 市場シェア、ブランド価値など

**戦略**:
```
1. 高価値顧客（Tier1）
   - Current Contract基準
   - 柔軟に対応
   - 長期的な関係を考慮

2. 中価値顧客（Tier2）
   - Target CM基準
   - CM最大化を優先
   - 競争力も考慮

3. 低価値顧客（スポット）
   - Target CM基準
   - CM最大化を最優先
   - スペースがタイトな場合はRollover
```

### 2. 市場状況に応じた動的Pricing

#### 市場分析の実践

**確認すべき情報**:
- **競合他社のレート**: EMC、CMA、Evergreenなど
- **市場レートレベル**: FAK、Tier1、スポットレート
- **スペース状況**: Roll Pool、Backlog、Draft issues
- **季節要因**: Golden Week後、年末年始、シーズン貨物

**戦略**:
```
1. 市場が強い場合（需要 > 供給）
   - Target CM基準でレート設定
   - サーチャージを積極的に付加
   - スペースがタイトな場合は、さらに上乗せ

2. 市場が弱い場合（需要 < 供給）
   - LT MRG基準でレート設定
   - サーチャージを最小限に
   - スペース余裕がある場合は、競争力重視

3. 市場が均衡している場合
   - Current Contract基準でレート設定
   - 標準的なサーチャージを設定
   - 顧客の価値に応じて調整
```

#### GRI（General Rate Increase）戦略

**GRIのタイミング**:
- **市場が強い場合**: GRIを積極的にPush
- **市場が弱い場合**: GRIは慎重に
- **競合他社の動向**: 競合がGRIをPushしている場合は、追随

**戦略**:
```
1. GRIの設定
   - 市場レベルを確認
   - 競合他社のGRIを確認
   - ONEのFAKを確認

2. GRIの実施
   - 市場が強い場合 → GRIをPush
   - 市場が弱い場合 → GRIは慎重に
   - 競合がGRIをPushしている場合 → 追随を検討
```

### 3. スペース管理との連携

#### Roll Poolの管理

**Roll Poolの確認**:
- **スペース余裕**: Roll Poolが大きい → 競争力重視
- **スペースタイト**: Roll Poolが小さい → CM最大化

**戦略**:
```
1. Roll Poolが大きい場合
   - 競争力重視
   - ボリューム確保
   - LT MRG基準でレート設定

2. Roll Poolが小さい場合
   - CM最大化
   - 高CM貨物を優先
   - Target CM基準でレート設定
```

#### Backlogの管理

**Backlogの確認**:
- **Backlogが大きい**: スペースがタイト → CM最大化
- **Backlogが小さい**: スペース余裕 → 競争力重視

**戦略**:
```
1. Backlogが大きい場合
   - CM最大化を優先
   - 高CM貨物を優先
   - 低CM貨物はRollover

2. Backlogが小さい場合
   - 競争力重視
   - ボリューム確保
   - LT MRG基準でレート設定
```

### 4. ポートペア別の最適化

#### ポートペアの評価

**評価基準**:
- **CM/TEU**: ポートペア別の平均CM/TEU
- **ボリューム**: ポートペア別の年間TEU数
- **EPP**: ポートペア別のEPP
- **競争力**: ポートペア別の市場競争力

**戦略**:
```
1. 高CMポートペア
   - CM最大化を優先
   - 高CM貨物を優先
   - Target CM基準でレート設定

2. 低CMポートペア
   - 競争力重視
   - ボリューム確保
   - LT MRG基準でレート設定
   - EPPを考慮
```

## 📋 チェックリスト

### Pricing前の確認事項

- [ ] 顧客情報の確認（BCO/NVO、過去のLifting実績、現在のContract）
- [ ] 市場状況の確認（競合他社のレート、スペース状況、季節要因）
- [ ] スペース状況の確認（Roll Pool、Backlog、Draft issues、Equipment availability）
- [ ] データソースの確認（PRISM、COA、DMT、TenderDB、Salesforce）

### Pricing時の確認事項

- [ ] Benchmark Ratesの選択（LT MRG、Target CM、Current Contract）
- [ ] All In Calculationの計算（Benchmark Rates + Benchmark Rate Structure）
- [ ] Base Rateの算出（All In Rates - Customer's Request Rate Structure）
- [ ] Expected CM/TEUの計算（目標: 660 USD/TEUまたは66 USD/t）
- [ ] Variable Costの確認（TES、TRS、EPP、Reefer Bunker consumption Cost、CM）

### Pricing後の確認事項

- [ ] レート提示の準備（必須条件（Remarks）の確認）
- [ ] 承認判断（CM/TEU、スペース状況、顧客の価値）
- [ ] システム入力（Tiger、OPUS、Eagle）
- [ ] メール送信（顧客向け回答メール、社内承認依頼メール）

## 🎓 実践例

### 例1: 高CM貨物のPricing

**状況**:
- 顧客: Tier1顧客（高ボリューム、長期契約）
- ポートペア: CNNGB → ECGYE
- コンテナ: 40HC
- 市場状況: 需要が高い、スペースがタイト

**Pricingプロセス**:
```
1. Benchmark Ratesの選択
   - Current Contract基準（Tier1顧客、長期契約）

2. All In Calculation
   - Current Contract + Benchmark Rate Structure（Subject）

3. Base Rateの算出
   - All In Rates - Customer's Request Rate Structure

4. 採算性の確認
   - Expected CM/TEU = 800 USD/TEU（目標: 660 USD/TEU以上）
   - Variable Cost: TES、TRS、EPP、CMを確認

5. レート提示
   - Base Rate: USD 2,000/40HC
   - サーチャージ: BRS/PSS/BAF/OBS subj HEA, LSF, CSS, SLF, THCS
   - Free Time: 21 days at POD
   - Validity: 7 days
```

### 例2: 低CM貨物のPricing

**状況**:
- 顧客: スポット顧客（低ボリューム、単発案件）
- ポートペア: CNNGB → CLSAO
- コンテナ: 20GP
- 市場状況: 需要が低い、スペース余裕

**Pricingプロセス**:
```
1. Benchmark Ratesの選択
   - LT MRG基準（スポット顧客、スペース余裕）

2. All In Calculation
   - LT MRG + Benchmark Rate Structure（Subject）

3. Base Rateの算出
   - All In Rates - Customer's Request Rate Structure

4. 採算性の確認
   - Expected CM/TEU = 500 USD/TEU（目標: 660 USD/TEU未満）
   - Variable Cost: TES、TRS、EPP、CMを確認
   - 判断: スペース余裕があるため、競争力重視で承認

5. レート提示
   - Base Rate: USD 1,200/20GP
   - サーチャージ: 最小限
   - Free Time: 21 days at POD
   - Validity: 7 days
```

### 例3: ネガティブCM貨物のPricing

**状況**:
- 顧客: スポット顧客（低ボリューム、単発案件）
- ポートペア: CNNGB → CLSAO
- コンテナ: 20GP
- 市場状況: 需要が低い、スペース余裕

**Pricingプロセス**:
```
1. Benchmark Ratesの選択
   - LT MRG基準（スポット顧客、スペース余裕）

2. All In Calculation
   - LT MRG + Benchmark Rate Structure（Subject）

3. Base Rateの算出
   - All In Rates - Customer's Request Rate Structure

4. 採算性の確認
   - Expected CM/TEU = -100 USD/TEU（ネガティブCM）
   - Variable Cost: TES、TRS、EPP、CMを確認
   - 判断: ネガティブCMのため、絶対に承認しない
   - 代替案: 取らずに空ポジさせたほうが優位

5. レート提示
   - Decline offer
   - Decline reason: Negative CM
```

## 🔗 関連リンク

- [[Pricingのプロセス-運賃設定の方法と手順]]
- [[CM-Contribution-Margin-計算方法-OPUS-COA]]
- [[CM-EPCについて-粗利と空コンテナポジショニングコスト]]
- [[EagleX-Pricing-Tool-Calculation-Logic]]
- [[Space-Management-Grand-Design-戦略設計]]
- [[Eagle-Project-Yield-Management-プロジェクト概要]]
- [[スポットビジネスとショートの違い-契約形態の理解]]
- [[../../../../../.cursor/commands/pricing.md]] - プライシング業務支援コマンド（Cursor AI）

## 📝 備考

- このガイドはPricerの視点から、CM最大化に焦点を当てた実践的な戦略とノウハウをまとめています
- 営業ではなく、**いかにCMを最大化するか**に焦点を当てています
- 実務での活用を想定して、具体的な戦略とテクニックを記載しています

#pricing #cm-maximization #pricer #yield-management #space-management #work/one #work/one/afla

