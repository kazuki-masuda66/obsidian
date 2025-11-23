# Master-Constraint-Tableの更新方法-詳細手順

## 概要
Master Constraint Tableは、Space Controlで使用する制約テーブルです。AP（Account Plan）のデータをSpace Controlに反映するために、定期的に更新する必要があります。この更新手順を詳細に説明します。

## 詳細

### Master Constraint Tableとは
- Space Controlで使用する制約テーブル
- APのデータをSpace Controlに反映
- 各サービス（AX1、AX2、AX3、AX4）の制約を管理

### 更新の全体フロー
```
1. BKがデータを固める
2. データのコピー
3. 対象月フォルダの作成
4. データの編集（AX1-3の削除、AX4のみ残す）
5. VVDと対象WKの確認
6. JP（翌月分）の作成
7. OQ（翌月分）の作成
8. Master ConstraintへのUpload
9. 保存と確認
```

## 基本的な使い方

### Step 1: BKがデータを固める

#### BKとは
- **BK = Booking**
- Bookingデータの確定

#### 確認事項
- BKがデータを固めたことを確認
- データが準備できていることを確認

### Step 2: データのコピー

#### コピー元
- **場所**: `G:\Shared drives\LW AP\4_Convert_AP`
- **内容**: BKが固めたデータ

#### コピー手順
1. `G:\Shared drives\LW AP\4_Convert_AP`を開く
2. 対象月のデータを確認
3. データをコピー

### Step 3: 対象月フォルダの作成

#### フォルダ構造
- **場所**: `G:\Shared drives\Latin West Coast\Space Control\AX4\Standby\2025`
- **構造**: 各月ごとのフォルダを作成

#### 作成手順
1. 対象年のフォルダを確認
2. 対象月のフォルダを作成（存在しない場合）
3. コピーしたデータを保存

### Step 4: データの編集（AX1-3の削除、AX4のみ残す）

#### 編集の目的
- AX4のデータのみをSpace Controlに反映
- AX1、AX2、AX3のデータは削除

#### 編集手順
1. ファイルを1つずつ開く
2. AX1、AX2、AX3のデータを削除
3. AX4のデータのみを残す
4. データの整合性を確認

### Step 5: VVDと対象WKの確認

#### 確認事項
- VVD（Vessel Voyage Date）が正しいか
- 対象WK（Week）が正しいか
- データの整合性を確認

#### 確認手順
1. VVDを確認
2. 対象WKを確認
3. データの整合性を確認

### Step 6: JP（翌月分）の作成

#### JPとは
- **JP = Japan**
- 日本向けのデータ

#### 作成手順
1. どれか1つを選ぶ
2. Submission OfficeをTYO以外を削除
3. 対象月を翌月に変更
4. 翌月のVVDをコンマつなぎで入れる（スペースは不要）
5. データを保存

### Step 7: OQ（翌月分）の作成

#### OQとは
- **OQ = ONE Quote**
- ONE Quote向けのデータ

#### 作成手順
1. 前月からOQの翌月分をコピー
2. 対象WKとVVDをUpdate
3. データを保存

### Step 8: Master ConstraintへのUpload

#### Upload手順
1. Master Constraintを開く
2. 各WKのデータを1つずつUpload
3. Upload結果を確認
4. Saveする

#### 注意事項
- 各WKのデータを1つずつUploadすること
- Upload後は必ずSaveすること
- Upload結果を確認すること

### Step 9: 保存と確認

#### 確認事項
- 翌月のVVDで検索して、JPの分とOQの分を削除
- JP+1をアップロード
- 翌月のVVDで検索して、OQをアップロード
- 翌月VVDで正しくJP+1とOQが入っているか確認

#### 確認手順
1. 翌月のVVDで検索
2. JPの分とOQの分を削除
3. JP+1をアップロード
4. 翌月のVVDで検索
5. OQをアップロード
6. 翌月VVDで正しくJP+1とOQが入っているか確認

## 高度な使い方

### 複数サービスの同時更新
- AX1、AX2、AX3、AX4を同時に更新
- サービス間の整合性を確認
- キャパシティの制約を考慮

### エラーチェック
- データの整合性を確認
- VVDとWKの整合性を確認
- 重複データの確認

## メリット・デメリット

### ✅ メリット
- Space ControlにAPデータを正確に反映できる
- 体系的なプロセスで確実に更新できる
- エラーを早期に発見できる

### ❌ デメリット
- 手順が多く、時間がかかる
- Manual workが多い
- 複数のファイルを編集する必要がある

## 使用例

### 例1: 6月分のMaster Constraint Table更新
```
5月25日: BKがデータを固める
5月26日: データをコピー（G:\Shared drives\LW AP\4_Convert_AP）
5月27日: 対象月フォルダを作成（AX4\Standby\2025）
5月28日: データを編集（AX1-3削除、AX4のみ残す）
5月29日: VVDと対象WKを確認
5月30日: JP（翌月分）を作成
5月31日: OQ（翌月分）を作成
6月1日: Master ConstraintにUpload
6月2日: 保存と確認
```

## よくある問題と解決策

### 問題1: データの編集ミス
- **原因**: AX1-3の削除漏れ、AX4のデータ漏れ
- **解決策**: チェックリストの作成と徹底

### 問題2: VVDとWKの不整合
- **原因**: VVDとWKの入力ミス
- **解決策**: データの整合性チェック

### 問題3: Uploadの失敗
- **原因**: データ形式の不整合、システムエラー
- **解決策**: データ形式の確認、エラーログの確認

## ベストプラクティス

1. **チェックリスト**: 各ステップでチェックリストを使用
2. **データ整合性**: VVDとWKの整合性を確認
3. **エラーチェック**: Upload前にデータを確認
4. **ドキュメント化**: プロセスをドキュメント化
5. **定期的な確認**: 更新後は必ず確認

## 関連技術との比較

| ステップ | 入力 | 出力 | ツール |
|---------|------|------|--------|
| データコピー | BKデータ | コピーデータ | Excel |
| データ編集 | コピーデータ | 編集データ | Excel |
| JP作成 | 編集データ | JPデータ | Excel |
| OQ作成 | 前月OQ | OQデータ | Excel |
| Upload | JP/OQデータ | Master Constraint | Master Constraint |

## 関連ノート
- [[APとは何か-Account-Planの基本概念]]
- [[APのUpdate方法-データ更新と修正の手順]]
- [[APの作成プロセス-ステップバイステップガイド]]
- [[AP-Summary-Standardの作成と管理]]

#ap #account-plan #master-constraint-table #work/one #work/one/afla

