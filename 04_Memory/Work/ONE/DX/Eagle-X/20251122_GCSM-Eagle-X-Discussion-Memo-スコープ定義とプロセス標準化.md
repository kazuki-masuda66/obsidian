---
title: GCSM × Eagle X Discussion Memo - スコープ定義とプロセス標準化
tags: [eagle-x, gcsm, scope-definition, process-standardization, traditional-case]
created: 2025-11-22
source: ★スター付きメール抽出_Part4.md
---

# GCSM × Eagle X Discussion Memo - スコープ定義とプロセス標準化

## 概要

GCSM（Global Commercial & Service Management）とEagle Xチームの議論メモ。スコープ定義、プロセス標準化、Traditional Caseの扱いについて。

## 背景

- **日付**: 2024年6月18-19日
- **発信者**: Shoichiro Terada (Eagle X), Daisuke Tsunematsu (GCSM)
- **受信者**: Koji Nakai, Kazuki Masuda, Carmen Yau
- **目的**: GCSMとEagle Xの協力体制の確立と、プロセス標準化

## 主要ポイント

### 1. Action Items

#### Clarify Scope
- **6/21**: GCSMがTender Calendarを最終確定（地域とのベストエフォート）
- **6/28**: Eagle XがOPUS Contract Dataを使用して不足顧客を追加
- **7/5**: JP SYMと不足顧客について議論し、カテゴリーを検討

#### Create Dashboard
- **6/28**: Status List & GCSM Management Dashboard Mock upをv47で更新（GCSM入力なし）
- **7/1以降**: GCSM Additional Infoを更新

#### Pending Items
- **Traditional Case**: 交渉後にコンバージョンする場合でも、Pricing tool revenue情報がない場合の扱い

### 2. Scope Definition

#### GCSM Calendarに入っていない対象

**1) Rate Inquiry**
- **Eagle Xの立場**: 原則含める（含めないと、どのシステムでも把握できない）
- **対応**: Tender Calendar vs Contract Masterで対象を把握したうえで議論
- **判断基準**: Liftingを調べて、かなりマイナーであればイレギュラーケースとして扱う

**2) POST Tender**
- **Tigerの機能**: TigerのAmendmentなどが機能する場合は、Eagle X対象外としても可
- **課題**: 来年以降も考慮するために、Tender DBへの登録方法を検討する必要がある

### 3. Traditional Caseの定義

- **定義**: Eagle Xで進められない場合（例：顧客フォーマットが対応不可など）
- **カテゴリー**:
  1. **時間切れ**: 顧客の期限に間に合わない
  2. **複雑で難しい**: 顧客フォーマットが複雑で対応困難
- **課題**: Revenue LaneなどをSalesに手入力してもらわないとCVAに登録できない問題
- **解決策**: 現時点では名案がなく、継続的に検討が必要

### 4. プロセス標準化の重要性

- **標準プロセスタイムライン**: すべてのステークホルダーが明確に判断できるよう、標準プロセスタイムラインを設定
- **例外処理**: 例外・予期しないケースを処理する意思決定プロセスを明確化
- **ガイドライン**: GCSMが提案を最終化し、Eagle Xに提出予定

### 5. Tender定義の重要性

- **課題**: "all long term contracts"を含む一般的なRFQをEagle Xで処理することに、Salesを納得させることが困難
- **RFQの特徴**: 
  - Spot、1つまたは少数のレーンのみ
  - Tenderフォーマットなし
  - 統一されたプロセスとタイムラインなし
  - Salesが顧客からいつ受け取るか予測できない
- **懸念**: すべての長期RFQをEagle Xで処理すると、作業負荷、リードタイム、プロセスの複雑さの観点で効率が犠牲になる可能性
- **解決策**: "Tenderとは何か？"の定義に到達することが重要。これはEagle XのスコープとTender Calendarの両方と整合する必要がある

## 実務上の注意点

### 1. プロセスリードタイム

- **重要性**: Eagle Xのプロセスリードタイムと顧客が提供するタイムフレームは、ライブフェーズでの重要な依存関係
- **標準化**: 処理時間を標準化することで、すべてのステークホルダーが明確に判断できる
- **ガイドライン**: 標準プロセスタイムラインと例外処理の意思決定プロセスを含む

### 2. Scopeの明確化

- **Tender Calendarとの統合**: GCSM Calendarに入っていない対象（Rate Inquiry、POST Tender）の扱いを明確化
- **Contract Masterとの分析**: Tender Calendar vs Contract Masterで対象を把握
- **判断基準**: Liftingを調べて、マイナーであればイレギュラーケースとして扱う

### 3. Traditional Caseの扱い

- **後からコンバージョン**: Traditional Caseは後からコンバージョンすることを検討
- **CVAデータへの昇華**: Revenue Laneなどの情報をSalesに手入力してもらう必要がある
- **解決策の検討**: 継続的に解決策を検討する必要がある

## 関連情報

- **システム**: 
  - GCSM Tender Calendar
  - Eagle X Status List
  - OPUS Contract
  - Tiger System
  - CVA (Contract Volume Analysis)
- **担当者**: 
  - Shoichiro Terada (Eagle X)
  - Daisuke Tsunematsu (GCSM)
  - Koji Nakai (Eagle X)
  - Kazuki Masuda (Eagle X)
  - Carmen Yau (GCSM)
  - Cary Low (GCSM)
  - Ben Cobb (GCSM)

## 今後の展開

1. **ガイドラインの完成**: GCSMがプロセス標準化のガイドラインを完成させ、Eagle Xに提出
2. **Tender定義の明確化**: "Tenderとは何か？"の定義を明確化し、Eagle Xのスコープと整合
3. **Traditional Caseの解決**: Traditional CaseのCVAデータへの昇華方法を検討
4. **継続的な議論**: GCSMとEagle Xの継続的な議論により、相互の結論に到達

## 関連ファイル

- [[Eagle-X-Scope-Definition]]
- [[GCSM-Tender-Calendar-Management]]
- [[Traditional-Case-Handling]]
- [[Process-Standardization]]

