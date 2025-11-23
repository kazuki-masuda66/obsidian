---
title: OPUS SPC Space Monitor - Bottleneck Check ガイド
tags: [opus, spc, space-control, bottleneck-check, system-guide, allocation]
created: 2025-11-22
source: 00_Memo/Space monitor.pdf
version: 3.0 (2 July 2025)
---

# OPUS SPC Space Monitor - Bottleneck Check ガイド

## 📚 概要

OPUS SPC（Space Control）システムにおけるスペース状況の監視方法、特にBottleneck Check機能の使用方法を説明するガイド（31ページ）。

**バージョン管理**:
- Version 01: 26 Feb 2017 - Shum Qin Ying
- Version 02: 6 June 2025 - DYM SPC（機能強化へのリンク追加）
- Version 03: 2 July 2025 - DYM SPC（Trade別照会、Sub Office別照会追加、Picked Teu/Gate-In Teu機能強化へのリンク追加）

## 🎯 Bottleneck Check の目的

### 目標
- **TEUと重量**による港別のボトルネックチェックを実行
- リアルタイムのブッキング情報を参照（積載量、船内残量、荷降ろし量など）

### 手順
1. **Bottleneck Check機能を使用**
   - 特定の港での吃水制限（structured BSA）については、Global Network Planning/Global Liner Operationsから情報が提供され、データ入力はマニラにオフショア

### アクセスパス
```
Sales Management > Space Control > Allocation Control > Control by HO
```

## 📋 Bottleneck Check の基本操作

### 1. 機能へのアクセス
- **画面**: Control by HO画面でBottleneck Check機能にアクセス可能
- **同じ画面**: RHQスペースコントローラーがMain Officeにスペースを割り当てる画面と同じ

### 2. VVD情報の選択
- **選択されたVVD情報**: 選択されたVVDにリンクされた前後の航海が表示される
- **Prior VVD**: 選択されたVVDの目的地港で荷降ろしされる貨物量を運ぶ航海
- **Post VVD**: 選択されたVVDの積出港で積載され、Post VVDで荷降ろしされる貨物量

### 3. TEU/重量タブの選択
- **By TEUタブ**: TEUベースで情報を表示
- **By Weightタブ**: 重量ベースで情報を表示
  - 総重量（貨物重量 + タラ重量）に基づいてボトルネックチェック情報を表示
- **デフォルト**: "Forecast + BKG"オプションが設定されている

### 4. ラジオボタンオプション

#### Forecast + BKG（デフォルト）
- **動作**: 動的にForecastまたはリアルタイムブッキング情報に基づいて表示
- **ルール**: 
  - VVDが港を出発した場合 → その港にはブッキング数値を使用
  - VVDが港を出発していない場合 → その港にはForecast数値を使用

#### BKG
- **動作**: VVDが港を出発したかどうかに関わらず、選択された場合、ブッキング数値のみを使用

#### Alloc + BKG
- **動作**: 動的にAllocationまたはリアルタイムブッキング情報に基づいて表示
- **ルール**:
  - VVDが港を出発した場合 → その港にはブッキング数値を使用
  - VVDが港を出発していない場合 → その港にはスペース割り当て数値を使用

#### Alloc
- **動作**: VVDが港を出発したかどうかに関わらず、選択された場合、スペース割り当て数値のみを使用

## 🚢 船舶スケジュール情報の表示

### 港の表示
- **最新の船舶スケジュール情報**: 選択されたVVDとPost VVD航海の港の回転が表示される
- **フォントカラー**:
  - **BLACK**: 船舶がまだ港を出発していない場合
  - **BLUE**: 船舶が港を出発した場合
- **特別な港**:
  - **Ad-hoc port call**: 表示される
  - **Skipped port**: 表示されない

### BSA割り当て
- **デフォルト**: 同じVVDの下のすべての港は同じBSA割り当てを持つ

## 📊 貨物量情報の表示

### 主要な指標

#### Load（積載量）
- その港で積載される貨物量

#### Discharge（荷降ろし量）
- その港で荷降ろしされる貨物量

#### Onboard（船内量）
- その港での船舶上の総貨物量
- **計算式**: 前の港からのOnboard数量 + Load数量 - 前の港からのDischarge数量

#### Loadable（積載可能量）
- その港で貨物を積載するための残りスペース
- **計算式**: BSA割り当て - Onboard数量

### 貨物分類
- **OCN**: Ocean（外航）
- **IPC**: Interport（港間）
- **TS**: Transshipment（積替え）
- **MT**: Empty bookings（空コンテナブッキング）

### 計算例

#### OCN貨物の例
- **状況**: Load数量とOnboard数量が同じ → すべてのOCN貨物が前の港で荷降ろしされた
- **例**: NTIA-0021-W（過去の航海）
  - Total Onboard: 158 TEU
  - Discharge at JPUKB01: 0 TEU
  - Loadable = BSA - 158 TEU - 0 TEU = 1,669 TEU

#### IPC貨物の例
- **状況**: Load数量もOnboard数量と同じ → すべてのIPC貨物が前の港で荷降ろしされた
- **注意**: システムは各IOC（Interport Origin Code）を個別に管理してLoadable数量を計算
- **例**: 
  - Total Onboard: 200 TEU
  - Discharge at JPUKB01: 0 TEU
  - Loadable = BSA - 200 TEU - 0 TEU = 1,627 TEU

#### TS貨物の例
- **状況**: JPUKB01でTS分類の積載がない場合、Loadable数量はBSA割り当てと同じ（1,827 TEU）

#### MT（空コンテナ）の例
- **状況**: NTIA-0020-Eの最後の港HKHKG出発時に400 TEUの空ブッキング量
- **結果**: JPUKB01到着時に初期の船内空ブッキングが400 TEU
- **追加**: JPUKB01で416 TEUの空コンテナを積載予定
- **計算**:
  - Total Onboard = 400 TEU + 416 TEU = 816 TEU
  - Loadable = BSA - 816 TEU - 0 TEU = 1,011 TEU

#### 合計残り積載可能量
- **計算**: OCN/IPC/TS/MTのすべての貨物情報を使用して計算
- **例**: JPUKB01
  - OCN/IPC/TS/MTで積載予定の合計貨物量: 714 TEU
  - 前の港からの貨物を含む船内貨物量: 1,174 TEU
  - **残りスペース**: BSA - Onboard - Discharge = 1,827 TEU - 1,174 TEU - 0 TEU = 653 TEU

## 🔍 実例: NVEA-0043-W/E

### 前提条件
- **現在のシステム日付**: 2015年5月20日
- **船舶状況**: SGSINを出発し、SAJEDに向かっている

### 最新情報
- **Forecast**: 488 TEU
- **Allocation**: 400 TEU
- **Booking**: 376 TEU

### Forecast + BKGオプションの動作
- **JPTYO01**: 船舶が出発済み → ブッキング数量376 TEUを表示し、Loadable数量の計算に使用
- **NLRTM01**: 船舶が未出発 → Forecast数量288 TEUを表示し、Loadable数量の計算に使用

### BKGオプションの動作
- **NLRTM01**: 船舶が未出発でも、最新のブッキング数量250 TEUを表示し、Loadable数量の計算に使用

### Alloc + BKGオプションの動作
- **NLRTM01**: 船舶が未出発 → Allocation数量360 TEUを表示し、Loadable数量の計算に使用
- **JPTYO01**: 船舶が出発済み → ブッキング数量376 TEUを表示し、Loadable数量の計算に使用

### Allocオプションの動作
- **JPTYO01**: 船舶が出発済みでも、スペース割り当て数量400 TEUを使用してLoadable数量を計算
- **NLRTM01**: 船舶が未出発 → スペース割り当て数量360 TEUを使用してLoadable数量を計算

## 🔎 その他の照会機能

### 2. Inquiry by Trade（Trade別照会）
**アクセスパス**:
```
Sales Management > Space Control > Allocation Status > Inquiry by Trade
```

### 3. Inquiry by Sub Office（Sub Office別照会）
**アクセスパス**:
```
Sales Management > Space Control > Allocation Status > Inquiry by Sub Office
```

## 🆕 機能強化

### Control by HO / Bottleneck Check の機能強化

1. **Control by HO の機能強化とMT bundle FR count の考慮** (2023.10.17)
   - [リンク]

2. **Control by HO Excel Upload Function** (2024.02.27)
   - [リンク]

3. **Bottleneck Check と Control by HO に Broken Route Checkbox を追加** (2024.11.19)
   - [リンク]

4. **Bottleneck Check でVVDのみの入力を許可** (2025.02.25)
   - [リンク]

5. **Control by HO に Picked Booking Teu/Tons と Gate-In Teu/Tons を追加** (2025.07.01)
   - [リンク]

## 📝 重要なポイント

### 計算ロジック
- **Onboard数量**: 前の港からのOnboard数量 + Load数量 - 前の港からのDischarge数量
- **Loadable数量**: BSA割り当て - Onboard数量
- **総残りスペース**: BSA - Onboard - Discharge

### 表示のタイミング
- **Forecast + BKG**: 船舶の出発状況に応じて動的にForecastまたはBookingを表示
- **BKG**: 常にBookingを表示
- **Alloc + BKG**: 船舶の出発状況に応じて動的にAllocationまたはBookingを表示
- **Alloc**: 常にAllocationを表示

### フォントカラーの意味
- **BLACK**: 船舶がまだ港を出発していない
- **BLUE**: 船舶が港を出発した

## 🔗 関連リンク

- [[OPUS-SPC-Standby-SOP-標準作業手順書]]
- [[Eagle-X-Calculation-Logic-Formula-計算ロジックノウハウ]]
- [[Space-Control-Allocation-Management]]
- [[Vessel-Schedule-Management]]

## 📝 備考

- このガイドはOPUS SPCシステムのBottleneck Check機能の詳細な使用方法を提供
- スペースコントローラーや営業担当者がスペース状況を監視する際の重要なリファレンス
- 定期的に更新される機能強化情報も含まれる

