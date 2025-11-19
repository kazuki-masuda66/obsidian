# CGMとAPの関係-Country-Goal-Managementとアカウントプラン

## 概要
CGM（Country Goal Management、国別目標管理）とAP（Account Plan、アカウントプラン）の関係について説明します。CGMはGHQ Trade Managementが策定する国別予算であり、APはCGM Targetに基づいて各顧客への船腹配分を決定します。

## 詳細

### CGMとは
- **CGM = Country Goal Management（国別目標管理）**
- GHQ Trade Managementが策定
- Fiscal Year毎のTrade Budgetを各国に分配した予算値
- 期初と下期の年2回見直し
- 予算値として「TEU」、「CM/TEU」、「Gross CM」が設定

### CGMの種類
1. **Loading Office Country CGM**: 積み国が日本となっているCGM予算値
2. **Contract Office Country CGM**: 契約国が日本となっているCGM予算値

### グローバルレベルでのCGMの扱い

#### グローバル（GHQ）では「Contract CGM」がメイン
- **根拠**: Individual Sales Budgetは「Contract CGM達成のために導入」
- **階層構造**: `Trade Budget (GHQ) -> Contract CGM (Country/Office) -> Individual Sales Budget (Person)`
- **理由**: 契約国ベースで管理することで、契約責任の所在が明確になる

#### ONE JAPANでは「Loading Office Country CGM」がメイン
- **理由**: 積み国ベースで管理することで、実際の船積み実績を正確に反映できる
- **適用**: ONE JAPANのモニタリング基準として使用

#### 使い分けの理由
| レベル | メインのCGM | 理由 |
|--------|-----------|------|
| グローバル（GHQ） | Contract CGM | 契約責任の所在が明確、契約ベースの管理 |
| ONE JAPAN | Loading Office CGM | 積み国ベースで実績を正確に反映 |

**注意**: グローバルレベルでは両方のCGMが管理されていますが、Individual Sales Budgetなどの新しい仕組みは「Contract CGM」をベースにしています。

### CGMカウントの具体例

#### 例: 横浜からメキシコに行く貨物
- **Loading Office（積み国）**: 日本（横浜）
- **Contract Office（契約国）**: 日本またはメキシコ（契約内容による）
- **CGMカウント**: **日本のCGMとしてカウントされる**

**理由**: ONE JAPANでは「Loading Office Country CGM」をベースにモニターしているため、積み国が日本であれば、契約国がどこであっても**日本のCGM**としてカウントされます。

#### 判断基準
```
CGMカウントの判断フロー:

貨物の積み国はどこ？
  ↓
日本（横浜、東京、神戸など）
  ↓ YES
日本のCGMとしてカウント
  ↓
（契約国は関係しない）

メキシコ、チリ、ペルーなど
  ↓ NO
その国のCGMとしてカウント
```

### APとCGMの関係

#### 1. CGM TargetがAP作成の基準となる
- AP Summary Standardのシートに**CGM Target**が含まれる
- SimonがInputしたCGMで話し合われたTargetがAPに反映される
- APはCGM Targetに基づいて各顧客への配分を決定

#### 2. APはCGM達成のための実行計画
- CGMは国別の予算目標
- APはCGM Targetを達成するための具体的な実行計画
- 各顧客への船腹配分を通じてCGM Targetを達成

#### 3. CGM TargetとBSAの関係
- AP Summary Standardのシートで**TEU allocation/BSA**と**CGM Target**を比較
- 30%以上の差異がある場合はSimonにシェア
- CGM TargetとBSAの整合性を確認

## 基本的な使い方

### AP作成時のCGM Target活用

#### Step 1: CGM Targetの確認
- AP Summary StandardのシートでCGM Targetを確認
- SimonがInputしたCGMで話し合われたTargetを確認
- 国別のCGM Targetを確認

#### Step 2: CGM TargetとBSAの比較
- CGM TargetとBSAを比較
- 30%以上の差異がある場合は確認
- 必要に応じて調整

#### Step 3: APへの反映
- CGM Targetに基づいて各顧客への配分を決定
- 各サービスへの配分を決定
- CGM Target達成を目指した配分を設定

### AP管理でのCGM Target確認

#### AP Summary Standardでの確認
- **TEU allocation/BSA**: 各顧客へのTEU配分とBSA
- **CGM Target**: CGMで話し合われたTarget
- **Actual Lifting**: 実際の船積み実績
- **差異分析**: 計画と実績の差異

#### 30%以上の差異の対応
- 30%以上の差異がある場合はSimonにシェア
- 差異の原因を分析
- 必要に応じてAPを調整

## 高度な使い方

### Dynamic CGMとAPの関係

#### Dynamic CGMとは
- FY2025より導入
- 各Trunk VVDのFinal BSA情報を反映
- 本船のアップサイズ／ダウンサイズも考慮したターゲット値

#### Dynamic CGM TEU Target計算方法
```
"Final BSA" x "Trade Budget Utilization %" x "Country Proportion" 
per each Trunk VVD Lane Domi / N-Domi respectively
```

#### APとの連携
- Dynamic CGM Targetに基づいてAPを作成
- BSAの変動を反映したAPを作成
- 実態に即したCGM達成率のモニタリング

### Individual Sales BudgetとAPの関係

#### Individual Sales Budgetとは
- FY2025より導入
- Contract CGM達成のために導入
- セールス担当者個人に割り当てられるターゲット値

#### 階層構造（グローバル基準）
```
Trade Budget (GHQ) 
  → Contract CGM (Country/Office) ← グローバルではContract CGMがメイン
    → Individual Sales Budget (Person) 
      → CVA (Customer) + Opportunity 
        → Actual Lifting
```

**重要**: この階層構造から、グローバルレベルでは**Contract CGM**がメインの管理指標であることが分かります。Individual Sales Budgetは「Contract CGM達成のために導入」されており、Contract CGMをベースにした仕組みです。

#### APとの連携
- Individual Sales Budgetに基づいてAPを作成
- セールス担当者個人のターゲットをAPに反映
- CVA（Customer Performance）と連携

## メリット・デメリット

### ✅ CGMとAPの連携のメリット
- CGM Target達成のための具体的な実行計画が立てられる
- 国別の予算目標と顧客別の配分計画が連携
- 実績と計画の比較が容易
- CGM達成率のモニタリングが可能

### ❌ CGMとAPの連携のデメリット
- CGM Targetの変更に対応する必要がある
- 複数のデータソースからの取得が必要
- データの整合性を確認する必要がある

## 使用例

### 例1: AP作成時のCGM Target活用
```
1. CGM Targetを確認（日本: 1000 TEU）
2. BSAを確認（800 TEU）
3. 差異を計算（25%の差異）
4. CGM Targetに基づいて各顧客への配分を決定
5. AP Summary StandardにCGM Targetを反映
6. APを作成
```

### 例2: AP管理でのCGM Target確認
```
1. AP Summary Standardを開く
2. TEU allocation/BSAを確認
3. CGM Targetを確認
4. Actual Liftingを確認
5. 差異を分析
6. 30%以上の差異がある場合はSimonにシェア
```

## よくある問題と解決策

### 問題1: CGM TargetとBSAの大きな差異
- **原因**: CGM Targetの設定ミス、BSA設定の誤り
- **解決策**: 差異の原因を分析、必要に応じて調整

### 問題2: CGM Targetの変更への対応
- **原因**: CGM Targetの見直し（期初と下期の年2回）
- **解決策**: CGM Targetの変更をAPに反映、APを更新

### 問題3: 複数のデータソースの管理
- **原因**: CGM Target、BSA、Sales Targetなど複数のデータソース
- **解決策**: データの一元管理、整合性チェック

## ベストプラクティス

1. **定期的な確認**: CGM TargetとAPを定期的に確認
2. **差異分析**: 30%以上の差異を必ず確認
3. **整合性確認**: CGM TargetとBSAの整合性を確認
4. **実績との比較**: CGM TargetとActual Liftingを比較
5. **ドキュメント化**: CGM TargetとAPの関係をドキュメント化

## 関連技術との比較

| 概念 | 特徴 | CGMとの関係 |
|------|------|----------|
| CGM Target | 国別の予算目標 | CGMの主要コンポーネント |
| BSA | 船腹保証 | CGM Targetと比較してAPを作成 |
| Sales Target | 営業目標 | CGM Target達成のための目標 |
| AP | アカウントプラン | CGM Targetに基づいて作成 |
| Actual Lifting | 実際の船積み実績 | CGM Targetとの比較データ |

## CGMとAPの階層構造

```
GHQ Trade Management
  ↓
Trade Budget（年度予算）
  ↓
CGM（Country Goal Management）
  - 国別の予算目標
  - TEU、CM/TEU、Gross CM
  ↓
AP（Account Plan）
  - CGM Targetに基づく実行計画
  - 各顧客への船腹配分
  - BSAの設定
  ↓
Actual Lifting
  - 実際の船積み実績
  - CGM Targetとの比較
```

## よくある質問

### Q: 横浜からメキシコに行く貨物はどこの国のCGMとしてカウントされる？
**A**: **日本のCGMとしてカウントされます。**

**理由**:
- ONE JAPANでは「Loading Office Country CGM」をベースにモニター
- Loading Office（積み国）が日本（横浜）であるため
- Contract Office（契約国）がメキシコであっても、積み国が日本なら日本のCGMとしてカウント

**具体例**:
- 横浜からメキシコ（MXLZC）への貨物 → **日本のCGM**
- 横浜からチリ（CLVAL）への貨物 → **日本のCGM**
- 横浜からペルー（PECLL）への貨物 → **日本のCGM**

**注意**: これはONE JAPANのモニタリング基準です。GHQレベルでは、**Contract Office Country CGMがメイン**として使用されており、Individual Sales Budgetなどの新しい仕組みもContract CGMをベースにしています。

## 関連ノート
- [[APとは何か-Account-Planの基本概念]]
- [[APの作成プロセス-ステップバイステップガイド]]
- [[AP-Summary-Standardの作成と管理]]
- [[BSAとAPの関係-船腹保証とアカウントプラン]]
- [[CGM-Country-Goal-Management-営業予算とDynamic-CGM]]
- [[Sales-TargetとAPの比較-営業目標と計画の整合性]]

#ap #account-plan #cgm #country-goal-management #work/one #work/one/afla

