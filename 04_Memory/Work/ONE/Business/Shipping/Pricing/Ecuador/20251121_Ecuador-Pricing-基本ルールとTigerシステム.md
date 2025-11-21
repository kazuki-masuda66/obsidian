# Ecuador-Pricing-基本ルールとTigerシステム

## 概要
Ecuadorのプライシング業務における基本ルールとTigerシステムの使用方法、レート設定の実例をまとめたノート。

## 内容

### Tigerシステムの基本フロー
- **Rate Amendment Request**: Tigerシステムを通じてレート修正リクエストが送信される
- **承認フロー**: `ghq.lawc.mktg@one-line.com` に必ずCCを入れる
- **レスポンス時間**: 7日以内にnominationがない場合、レートは無効になる

### レート設定の実例

#### Asia → Guayaquil (ECGYE)
- **CNWUH-ECGYE**: USD 1,650/40NOR (USD 450 barge cost from CNWUH to CNSHA), 後にUSD 1,450/40NORに調整
- **CNXIL-ECGYE**: Base port rate + USD 250 add-on
- **CNSWA-ECGYE**: Base port rate + USD 400 add-on
- **CNTAO-ECGYE**: NOR rate requests

#### India → Guayaquil
- **MUNDRA/NHAVA SHEVA-ECGYE**: USD 4,500/40RH (Reefer, 2x40'REEFER per month, validity until Dec 31, 2025, 10 days free detention at destination)

#### Rate Backdateの実例
- **MAVIJU**: 22 units of 40NOR containers rolled since October, USD 1,100/40NOR rate backdate request (validity: 31 October - 14 November 2025)
- **Booking確認日**: October 31st
- **Vessel**: ORIT2543E

### NORレートの詳細
- **BP定義**: Base port rate + barge cost
- **CNWUH-ECGYE**: USD 1,650/40NOR (USD 450 barge cost), 後にUSD 1,450/40NORに調整
- **CNXIL-ECGYE**: Base port rate + USD 250
- **CNSWA-ECGYE**: Base port rate + USD 400
- **レート有効期限**: 7日以内nomination、Validity: 11-14 November 2025

### レート有効期限のルール
- **7日ルール**: 7日以内にnominationがない場合、レートは無効になる
- **Validity例**: 11-14 November 2025

### 特殊条件の実例

#### FARLETZA
- **AHA (Adjusted Handling Allowance)**: Special conditions
- **DOF (Destination Origin Fee)**: Special conditions
- **Tier 2 rate**: USD 100 on top of tier 1 for tier 2

#### PLUSCARGO
- **AHA Fixed USD 50**: Local concession
- **OFT計算**: AHA is 112 - 50 = 62, If OFT is 1350 - 62 = 1288

## 次アクション
- [ ] 04_Memory/Work/ONE/Pricing/Ecuador/に移動を検討
- [ ] 他のラテンアメリカ諸国との比較分析

#inbox #ecuador #pricing #tiger-system #rate-setting