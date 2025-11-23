# Windsurf Workflows for Obsidian Vault

このフォルダには、Obsidian Vault管理用のWindsurfワークフローが含まれています。

## 📖 Windsurfワークフローの使い方

### ワークフローの実行方法

Windsurfでは、Cascade（AIチャット）でスラッシュコマンド（`/`）を使用してワークフローを実行できます。

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

#### 方法2: バックスラッシュ（\）でコマンドパレットを開く

1. **キーボードショートカットの設定**
   - `Ctrl+K` (Windows/Linux) または `Cmd+K` (Mac) でコマンドパレットを開く
   - 「Preferences: Open Keyboard Shortcuts (JSON)」を選択
   - 以下の設定を追加：

```json
[
  {
    "key": "\\",
    "command": "workbench.action.showCommands"
  }
]
```

2. **コマンドの実行**
   - バックスラッシュ（`\`）を押す
   - コマンドパレットが開く
   - `/ワークフロー名` を入力して実行

---

## 🛠️ 利用可能なワークフロー

### 1. /daily
**説明**: 今日のデイリーノートを作成  
**使用例**: `/daily`

### 2. /mtg
**説明**: MTG議事録を作成  
**使用例**: `/mtg`（議題は対話形式で入力）

### 3. /inbox-review
**説明**: Inboxを分析して整理案を提示  
**使用例**: `/inbox-review`

### 4. /make-memory
**説明**: InboxノートをMemory Note（長期記憶）に昇華  
**使用例**: `/make-memory`（ファイル名は対話形式で指定）

### 5. /find-unlinked-notes
**説明**: リンクされていないノート（バックリンク0）を検索してリンク候補を提案  
**使用例**: `/find-unlinked-notes`

### 6. /suggest-links
**説明**: 現在のノートに関連するノートを提案  
**使用例**: `/suggest-links`

### 7. /optimize-tags
**説明**: 指定ファイルのタグを最適化  
**使用例**: `/optimize-tags`（ファイル名は対話形式で指定）

### 8. /weekly-review
**説明**: 週次レビューを実行  
**使用例**: `/weekly-review`

### 9. /summarize
**説明**: 指定ノートを要約  
**使用例**: `/summarize`（ファイル名は対話形式で指定）

### 10. /project-view
**説明**: プロジェクトに関連する全ノートを統合表示  
**使用例**: `/project-view`（プロジェクト名は対話形式で指定）

### 11. /archive-review
**説明**: 3ヶ月以上前のアーカイブをレビュー  
**使用例**: `/archive-review`

### 12. /research
**説明**: 指定テーマについて網羅的に知識を調査  
**使用例**: `/research`（テーマは対話形式で指定）

### 13. /memo-to-inbox
**説明**: 00_Memoのメモを01_Inboxの形式に整理して移動（承認不要で自動実行）  
**使用例**: `/memo-to-inbox`（ファイル名は対話形式で指定）

### 14. /organize-inbox
**説明**: Inboxフォルダ内のファイルを適切なフォルダに振り分け  
**使用例**: `/organize-inbox`（ファイル名は対話形式で指定）

### 15. /organize-memory
**説明**: 04_Memoryフォルダ内の知識ノートを重複なく、綺麗に整理  
**使用例**: 
- `/organize-memory` - 全カテゴリを整理
- `/organize-memory AI` - AIカテゴリのみ整理

### 16. /self-analysis
**説明**: あきらパパの自己分析会議を実施（月1回推奨）  
**使用例**: `/self-analysis`

### 17. /create-dashboards
**説明**: 各種ダッシュボードを作成・更新  
**使用例**: 
- `/create-dashboards` - 全てのダッシュボードを作成
- `/create-dashboards home` - HOMEダッシュボードのみ作成

### 18. /pricing
**説明**: プライシング業務（見積もり作成、承認判断、システム入力、メール対応）を支援  
**使用例**: `/pricing エクアドルのStarcargo向けの40HCレートを教えて`

**詳細**: [[pricing.md]]

### 19. /dar
**説明**: DAR（Demurrage and Detention Request）業務を支援  
**使用例**: `/dar エクアドルのStarcargoのFree Time延長リクエストを承認して`

**詳細**: [[dar.md]]

### 20. /space-control
**説明**: Space Control業務（スペース管理、Roll List作成、Wayport処理など）を支援  
**使用例**: `/space-control AX4のスペース更新の手順を教えて`

**詳細**: [[space-control.md]]

---

## 🔄 よく使う組み合わせ

### 朝のルーティン
```
1. /daily
2. /create-dashboards home
3. 今日のタスクを追記
```

### 夕方のルーティン
```
1. Dailyに気づきを追記
2. /summarize で今日のInboxを要約
```

### 金曜日のルーティン
```
1. /weekly-review
2. /create-dashboards weekly
3. /inbox-review
4. /find-unlinked-notes
```

---

## 📌 ヒント

- ワークフロー名の最初の数文字を入力すると補完されます
- ファイル名の引数がない場合、現在開いているファイルが対象になります
- 各ワークフローは対話形式で実行され、確認や選択を求められる場合があります
- Windsurfは `.windsurf/workflows/` フォルダ内のMarkdownファイルを自動的に検出します

---

## 📚 関連リソース

- **Windsurf設定**: [[../README.md]] - Windsurfでの使用方法
- **Cursor版コマンド**: [[../../.cursor/commands/README.md]] - Cursor用のコマンド集
- **プロンプト集**: [[../../08_prompts/README.md]] - 効果的だったプロンプトをカテゴリ別に保存
- **Brain System Rules**: [[../../AGENTS.md]] - システム全体のルール

詳細は各ワークフローファイル（`.md`）を参照してください。

---

## 🔧 ワークフローの作成・編集

### WindsurfのUIから作成

1. Windsurfエディタの右上にあるスライダーメニューから「カスタマイズ」アイコンをクリック
2. 「Workflows」パネルに移動
3. 「+ Workflow」ボタンをクリックして新しいワークフローを作成
4. 作成されたワークフローは `.windsurf/workflows/` に自動保存されます

### 手動で作成

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

---

## ⚠️ 注意事項

- ワークフローファイルは、1ファイルあたり最大12,000文字までです
- ワークフロー内で他のワークフローを呼び出すことも可能です
- Windsurfのバージョンによって、ワークフローの動作が異なる場合があります
- 最新のWindsurfを使用することを推奨します
