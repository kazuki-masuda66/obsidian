---
title: GKA position on Tender conversion - 状況管理
tags: [gka, tender-conversion, bco, potential, workable-status]
created: 2025-11-22
---

# GKA position on Tender conversion - 状況管理

## 概要
GKA（Global Key Account）BCOのTender conversion状況の管理。変換済み、変換失敗、保留中のアカウントの追跡と、Potential変換の状況確認。

## 背景情報

### GKA定義
- **GKA**: Global Key Account
- **BCO**: Beneficial Cargo Owner
- **総数**: 86アカウント（GCSM tender calendarベース）

### Conversion状況の分類
1. **Converted**: 2024年または2025年のテンダーファイル変換が完了（少なくとも1つのバージョンのPotentialが存在）
2. **Failed conversion**: 変換に失敗
3. **Pending**: 変換待ち（変換可能な時期を確認）

## Conversion状況分析

### 変換済みアカウント
- **基準**: 2024年または2025年のPotential列にTEU数値が存在
- **判定方法**: Volume potential columns（2024または2025）にTEU figureが存在する場合、変換済みと判定
- **結果**: 大部分のGKAが変換済み

### 保留中アカウント（3アカウント）
1. **DAIMLER TRUCK**: Workable（変換可能）
2. **H&M**: GKAから削除予定（重要度低）
3. **PROCTER & GAMBLE**: Workable（変換可能）

### Conversion判定基準
- **変換済み**: 2024年または2025年のPotential列にTEU数値が存在
- **保留中**: Potential列が空白またはN/A
- **Workable**: ファイル形式が変換可能

## 実務ノウハウ

### Conversion状況の確認方法
1. **GCSM Tender Calendar確認**: 総GKA数を確認（86アカウント）
2. **Potential列確認**: 2024年または2025年のPotential列にTEU数値が存在するか確認
3. **Workable Status確認**: 保留中のアカウントがWorkableか確認

### Conversion判定の注意点
- **手動分析**: Ben Cobbによる手動分析（Potential列の存在確認）
- **自動判定**: システムによる自動判定との整合性確認
- **Workable確認**: 保留中のアカウントがWorkableか確認が必要

### 変換計画の管理
- **DAIMLER TRUCK**: Workable、変換計画を確認
- **PROCTER & GAMBLE**: Workable、変換計画を確認
- **H&M**: GKAから削除予定のため、変換不要

## 担当者連携

### GCSM側
- **担当者**: Ben Cobb (Global Sales Process, Global Commercial & Service Management)
- **役割**: GKA conversion状況の確認とGCSM leadersへの報告

### GHQ Eagle X側
- **担当者**: Koji Nakai、Kazuki Masuda
- **役割**: Conversion状況の提供とWorkable status確認

### 参考資料
- **GCSM Tender Calendar**: https://docs.google.com/spreadsheets/d/1nM4yZ4NfQNOKKwLHqDwFaIq7zHERHLlMFkAV-9n8FHc/edit?gid=203001380#gid=203001380

## 関連情報

### Conversion状況の更新
- **更新頻度**: 定期的に更新
- **確認方法**: Potential列の存在確認
- **報告先**: GCSM leaders

## 次アクション
- [ ] DAIMLER TRUCKの変換計画確認
- [ ] PROCTER & GAMBLEの変換計画確認
- [ ] Conversion状況の定期更新
- [ ] Workable statusの確認プロセス確立

