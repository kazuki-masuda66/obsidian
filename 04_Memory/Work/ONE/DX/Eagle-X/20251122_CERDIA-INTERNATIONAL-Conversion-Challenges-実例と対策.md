---
title: CERDIA INTERNATIONAL Conversion Challenges - 実例と対策
tags: [cerdia, conversion-challenges, location-mapping, sales-instruction, wns-india]
created: 2025-11-22
---

# CERDIA INTERNATIONAL Conversion Challenges - 実例と対策

## 概要
CERDIA INTERNATIONALテンダーにおけるConversion Challengesの実例と対策。Location Mapping、Sales Instructionの反映、POD Portionの入力エラーなど。

## 背景情報

### 顧客情報
- **顧客名**: CERDIA INTERNATIONAL
- **処理チーム**: WNS IN (TST)
- **担当者**: Benhur Dalumpines (GHQ Eagle X Conversion Team)

### 問題の概要
- **発見日**: 2024年11月7日
- **問題**: Sales Review段階でCKAMが提供した指示がConversion toolに反映されていない
- **影響**: 複数の項目でConversion toolとSales Instructionの不一致

## 問題詳細

### 1. Location Mappingエラー（最重要）

#### 問題内容
- **Sales Instruction**: Freiburgに"DEFBG"コードを使用（DE76Cではなく）
- **実際の処理**: Location Mappingが更新されていない
- **影響**: 誤ったLocation Codeが使用された

#### WNS INの回答
- **対応**: DEFBGはConversion前に更新済み
- **スクリーンショット**: 更新済みの証拠を提供
- **問題**: それでも誤ったコードが使用された可能性

#### 対策
- **事前確認**: Conversion前にLocation Mappingの確認
- **Auditor Review**: C-KAMからの変更要求をFirst auditorがレビュー
- **GHQ連携**: 変更がある場合はGHQ Eaglex memberと調整してからPricing tool作成

### 2. CY-CY (Port to Port) Rate処理

#### 問題内容
- **Sales Instruction**: CY-CY (Port to Port) rateをPricersに要求
- **実際の処理**: 2つのDoor LocationがDoorとしてタグ付けされた
- **背景**: C-KAMがGreensboroをDoor locationとして考慮するよう指示
- **処理**: On-carriageが明確に記載されていないため、Through rateとして考慮

#### WNS INの回答
- **対応**: C-KAMの指示に従い、GreensboroをDoor locationとして処理
- **確認**: Jasmine Ekambaramも同意
- **問題**: CY-CY rateの要求とDoor locationの処理が矛盾

### 3. POD Portion入力エラー

#### 問題内容
- **POD Portion**: 入力が正しくない
- **詳細**: 具体的な入力内容が不明確
- **影響**: Conversion toolでのPOD情報が不正確

#### WNS INの回答
- **原因**: PricerがMandatory columnを更新していない
- **問題**: WNS INもFinal consolidation時に確認を漏らした
- **処理**: Origin portをDEFBGとして考慮

## 実務ノウハウ

### Sales Instructionの反映プロセス
1. **指示の確認**: C-KAMからの指示を必ず確認
2. **Location Mapping更新**: 指示に基づいてLocation Mappingを更新
3. **Auditor Review**: First auditorが変更をレビュー
4. **GHQ連携**: 変更がある場合はGHQ Eaglex memberと調整
5. **Pricing Tool作成**: 確認後にPricing toolを作成

### エラー防止策
1. **事前確認**: Conversion前に全ての指示を確認
2. **ダブルチェック**: Final consolidation時にMandatory columnを確認
3. **プロセス遵守**: Sales Instructionの反映プロセスを遵守
4. **連携強化**: C-KAM、WNS IN、GHQ Eaglex間の連携強化

### 改善点
- **Check Pointの実装**: 電話会議で議論したCheck Pointを実装
- **プロセス明確化**: Sales Instructionの反映プロセスを明確化
- **エラー防止**: 同様の懸念を将来回避するための安全策を設定

## 担当者連携

### GHQ Eagle X側
- **担当者**: Benhur Dalumpines
- **役割**: 問題の発見とフィードバック提供

### WNS IN側
- **担当者**: Murali Krishna、Siva Rama Krishna Buddha
- **役割**: Conversion処理の実施と修正

### C-KAM側
- **担当者**: Caroline Kempf、Jasmine Ekambaram
- **役割**: Sales Instructionの提供と確認

## 関連情報

### 参考資料
- CERDIA Conversion tool
- Sales Review comments
- Location Mapping documentation

## 次アクション
- [ ] Check Pointの実装
- [ ] Sales Instruction反映プロセスの明確化
- [ ] エラー防止策の実施
- [ ] WNS INへの教育とトレーニング

