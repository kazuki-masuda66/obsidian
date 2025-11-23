# Sales Checklist Review - 改善要件とChange Requestノウハウ

---
title: Sales Checklist Review - 改善要件とChange Requestノウハウ
tags: [eagle-x, sales-checklist, review, enhancement, change-request, pwc]
created: 2025-11-22
---

## 概要
Sales Checklistのレビューと改善要件に関するノウハウ。PwCによる改善案、LA/EUA RHQからの要件、Change Requestの作成、優先順位の決定プロセスをまとめた。

## Sales Checklist改善の背景

### PwCによる改善案
- **提供日**: 2023年5月3日（水）08:00:00
- **提供者**: Makoto Ohmi（近江さん）
- **リンク**: https://docs.google.com/spreadsheets/d/1ncY81tYmR0JcbExDhXZO6jSbFWbexRGFELD4HKoCfC4/edit#gid=523332967
- **内容**: Ben（Benhur Dalumpinesさん）の前回コールでの提案を考慮した改善案

### LA/EUA RHQからの要件
- **ソース**: E2E trialを通じて要件を受領
- **目的**: 優先順位を付けて改善を実施

## Change Requestの作成

### Change Request Form
- **リンク**: https://docs.google.com/spreadsheets/d/1iEvYDgcFyeFyu9MEtj9mTyPuF-MIljJ1/edit#gid=311035452
- **更新版（Gsheet形式）**: https://docs.google.com/spreadsheets/d/1BaQmFAfYgrcEdGAQGUkvIs85RNSo4Fym56Ju5VDtTEA/edit#gid=1974164588
- **ファイルフォルダ**: G:\Shared drives\Eagle-X\Documentation\99_DX Main Folder\Change Request
- **作成者**: Yuesheng Chia（謝越盛さん）

### Enhancement Tracker
- **タブ**: 2. Enhancement Tracker
- **優先順位**: Column Gで優先順位を考慮
- **目的**: 改善要件のリストと優先順位を管理

## Change Requestの詳細

### CR00001: Sales Checklist enhancement（統合）
- **内容**: Sales Checklist改善を統合
- **Mock up draft**: https://docs.google.com/spreadsheets/d/15O4ro3loF-l3dvNQgF-v8CGY-fK77Fqpv2VIugOx9c8/edit#gid=279806227
- **担当**: Yue Sheng（謝越盛さん）がCR00001とCR00002を含むSales Checklistの強化版テンプレートを作成

### CR00002: 8 Place Location Review & TT Input
- **内容**: Place Location Review & TT Input
- **Mock up draft**: https://docs.google.com/spreadsheets/d/1Jla5Y3HxnDkk0KRju_Xod0J2_oNw8LrcjuTtMXYTa3A/edit#gid=0
- **提供者**: Flourance Tanさん
- **テスト**: G-US112079_ASCEND Test Studyを使用してドラフト改善要件を作成
- **注意**: Gsheetがクラッシュする可能性があるため、OPUS master location listを使用したドロップダウン選択は説明用のみ

### CR00003: Sales Review Request / Review Location Mapping & Input TT Info
- **提供者**: Flourance Tanさん
- **内容**: Sales Review Request / Review Location Mapping & Input TT Info
- **テスト**: G-US112079_ASCEND Test Studyを使用

### CR00004: 新しいSales Checklist設計
- **提供者**: Benhur Dalumpinesさん
- **内容**: 新しいSales Checklist設計のコンセプト全体が説明部分に適切に反映されているか確認が必要
- **担当**: Benhurさんがコンセプト全体を確認

### CR00005: KPI report dashboard usage
- **提供者**: DX CM Team
- **内容**: KPI report dashboard usage
- **追加者**: Masuda san（増田さん）

### CR00006: Conversion toolsの自動化設定
- **内容**: Conversion toolsの自動化設定リクエスト
- **追加者**: Masuda san（増田さん）
- **ボタン機能**:
  1. Upload of Field mapping to Field Master Database
  2. Retrieve/download Field Mapping information from Field Master Database
  3. Navigation button back to Control Panel at various worksheet
  4. Navigation button/hyperlink from Control Panel different step to have the button to go to the respective sheet to check

### Field Master v1.0
- **リンク**: https://docs.google.com/spreadsheets/d/1-C5jvSRCIRI0mshtFQAjzNklTJLr2kbh5j1IJZilphc/edit
- **ワークシート**: Master Update Flow worksheet
- **目的**: 2iと2iiのプロセスフローをBenhurさんとレビューして、PwCにアイデアを伝えやすくする

## Update Checklist (Details)

### テンプレート
- **リンク**: https://docs.google.com/spreadsheets/d/1ncY81tYmR0JcbExDhXZO6jSbFWbexRGFELD4HKoCfC4/edit#gid=523332967

### 追加事項
1. **Remark列の追加**: PwC提案テンプレートにRemark列を追加
2. **目的の明確化**: Update Checklistは新しくSales Checklistを刷新するものではなく、内部使用用で、CST Teamが更新する可能性がある
3. **データ保持**: PwCとプロセスをレビューして、このシートを更新してデータを保持する方法を確認

## Commodity情報の設定

### Benhurさんからの提案
- **設定内容**: Commodity情報を設定
- **画像**: 画像で設定内容を提示
- **対応**: 謝越盛さんがCommodity情報要件をさらに調整

### 最終設定
- **内容**: Salesが最大3つまでのCommodity typesを指定できるように強化版で設定
- **目的**: "To Be" mock up draftをPwCに提示

## ExcelからGsheetへの変換問題

### 問題点
- **問題**: ExcelからGsheetへの変換、GsheetからExcelへの変換で問題が発生
- **具体的な問題**:
  - Hyperlinkが消失
  - 画像の配置が乱れる
- **対応**: CR formをGsheet形式に変換

## 実務上のポイント

### Change Requestの管理
- Change Request Formで全ての改善要件を管理
- Enhancement Trackerで優先順位を管理
- 各CRにMock up draftを作成

### Sales Checklist改善の統合
- CR00001にSales Checklist改善を統合
- CR00001とCR00002を含むSales Checklistの強化版テンプレートを作成
- PwCに提示して議論

### Place Location Review & TT Input
- CR00002として作成
- OPUS master location listを使用したドロップダウン選択は説明用のみ（Gsheetがクラッシュする可能性があるため）
- Flourance Tanさんがレビューして調整

### Commodity情報の設定
- Salesが最大3つまでのCommodity typesを指定できるように設定
- Benhurさんからの提案を基に、謝越盛さんが調整

### Update Checklistの扱い
- 新しくSales Checklistを刷新するものではない
- 内部使用用で、CST Teamが更新する可能性がある
- データ保持の方法をPwCとレビュー

## 次アクション
- [ ] 各CRの優先順位を決定
- [ ] PwCとの改善要件セッションを実施（火曜日）
- [ ] Mock up draftをPwCに提示
- [ ] 改善要件の必要性と優先順位をアライメント
- [ ] Field Master v1.0のプロセスフローをBenhurさんとレビュー

#inbox #eagle-x #sales-checklist #review #enhancement #change-request #pwc

