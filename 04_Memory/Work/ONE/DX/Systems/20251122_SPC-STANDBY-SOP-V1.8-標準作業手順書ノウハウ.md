# SPC STANDBY SOP V1.8 - 標準作業手順書ノウハウ

---
title: SPC STANDBY SOP V1.8 - 標準作業手順書ノウハウ
tags: [opus, spc, standby, sop, booking, space-control, allocation]
created: 2025-11-22
---

## 概要
OPUS SPC/BKG "Standby" Functionに関する標準作業手順書（SOP）V1.8。Booking作成時の自動チェック、Standby Bookingプロセス、Final Guidance、Escalationプロセス、Master Constraint Tableの設定方法をまとめた。

## バージョン情報
- **バージョン**: V1.8
- **最終更新日**: 2025年5月27日
- **作成者**: Pamela Sevilla (GHQ DYM BPM)
- **連絡先**: pamela.sevilla@one-line.com / ghq.dym.bpm@one-line.com

## プロセス概要

### プロセス説明
Booking StaffがBookingを作成すると、システムが自動的にチェックを実行。Overall Trunk/POL/Feeder/Customer allocation、EQ、commodity restrictionsに関連する問題がある場合、Bookingは"Standby"Bookingとなり、Standby Bookingプロセスで処理される。制約がない場合、BKG staff（Off/On Shore）は即座に確認してリリースできる。

### プロセスフロー
On/Offshore booking staffがBookingを作成すると、システムはGHQ/RHQ trade teamsによって設定された制約/制限をチェック。制約/制限がない場合、Bookingは即座にFirmになる。Allocation/EQ/commodityに関連する制約/制限がある場合、Bookingは関係者にエスカレートされ、レビューと決定が行われる。

## ロールと責任

### Three Tiers of Business Roles
1. **Tier 1**: On/Off-shore CSVC manager
2. **Tier 2**: On-Shore CSVC manager and approvers
3. **Tier 3**: GHQ/RHQ Space Controllers

### Booking Escalation Process
BookingはTier 2（On-Shore CSVC Manager and approvers）にエスカレートされる。Tier 2はTier 1にガイダンスを返し、Tier 1はBookingをFirmまたはCancelできる。

### Standby Booking Roles設定
- **設定場所**: Booking/Documentation - Standby Booking Role Setup
- **設定者**: GHQ/RHQ/BKG office User IDs
- **例**: EA/SAでは3つのTierがあり、各Tierは異なるタイプのUser IDsを表す（On/Offshore Booking StaffからGHQ/RHQ Space Controllersまで）

## Process Steps

### 1.4.1 Space Control - Data Setup

#### 1.4.1.1 Standby Guidance Setup
Standby Guidanceの設定方法

#### 1.4.1.2 Standby Priority Setup Creation
Priority ruleの設定は重要。設定方法が異なると、Final Guidanceが異なる結果になる。SINHQのPriority rule setupは標準化され、全てのTradesに適用される（HKGHQとSINHQを含む）。

**Priority Rules**:
1. **Rule 1**: If EQ Restriction is GD1, Final guidance will be GD1
2. **Rule 2**: If EQ Restriction is GD6, Final guidance will be GD6
3. **Rule 3**: If EQ Restriction is GD4, Final guidance will be GD4（削除済み - SINHQはSequential Logicを使用）
4. **Rule 4 & 5**: If EQ Availability Master is GDN/GD1, Final guidance will be GD1
5. **Rule 6 & 7**: If EQ Availability Master is GD6/GD4, Final guidance will be GD6/GD4 respectively
6. **Rule 8**: If VIP is GD1, Final guidance will be GD1
7. **Rule 9**: If Loading/POL Customer is GDN, Final guidance will be GD1
8. **Rule 10**: If Trunk Customer is GDN, Final guidance will be GD1

**用語説明**:
- **Loading/POL Master** = Trunk-Loading Tab Constraint
- **Loading/POL Customer** = Customer Tab Constraint with Loading Port/POL set-ups
- **Trunk Master** = Trunk-Overall Tab Constraint
- **Trunk Customer** = Customer Tab Constraint with VVD allocation set-ups
- **Feeder Master** = Feeder Tab Constraint
- **Feeder Customer** = Customer Tab Constraint with Transhipment set-ups

#### 1.4.1.3 Sequential Validation
Sequential ValidationはMaster Constraint Table Tabsをdecision-tree flow chartのようにチェック。全ての制約を同時にチェックしてPriority Rule TableでFinal guidanceを決定する代わりに、Sequential Validationは次のTabに進む前にConstraint Tabをチェックし、複数の制約をFinal guidanceに考慮できる。

**チェック順序**:
1. Commodity Restriction（最初にチェック）
2. EQ restriction
3. EQ availability
4. Trunk-loading, Feeder and Trunk-overall（Master Tab and Customer Tab）

**有効化/無効化**:
- Standby Priority Setup Creation画面で有効化または無効化可能
- 有効化時: Standby Priority Set-up Creation Table、Sequential Validation Logic、Master Constraint TableのTrade Teams設定が連携してFinal Guidanceを導出
- 無効化時: Standby Priority Set-up Creation TableとMaster Constraint TableのTrade Teams設定のみでFinal Guidanceを導出

**使用リージョン**:
- SINHQとRICHQがSequential Validationを使用

#### 1.4.1.4 Standby Revalidation Logic
既にStandbyを通過してguidanceが与えられたBookingは、Hard Coding Setup Tableに基づいてシステムによって再検証される。Validationが"Y"の場合、Booking item（例: POR）の変更は再検証を引き起こさない。Validationが"N"の場合、フィールド（例: DEL）の変更はBookingの再検証を引き起こす。

**注意**: Group VVD/Port Assign UIを使用してBooking itemが更新された場合、再検証は機能しない。

#### 1.4.1.5 Booking Status Definition
Booking画面には、ステータスを表す2つのボックスがある。最初のボックスはBooking自体のステータスで、2番目のボックスはStandbyステータス。

**ステータス定義**:
- **F/blank**: BookingはStandbyによって検証されていない（Asiaでは、ユーザーがStandby Hardcoding tableに登録されていない場合、またはその他のシステムエラーによる場合）
- **F/F**: BookingはStandbyを通じてFirmになった
- **W/F**: Booking Waiting/Standby Approved
- **W/S**: Booking Waiting/in Standby
- **W/X**: Booking Waiting/Decline advised
- **X/X**: BookingはDeclineによりCancelled

**Standby時の抑制プロセス**:
- Trans Request Order on Booking Creation
- FAX/EDI on Booking Creation (Booking Receipt Notice, Draft BL etc.)
- Booking Receipt Notice (Fax/Email)
- Booking Receipt Notice (EDI)
- Booking EDI Transmit to Terminal
- Empty Container Release Order
- VGM Dashboard

#### 1.4.1.6 Master Constraint Table Creation
Master Constraint Tableにより、GHQ/RHQ trade teamsはTrunk-Overall、Trunk-Loading、Feeder、EQ、Commodity、Customerによるスペース割り当てと制約の全体的な管理が可能。GHQ/RHQ Trade teamsはMaster Constraint Tableで制約と顧客Account Planを更新できる。

**Trunk-Overall**:
- Trade TeamsはTradeレベルでTrunk vesselのthreshold %を設定可能
- **例**: FE2 WB Trunk vessel thresholdが85%に設定されている場合、実際のBooking volumeが85%を超えるとGD4がトリガーされる
- RemarksはStandby popup detail pageに表示される

**Trunk-Loading**:
- Trade TeamsはTrunk-Loading threshold %も設定可能
- **例**: FE2 WB、Loading office NBOBBがthreshold % 110%を超えると、GD4がトリガーされる
- RemarksはStandby popup detail pageに表示される
- Port pairsでTEU allocationとthreshold %によるAllocationも設定可能

**Customer (with <>7 or 10 days logic) in Asia**:
- Customer Account PlanはTrade TeamsがMaster Constraint Tableからダウンロード/アップロード可能
- 実際のBooking volumeが顧客allocationを超えるとGuidanceがトリガーされる
- Master Constraint Tableには10-day logicがあり、Bookingが最初のVVDのETAの10日前より前に作成された場合と、10日前より後に作成された場合でFinal Guidanceが異なる可能性がある（時間でカウント: 1st VVD ETA - 10*24 hours）

**10-day logic例**:
- Bookingが最初のVVDのETAの10日前より前に作成された場合: GD1
- 10日前より後に作成された場合: GD4

**Customer GD4 Hard coding for Asia**:
- Customer without allocation
- S/C or RFA info is not available in the Master Constraint Table
- Only apply to OCN bookings

**Weight Allocation**:
- TEUまたはTotal WGT allocationで設定可能
- Customer tabの下で、BookingあたりのAverage WGT MT/TEUも利用可能
- Tradesは"Add Tare Weight"ボックスをチェックすることで、WGT allocationにtare weightが含まれるかどうかを示すことも可能
- Tare weightは特定のContainer Type SizeのOPUS Master Dataから導出される

**Common constraint**:
- 一般的なコメント/guidanceが表示されるが、common guidanceはFinal Guidanceに影響しない

**Validation Error Pop-out Table**:
- ユーザーが"Upload Excel"ボタンを使用して制約をアップロードする場合、validation error tableがポップアウトし、エラーのフィールドと可能な理由を識別
- Validation Error Tableの行番号はExcelファイルの行番号に対応
- Excelファイルのエラーをクリアし、制約をMaster Constraint Tableに保存する前に再アップロードする必要がある

**Exact Match checkbox**:
- EQ Restriction、EQ Availability & Customer Tabsで利用可能
- 特定の制約が特定のコンテナタイプ/サイズに厳密に適用されるかどうかを指定し、mixed bookingsのリリースを許可しない
- **例**: RF flagとExact Match flagがチェックされた制約は、1xR5と10xD4のmixed bookingのリリースを許可しない

**Move Count Field**:
- Trunk-Loading、EQ Restriction & Customer Tabsで利用可能
- "Move Count"フィールドの下で制限を示すことで、move countsを制御するオプションを提供
- Move count logicはtotal teuではなく、total number of containersに基づく
- **例**: 2xD4のBookingは2 move countsに等しい。5 move countsの制限で制約が作成された場合、Bookingは制限内のためGDNとしてガイドされる

**% Threshold in Customer Tab**:
- Tradesが初期Account Plan番号を変更せずに、超過APの%をリリースすることを制御可能
- **例**: allocationが50 teusで% thresholdが200の場合、この制約の下でリリースできるtotal bookingsは100 teus

**Code Field in Feeder Tab**:
- ユーザーがFeeder tabで"PRE"を入力または選択してPre-feeder制約を設定、または"POST"でPost-feeder制約を設定可能
- Final guideはPriority approachに基づく: GD6> GD2> GD3> GD5> GD4> GD1/ GDN
- "PRE/POST"フィールドが空白の場合、PREまたはPOST Feederかどうかを決定するためにOpus logicに依存

**Utilization Calculation Pop-Out**:
- ユーザーが制約のutilizationをチェックし、必要に応じて更新された方向を提供したり、制約を調整したりすることを可能にする機能
- "Utilization"ボタンはCommodity、Common、VIP tabsを除く全てのtabsで利用可能
- このボタンを表示するには、まず"Select"ボタンをクリックする必要がある
- **例**: Utilization calculation pop-outはSEQ 8998908について14 teusを生成（以下のBookingsをキャプチャ）。VVDが利用可能な場合、Utilization/BKG VOLは自動的に計算される。利用できない場合、Sales/EQ Weekをpop-outに入力して計算をトリガーする必要がある

**Soft Warning Pop-Out**:
- ユーザーがblank Trade/T.Lane/Transshipment Laneで制約を作成し、各ラインがMCTに直接登録された場合（excel uploadの検証がない）に表示される
- これはsoft warningのみであるため、ユーザーはOKをクリックして進む場合、制約を保存できる

**Backend Archiving Logic**:
- MCT UIにパフォーマンスの問題があった（削除されていない制約が、VVDが長く航行しているため現在のStandby計算に使用されていなくても、Standby Live Databaseに保持されていた）
- パフォーマンスを改善するために、backend Archive flagまたはlogicが追加され、過去のデータが週次バッチを介してStandby History databaseに移動される

**Archive基準**:
- **Customer Tab**: 1 VVD入力の制約のみ、最後の更新日から4ヶ月後（制約の最後の更新日から4ヶ月後にのみアーカイブ）、BKG via WEQ、OTHERS、Blankを含む
- **EQ Availability Tab**: EQ Date/Full Cut Off Toの制約のみ、週次アーカイブバッチ中に"EQ Date/Full Cut Off To"が経過した場合にのみアーカイブ
- Standby judgement/validationはStandby Live Databaseのみを参照

**例**: FE2 serviceの202347について840 Archived制約が取得され、全ての制約に1 VVD入力があり、4ヶ月以上前に更新されていた

**Update in Standby Logic for SINHQ/HKGHQ/DXBHQ**:
- 以前、Standby judgementは全てのFirmとWaiting bookingsを考慮し、allocationと比較してfirm bookingsがない、または限られた数のfirm bookingsしかない場合でも、BookingsがGD4になる結果になった
- Standby logicが更新され、self booking plusのみを考慮するようになった:
  - Firmed Booking Status
  - GD1 bookings that are not firmed yet (status W/F) due to further checking required for OOG/DG or other hold status by offshore/onshore etc.
  - Other Standby Guide (e.g GD2/GD3/GD4/GD5) bookings that are currently in Waiting/Standby status (W/S) or W/Blank or W/E status, but already guided by onshore to Firm (only pending action to firm it)

**例**: APが設定される前に以下のBookingsが作成されたため、全てのBookingsがGD4になった。AP（12 teus）が設定されると、ユーザーは同時に全てのBookingsを再計算した。再計算後、以下のFinal guidanceを受信。複数のBookingsが再計算のために選択された場合、システムはBooking作成時間に応じてfirst-come-first-serve basisでガイドする。Booking SINE70452400は設定されたallocationが既に超過していたためGD4になった。次のBooking SINE70453500は残りのスペース内のためGD1になった

**Standby Booking Status Reportに追加されたフィールド**:
- BKG for Standby Judgement TEU/Box/TONS
- "Current TTL TEU Calculation"がクリックされた場合、以下のフィールドが表示される:
  - Current BKG for Standby Judgement TEU/Box/TONS
  - Current Standby Firm/Guided Firm TEU/Box/Tons
  - Current Standby Wait TEU/Box/TONS

**Spot/Non-Spot AP Constraint in Customer Tab**:
- SpotとNon-Spot AP制約がMCT Customer tabに追加され、ユーザーがSpot volumesからAP volumesを除外し、SpotとAPの間でBookingリリース判断を完全に分離可能
- SpotはSpot allocationの作成に使用され、Account Planの"Parent"シーケンスとして機能。Non-Spot APは"Customer"と同様に機能するが、Spot制約の"Child"であるため、最初にSpot制約を作成せずにNon-Spot AP制約を作成することは不可能
- Customer Tabには現在3つのタイプがある（Customer、Spot、Non-Spot AP）。Judgement PriorityはCustomer > Spot/Non-Spot AP。ただし、間違った結果を得ることを避けるために、Customer ConstraintまたはSpot/Non-Spot AP制約のいずれかのみを使用することが推奨される

**例**: 以下の制約がCustomer Tabで作成された。Booking SINE05512600はRFA No.が一致するためSEQ 7306068を参照した。Booking SINE05514800はRFA No. NBON00621AがNon-Spot AP制約の一部ではないためSEQ 7306067を参照した。Non-Spot AP volumeもSpot volumeから除外された

#### 1.4.1.7 Creation of Group RFAs
複数のSC/RFAsを単一のGRFAにグループ化可能。GRFAに設定されたAllocationは、グループ内の単一のSC/RFAsによって共有される。グループ化設定はTradeによって行われる。

#### 1.4.1.8 Standby Hardcoding Table for Pre/Post Feeder
OPUS Standby judgement logic for Feeder Tab制約はDominantまたはNon-Dominant legに基づく。Dominant legの場合、Feeder logicはpre feederに基づく。Non-Dominant legの場合、Feeder logicはpost feederに基づく。Feeder Tabの設定はOPUS Standbyのlogicと一致する必要があり、そうでない場合、制約はFeeder bookingsを制御するために機能しない。

ただし、Hard Coding Setup Tableを使用して、GHQ/RHQ、Trade、またはLaneベースでStandby Feeder logicを変更可能。

### 1.4.2 Booking/Documentation

#### 1.4.2.1 Standby Booking Status Report
Standby Booking Status Reportは、Final Guidanceが推奨されたことと、Bookingが承認または拒否されるかどうかを判断するためのその他のデータを全員に迅速に表示する。

全てのStandby bookingsはStandby Booking Status Reportで取得可能で、Standby reason、current Tier/Role、Directionが与えられる。Tier 2とTier 3ユーザーは、BookingがTier/Roleにエスカレートされたときに、BKG staffにguidance（Firm/Cancel/Direction/Firm as Rollpool/Comment）を送信可能。BKG staffはその後、Bookingを確認またはキャンセルできる。

**CM/Teu情報**:
- Standby Status: S、X、またはEが割り当てられたBookingsについて、CM/TeuとAve CM/Teu情報も利用可能
- これはBookingリリース時の意思決定を支援するために設計されている
- **CM/Teu (EPP-A or B)**: [Ocean Freight (OFT) + Surcharge (SUR) - Cost (EPP-A or B)]/Total Teu
- 約40-50%のBookingsは、contractに適用可能なレートがない、またはBookingが作成されたときのcontractのcontainer type sizeに適用可能なレートがないため、CM/Teu計算で"No Rate"になる
- このような場合、ユーザーは代わりにAve CM/Teu (EPP-A or B)を参照できる。Ave CM/TEUの計算は、PF First POL ETD dateの3ヶ月前のapplication datesを持つBookingsに基づく。Service Scope、Revenue Lane、SC/RFA番号を考慮。**例**: Standbyが検証されたとき、PF First POL ETDが21/Mar/2021の場合、Ave CM/TEUは20/Dec/2020から20/Mar/2021のapplication datesを持つBookingsに基づいて計算される

#### 1.4.2.2 Standby Booking Monitoring Report
Standby Booking Monitoring Reportでは、Trade/Dominant leg/Bound/VVD別にtotal booking volumeを取得可能で、全てのFirm/Waiting/Standby/Error bookingsを含む。

## Business Rules

### 2.2 Final Guidance, Escalation, Decision Making Authority

#### 2.2.1 Country with Off-shore Booking Team
1.4.1.1 Standby Guidance Setupを参照

#### 2.2.2 Country without Off-shore Booking Team
1.4.1.1 Standby Guidance Setupを参照

#### 2.2.3 Trade-specific booking release process

##### 2.2.3.1 AET
Account Plan内では、即座にリリース可能。

**Green customers**:
- APの120%(*)までリリースする裁量権を与える
- 10日カットオフを通過すると、これまでに蓄積された全てのGreen "standby" bookingをリリース
- Sales forecast(**)が後で来ると伝えている場合、最後の瞬間までスペースを予約する必要がある

**Non-Green customers**:
- beyond-AP部分については10日カットオフまで待つ必要がある
- 残りのスペースがある場合、Non-Green customer "Standby" bookingsのリリースを開始可能

**注**:
- *: Trade directionによって異なる
- **: Sales forecastは10日後にGreen customerスペースを保護するために非常に重要

## ONE Quote Standby Functions

### 3.1 ONE Quote Allocation Set-up

#### 3.1.1 BKG VIA field
Customer tabの下で、tradesは"BKG VIA"列で"WEQ"を選択することで、ONE Quote bookingsのallocationを設定可能。

#### 3.1.1.2 BKG VIA filter
簡単なアクセスのために、tradesはMaster Constraint TableでWEQ制約をチェックするために"BKG VIA"フィルターを利用可能。

#### 3.1.2 POR/POL/POD/DEL Allocation
ONE Quote allocationsはPOR/POL/POD/DELでも設定可能。

#### 3.1.3 ONE Quote Standby Guidance and VVD removal from Platform
3.1.1と3.1.2の下で設定されたallocationを超えるtotal bookingsがある場合、thresholdを超えるBookingsはGD6（拒否）になる（Tradeが特定のallocationをGD6として設定した場合）。

判断時にtotal bookingsがallocationを超える場合、VVDsもONE Quote platformから削除される（closed）。

**Scenario 1**: WEQ allocationsがGD6として設定されている場合

**Scenario 2**: WEQ allocationsがGD6として設定されている場合

#### 3.1.4 Premium Flag Field
Premium flag allocationはpremium flag fieldの下で設定可能。

**Scenario 1**: 全ての顧客（premium flagあり/なし）のTotal WEQ allocationが200teus。200teusを超えるthresholdに達すると、BookingsはGD6になる

**Scenario 2**: Non-premium customersのTotal WEQ allocationが50teus。全ての顧客（premium flagあり/なし）のTotal WEQ allocationが200teus。Non-premium customersのtotal bookingsが15teusのみの場合、premium customersは185teusまで積載可能

**Scenario 3**: Premium customersのTotal WEQ allocationが50teus。全ての顧客（premium flagあり/なし）のTotal WEQ allocationが100teus。Premium customersはエスカレーションのthresholdに達する前に50teusまで積載可能。Premium bookingsがnilの場合、non-premium customersの最大値は100teusまで

**Scenario 4**: ONE Quoteでpremium cargoのみが提供される場合、Scenario 1の設定で十分。すなわち、StandbyでPremium flag "blank"

## Supporting Information

### 4.1 System Manuals
- Notes by CLT
- How to Guide by NA
- ONE Quote Standby Set-up Guideline

### 4.2 Additional Documents

#### 4.2.1 Test Scenario (Asia)
- **Scenario 1**: Trunk Overall
- **Scenario 2**: Trunk Loading
- **Scenario 3**: Customer
- **Scenario 4**: Common
- **Scenario 5**: 10 Days Logic（サンプルBookingの作成日が最初のVVDのETAの10日前未満のため、Trunk-Overall、Trunk-Loading、Customerが全てallocation内であっても、10日機能の設定により、Final Guidanceは依然としてGD4（CSVC Managerにエスカレート）になる）

#### 4.2.2 Launch Status - Countries and Trades
Standby New Matrixを参照

#### 4.2.3 Asia Booking Process
**Booking Acceptance Priority Rules under Standby Function**

**Split/Combine/NROF bookings**:
- **Booking Split**: 元のBookingが既にFirmまたはblankの場合、Standby logicは実行されない。ただし、元のBookingがStandbyステータスの場合、Bookingが分割されるとStandby logicが実行される
- **Booking Combine**: 全ての元のBookingsのBookingステータスがFirmまたはBlankの場合、既にFirmになっているため、Standby logicは不要。ただし、元のBookingsの1つまたは全てがStandbyステータスの場合、Standby logicが実行される
- **No Rates on File (NROF) bookings**: Final guidanceはGD4になり、関係者にエスカレートされる
- **Empty bookings**: Empty bookingsは現在のStandby Booking scopeに含まれない

**Customer over account plan**: 顧客がaccount planを超える場合の処理

**Releasing of GD1 bookings/Offline checking of Blacklist**:
- 現時点では、GD1 bookingsは自動的にリリースされない
- Bookingsは手動で保持され、リリース前に全てのGD1 bookingsについて、offshore booking staffによってオフラインで手動で他の制約/制限をチェックする必要がある

### 4.3 Glossary
OPUS ContainerのGlossary

## Final Guidance定義

### Guide Type別の定義
- **GD1**: OK to Book - W_F - Bookingはlocal constraintsをチェックした後、Off/On Shore BKG staffによってリリースされる
- **GD2**: Book to next available vessel - W_S - Bookingは1) Standbyになり、On-shoreにエスカレート、または2) Firmになり、次の利用可能なvesselにロールされる
- **GD3**: If necessary, escalate to CSVC manager (On/Off SHore) - W_S - Offshore BKG Staffは1) Firmまたは2) 次のレベルにエスカレートを選択可能 - Offshore BKG Staff
- **GD4**: Escalate to CSVC manager - W_S - On/Off shore CSVC Managerは1) Offshore BKG Staffにdirectionを与える（Ok to book/Cancel）または2) 次のレベルにエスカレート可能 - On/Off shore CSVC Manager
- **GD5**: Escalate to RHQ and GHQ Space controllers - W_S - GHQ/RHQ space controllersはOn/Off shore CSVC Managerにdirectionを与える（Ok to book/Cancel） - GHQ/RHQ Space controller
- **GD6**: Decline - X - Bookingは自動的にキャンセルされる
- **GDN**: Trunk-Loading/Customer is within allocation（Priority Rule Setupの特別なguidance）

## 実務上のポイント

### Standby Guidanceの決定
- Priority Rules、Sequential Validation、Master Constraint Tableの設定が連携してFinal Guidanceを決定
- 10-day logicにより、Booking作成タイミングによってFinal Guidanceが異なる可能性がある

### Escalation Process
- Tier 1からTier 3への段階的なエスカレーション
- 各Tierが適切な権限でBookingを承認または拒否

### Master Constraint Tableの設定
- Trunk-Overall、Trunk-Loading、Feeder、EQ、Commodity、Customerによる包括的な制約管理
- Spot/Non-Spot AP制約により、SpotとAPのBookingリリース判断を分離

### ONE Quote Standby Functions
- BKG VIA field、POR/POL/POD/DEL Allocation、Premium Flag Fieldによる柔軟なallocation設定
- Total bookingsがallocationを超える場合、GD6またはVVD removalがトリガーされる

## 次アクション
- [ ] 04_Memory/Work/ONE/Systems/OPUS/SPC/に移動を検討
- [ ] 実際の使用例を追加
- [ ] 関連するシステムマニュアルとリンク

#inbox #opus #spc #standby #sop #booking #space-control #allocation

