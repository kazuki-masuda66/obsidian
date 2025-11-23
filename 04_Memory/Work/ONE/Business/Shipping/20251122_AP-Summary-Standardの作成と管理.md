# AP-Summary-Standardの作成と管理

## 概要
AP Summary Standardは、AP（Account Plan）の概要をまとめたシートです。TEU allocation/BSAの情報を含み、SimonがInputしたCGMで話し合われたTargetを含みます。このシートの作成と管理方法を説明します。

## 詳細

### AP Summary Standardとは
- APの概要をまとめたシート
- TEU allocation/BSAの情報を含む
- SimonがInputしたCGMで話し合われたTargetを含む
- 営業活動の参考資料として使用

### AP Summary Standardの構成要素
1. **TEU allocation/BSA**: 各顧客へのTEU配分とBSA
2. **CGM Target**: CGMで話し合われたTarget
3. **Actual Lifting**: 実際の船積み実績
4. **差異分析**: 計画と実績の差異

## 基本的な使い方

### Step 1: AP Summary Standardのテンプレートを開く

#### テンプレートの場所
- **場所**: `G:\Shared drives\Latin West Coast\Account plan Year 2024\New AP process\`
- **ファイル名**: AP Summary Standard（テンプレート）

#### 開き方
1. 対象フォルダを開く
2. テンプレートファイルを開く
3. 対象月のシートを作成

### Step 2: TEU allocation/BSAを入力

#### TEU allocationとは
- 各顧客へのTEU配分
- サービス別のTEU配分

#### BSAとは
- **BSA = 船腹保証（Berth Space Allocation）**
- 各顧客に保証する船腹量

#### 入力手順
1. 各顧客のTEU allocationを入力
2. 各顧客のBSAを入力
3. サービス別のTEU allocationを入力
4. サービス別のBSAを入力
5. データの整合性を確認

### Step 3: CGM Targetを入力

#### CGM Targetとは
- **CGM = Country Goal Management**
- CGMで話し合われたTarget
- SimonがInputしたデータ

#### 入力手順
1. CGM Targetのデータを取得
2. 各顧客のCGM Targetを入力
3. サービス別のCGM Targetを入力
4. データの整合性を確認

### Step 4: Actual Liftingを入力

#### Actual Liftingとは
- 実際の船積み実績
- 計画と実績の比較に使用

#### 入力手順
1. Actual Liftingのデータを取得
2. 各顧客のActual Liftingを入力
3. サービス別のActual Liftingを入力
4. 計画との差異を計算

### Step 5: 差異分析を追加

#### 差異分析とは
- 計画と実績の差異
- 30%以上の差異がある場合は注意が必要

#### 分析手順
1. 計画と実績の差異を計算
2. 差異のパーセンテージを計算
3. 30%以上の差異をハイライト
4. 差異の原因を分析

## 高度な使い方

### 複数サービスの同時管理
- AX1、AX2、AX3、AX4を同時に管理
- サービス間の配分バランスを考慮
- キャパシティの制約を考慮

### 実績との比較分析
- Actual Liftingと計画の比較
- 差異の分析
- 次月の計画への反映

### 警告機能の活用
- 30%以上の差異がある場合は警告
- 大きな変化がある場合は警告
- エラー箇所を指摘

## メリット・デメリット

### ✅ メリット
- APの概要を一目で把握できる
- 計画と実績の比較が容易
- 営業活動の参考資料として使用できる

### ❌ デメリット
- Manual workが多い
- データの更新に時間がかかる
- 複数のデータソースからの取得が必要

## 使用例

### 例1: 6月分のAP Summary Standard作成
```
5月25日: テンプレートを開く
5月26日: TEU allocation/BSAを入力
5月27日: CGM Targetを入力
5月28日: Actual Liftingを入力
5月29日: 差異分析を追加
5月30日: レビューと承認
```

## よくある問題と解決策

### 問題1: データの不整合
- **原因**: 複数のデータソースからの取得
- **解決策**: データの一元管理とバリデーション

### 問題2: 30%以上の差異の見落とし
- **原因**: 差異分析が不十分
- **解決策**: 自動計算とハイライト機能の活用

### 問題3: データの更新が遅れる
- **原因**: Manual workが多い
- **解決策**: 自動化ツールの導入（DX taskforceで進行中）

## ベストプラクティス

1. **定期的な更新**: 月次で必ず更新する
2. **データ整合性**: 複数のデータソースの整合性を確認
3. **差異分析**: 30%以上の差異を必ず確認
4. **警告機能**: 警告機能を活用
5. **ドキュメント化**: プロセスをドキュメント化

## 関連技術との比較

| 要素 | 入力 | 出力 | ツール |
|------|------|------|--------|
| TEU allocation | APデータ | TEU配分 | Excel |
| BSA | BSAデータ | BSA情報 | Excel |
| CGM Target | CGMデータ | CGM Target | Excel |
| Actual Lifting | 実績データ | 実績情報 | Excel |
| 差異分析 | 計画・実績 | 差異情報 | Excel |

## 関連ノート
- [[APとは何か-Account-Planの基本概念]]
- [[APの作成プロセス-ステップバイステップガイド]]
- [[BSAとAPの関係-船腹保証とアカウントプラン]]
- [[Sales-TargetとAPの比較-営業目標と計画の整合性]]
- [[CGMとAPの関係-Country-Goal-Managementとアカウントプラン]]

#ap #account-plan #ap-summary-standard #work/one #work/one/afla

