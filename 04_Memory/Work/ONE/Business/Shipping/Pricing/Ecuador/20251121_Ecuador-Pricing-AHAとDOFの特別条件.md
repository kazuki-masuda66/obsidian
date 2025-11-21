# Ecuador Pricing - AHAとDOFの特別条件

## 概要
Ecuador PricingにおけるAHA（Adjusted Handling Allowance）とDOF（Destination Origin Fee）の特別条件についてまとめました。FARLETZA、PLUSCARGOなど、特定の顧客に適用される特別条件を含みます。

## 内容

### AHAとDOFとは
- **AHA（Adjusted Handling Allowance）**: 調整されたハンドリング手当
- **DOF（Destination Origin Fee）**: 目的地・積出地手数料
- **特別条件**: 特定の顧客に適用される特別な条件

### 特別条件を持つ顧客

#### FARLETZA S.A.
- **顧客コード**: EC100277
- **RFA**: GYE00176
- **特別条件**: AHAとDOFの特別条件あり
- **注意点**: MRG rate approval時に特別条件を考慮

**処理時の注意点**:
- MRG rate approval時にAHAとDOFの特別条件を必ず確認
- Tigerシステムでレート修正リクエストを作成する際に、特別条件を明記
- 特別条件の詳細はRFAで確認

#### PLUSCARGO-ECUADOR S.A.
- **顧客コード**: EC100598
- **RFA**: GYEN00147A
- **特別条件**: AHA Fixed USD 50の現地特典あり
- **処理**: AHA concessionをOFTに反映

**AHA concessionの計算**:
- **AHA**: 112 - 50 = 62
- **OFT**: 1,350 - 62 = 1,288
- **処理**: AHA Fixed USD 50の現地特典を考慮して、AHA concessionをOFTに反映

**処理時の注意点**:
- AHA Fixed USD 50の現地特典を考慮
- AHA concessionをOFTに反映する必要がある
- Tigerシステムでレート修正リクエストを作成する際に、AHA concessionの計算を明記

### AHAとDOFの特別条件の処理方法

#### 1. FARLETZA - AHAとDOFの特別条件
**処理フロー**:
1. MRG rate approval時にAHAとDOFの特別条件を確認
2. Tigerシステムでレート修正リクエストを作成
3. 特別条件を明記（Freetext Sectionに記載）
4. 承認を待つ

**Tigerシステムでの記載例**:
```
Freetext Section: Dear all, Please your kind help with this MRG rate 
approval, the correct rate for this range is the sent one, note this 
customer has special conditions for AHA and DOF, thanks,
```

#### 2. PLUSCARGO - AHA Fixed USD 50の現地特典
**処理フロー**:
1. AHA Fixed USD 50の現地特典を確認
2. AHA concessionを計算（AHA: 112 - 50 = 62）
3. OFTにAHA concessionを反映（OFT: 1,350 - 62 = 1,288）
4. Tigerシステムでレート修正リクエストを作成
5. AHA concessionの計算を明記

**Tigerシステムでの記載例**:
```
Freetext Section: Your kind approval with rates approval for TIER 2 please, 
note that that Pluscargo has a local concession AHA Fixed USD 50 but we 
affect this concession in OFT. Therefore, AHA is 112 - 50 = 62 If the OFT 
is 1350 - 62 = 1288
```

### AHAとDOFの特別条件のベストプラクティス

#### 1. 特別条件の確認
- MRG rate approval時にAHAとDOFの特別条件を必ず確認
- RFAで特別条件の詳細を確認
- Tigerシステムでレート修正リクエストを作成する際に、特別条件を明記

#### 2. AHA concessionの計算
- AHA Fixed USD 50の現地特典を考慮
- AHA concessionを計算（AHA: 112 - 50 = 62）
- OFTにAHA concessionを反映（OFT: 1,350 - 62 = 1,288）

#### 3. 明確な記載
- Tigerシステムでレート修正リクエストを作成する際に、特別条件を明確に記載
- AHA concessionの計算を明記
- 承認を待つ

#### 4. 承認後の確認
- 承認後、特別条件が正しく適用されているか確認
- 問題がある場合は、すぐに修正

### AHAとDOFの特別条件を持つ顧客の一覧

#### FARLETZA S.A.
- **RFA**: GYE00176
- **特別条件**: AHAとDOFの特別条件あり
- **処理**: MRG rate approval時に特別条件を考慮

#### PLUSCARGO-ECUADOR S.A.
- **RFA**: GYEN00147A
- **特別条件**: AHA Fixed USD 50の現地特典あり
- **処理**: AHA concessionをOFTに反映

### 注意点

#### 1. 特別条件の見落とし
- MRG rate approval時に特別条件を見落とさない
- RFAで特別条件の詳細を確認
- Tigerシステムでレート修正リクエストを作成する際に、特別条件を明記

#### 2. AHA concessionの計算ミス
- AHA Fixed USD 50の現地特典を考慮
- AHA concessionを正確に計算
- OFTにAHA concessionを正確に反映

#### 3. 承認後の確認
- 承認後、特別条件が正しく適用されているか確認
- 問題がある場合は、すぐに修正

## 次アクション
- [ ] [[20251121_Ecuador-Pricing-基本ルールとTigerシステム]]にリンク
- [ ] [[20251121_Ecuador-Pricing-主要顧客別ルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#ecuador #pricing #aha #dof #special-conditions #farletza #pluscargo #inbox

