# Eagle X Target Accounts Summary - FY24管理とデータ品質ノウハウ

---
title: Eagle X Target Accounts Summary - FY24管理とデータ品質ノウハウ
tags: [eagle-x, target-accounts, data-quality, fy24, tender-management]
created: 2025-11-22
---

## 概要
Eagle Xターゲットアカウントのサマリー管理とデータ品質向上のためのノウハウ。各リージョン（JPN、NA、LATAM、SAS、EUA、TST）のターゲットアカウントデータの統合、重複排除、データ品質チェックの実務プロセスをまとめた。

## データソースと管理方法

### データソース
1. **各リージョンからのターゲットアカウントファイル**
   - 保存場所: `EAGLE-X-TEST\>SALES\>Account List from each region`
   - 各リージョンから提供されたターゲットアカウントリストをベースに統合

2. **JPNターゲットアカウント**
   - 最新ファイル: Anzai-san提供（2024年4月9日火曜日）
   - 注意点: 重複の可能性あり（後述）

3. **TSTテンダー**
   - データソース: TST Calendar（2024年1月時点）
   - オフショアテンダーの管理

### サマリーファイル
- **Google Sheetsリンク**: https://docs.google.com/spreadsheets/d/1NCRBN7Q997lIwvCMd8Tk_leVMGEfNUiN/edit#gid=745089631
- 全リージョンのターゲットアカウントを統合管理

## リージョン別データ品質課題と対応

### 1. JPN Accounts（日本アカウント）

#### データ品質課題
- **重複の可能性**: 以下のパラメータで重複チェックが必要
  - Group Customer Code
  - Customer Code
  - SC_ RFA Number
  - NAC Name

#### 重複が発生する理由
- **不完全な詳細情報**: Group Customer Codeが提供されていないアカウントがある
- **複数NACアカウント/契約番号**: 1つのテンダー下に複数のNACアカウントや契約番号が存在する可能性

#### 対応方法
- 重複チェックを実施し、統合前にデータクレンジングを実施
- 不完全なデータは補完を依頼

### 2. NA Accounts（北米アカウント）

#### データ品質課題
- **顧客詳細情報の不足**: 各契約のGroup Customer CodeやCustomer Codeが不完全
- **重複の可能性**: 提供された情報が限定的なため、他のターゲットアカウントと重複する可能性

#### 対応方法
- データ提供時に完全な顧客詳細情報を要求
- 重複チェックを継続的に実施

### 3. LATAM Accounts（ラテンアメリカアカウント）

#### データ統合方法
- **2つのファイルを統合**:
  1. `EAGLE X - LATAM Target Accounts_2023`
  2. `LATAM - 2024 BCO Tender Calendar (updated onshore x offshore_missing tender formats)`
- **重複排除**: 2つのファイルを結合後、重複を削除

#### 対応方法
- ファイル統合時に重複チェックを実施
- 統合後のデータ品質を確認

### 4. SAS Accounts（南アジアアカウント）
- データ品質: 確認済み

### 5. EUA Accounts（欧州・アフリカアカウント）
- **データ品質**: 全てのターゲットアカウントをキャプチャ済み
- データ完全性が高い

### 6. TST-Offshore（オフショアテンダー）
- **データソース**: TST Calendar（2024年1月時点）
- **管理方法**: 他のリージョンのターゲットアカウントと統合管理

## データ品質管理のベストプラクティス

### 重複チェックの実施
1. **チェックパラメータ**:
   - Group Customer Code
   - Customer Code
   - SC_ RFA Number
   - NAC Name

2. **チェックタイミング**:
   - データ統合前
   - 定期的なデータ品質レビュー

### データ補完プロセス
1. **不完全データの特定**: Group Customer Code、Customer Codeが欠落しているアカウントを特定
2. **データ提供依頼**: 各リージョンに完全なデータ提供を依頼
3. **データ検証**: 提供されたデータの整合性を確認

### データ更新プロセス
1. **定期的な更新**: 各リージョンから最新のターゲットアカウントリストを取得
2. **変更履歴の管理**: データの変更履歴を記録
3. **サマリーファイルの更新**: Google Sheetsのサマリーファイルを最新状態に保つ

## 実務上の注意点

### データ品質の重要性
- **重複データの影響**: 重複データがあると、テンダー管理やPricing Toolの作成に支障をきたす
- **不完全データの影響**: 不完全なデータは、Eagle Xプロセスの効率を低下させる

### コミュニケーション
- **リージョンとの連携**: データ品質に関する課題は、各リージョンと直接議論して解決
- **継続的な改善**: データ品質の改善は継続的なプロセス

## 関連ノート
- [[20250113_Eagle-X-Target-Accounts-LATAM-FY25-管理とPre-conversionノウハウ]]
- [[20250113_Potential-Tenders-May-June-FY25-管理とPre-conversionノウハウ]]
- [[20250113_GCSM-Tender-Calendar-FY25-統合と管理ノウハウ]]

## 次アクション
- [ ] 各リージョンのデータ品質を定期的にレビュー
- [ ] 重複チェックの自動化を検討
- [ ] データ品質向上のためのガイドライン作成

#inbox #eagle-x #target-accounts #data-quality #tender-management #fy24

