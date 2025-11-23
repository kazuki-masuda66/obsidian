# Eagle X E2E Conversion Test for OMMC-GTMテスト計画ノウハウ

---
title: Eagle X E2E Conversion Test for OMMC-GTMテスト計画ノウハウ
tags: [eagle-x, e2e-test, ommc-gtm, conversion-test, test-plan, toyotire, covestro, lanxess]
created: 2025-11-22
---

## 概要
Eagle X End to End Conversion Test for OMMC-GTM（ONE Manila Marketing & Commercial Center - Global Tender Management）のテスト計画と実施に関するノウハウ。テスト対象アカウント、実施フロー、タイムライン、関係者、課題と対応をまとめた。

## テスト対象アカウント

### 初期計画（2023年9月）
1. **Procter & Gamble**
2. **Toyo Tire**
3. **Electrolux**
4. **Covestro**

### 実施方針
- **実施方法**: 1アカウントずつテスト（1 account per week）
- **最初のアカウント**: クイックデモンストレーションを注入して、参加者がプロセスを思い出せるようにする
- **後続のテスト**: 発生した懸念や問題に対応するためのTouchpointセッションを設定

### 変更後の計画（2023年10月）
- **Toyo Tire**: 継続実施
- **Covestro**: Electroluxの代わりに実施
- **Lanxess**: Electroluxの代わりに追加

## 関係者

### 参加チーム
- **OMMC GTM (TST)**: テンダー管理チーム
- **OMMC Pricer / HKG Pricer / GHQ Pricer / AU Pricer**: 該当するテンダー要件に応じて参加
- **OMMC Surcharge Team (CST-S)**: サーチャージチーム
- **CST - Conversion**: コンバージョンチーム
- **GHQ EAGLE X Team**: GHQ Eagle Xチーム
- **GCSM HK**: GCSM香港チーム

## E2E Test General Flow

### プロセスフロー
1. **Tender Preparation** - by OMMC GTM
2. **Initial Check In (Google Form)** - by OMMC GTM
3. **Initial Checklist Generation** - by OMMC GTM
4. **Conversion Tool** - by CST Conversion Team (offline)
5. **Surcharge Summary Creation** - by Surcharge Team (Offline)
6. **Sales Review** - by OMMC GTM
7. **Pricing Tool** - by Pricer Trade (Offline)
8. **Consolidation Tool** - by OMMC GTM
9. **Transit Time inputting** - by OMMC GTM
10. **Submission to Sales** - by OMMC GTM

### カバー範囲
- **開始**: Tender Preparation
- **終了**: Submission of Consolidated File back to Sales

### 個別フォルダとシーケンス番号
- 各参加者に個別のフォルダとStatus List内のシーケンス番号が割り当てられる
- ハンズオン生成用に使用

### 注意事項
- Conversion、Surcharge、Pricingでは1つのシーケンス番号のみを使用

## Toyo Tireテストのタイムライン

### 実施期間
- **アカウント**: TOYO TIRE
- **OMMC PIC**: Elmer Pecban

### タイムライン（2023年10月）
- **October 2-3 (12NN)**: OMMC Submission of Initial Check-In & Checklist (Offline)
- **October 03 (2:30-5:00PM)**: CST-C Actual generation of Conversion Tool (Virtual)
- **October 04 (2:30-5:00PM)**: CST-S Actual generation of Surcharge Tool (Virtual)
- **October 06 (2:30-5:00PM)**: Pricing Trade Actual generation of Pricing Tool (Virtual)
- **October 18 (2:30-5:00PM)**: CST-C Actual generation of Consolidation Tool (Virtual)

## Covestro / Lanxessテストのタイムライン

### 実施期間
- **アカウント**: Covestro / Lanxess
- **OMMC PIC**: 
  - Covestro: Joan Cabanlong
  - Lanxess: Steven Ortega

### タイムライン（2023年10月）
- **October 19-20**: OMMC Submission of Initial Check-In & Checklist (Offline)
- **October 24 (3:00-5:00PM)**: Touchpoint Meeting (highlight TST's concerns encountered)
- **October 25 (2:30-4:00PM)**: Touchpoint Meeting (highlight TST's concerns encountered)
- **October 27 (4:00-5:00PM)**: Touchpoint Meeting (highlight TST's concerns encountered)

### 実施方法の変更
- **Offline**: CSTやPricing側からの実際のデモンストレーションは行わない
- **目的**: TSTが遭遇した懸念や問題をハイライトする

## OMMC GTMからのフィードバック

### Covestroに関する注意事項
- **ポータル変更**: Covestroのポータルが今年変更される予定（CKAMからのアドバイス）
- **影響**: テンダーファイルが異なる可能性が高い

### 同時処理の確認
- **質問**: CovestroとLanxessの2つのテンダーを同時に処理するか？
- **回答**: はい、2つのアカウントを同時に処理する

### Touchpoint Meetingの提案
- **提案**: テストラン完了後にコールを設定
- **代替案**: 問題が発生した場合は、グループチャットまたは必要に応じてミーティングを作成

### その他の要望
1. **Pricerへの通知**: テストが"live"であることをPricerに通知（認識のため）
2. **Live Tenderとして扱う**: ダミー入力ではなく、Live Tenderとして扱う（昨年のファイルがあるため）
3. **全Pricerの参加確認**: 全Pricerを参加させるか、少数を選択するか確認（受信数を把握するため）
4. **OMMC GTMアドレスの確認**: OMMC GTMのアドレスが既に含まれているか確認

## Eagle Xチームからの対応

### Touchpoint Meetingのスケジュール
- **提案**: 予定されたスケジュールを維持
- **理由**: CSTチームが既に複数のLIVE Tenderを処理しており、優先順位を付ける必要がある
- **柔軟性**: テストの進捗に応じて、Touchpoint Meetingを実施するか、次の予定セッションに移動するかを決定

### Group Chatの設定
- **既存**: Hangout space "OMMC E2E Test"が既に存在
- **用途**: このオフラインプロセスのコミュニケーションチャネルとして継続使用
- **追加**: 関係するPricing Trades PICとGCSM HKGを追加

### Pricerへの通知
- **方法**: メールでPricerに通知、OMMCをccに追加
- **内容**: テストが"live"であることを通知
- **確認**: 関係するTradesを確認してから、該当Pricerにメール送信

### Pricerの参加確認
- **現状**: ほぼ全てのPricing Tradesがオンボード済み（NA Pricing Tradeを除く）
- **確認**: PricerにQuote提供の可否を確認して、受信数を把握

## 実務上のポイント

### E2E Testの目的
- Tender PreparationからSubmissionまでの全プロセスをテスト
- 各ステップでの課題や問題を特定
- プロセスの改善点を洗い出す

### Offline実施の利点
- 実際のデモンストレーションに時間を取られない
- TSTが実際に作業を実施して、課題を発見できる
- より実践的なテストが可能

### Touchpoint Meetingの重要性
- TSTが遭遇した懸念や問題を共有
- CSTやPricingチームが対応方法を説明
- プロセスの改善につなげる

## 次アクション
- [ ] CovestroとLanxessのテストを実施
- [ ] Touchpoint Meetingで課題を共有
- [ ] プロセスの改善点を文書化
- [ ] 次のE2E Testの計画を立てる

#inbox #eagle-x #e2e-test #ommc-gtm #conversion-test #test-plan #toyotire #covestro #lanxess

