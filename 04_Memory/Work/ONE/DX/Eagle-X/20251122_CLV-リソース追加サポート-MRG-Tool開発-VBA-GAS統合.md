---
title: CLVリソース追加サポート - MRG Tool開発 VBA/GAS統合
tags: [clv, mrg-tool, vba, gas, resource-allocation, development-support]
created: 2025-11-22
---

# CLVリソース追加サポート - MRG Tool開発 VBA/GAS統合

## 概要
CLVリソースを活用したMRG Tool開発支援。Ying Enからの業務シフトに伴うリソース補填と、VBA/GAS統合の課題。

## 背景情報

### 業務シフトの背景
- **従来担当**: Ying En（Sick leave）
- **新担当**: 田村さん（丸々担当）
- **追加支援**: CLVリソースの援用
- **目的**: 業務の早期シフトとリソース補填

### CLVの現状
- **現在のサポート範囲**: Conversion toolの保守(GAS) / Game Plan (Simulation Sheet : GAS)の開発フォロー
- **Pricing tool**: Ying Enがメインで開発（CLVは未対応）
- **LT MRG**: Pricing部分はCLVが触れていない

### リソース拡張
- **夜勤対応開始**: 2024年11月から
- **Headcount増加**: 5名増（QA 1名 + Developer 4名）
- **新メンバー**: 2ヶ月間の学習期間後、シフト対応開始

## 依頼内容

### MRG Tool開発支援
- **技術**: VBAを用いたMRG Toolの保守・開発
- **機能**: 
  - Tool内のSummary viewの作成
  - 別エクセルへの抽出機能の実装
- **役割分担**:
  - **田村さん**: レートのデータ抽出周り
  - **CLV**: ビューやその他の付随機能作成
- **Workload**: 週3~4時間程度

### 業務シフトのイメージ
- **田村さん**: Ying Enが担当していた業務を丸々担当
- **CLV**: 外注可能なCodeの作成やツールの修正を担当

## 技術的課題

### VBA vs GAS
- **GAS**: JavaScriptベース（CLVの現在のスキルセット）
- **VBA**: Visual Basic（MRG Toolで使用）
- **問題**: 書き方が大きく異なるため、CLVのスキルセットとのミスマッチ

### 統合方針の検討
1. **GAS統一**: 今後委託するツールをGASで統一し、CLVに保守を統一化
2. **VBA要員**: VBAの保守要員を長期的な目線（Pricing tool含む）でCLVで別に抱える

### MRG Toolの将来
- **GAS化検討**: MRG toolも将来的にはGAS化を検討
- **現状**: VBAのまま維持
- **課題**: GAS統一の選択肢は現状ないため、VBA対応もスコープに含める必要

## プロセス詳細

### 依頼プロセス
1. **Requirement準備**: 田村さんが英文依頼用のサマリーを作成
2. **CLV Management打診**: 増田さんがNeoに打診
3. **説明MTG**: CLVメンバーへの説明MTGを設定
4. **リソース確保**: CLV ManagementとのTouch pointで確認

### 説明MTGの必要性
- **理由**: CLVがEagle XのPricingツールを見たことがない
- **対応**: 大塚さんまたは田村さんから説明が必要
- **内容**: CLVメンバーにお願いしたいことを明確に伝達

## 実務ノウハウ

### リソース確保のポイント
1. **既存チャンネル活用**: Eagle Xチャンネルでの依頼により速やかにリソース確保
2. **説明の重要性**: CLVメンバーへの明確な説明が必要
3. **スキルセット確認**: VBA対応可能かどうかを確認

### 技術統合の検討
- **短期**: VBA対応もスコープに含めてCLVに打診
- **長期**: GAS統一またはVBA要員の別途確保を検討
- **判断基準**: CLVのリソースと能力で解消できない場合は別のリソース元を検討

## 担当者連携

### GHQ側
- **担当者**: 大塚さん、田村さん、増田さん、仲井さん
- **役割**: 依頼内容の明確化とCLV Managementへの打診

### CLV側
- **担当者**: Neo (Nam) Nguyen
- **役割**: リソース確保とメンバーアサイン

## 関連情報

### 参考資料
- MRG Tool prototype（TP trade Dry cargo用）
- Requirementサマリー（英文）
- CLVメンバープロファイル

## 次アクション
- [ ] Requirementサマリーの完成
- [ ] CLV Managementへの打診
- [ ] 説明MTGの設定
- [ ] VBA対応可能性の確認
- [ ] リソース確保の確認

