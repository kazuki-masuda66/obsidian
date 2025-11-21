# Mexico Pricing - 特殊貨物とAP処理

## 概要
Mexico Pricingにおける特殊貨物（HAZ、OOG、Reefer、Flexibagなど）の対応方法、AP（Allocation Plan）の処理方法をまとめました。

## 内容

### 特殊貨物の対応

#### 1. HAZ（危険物）
**ケース**: HAZ IMP MAR // FCL 20 // FOB SHENZHEN/SHEKOU - ZLO // UN 1950/IMO 2
- **POL**: SHENZHEN/SHEKOU
- **POD**: Manzanillo
- **クラス**: UN 1950 CLASS（aerosols）
- **コンテナ**: 1X20GP
- **重量**: 9,808.5 kg
- **容積**: 27.35

**HAZサーチャージ**:
- **クラス2.1（UN 1950）**: USD 700/TEU
- **条件**: DG acceptance subject
- **実例**: 
  - POL: SHENZHEN/SHEKOU
  - POD: Manzanillo
  - UN 1950 CLASS（aerosols）
  - コンテナ: 1X20GP
  - 重量: 9,808.5 kg
  - 容積: 27.35

**注意点**:
- HAZ貨物は事前承認が必要
- UN番号とIMOクラスを確認
- DG acceptanceが必要

#### 2. OOG（Out of Gauge - 重量超過・寸法超過）
**ケース**: DACHSER // 45000068740 // ONE
- **POL**: CNNSA
- **POD**: MXZLO
- **コンテナ**: 40FR
- **寸法**: 350cm x 320cm x 260cm
- **重量**: 6,722 kg

**OOGレート**:
- CNNSA - MXZLO: USD 7,700/40FR (OWOH)
- **実例**: 
  - POL: CNNSA (Nansha)
  - POD: MXZLO (Manzanillo)
  - コンテナ: 40FR
  - 寸法: 350cm x 320cm x 260cm
  - 重量: 6,722 kg
  - レート有効期限: 7 days（nominationなしの場合null and void）

**OOG条件**:
- **Underdeck stowage**: 価格はUnderdeck stowageとして設定、vessel stabilityとspace availabilityに依存
- **On deck stowage**: vessel stabilityの問題やstowage制約がある場合、OOGはon deckに積載され、追加のTEU voidが発生。レートはslot killの変更に応じて修正が必要
- **Corner casting clearance**: ハンドリングのため、貨物はコンテナのcorner castingまでclearanceが必要
- **Lashing**: Shipperは適切なstuffingとlashingを確保し、貨物がsea worthyであることを確認
- **VO approval**: OOG applicationはVO（Vessel Operator）の承認が必要

**注意点**:
- OOG貨物はVOの承認が必要
- Underdeck stowageが基本だが、on deckになる場合もある
- LashingはShipperの責任

#### 3. Reefer（冷凍コンテナ）
**ケース**: OEC REEFER REQUEST || TIANJIN MXZLO
- **POL**: CNTXG（Tianjin）
- **POD**: MXZLO
- **コンテナ**: Reefer

**対応方法**:
- Reeferレートを設定
- 電源確保が必要
- 温度管理が必要

**注意点**:
- Reeferは通常のコンテナより高額
- 電源確保のため、スペース制限がある
- 温度管理が重要

#### 4. Flexibag（フレキシブルバッグ）
**ケース**: PR25-1835 / ONE
- **POL**: IDSUB（Surabaya）
- **POD**: MXZLO
- **コンテナ**: 1x20' flexibag GP
- **特徴**: FlexibagはsupplierがSurabayaで購入・設置

**Flexibag Add-on**:
- **Base**: IDSUB-MXZLO FAK MRG
- **Add-on**: USD 100/unit on top of FAK for flexitank

**注意点**:
- Flexibagは特別なadd-onが必要
- Supplierが設置する場合もある

### AP (Allocation Plan) 処理

#### APとは
- **Allocation Plan**: 船腹配分計画
- **目的**: 各オフィスへの船腹配分を決定
- **期間**: 月次（例: December Week 49-01）

#### AP処理のフロー

**1. AP Inputの準備**
- **配布**: Marketingから各オフィスに配布
- **期間**: 8th November 2025 - MKTG to distribution to origins for input
- **フォーマット**: Google Sheets（共有ドライブ）

**2. AP Inputの提出**
- **期限**: 13th November 2025 - Sales to return AP Submission
- **確認**: PIC Check columnに"Done"を記入
- **完了**: "Complete"チェックボックスをチェック

**3. AP最終化**
- **期限**: 17th November 2025 - MKTG to finalize the AP and distribute to all offices
- **変更不可**: AP配布後は変更不可

#### AP処理のポイント

**ボリュームの調整**:
- 顧客の需要増加に対応
- 例: December APでボリューム調整

**サービス別の配分**:
- **AX1**: MONTEVIDEO EXPRESS
- **AX2**: ONE SPIRIT
- **AX3**: SEASPAN BRAVO
- **AX4**: HYUNDAI PREMIUM

**BSA (Basic Space Allocation)**:
- DecemberのBSAは船のサイズに応じて配分
- 大型船の到着により配分が増加する可能性

**Loading Office変更**:
- **例**: OEC FREIGHT, S. DE R.L. DE C.V.
  - 削除: CN SHABB AX1E（10.00 TEU）
  - 追加: CN NBOBB AX1E（8.00 TEU）
  - RFA: TMEXN00831A
- **条件**: AP最終化後は例外として変更可能な場合がある

**APボリューム調整**:
- **合意ボリューム**: 500TEU（CGM meetingで合意）
- **実例**: December Week 49-01 AP
  - 515 TEU提出 → 500TEUに調整要求
  - 8 TEU超過分を削除

#### AP処理の注意点

**1. 期限厳守**
- AP Inputの提出期限を厳守
- 遅延は全体のスケジュールに影響

**2. 正確な情報**
- ボリューム、サービス、期間を正確に入力
- 誤りがあるとAP全体に影響

**3. 変更不可**
- AP配布後は変更不可
- 提出前に十分に確認

**4. 例外対応**
- Loading Office変更など、例外として変更可能な場合がある
- ただし、慎重に判断

#### AP処理の連携

**メキシコチーム**:
- **Josue Sanchez**: Commercial Steering Expert Analyst、AP処理
- **その他のメンバー**: AP Input対応

**シンガポールチーム**:
- **Boon Keng Lua**: AP配布・最終化
- **Soon Ang Chong**: AP確認

### 特殊貨物のベストプラクティス

#### 1. HAZ貨物
- UN番号とIMOクラスを確認
- HAZサーチャージを正確に設定
- DG acceptanceが必要

#### 2. OOG貨物
- VOの承認が必要
- Underdeck stowageが基本だが、on deckになる場合もある
- LashingはShipperの責任

#### 3. Reefer貨物
- 電源確保が必要
- 温度管理が重要
- スペース制限がある

#### 4. Flexibag
- 特別なadd-onが必要（USD 100/unit）
- Supplierが設置する場合もある

### AP処理のベストプラクティス

#### 1. 期限厳守
- AP Inputの提出期限を厳守
- 遅延は全体のスケジュールに影響

#### 2. 正確な情報
- ボリューム、サービス、期間を正確に入力
- Loading Office変更など、例外は慎重に判断

#### 3. 変更不可
- AP配布後は変更不可
- 提出前に十分に確認

#### 4. 例外対応
- Loading Office変更など、例外として変更可能な場合がある
- ただし、慎重に判断

## 次アクション
- [ ] [[20251121_Mexico-Pricing-基本ルールとTigerシステム]]にリンク
- [ ] [[20251121_Mexico-Pricing-主要顧客別ルール]]にリンク
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）

#mexico #pricing #haz #oog #reefer #flexibag #ap #allocation-plan #inbox

