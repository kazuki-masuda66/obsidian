# Eagle X Filing Unit Regular Call - CVA Format & Game Planノウハウ

---
title: Eagle X Filing Unit Regular Call - CVA Format & Game Planノウハウ
tags: [eagle-x, filing-unit, cva-format, game-plan, reporting, pwc]
created: 2025-11-22
---

## 概要
Eagle X Filing Unitの定期会議（2023年12月26日）で共有された資料とアクティビティに関するノウハウ。CVAフォーマット、Game Plan Summary、Filing data field labelsの整理プロセスをまとめた。

## 会議資料の共有

### 資料の保存場所
- **Google Driveリンク**: https://drive.google.com/drive/folders/1gsT4eDBcpAJw2FxwU78qvTFZEyWYpssE?usp=drive_link
- **形式**: PowerPointプレゼンテーション資料

### 担当者
- **PwC側**: Haruka Kawata (河田遥香)
  - Senior Associate, Business Transformation Consulting - Operation Transformation Unit
  - Email: haruka.kawata@pwc.com
  - Tel: 070-1294-3455

## アクティビティ

### 1. GCSM Reporting Formatの提供
- **目的**: GCSM（Global Commercial & Service Management）向けのレポートフォーマットを提供
- **担当**: ONE側（仲井さん）
- **タイミング**: 会議後、2023年12月27日にCVAフォーマットを共有

### 2. Filing Data Field Labelsのフィルタリング
- **ステータス**: [ongoing] 進行中
- **目的**: Filingデータのフィールドラベルを整理・フィルタリング
- **担当**: PwC側

## CVAフォーマットの詳細

### CVAフォーマットの特徴
- **ファイルサイズ**: 大きめ（big file size a bit）
- **入力方式**: Salesは年間で限られた列のみ入力
- **その他の列**: 既に数式が設定されているため、自動計算される

### 自動移行の可能性
- **移行元**: Pricing Toolまたは変換済みNomination Sheet
- **移行先**: CVAフォーマット
- **移行内容**: 必要な情報を自動的に移行可能と判断

### Volume Agreement Inputの扱い

#### BCOアカウントの場合
- **基準**: Nomination volumeと一致させる必要がある
- **確認事項**: Volume Agreement InputがNomination volumeと一致しているか確認

#### NVOまたはNon Tenderアカウントの場合
以下のいずれかを使用可能：
- **Historical footprint**: 過去の実績データ
- **Forecast volume**: 予測ボリューム
- **Agreed volume**: 顧客と合意したボリューム

### Volume Agreement Inputの課題
- **定義の多様性**: 
  - Hirecast（予測）か？
  - Actual（実績）か？
  - その他の定義か？
- **タイミングの問題**: 
  - Awardデータは抽出タイミングによって変動する可能性がある
  - 更新直後に抽出すれば問題ないが、時間が経つと若干の差異が生じる可能性
- **解決策**: テストラン中に最適なタイミングと頻度を決定

## Game Plan Summaryの扱い

### Game Planの種類
1. **Route Portfolio Simulation (RPS)**: ルートポートフォリオのシミュレーション
2. **Game Plan Summary (GPS)**: ゲームプランのサマリー

### RPSのサンプルシート
- **目的**: CSVと照らし合わせて項目を確認
- **提供**: 2024年1月21日に仲井さんから提供
- **種類**: 
  - **Domi RPS**: ドミナントルート向け
  - **Non-Domi RPS**: 非ドミナントルート向け
- **注意点**: Domi/Non-Domiで必要な情報が多少異なる

## 関連ファイルとリンク

### CVAフォーマット
- **提供日**: 2023年12月27日
- **提供者**: Koji Nakai（仲井さん）
- **共有先**: PwC側（Haruka Kawataさん）

### Game Plan Summary
- **サンプルシート提供日**: 2024年1月21日
- **提供者**: Koji Nakai（仲井さん）
- **種類**: Route Portfolio Simulation (RPS)

## 実務上のポイント

### CVAフォーマットの活用
- Salesは限られた列のみ入力すればよいため、作業効率が向上
- 自動計算される列が多いため、ミスを減らせる
- Pricing Toolからの自動移行により、データ入力の手間を削減

### Volume Agreement Inputの管理
- BCOアカウントでは必ずNomination volumeと一致させる
- NVOアカウントではHistorical footprint、Forecast volume、Agreed volumeのいずれかを使用
- 抽出タイミングを考慮して、レポート発行のタイミングを決定

### Game Plan Summaryの確認
- CSVと照らし合わせて項目を確認する際は、RPSのサンプルシートを参照
- Domi/Non-Domiで必要な情報が異なるため、適切なRPSを選択

## 次アクション
- [ ] CVAフォーマットの自動移行機能の実装状況を確認
- [ ] Volume Agreement Inputの定義を明確化
- [ ] Filing data field labelsのフィルタリング完了を確認
- [ ] Game Plan SummaryのCSV項目との照合完了を確認

#inbox #eagle-x #filing-unit #cva-format #game-plan #reporting #pwc

