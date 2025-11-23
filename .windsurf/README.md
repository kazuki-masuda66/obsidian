# Windsurf Workflows for Obsidian Vault

このフォルダには、Obsidian Vault管理用のWindsurfワークフローが含まれています。

## 📁 フォルダ構造について

- **`.windsurf/workflows/`** - Windsurfのワークフロー（推奨）
  - Windsurfが自動的に検出し、`/[ワークフロー名]` で呼び出せます
  - Cascadeでスラッシュコマンドを使用して実行できます
  
- **`.windsurf/commands/`** - 旧形式（互換性のため残しています）
  - 将来的に削除予定
  - 現在は `.windsurf/workflows/` を使用してください

## 📖 使い方

### Windsurfでのワークフロー実行方法

Windsurfでは、Cascade（AIチャット）でスラッシュコマンド（`/`）を使用してワークフローを実行できます。

**重要**: Windsurfは `.windsurf/workflows/` フォルダ内のMarkdownファイルを自動的に検出し、ワークフローとして認識します。

#### 方法1: Cascadeでスラッシュコマンドを使用（推奨）

1. **Cascadeを開く**
   - `Ctrl+L` (Windows/Linux) または `Cmd+L` (Mac) でCascadeを開く
   - または、サイドバーのCascadeアイコンをクリック

2. **スラッシュコマンドを入力**
   - チャット入力欄に `/ワークフロー名` を入力
   - 例: `/daily`、`/mtg`、`/pricing`
   - Windsurfが自動的に `.windsurf/workflows/[ワークフロー名].md` を読み込みます

3. **ワークフローを実行**
   - Enterキーを押すと、ワークフローファイル内の手順に従ってAIが動作します

#### 方法2: バックスラッシュ（\）でコマンドを呼び出す（カスタマイズ）

Windsurfでバックスラッシュ（`\`）でコマンドを呼び出すには、キーボードショートカットをカスタマイズします：

1. **キーボードショートカットの設定**
   - `Ctrl+K` (Windows/Linux) または `Cmd+K` (Mac) でコマンドパレットを開く
   - 「Preferences: Open Keyboard Shortcuts」を選択
   - 「コマンドパレットを表示」を検索
   - バックスラッシュ（`\`）キーに割り当て

2. **コマンドの実行**
   - バックスラッシュ（`\`）を押す
   - コマンドパレットが開く
   - `/コマンド名` を入力して実行

#### 方法3: プロンプトファイルを直接参照

Cascadeで、以下のようにワークフローファイルを参照することもできます：

```
.windsurf/workflows/daily.md の内容を読み込んで実行してください
```

または：

```
以下のプロンプトに従って実行してください：
[.windsurf/workflows/daily.md の内容を貼り付け]
```

---

## 🛠️ 利用可能なワークフロー

**注意**: ワークフローは `.windsurf/workflows/` フォルダに保存されています。詳細は [[.windsurf/workflows/README.md]] を参照してください。

### 1. /daily
**説明**: 今日のデイリーノートを作成  
**使用例**: `/daily`

### 2. /mtg [議題]
**説明**: MTG議事録を作成  
**使用例**: `/mtg ProjectX定例`

### 3. /inbox-review
**説明**: Inboxを分析して整理案を提示  
**使用例**: `/inbox-review`

### 4. /make-memory [ファイル名]
**説明**: InboxノートをMemory Note（長期記憶）に昇華  
**使用例**: `/make-memory 20241022_API設計メモ.md`

### 5. /find-unlinked-notes
**説明**: リンクされていないノート（バックリンク0）を検索してリンク候補を提案  
**使用例**: `/find-unlinked-notes`

### 6. /suggest-links
**説明**: 現在のノートに関連するノートを提案  
**使用例**: `/suggest-links`

### 7. /optimize-tags [ファイル名]
**説明**: 指定ファイルのタグを最適化  
**使用例**: `/optimize-tags` または `/optimize-tags 20241022_API設計.md`

### 8. /weekly-review
**説明**: 週次レビューを実行  
**使用例**: `/weekly-review`

### 9. /summarize [ファイル名]
**説明**: 指定ノートを要約  
**使用例**: `/summarize` または `/summarize 20241022_長文ノート.md`

### 10. /project-view [プロジェクト名]
**説明**: プロジェクトに関連する全ノートを統合表示  
**使用例**: `/project-view ProjectX`

### 11. /archive-review
**説明**: 3ヶ月以上前のアーカイブをレビュー  
**使用例**: `/archive-review`

### 12. /research [テーマ]
**説明**: 指定テーマについて網羅的に知識を調査  
**使用例**: `/research React Hooks` または `/research TypeScript`

### 13. /memo-to-inbox [ファイル名]
**説明**: 00_Memoのメモを01_Inboxの形式に整理して移動（承認不要で自動実行）  
**使用例**: `/memo-to-inbox` または `/memo-to-inbox 雑メモ.md`

### 14. /organize-inbox [ファイル名]
**説明**: Inboxフォルダ内のファイルを適切なフォルダに振り分け  
**使用例**: `/organize-inbox` または `/organize-inbox 20241022_API設計メモ.md`

### 15. /organize-memory [カテゴリ]
**説明**: 04_Memoryフォルダ内の知識ノートを重複なく、綺麗に整理（重複統合、タグ最適化、リンク追加、リファクタリング）  
**使用例**: 
- `/organize-memory` - 全カテゴリを整理
- `/organize-memory AI` - AIカテゴリのみ整理
- `/organize-memory Technical` - Technicalカテゴリのみ整理

### 16. /self-analysis
**説明**: あきらパパの自己分析会議を実施（月1回推奨）  
**使用例**: `/self-analysis`

### 17. /create-dashboards [ダッシュボード名]
**説明**: 各種ダッシュボードを作成・更新  
**使用例**: 
- `/create-dashboards` - 全てのダッシュボードを作成
- `/create-dashboards home` - HOMEダッシュボードのみ作成
- `/create-dashboards projects` - プロジェクトダッシュボードのみ作成

### 18. /pricing [質問内容]
**説明**: プライシング業務（見積もり作成、承認判断、システム入力、メール対応）を支援  
**使用例**: 
- `/pricing エクアドルのStarcargo向けの40HCレートを教えて`
- `/pricing チリのSan Antonio向けのDG貨物の承認ルールは？`
- `/pricing メキシコのDAR申請の手順を確認したい`

**詳細**: [[.windsurf/commands/pricing.md]]

### 19. /dar [質問内容]
**説明**: DAR（Demurrage and Detention Request）業務を支援  
**使用例**: 
- `/dar エクアドルのStarcargoのFree Time延長リクエストを承認して`
- `/dar チリのFalabellaのCTIC延長の判断基準は？`

**詳細**: [[.windsurf/commands/dar.md]]

### 20. /space-control [質問内容]
**説明**: Space Control業務（スペース管理、Roll List作成、Wayport処理など）を支援  
**使用例**: 
- `/space-control AX4のスペース更新の手順を教えて`
- `/space-control Roll List作成の方法を確認したい`

**詳細**: [[.windsurf/commands/space-control.md]]

---

## 🔄 Windsurfでのワークフロー実行の詳細

### WindsurfのCascadeでの動作

WindsurfのCascadeでスラッシュコマンド（`/`）を使用すると：

1. **ワークフロー認識**: Windsurfが `/ワークフロー名` を認識
2. **ファイル読み込み**: `.windsurf/workflows/[ワークフロー名].md` を自動的に読み込む
3. **プロンプト実行**: ファイル内の「Prompt」セクションに従ってAIが動作

### カスタムワークフローの追加方法

新しいワークフローを追加する場合：

#### 方法A: WindsurfのUIから作成（推奨）

1. Windsurfエディタの右上にあるスライダーメニューから「カスタマイズ」アイコンをクリック
2. 「Workflows」パネルに移動
3. 「+ Workflow」ボタンをクリックして新しいワークフローを作成
4. 作成されたワークフローは `.windsurf/workflows/` に自動保存されます

#### 方法B: 手動で作成

1. `.windsurf/workflows/` フォルダに新しい `.md` ファイルを作成
2. 以下の形式でワークフローを記述：

```markdown
# [ワークフロー名]

## Description
[ワークフローの説明]

## Prompt
[実行するプロンプト内容]

[具体的な手順]
```

3. Windsurfが自動的に検出し、`/[ワークフロー名]` で呼び出せるようになります
4. `README.md` にワークフローを追加

---

## 📌 ヒント

- コマンド名の最初の数文字を入力すると補完されます
- ファイル名の引数がない場合、現在開いているファイルが対象になります
- 各コマンドは対話形式で実行され、確認や選択を求められる場合があります

---

## 📚 関連リソース

- **ワークフロー一覧**: [[.windsurf/workflows/README.md]] - 利用可能なワークフローの一覧
- **Cursor版コマンド**: [[.cursor/commands/README.md]] - Cursor用のコマンド集
- **プロンプト集**: [[08_prompts/README.md]] - 効果的だったプロンプトをカテゴリ別に保存
- **Brain System Rules**: [[AGENTS.md]] - システム全体のルール

詳細は各コマンドファイル（`.md`）を参照してください。

---

## 🔧 Windsurfの設定

### キーボードショートカットのカスタマイズ

Windsurfでバックスラッシュ（`\`）でコマンドパレットを開く設定：

1. `Ctrl+K` (Windows/Linux) または `Cmd+K` (Mac) でコマンドパレットを開く
2. 「Preferences: Open Keyboard Shortcuts (JSON)」を選択
3. 以下の設定を追加：

```json
[
  {
    "key": "\\",
    "command": "workbench.action.showCommands"
  }
]
```

これで、バックスラッシュ（`\`）を押すとコマンドパレットが開き、`/コマンド名` を入力して実行できます。

---

## ⚠️ 注意事項

- Windsurfのバージョンによって、スラッシュコマンドの動作が異なる場合があります
- 最新のWindsurfを使用することを推奨します
- コマンドが認識されない場合は、プロンプトファイルを直接参照する方法を使用してください

## 🔧 実用的な使用方法

### Windsurfでコマンドを実行する実際の手順

WindsurfのAIチャットでコマンドを実行するには、以下のいずれかの方法を使用します：

#### 方法A: スラッシュコマンドを直接入力（推奨）

1. `Ctrl+L` (Windows/Linux) または `Cmd+L` (Mac) でCascadeを開く
2. チャット入力欄に `/daily` などと入力
3. Windsurfが自動的に `.windsurf/workflows/daily.md` を読み込みます

#### 方法B: プロンプトファイルを明示的に参照（確実）

1. `Ctrl+L` でCascadeを開く
2. 以下のように入力：

```
.windsurf/workflows/daily.md の内容を読み込んで、そのプロンプトに従って実行してください
```

または：

```
以下のファイルの内容を読み込んで実行してください：
.windsurf/workflows/daily.md
```

#### 方法C: プロンプトを直接貼り付け（最も確実）

1. `.windsurf/workflows/daily.md` を開く
2. 「Prompt」セクションの内容をコピー
3. Cascadeに貼り付けて実行

### バックスラッシュ（\）でコマンドパレットを開く設定

Windsurfでバックスラッシュ（`\`）キーでコマンドパレットを開くには：

1. `Ctrl+K` (Windows/Linux) または `Cmd+K` (Mac) でコマンドパレットを開く
2. 「Preferences: Open Keyboard Shortcuts (JSON)」を選択
3. 以下の設定を追加：

```json
[
  {
    "key": "\\",
    "command": "workbench.action.showCommands"
  }
]
```

4. 保存後、バックスラッシュ（`\`）を押すとコマンドパレットが開きます
5. `/コマンド名` を入力して実行

### トラブルシューティング

#### ワークフローが認識されない場合

1. **プロンプトファイルを直接参照する**
   ```
   .windsurf/workflows/daily.md を読み込んで実行してください
   ```

2. **ファイルの内容を確認する**
   - `.windsurf/workflows/[ワークフロー名].md` が存在するか確認
   - ファイル内に「Prompt」セクションがあるか確認
   - ファイル名が正しいか確認（拡張子なしのファイル名がワークフロー名になります）

3. **Windsurfのバージョンを確認する**
   - 最新のWindsurfを使用しているか確認
   - 必要に応じて更新

4. **ワークフローの再読み込み**
   - Windsurfを再起動する
   - または、Cascadeで「ワークフローを再読み込み」を実行

#### バックスラッシュキーが機能しない場合

1. **キーボードショートカットの設定を確認**
   - `Ctrl+K` → 「Preferences: Open Keyboard Shortcuts」
   - 「コマンドパレットを表示」を検索
   - バックスラッシュ（`\`）が割り当てられているか確認

2. **代替方法を使用**
   - `Ctrl+Shift+P` (Windows/Linux) または `Cmd+Shift+P` (Mac) でコマンドパレットを開く
   - `/コマンド名` を入力して実行

## 📝 まとめ

Windsurfで`.cursor`のコマンドを使用するには：

1. ✅ `.windsurf/workflows/` フォルダに全ワークフローファイルをコピー済み
2. ✅ WindsurfのCascadeで `/ワークフロー名` を入力
3. ✅ または、`.windsurf/workflows/[ワークフロー名].md` を直接参照
4. ✅ バックスラッシュ（`\`）キーでコマンドパレットを開く設定（オプション）

**重要**: Windsurfは `.windsurf/workflows/` フォルダ内のMarkdownファイルを自動的に検出し、`/[ワークフロー名]` で呼び出せるようにします。

これで、Cursorと同様にWindsurfでもワークフローを使用できます！

