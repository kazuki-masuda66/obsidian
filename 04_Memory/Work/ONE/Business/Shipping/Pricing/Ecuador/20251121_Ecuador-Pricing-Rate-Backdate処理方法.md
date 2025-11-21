# Ecuador Pricing - Rate Backdate処理方法

## 概要
Ecuador PricingにおけるRate Backdate（レートの遡及適用）の処理方法、判断基準、実際のケーススタディをまとめました。

## 内容

### Rate Backdateとは
- **Rate Backdate**: 過去のbookingに適用するレートの遡及適用
- **目的**: Rollされたbookingに対する補償的なレート設定
- **使用場面**: 
  - コンテナが繰り返しRollされた場合
  - 顧客が先行予約（bookings placed in advance）をしたが、レートが期待したレベルに達しなかった場合
  - 商業的な配慮（commercial gesture）が必要な場合

### Rate Backdate処理の基本フロー

#### 1. Rate Backdateリクエストの受信
- **Maria Esther Parrales** (`maria.parrales@one-line.com`): Sales、MAVIJU担当、Rate Backdate
- **Erick Guerrero** (`erick.guerrero@one-line.com`): Sales、MAVIJU担当
- **Adriana Naula** (`adriana.naula@one-line.com`): Sales、STARCARGO担当、例外レート

#### 2. リクエスト内容の確認
- **対象booking**: どのbookingに適用するか
- **適用期間**: いつからいつまでのレートを適用するか
- **理由**: なぜRate Backdateが必要か（Rollされた、先行予約など）
- **要求レート**: どのレートを適用するか
- **数量**: 何コンテナに適用するか

#### 3. 判断基準

**承認するケース**:
- コンテナが繰り返しRollされた場合（ONEの責任）
- 顧客が先行予約（bookings placed in advance）をしたが、レートが期待したレベルに達しなかった場合
- 商業的な配慮（commercial gesture）が必要な場合
- 重要な顧客（Tier 1、Tier 2）の場合
- 明確な理由があり、顧客のミスではない場合

**却下するケース**:
- 顧客の計画ミスが原因の場合
- 根拠が不十分な場合
- 既に適切なレートを提供した場合

#### 4. 承認・却下の判断
- **Kazuki Masuda**: 最終判断者
- **Adele Chia**: 判断者
- **Soon Ang Chong**: 判断者
- 判断後、エクアドルチームに返答

### Rate Backdate処理の実際のケース

#### ケース1: MAVIJU S.A. - Rate Backdateリクエスト
**状況**:
- **BCO**: MAVIJU
- **B/L**: TAOFJ0701800
- **Vessel**: ORIT2543E
- **数量**: 22x40NORコンテナ
- **問題**: コンテナが繰り返しRollされた
- **要求**: 9月20日〜10月14日のレートを遡及適用

**要求内容**:
- **元の要求レート**: 9月20日〜10月14日に適用される予定だったレート
- **提案レート**: USD 1,100/40NOR（Qingdao to ECGYE）
- **適用期間**: 9月20日〜10月14日
- **数量**: 22x40NORコンテナ

**判断プロセス**:
1. **リクエスト**: 22x40NORコンテナに対してRate Backdateを要求
2. **確認事項**:
   - 10月に提供したレートオファーの確認
   - OPUS release historyのスクリーンショット
   - 内部コミュニケーションの証拠
   - Rollされた理由の確認
3. **承認条件**: 
   - 10月に提供したレートオファーの確認
   - OPUS release historyのスクリーンショット
   - 内部コミュニケーションの証拠
4. **承認**: 条件が満たされた場合、Rate Backdateを承認

**ポイント**:
- コンテナが繰り返しRollされた場合、ONEの責任として補償を検討
- Tier 2顧客として、商業的な配慮を検討
- 明確な証拠が必要

#### ケース2: STARCARGO - IMPORTADORA ALVARADO - 例外レート
**状況**:
- **顧客**: IMPORTADORA ALVARADO VASCONEZ CIA. LTDA.
- **経由**: STARCARGO
- **特徴**: STARCARGOの最大顧客、390 TEU（YTD 2025）
- **問題**: 先行予約（bookings placed in advance）をしたが、レートが期待したレベルに達しなかった
- **要求**: 特定のbookingに例外レートを適用

**要求内容**:
- **SHAFW3674700**: CNSHA 1xR5 USD 1,000
- **TPEF74167800 / TPEF74168900**: TWTXG + TWKHH 4 x R5 + 3 x R5 USD 1,000
- **BKKFZ2609700**: THBKK 2 x R5 USD 1,350
- **PKGF67203800**: MYPKG 2 x R5 USD 1,250

**判断プロセス**:
1. **リクエスト**: 特定のbookingに例外レートを適用することを要求
2. **理由**: 先行予約をしたが、レートが期待したレベルに達しなかった
3. **実績**: 390 TEU（YTD 2025）、STARCARGO経由でONEに372 TEU
4. **承認**: 商業的な配慮（commercial gesture）として、一度限り（once off）で承認

**ポイント**:
- 先行予約をしたが、レートが期待したレベルに達しなかった場合、商業的な配慮を検討
- 重要な顧客（STARCARGOの最大顧客）として、例外レートを承認
- 一度限り（once off）として承認

### Rate Backdate処理の注意点

#### 1. 証拠の確認
- 10月に提供したレートオファーの確認
- OPUS release historyのスクリーンショット
- 内部コミュニケーションの証拠
- Rollされた理由の確認

#### 2. 顧客の実績を確認
- 年間を通じて良好な実績がある場合は、商業的な配慮を検討
- 重要な顧客（Tier 1、Tier 2）の場合は、優先的に対応

#### 3. 商業的な配慮
- 重要な顧客の場合は、商業的な配慮を検討
- ただし、根拠が明確であることが前提
- 一度限り（once off）として承認する場合がある

#### 4. エクアドル特有のケース
- **Rollされたbooking**: ONEの責任として補償を検討
- **先行予約**: レートが期待したレベルに達しなかった場合、商業的な配慮を検討
- **例外レート**: 特定のbookingにのみ適用する例外レート

### Rate Backdate処理のベストプラクティス

#### 1. 迅速な対応
- Rate Backdateリクエストは迅速に対応
- 顧客の信頼を維持するため、遅延を避ける

#### 2. 明確な説明
- 承認・却下の理由を明確に説明
- 証拠が不十分な場合は、追加の情報を要求

#### 3. 記録の保持
- Rate Backdate処理の記録を保持
- 将来の判断の参考にする

#### 4. 顧客との関係維持
- 重要な顧客とは良好な関係を維持
- 商業的な配慮と厳格な判断のバランスを取る

#### 5. 一度限り（once off）の原則
- 例外レートは一度限り（once off）として承認
- 継続的な例外レートは避ける

## 次アクション
- [ ] [[20251121_Ecuador-Pricing-基本ルールとTigerシステム]]にリンク
- [ ] [[20251121_Ecuador-Pricing-主要顧客別ルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#ecuador #pricing #rate-backdate #exception-rate #commercial-gesture #roll #inbox

