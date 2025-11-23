# Eagle X - Aurora R3 Pricing Request実務ノウハウ

---
title: Eagle X - Aurora R3 Pricing Request実務ノウハウ
tags: [eagle-x, aurora, pricing-request, r3, live-tender, brazil, laec]
created: 2025-11-22
---

## 概要
Eagle X Live環境で処理したAurora（G-BR101019）のR3（Round 3）プライシングリクエストに関する実務ノウハウ。Pricing Requestの送信、Rate Offerの作成、Consolidation、顧客への提出までのプロセスをまとめた。

## テンダー基本情報

### 顧客情報
- **Group Code**: G-BR101019
- **Group Name (Short)**: Aurora
- **Sequence #**: seq01
- **Round**: R3
- **Type**: BCO
- **Sales Office Group**: NAM/LAT
- **Sales Office**: BR（Brazil）

### 契約情報
- **SC/RFA Contract #**: SAOM010B22, CWBB00101A
- **Contract Start Date**: 2023-12-31
- **Contract Period**: 1 year
- **Due Date (Pricing)**: 2023-11-24
- **Due Date (Customer)**: 2023-11-24（テンダー提出期限）

### Sales担当者
- eduardo.ogawa@one-line.com
- natan.gonzalez@one-line.com
- irving.najera@one-line.com
- cassandra.peretto@one-line.com
- marina.mantovani@one-line.com
- adailton.ribeiro@one-line.com
- eduardo.alves@one-line.com

## Pricing Requestの送信

### 送信日時
- **送信日**: 2023年11月24日（金）18:49:50
- **送信者**: darrell.domalaon@one-line.com

### 宛先
- **To (email address)**:
  - br.mktg.laec.am@one-line.com
  - br.mktg.laec.as@one-line.com
  - ghq.eaglex.pricing.support@one-line.com
  - cst.eaglex.support@one-line.com

### To Pricer Grp for 'Pricing Trade File'
- **LE NonDomi Pricing (For US)**
- **LE NonDomi Pricing (For Asia)**

### メッセージ
- **締切**: 2023-11-24までにQuoteを提出
- **目的**: テンダーを期限までに提出できるようにする

## Salesからのコメント

### 1. Previous Round Targetsの確認
- **内容**: Customer's Previous Round Targets for Rate and Freetimeを確認・考慮する
- **重要性**: 前回ラウンドのターゲットを参考にする

### 2. Rate Structureの確認
- **構造**: Previous Round（R3 FRETE counter offer + BUNKER）と同じ構造
- **注意点**: Rate構造が前回ラウンドと同じであることを確認

### 3. R3 Rate OfferとFreetime Remarksの確認
- **確認事項**: R3 Rate OfferとFreetime Remarksを確認してからOfferする
- **タイミング**: Offer前に必ず確認

### 4. Preferred Serviceの変更時の対応
- **変更があった場合**: Preferred Serviceが変更された場合、R3 Target for 'Rate', 'DMIF', or 'DTIC'に一致できない場合
- **対応**: 
  - 正しい'Route Summary'を記載
  - 一致できない理由をPricing 'Internal Remarks'に記載

### 5. TAXASの考慮
- **内容**: R3 Target for 'TAXAS'を考慮する
- **確認事項**: 'Note to Pricer'を確認
- **入力方法**: 手動で"40-2 Other than OFT" Gdrive folderに入力

## キードキュメントとフォルダ

### Key Documents
- **フォルダ**: https://drive.google.com/drive/folders/1IdJevjiadqgZ6R6DeQhy8UR2_VIizQON
- **内容**: OFT以外のキードキュメント（Sales Intention Sheet等）

### Conversion Checklist
- **フォルダ**: https://drive.google.com/drive/folders/1O4cFLh88H19QB99lGQHe9-VjwVXj-XGq
- **内容**: T&C Summary、Conversion Checklist

### 40-2 Other than OFT
- **フォルダ**: https://drive.google.com/drive/folders/1IdJevjiadqgZ6R6DeQhy8UR2_VIizQON
- **内容**: OFT以外のシート（TAXAS等）

### Pricing Tool
- **パス**: G:\Shared drives\Eagle-X-FY24ForPricer\LA\BR\Aurora\seq01\
- **内容**: Pricing Data and Tool

## Rate Offerの作成と提出

### Rate Offerの作成
- **作成者**: Cali Yaptangco（CST - Conversion Supporting Team）
- **作成日**: 2023年11月27日（月）17:33:45

### Rate Offerの内容
- **計算基準**: R3 OFFER OFT + R1 BUNKER
- **ファイル**: 
  - Consolidated Rate file（内部用）
  - Updated Original Customer file（顧客提出用）

### ファイルのアップロード先
- **リンク**: https://drive.google.com/drive/folders/1AmotUPKOq_KltT8YRgVXPKwJOjYMLb2L
- **注意**: Updated Original Customer fileのみを顧客に提出（Consolidated Rate fileは機密情報を含むため提出不可）

### CST Comments
1. **計算方法**: Round 3 offerは（R3 OFFER OFT + R1 BUNKER）に基づいて計算
2. **TAXASシート**: 40-2 OtherThanOFT内の'TAXAS'シートにはまだOfferがないため、該当Pricerと調整が必要
3. **ALOCAÇÃOシート**: 顧客提出前に、関係Pricerと確認して'ALOCAÇÃO'シート名を記入

## Pricing Processの実務ポイント

### Rate Structure
- **構造**: R3 FRETE counter offer + BUNKER
- **前回ラウンド**: 同じ構造を維持

### Preferred Serviceの変更
- **変更があった場合**: Route Summaryと理由をInternal Remarksに記載
- **目的**: Salesが後で確認できるようにする

### TAXASの扱い
- **入力方法**: 手動で"40-2 Other than OFT" Gdrive folderに入力
- **確認事項**: Note to Pricerを確認

### Consolidation
- **内部ファイル**: Consolidated Rate file（機密情報を含む）
- **顧客提出ファイル**: Updated Original Customer file（機密情報を除く）
- **注意**: Consolidated Rate fileを顧客に提出しない

## 実務上の課題と対応

### COD（Cash on Delivery）の扱い
- **課題**: TariffよりUSD 100下回ることはできない
- **対応**: Counter offerをUSD 350に変更（USD 400から）

### Rate Offerの調整
- **背景**: 4つの大手キャリアがOsaka向けにUSD 3,100 all-inでOffer
- **対応**: OsakaとTokyo向けにUSD 3,100（ALL IN）でRevised fileを作成
- **変更箇所**: R3 columnの変更箇所をREDでハイライト

### Award決定のタイミング
- **状況**: Aurora BIDで、Auroraのボードと2024 nomination/Awardを決定中
- **影響**: 4つの大手キャリアがOsaka向けにUSD 3,100 all-inでOffer

## 次アクション
- [ ] TAXASシートのOfferを該当Pricerと調整
- [ ] ALOCAÇÃOシートを関係Pricerと確認して記入
- [ ] Updated Original Customer fileを顧客に提出
- [ ] Award決定を待つ

#inbox #eagle-x #aurora #pricing-request #r3 #live-tender #brazil #laec

