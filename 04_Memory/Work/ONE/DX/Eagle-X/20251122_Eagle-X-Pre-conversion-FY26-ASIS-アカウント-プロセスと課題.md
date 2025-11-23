---
title: Eagle-X Pre-conversion FY26 - ASISアカウント プロセスと課題
tags: [eagle-x, pre-conversion, fy26, asis-accounts, tender-management, ommc, wns]
created: 2025-11-22
---

# Eagle-X Pre-conversion FY26 - ASISアカウント プロセスと課題

## 概要
FY26 Pre-conversion for ASIS accounts in FY25 liveのプロセスと実務上の課題。OMMCとWNS INチームによる事前変換作業の詳細と、Sequence番号の分割判断基準。

## 背景情報

### Pre-conversionの目的
- **FY26テンダーの事前準備**: FY25でLive処理されたASISアカウントのFY26テンダーに向けた事前変換
- **完了期限**: 2025年4月末
- **環境**: TEST環境を使用

### 使用環境
- **Initial Check-in**: https://docs.google.com/forms/d/e/1FAIpQLSfms5tobWJ2_3ODEmc97ojHVd9VWNyAljTruPvjk6f8C69ktg/viewform?usp=preview
- **Sales Folder**: https://drive.google.com/drive/folders/1jn7C_R1cJicfkSByFXRHAJ7fsyVSb5xq (TEST > FY26 > Sales folder)
- **Status List**: https://docs.google.com/spreadsheets/d/1D1OUHJakwfxnMVZeV4m2edlK2pk4bzXOEPb5zFhP4EA/edit?gid=169003602#gid=169003602

## Sequence番号分割の判断基準

### 分割が必要なケース
1. **1H/2Hの分割**: KNAアカウント（Hankook, Hyundai, Samsung, Pantos）
   - **理由**: 1Hと2Hの両方で潜在ボリュームを捕捉・収集する必要がある
   - **例外**: 2HがFY25でLiveになる場合、2Hのpre-conversionは不要

2. **Round別の分割**: Round Filing/Award
   - **例**: Minerva seq02 - Round Filing/Award

3. **地域別の分割**: 
   - **例**: Cargill seq03 - Cargill NA

4. **TP/NON-TPの分割**: 
   - **例**: HANKOOK TIRE seq01 (NON TP ex CN) と seq04 (TP ex CN)
   - **注意**: 統合された場合はseq01のみ使用

### 分割が不要なケース
1. **複数シートの統合**: 
   - **例**: Eastman Chemicals - 2シートだが、元々1テンダーファイル
   - **対応**: 1つのSequence番号に統合

2. **RFA/SCの混在**: 
   - **判断**: RFAとSCが混在していても、Sequence番号を分割する必要はない

3. **単一テンダー**: 
   - **例**: DOLE Asia Fresh and Packaged Foods - 1テンダーのみ処理
   - **対応**: seq02は処理不要

4. **既にEagle Xで処理済み**: 
   - **例**: Bridgestone seq01 - 既にEagle Xで処理済み
   - **対応**: seq03は処理不要

## 実務上の課題と対応

### 課題1: JBG（Joint Business Group）の処理

**状況**:
- JBG = Unilever + Electrolux + Mondelezの共同テンダー
- Round 1後、Electroluxが離脱
- Round 2はUnileverとMondelezのみ

**対応**:
- **Electrolux**: Round 2ファイルを使用してpre-conversion
- **Unilever**: JBG Round 2ファイルを使用（UnileverとMondelezの両方のボリュームを含む）
  - **注意**: 2つのテンダーデータが含まれることを明記する必要がある

### 課題2: Mercedes BenzのMini Bid

**状況**:
- Mini Bid for extension（IBL）を受領
- 有効期間: 2025年4月 - 2026年9月
- 3つのSequence番号が存在

**対応**:
- **使用Sequence**: seq01（Mini Bid IBL用）
- **理由分割**: IBL（Inter-Business Lane）のため
- **他のSequence**: seq02, seq03は削除

**詳細**:
- **FBU&CKD (Block2-EU)**: Round 1受領日 2023年3月8日、有効期間 2024年4月1日-2027年9月30日、Awardなし
- **EU-SAF**: Round 1受領日 2023年3月、有効期間 2024年10月-2027年9月

### 課題3: BMWの処理

**状況**:
- 契約有効期間: 2024年10月 - 2027年9月
- FY25テンダーシート未受領

**対応**:
- FY25テンダーから除外
- Pre-conversion対象外

### 課題4: 複雑なファイル形式の処理

**対応方法**:
1. **Simplified Format Templateの使用**:
   - ツール: https://docs.google.com/spreadsheets/d/1iXfrbzbb8ESe9DoAWc4KdVk4ZvyxVrGyg64iZA1d314/edit?gid=1374956686#gid=1374956686
   - **手順**:
     - ツールを複製
     - "10-1_CustomerFile"フォルダに保存
     - 情報を入力（"Target Rate"と"Yearly Tender Volume (TEU basis)"を含む）
     - 黄色でハイライトされた列は必須
     - このファイルを顧客の元ファイルとして使用

2. **手動編集**: 
   - 複雑な顧客ファイル形式の場合、Simplified Formatに手動編集
   - この形式を顧客シートとして使用し、変換プロセスを進行

### 課題5: レーン数が多すぎる場合

**対応**:
- レーン数が多すぎる、またはファイルが複雑すぎる場合、ケースバイケースで検討
- GHQ EAGLEX SUPPORTに相談

## 進捗管理

### Status Listの確認項目
- **10-h-3-b**: Completed
- **Sales Review**: Submitted
- **GHQ Review**: In-Progress
- **Not Received**: Bid After Sep 2024
- **Un-workable**: Live Completed
- **Status issue**: Merging two Seq

### 2025年4月30日時点の進捗
- **Completed**: 19件
- **Sales Review Submitted**: 1件
- **GHQ Review In-Progress**: 43件
- **Not Received Bid After Sep 2024**: 7件
- **Un-workable**: 57件
- **Live Completed**: 13件
- **Status issue**: 1件
- **Merging two Seq**: 4件
- **Grand Total**: 146件

### データ問題の対応

**問題**: 4件のアカウントが"GHQ Review"に進んでいるが、FY26 Pre-Conversion Dashboardでは"S1_Not Started"と表示

**原因**: データ問題（タイムスタンプがFY26 TEST status listに登録されていない）

**対応**:
- CLV側に4件の個別チケットを発行
- 一時的な対応:
  - TRACTOR: Perform Initial Check-In
  - COLUMBIA: Perform Initial Check-In
  - ANSELL: Start the Conversion Form
  - ARKEMA: CLVがデータ問題を修正済み

## 実務ノウハウ

### Pre-conversion開始前の確認事項
- [ ] Sequence番号の分割理由を確認
- [ ] テンダーシートの受領状況を確認
- [ ] 契約有効期間を確認
- [ ] 既にEagle Xで処理済みか確認

### ファイル形式の確認
- [ ] 顧客ファイルの形式を確認
- [ ] 複雑な形式の場合、Simplified Format Templateの使用を検討
- [ ] レーン数が多すぎる場合、GHQ EAGLEX SUPPORTに相談

### 進捗管理
- [ ] Status Listを定期的に確認
- [ ] データ問題が発生した場合、CLV側にチケットを発行
- [ ] GHQ Reviewの進捗を確認

## 担当者情報

- **GHQ**: Kazuki Masuda (kazuki.masuda@one-line.com)
- **OMMC**: Mariel Jimeno (mariel.jimeno@one-line.com)
- **WNS IN**: Naga Murali Krishna Sajja, Srinivas Kokkonda
- **GHQ EAGLEX SUPPORT**: ghq.eaglex.support@one-line.com
- **GHQ DYM EAGLEX**: ghq.dym.eaglex@one-line.com

## 関連リンク
- [[Eagle-X Workflow]]
- [[Tender Management Process]]
- [[Pre-conversion Guidelines]]

## 次アクション
- [ ] 04_Memory/Work/ONE/DX/Eagle-X/に移動を検討
- [ ] Sequence番号分割判断基準の標準化を検討

#inbox #eagle-x #pre-conversion #fy26 #tender-management #ommc #wns

