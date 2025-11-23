# Eagle X - FR503452 BUTIntl Post-Mortem - TCT Tenderプロセス改善ノウハウ

---
title: Eagle X - FR503452 BUTIntl Post-Mortem - TCT Tenderプロセス改善ノウハウ
tags: [eagle-x, tct, tender, post-mortem, process-improvement, pricing-tool]
created: 2025-11-22
---

## 概要
Eagle Xで処理した初めてのTCT（Trade Commercial Team）テンダー（FR503452 BUTIntl）のポストモーテム分析とプロセス改善ノウハウ。テンダー処理の遅延要因、Pricing Toolの使いやすさ、改善提案をまとめた。

## テンダー概要

### 基本情報
- **テンダー番号**: FR503452 BUTIntl
- **テンダータイプ**: TCT（Trade Commercial Team）
- **リリース日**: 2023年12月18日
- **内部締切**: 2023年12月22日
- **処理方法**: Eagle X Pricing Toolを使用

### タイムラインの課題
- **リリースから締切まで**: 4日間（12月18日〜12月22日）
- **時期の問題**: クリスマス前の忙しい週
- **12月22日**: EUAでは半日のみの営業日

## プロセス上の課題と改善提案

### 1. コミュニケーションの課題

#### 課題
- **PricerとOMMCの誤解**: PricerとOMMCの間でマンデート/サーチャージ条件について誤解が発生
- **結果**: OMMCがEagle X Pricing Tool入力をやり直す必要があった

#### 改善提案
- **事前の明確化**: マンデート/サーチャージ条件を事前に明確に共有
- **確認プロセス**: Pricing Tool入力前に、PricerとOMMCで条件を確認

### 2. Pricing Toolの使いやすさ

#### 課題
- **不慣れなPricer**: Pricing Toolに不慣れなPricerが、OMMC入力をレビューするのに時間がかかった
- **レビュー時間**: 慣れていないため、レビューに時間がかかった

#### 改善提案
- **チェック項目の明確化**: OMMCがPricerに、どの列をチェックすべきか（O/F、OBS、THC等）をガイド
- **特に学習期間中**: Eagle Xツールをまだ学習中の間は、このガイドが特に重要

### 3. TT/Routing入力の混乱

#### 課題
- **ルーティング詳細の生成**: Eagle Xテンダーでは、ルーティング詳細はEagle X Pricing Toolによって生成される（OMMC for TCTテンダー）
- **条件**: TT Toolで利用可能な限り
- **混乱**: この点について混乱が発生

#### 改善提案
- **明確な説明**: Eagle Xテンダーでは、ルーティング詳細は自動生成されることを明確に説明
- **TT Toolの確認**: TT Toolで利用可能かどうかを事前に確認

### 4. レートの差異

#### 課題
- **レートの差異**: Eagle X Pricing Toolで生成されたレートが、Pricerマンデートより約$3高かった
- **原因の可能性**: 一部サーチャージのROE（Rate of Exchange）に関連している可能性

#### 改善提案
- **GHQ Eagle X teamのレビュー**: GHQ Eagle X teamがレビューを実施
- **ROEの確認**: サーチャージのROEを確認し、必要に応じて修正

### 5. エクスポート/提出プロセスの課題

#### 課題
- **不慣れなPricer**: Pricing Toolに不慣れなPricerが、レートファイルのエクスポート/提出に時間がかかった
- **結果**: CSTが顧客フォーマットに変換するプロセスが遅延

#### 改善提案
- **エクスポート手順の明確化**: レートファイルのエクスポート/提出手順を明確に説明
- **トレーニング**: Pricing Toolの使用方法に関するトレーニングを実施

## 改善提案の詳細

### 1. 内部締切の1日前に入力を依頼

#### 提案内容
- **タイミング**: OMMCから入力を内部締切の1日前に依頼
- **目的**: PricerがOMMC入力を適切にチェックする時間を確保
- **効果**: Pricing Toolに慣れながら、適切なレビューを実施

#### 実現可能性
- **検討が必要**: 実現可能性を検討する必要がある
- **OMMCのガイド**: OMMCがPricerに、どの列をチェックすべきかをガイド

### 2. Pricing Toolの使いやすさの向上

#### 数値の大きさ
- **課題**: Pricing Toolの数値が小さく、読みにくい
- **改善提案**: 数値を大きくする（ズームインしても小さく見える場合）
- **注意**: Pricing ToolはExcelファイルなので、ファイル内でズームイン可能

#### 誤ったプライシングの防止
- **目的**: 誤ったプライシングを防止
- **改善提案**: 数値を大きくし、読みやすくする

### 3. サポート体制の活用

#### GHQ Eagle Xサポートチーム
- **連絡先**: GHQ EAGLEX PRICING SUPPORT (ghq.eaglex.pricing.support@one-line.com)
- **ポータル**: https://sites.google.com/one-line.com/eaglex/contact-us?authuser=0
- **連絡方法**: チャットまたはVCが最速（EUA Pricersの経験に基づく）

#### 活用の推奨
- **質問がある場合**: 迅速にサポートチームに連絡
- **問題解決**: 問題が発生した場合は、すぐにサポートを依頼

## 実務上の注意点

### テンダー処理の効率化
- **事前準備**: マンデート/サーチャージ条件を事前に明確に共有
- **確認プロセス**: Pricing Tool入力前に、PricerとOMMCで条件を確認
- **ガイドの提供**: OMMCがPricerに、どの列をチェックすべきかをガイド

### Pricing Toolの使いやすさ
- **トレーニング**: Pricing Toolの使用方法に関するトレーニングを実施
- **サポート体制**: サポートチームを積極的に活用
- **改善提案**: 使いやすさに関する改善提案を継続的に実施

### プロセスの継続的改善
- **ポストモーテム**: 各テンダー処理後にポストモーテムを実施
- **改善提案**: 改善提案を継続的に実施
- **フィードバック**: PricerやOMMCからのフィードバックを収集

## 関連ノート
- [[20250113_Eagle-X-Target-Candidates-January-FY24-事前通知ノウハウ]]
- [[20250113_Eagle-X-training-preparation-LATAM-トレーニング準備ノウハウ]]
- [[20250113_Eagle-X-EUA-Touchpoint-Follow-Up-トレーニング計画ノウハウ]]

## 次アクション
- [ ] 内部締切の1日前に入力を依頼するプロセスの実現可能性を検討
- [ ] Pricing Toolの数値を大きくする改善を実施
- [ ] サポート体制の活用を促進

#inbox #eagle-x #tct #tender #post-mortem #process-improvement #pricing-tool

