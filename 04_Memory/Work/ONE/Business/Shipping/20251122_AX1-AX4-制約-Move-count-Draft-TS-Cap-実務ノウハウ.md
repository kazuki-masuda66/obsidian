---
title: AX1-AX4 制約 - Move count/Draft/TS Cap 実務ノウハウ
tags: [space-control, ax1, ax2, ax3, ax4, move-count, draft-limitation, transshipment-cap]
created: 2025-11-22
---

# AX1-AX4 制約 - Move count/Draft/TS Cap 実務ノウハウ

## 概要
LAWC（Latin America West Coast）ループにおけるAX1/AX2/AX3/AX4の各種制約。Move count制限、Draft制限、Transshipment Capの詳細と実務対応方法。

## AX1: Move count Limitation for CLIQQ

### 制約内容
- **揚げ地Move count制限**: 250unitがMaxload
- **積地側での制限**: 250unitを超えないよう、積地側でも制限を設定
  - KR: 50 units
  - JP: 75 units
  - CPRC+NPRC: 50 units
  - XMN: 25 units
  - OTHERS: 50 units

### 実務対応
- **Bookingリリース判断**: APがあってもBookingがリリースされない場合、基本的に250unitに達していないためリリース可能と伝える
- **確認方法**: IQQ MovecountはLookerで定期的に配信される

### 制約の背景
- **歴史的経緯**: 昔に決められた制約
- **根拠**: ターミナルのProductivityに起因
- **計算方法**: 
  - 各港のBerth Windowに基づく停泊可能時間
  - 1時間あたりのProductivity（例: 100unit/時間）
  - 8時間停泊の場合: 800unitが丸船での最大荷役数量
  - 各OperatorのBSAで按分
  - その後輸出入で分割（通常50:50）

### 超過時の対応
- **LA輸入250 Units超過時**: 現地側へ連絡
- **理由**: 超過分により、LA輸出側が通常よりも積載できなくなるため

## AX2: Allocation for CSE cargo

### 制約内容
- **CSE（Caribbean Sea）向け貨物のALC**: 150TEU程度

### 背景
- **EC1の変更**: PAMITへ寄港しなくなった
- **代替ルート**: AX-2のPAROD経由でAL5（Trans Atlanticサービス）を使用
- **目的地**: DOCAU（DP world Caucedo@Dominican Republic）

## AX2: Draft Limitation at COBUN

### 制約内容
- **Non ONE vessels**: 問題なし
- **ONE vessels（大型船）**: 注視が必要
  - **Small vessel**: 28,327MT
  - **Big vessel**: 35,827MT

### 実務対応
- **大型船時**: 通常よりもBSAが大きいため、Draft制限に注意が必要

## AX3: Draft Limitation at GTPRQ

### 制約内容
- **港**: GTPRQ（PUERTO QUETZAL@GUATEMALA）
- **Draft Limitation**: 17,000MT at 11.8m

### 寄港順と重複港
- **寄港順**: MX-GT-CO-PE
- **重複港**: MXZLO/MXZLC/PECLLがAX1-AX3と重複

### 実務対応
- **GT前のMX貨物シフト**: 意味がない（GT寄港時に制限を下回る必要があるため）
- **AX1への貨物シフト**: GT以降で且つAX1と重複するPECLL向けの貨物をシフト

## AX4: Minimum Target for MXZLO

### 制約内容
- **必達数量**: 500-600TEUs
- **背景**: 当初ZLO寄港がなかったため、AdhocCall扱い
- **基準**: 500TEUを超えないと寄港のメリットがない

### Transshipment制限
- **T/S at MXZLO**: NOT accepted
- **受け入れ可能**: MXZLO CYもしくはMX Doorのみ

## AX4: Transshipment CAP at MXZLC

### 制約内容
- **トランシップ可能数量**: 500UNIT
- **カウント対象**: T/Sのみ（LZC CYもしくはMX Doorはカウントされない）

### Priority of T/S
**MARとMX2サービスのみがMXZLC経由で接続可能**

1. **SVAQJ**: MX2経由のみ輸送可能
2. **GTPRQ**: MAR経由のみ輸送可能
3. **NICIO + CRCAL**: 
   - MAR経由でサービス提供
   - 現在はMX3ルートのCOBUN経由で輸送中
   - AX4にスペース余裕があり、MX3が満載の場合、AX4経由MARでの輸送を検討

## 実務ノウハウ

### Move count制限の確認方法
- **Looker**: IQQ Movecountを定期的に確認
- **判断基準**: 250unitに達していない場合、Bookingリリース可能

### Draft制限の確認タイミング
- **AX2**: ONE vessels（大型船）時のみ注視
- **AX3**: GT寄港前に必ず確認（17,000MT at 11.8m）

### Transshipment Capの管理
- **AX4**: MXZLCでのT/Sは500UNITまで
- **優先順位**: MAR/MX2サービスのみ
- **スペース管理**: AX4に余裕がある場合、MX3の満載状況を確認してシフト検討

## 関連リンク
- [[Space Control Workflow]]
- [[LAWC Route Management]]
- [[BSA Allocation Rules]]

## 次アクション
- [ ] 04_Memory/Work/ONE/Business/Shipping/Space-Control/に移動を検討
- [ ] 制約一覧の定期更新を検討

#inbox #space-control #ax1 #ax2 #ax3 #ax4 #constraints #operational-limitations

