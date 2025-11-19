# Sales-TargetとAPの比較-営業目標と計画の整合性

## 概要
Sales Target（営業目標）とAP（Account Plan）の関係について説明します。Sales TargetはAP作成の入力データであり、APはSales Targetに基づいて各顧客への配分を決定します。

## 詳細

### Sales Targetとは
- **Sales Target = 営業目標**
- Cimonから提供されるデータ
- 各顧客の営業目標
- AP作成の入力データ

### APとSales Targetの関係
- Sales TargetはAP作成の入力データ
- APはSales Targetに基づいて各顧客への配分を決定
- Sales TargetとBSAを比較してAPを作成

## 基本的な使い方

### Sales Targetの取得

#### データソース
- **提供者**: Cimon
- **取得タイミング**: 前月末〜当月20日頃
- **保存場所**: `G:\Shared drives\Latin West Coast\Account plan Year 2024\New AP process\Sales target\2025`

#### 取得手順
1. CimonにSales Targetのデータ提供を依頼
2. データを受領
3. 対象フォルダに保存
4. データの整合性を確認

### Sales TargetとBSAの比較

#### 比較の目的
- Sales TargetとBSAの整合性を確認
- 大きな差異がある場合は確認が必要
- AP作成の参考データとして使用

#### 比較手順
1. Sales Targetを確認
2. BSAを確認
3. 差異を計算
4. 30%以上の差異がある場合は確認
5. 必要に応じて調整

### AP作成でのSales Target活用

#### AP作成時のSales Target使用
1. Sales Targetを確認
2. BSAと比較
3. 各顧客への配分を決定
4. サービス別の配分を決定

## 高度な使い方

### 複数期間のSales Target比較
- 前月のSales Targetと比較
- 前年同月のSales Targetと比較
- トレンド分析

### Sales TargetとActual Liftingの比較
- Sales TargetとActual Liftingの比較
- 差異の分析
- 次月のSales Target設定への反映

### Sales Targetの動的調整
- 実績に基づいてSales Targetを調整
- 需要変動に応じてSales Targetを調整
- 顧客の優先度に応じてSales Targetを調整

## メリット・デメリット

### ✅ Sales Targetのメリット
- 営業目標が明確
- AP作成の参考データとして使用できる
- 実績との比較が容易

### ❌ Sales Targetのデメリット
- 需要予測の誤りがある可能性
- 実績との差異が発生しやすい
- データの取得が遅れる可能性

## 使用例

### 例1: Sales Targetの取得と比較
```
5月20日: CimonからSales Targetを取得
5月21日: Sales Targetを確認（1000 TEU）
5月22日: BSAを確認（800 TEU）
5月23日: 差異を計算（25%の差異）
5月24日: 差異が30%未満のため、AP作成を継続
```

### 例2: AP作成でのSales Target活用
```
1. Sales Targetを確認（1000 TEU）
2. BSAと比較（800 TEU）
3. 各顧客への配分を決定（Tier1: 600 TEU, Tier2: 400 TEU）
4. サービス別の配分を決定（AX1: 300 TEU, AX2: 200 TEU, AX3: 300 TEU, AX4: 200 TEU）
```

## よくある問題と解決策

### 問題1: Sales Targetの取得が遅れる
- **原因**: Cimonからのデータ提供が遅い
- **解決策**: 前月末に依頼、20日頃にリマインダー

### 問題2: Sales TargetとBSAの大きな差異
- **原因**: 需要予測の誤り、BSA設定の誤り
- **解決策**: 差異の原因を分析、必要に応じて調整

### 問題3: 実績とSales Targetの大きな差異
- **原因**: 需要予測の誤り、顧客の急な需要変化
- **解決策**: 定期的な実績確認とSales Targetの見直し

## ベストプラクティス

1. **早期取得**: Sales Targetは前月末に依頼
2. **定期的な比較**: Sales TargetとBSAを定期的に比較
3. **差異分析**: 30%以上の差異を必ず確認
4. **実績との比較**: Sales TargetとActual Liftingを比較
5. **ドキュメント化**: 比較プロセスをドキュメント化

## 関連技術との比較

| 概念 | 特徴 | Sales Targetとの関係 |
|------|------|-------------------|
| BSA | 船腹保証 | Sales Targetと比較してAPを作成 |
| Actual Lifting | 実際の船積み実績 | Sales Targetとの比較データ |
| Forecast | 需要予測 | Sales Target設定の参考データ |
| AP | アカウントプラン | Sales Targetを入力データとして使用 |

## 関連ノート
- [[APとは何か-Account-Planの基本概念]]
- [[APの作成プロセス-ステップバイステップガイド]]
- [[BSAとAPの関係-船腹保証とアカウントプラン]]
- [[AP-Summary-Standardの作成と管理]]
- [[CGMとAPの関係-Country-Goal-Managementとアカウントプラン]]

#ap #account-plan #sales-target #work/one #work/one/afla

