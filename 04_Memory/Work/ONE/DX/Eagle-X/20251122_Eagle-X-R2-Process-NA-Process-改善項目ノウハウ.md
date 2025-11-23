# Eagle X R2 Process / NA Process改善項目ノウハウ

---
title: Eagle X R2 Process / NA Process改善項目ノウハウ
tags: [eagle-x, r2-process, na-process, improvement, todo, checklist]
created: 2025-11-22
---

## 概要
Eagle X R2 ProcessとNA Processに関する改善項目とTodoリスト。2023年9月27日の会議で決定した改善項目、NA Feedback、Add Account Tool、R2プロセス、メール送付、IOPプロセス、Status ListのClean up、Consoli Tool、Jiraに関する改善項目をまとめた。

## 会議情報

### 会議詳細
- **日時**: 2023年9月27日（水）17:00-18:30
- **形式**: Google Meet
- **リンク**: https://meet.google.com/cbs-esaz-cxh?hs=224
- **電話参加**: (JP) +81 3-4545-0450, PIN: 2207332813753

### 参加者
- **主催者**: Yohei Mori (JP) - yohei.mori@pwc.com
- **参加者**:
  - kazuki.masuda@one-line.com
  - Marina Kawaguchi (JP)
  - Shoichiro Terada (JP)
  - Takuya Sano (JP)
  - Shogo Otsuka
  - Koji Nakai
  - Naoki Unno (JP) - 任意
  - Shodai Kashiwazaki (JP) - 任意

## NA Feedback改善項目

### 1. 154 minsの最新情報取得
- **内容**: 154 minsの最新の情報が取れるかCSTに確認する
- **担当**: ONE

### 2. NAのみReviewをスキップ
- **内容**: NAのみReviewをスキップできるようにする
- **担当**: PwC

### 3. NAのみのInitial Checkin作成
- **内容**: NAのみのInitial Checkinを作成する
- **担当**: PwC

### 4. 入力Formの統一
- **内容**: GCSMと協議して入力Formを統一していく
- **担当**: ONE/PwC

### 5. Initial CheckinのContract Period変更
- **内容**: Initial CheckinのContract Periodは、1-3 monthsという形に全Region変更する
- **担当**: PwC

### 6. ChecklistのPOL/POD追加
- **内容**: Checklistで、全RegionにPOL/PODをOptionとして追加する
- **担当**: PwC

### 7. Group Locationの扱い
- **内容**: Group Locationは、NAは選択しないとし、それ以外の地域は文言を変えるか、どう選択をするか引き続き検討
- **担当**: ONE/PwC

### 8. Checklistの列削除
- **内容**: Checklistで、NA向けは、3. G-I列を削除する。その他もG-K列を削除する。4も削除する。6にOcean Freightを追加する
- **担当**: PwC

### 9. Conversion ToolのReliability列削除
- **内容**: Conversion Toolで、Reliabilityの列を消す。全Region対象
- **担当**: PwC

## Add Account Tool改善項目

### 1. TEST FolderのOLD配下問題
- **内容**: TEST FolderはOLD配下になっているのを戻す
- **担当**: PwC

### 2. FY22のフォルダ名変更
- **内容**: FY22のフォルダ名の変更する
- **担当**: PwC

### 3. Add Account Toolの説明タイミング
- **内容**: Add Account ToolのFlouranceへの説明は、タイミングを調整いただき連絡をいただく
- **担当**: ONE

### 4. Status Listの年度管理
- **内容**: Status Listで年度ごとの情報をどう管理していくか検討する（Live Tenderとしては行わないが、Conversionは実施したい。FY23, 24どこでやるのが妥当か？）
- **担当**: PwC

## R2プロセス改善項目

### 1. SodiaalのR2追加列の確認
- **内容**: SodiaalのR2の追加されている4列はSalesが記入したものか確認していただく
- **担当**: ONE

### 2. Customer intentionの整理
- **内容**: Customer intentionをLaneごとに記載し、Conversionプロセスを通すことのProsConsを整理する
- **担当**: PwC

### 3. R2 EtoEテスト用カスタマーシート
- **内容**: R2 EtoEテスト用のカスタマーシート（Lane行追加、Target列追加）を提供する
- **担当**: PwC

### 4. Conversion StudyでのR2プロセス説明
- **内容**: 9/28のConversion StudyでR2プロセスについて説明する
- **担当**: PwC

## メール送付改善項目

### オンショアのメール送付
- **内容**: オンショアは、CSTからSalesとPricerに両方にメールを送信するようにする。当面は、マニュアルで宛先を追加とし、自動で連携が必要となったタイミングで連絡をいただく
- **担当**: ONE

## IOPにおけるZIPコード改善項目

### Reliability列のZIPコード取得
- **内容**: Reliabilityの列をつぶしてZipコードを持ってこれるか検討する
- **担当**: PwC

## IOPプロセス改善項目

### 1. Conversion tool for IOPの作成
- **内容**: 真ん中の選択肢(Yes (the customer has another sheet other than OFT sheet for IOP))の場合、Conversion tool for IOPを作成する
- **担当**: PwC

### 2. Conversion for IOPのStatus管理
- **内容**: Conversion for IOPのStatusをStatus Listで管理していく
- **担当**: PwC

### 3. IOPのフォルダ作成
- **内容**: IOPは別のフォルダに作成して、Status Listでカウントする。具体的なフォルダパスは今後検討
- **担当**: PwC

## Status ListのClean up改善項目

### 1. 削除候補の列挙
- **内容**: Status Listに列がたくさんあるため、削除候補を挙げていただく。不要なシートも
- **担当**: ONE

### 2. JP Sales向けのStatus List作成
- **内容**: JP Sales向けのStatus Listのようなものを作成して見やすくしていく
- **担当**: ONE/PwC

## Consoli Tool改善項目

### Nikko環境での動作確認
- **内容**: Nikkoの環境でまだ動作しないか確認し、動作しない場合は、打ち合わせを設定しDebugを行う
- **担当**: PwC

## Jira改善項目

### 開発関連タスク管理環境
- **内容**: 開発関連のタスク管理用に環境とアカウントを準備いただく
- **担当**: ONE

## 関連資料

### Add Account Tool
- **資料**: How to use automatic new account addition tool in Status list
- **リンク**: https://docs.google.com/spreadsheets/d/1a1tJhpetV2ishv58aEs_LNPZOTSxZ6N7Zba6Ce2nGFk/edit

### R2 Process / NA Process
- **資料**: R2 Process / NA Process
- **リンク**: https://docs.google.com/spreadsheets/d/1yAGIpz-VAfsv2MLMSFOAoInhWbIKfh7uJI8DGs3P1R8/edit#gid=294087546

## 実務上のポイント

### NA Processの特殊性
- NA向けはReviewをスキップできる
- NA向けはInitial Checkinが異なる
- Checklistの列構成がNA向けは異なる（G-I列削除、4削除、6にOcean Freight追加）

### R2プロセスの重要性
- Customer intentionをLaneごとに記載する
- Conversionプロセスを通すことのProsConsを整理する
- R2 EtoEテスト用のカスタマーシートを準備する

### IOPプロセスの扱い
- IOPは別フォルダに作成
- Status Listで管理
- Conversion tool for IOPを作成する場合がある

## 次アクション
- [ ] 各改善項目の進捗を確認
- [ ] PwC担当項目の実装状況を確認
- [ ] ONE担当項目の対応状況を確認
- [ ] 次回会議で進捗を共有

#inbox #eagle-x #r2-process #na-process #improvement #todo #checklist

