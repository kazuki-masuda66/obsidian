# Ecuador-Pricing-特殊貨物とAP処理

## 概要
Ecuadorにおける特殊貨物（NOR、Reefer、OOGなど）のレート設定とAP（Allocation Plan）処理方法をまとめたノート。

## 内容

### NOR (Non-Operating Reefer)
- **定義**: 冷凍機能を使わない冷凍コンテナ（Dry cargo用）
- **レート例**:
  - CNWUH-ECGYE: USD 1,650/40NOR (USD 450 barge cost), 後にUSD 1,450/40NORに調整
  - CNXIL-ECGYE: Base port rate + USD 250
  - CNSWA-ECGYE: Base port rate + USD 400
- **Barge Cost**: Outportからのshipmentはbarge costを考慮
- **Equipment確認**: R5 container availabilityを確認してからレート設定
- **Booking例**: 
  - WU5MA2512800 (CNWUH-ECGYE, 1x R5 NOR, Commodity: CHAIR BEDS OR SOFA BEDS, Weight: 4600 kgs)
  - SZPFAD102300 (CNXIL-ECGYE, 1x R5 NOR, Application date: Nov 29, Commodities: GAS BURNERS OR RANGES, DOMESTIC, IRON OR STEEL, Weight: 13 tons approx.)
  - SZPFAD370300 (CNSWA-ECGYE, 1x R5 NOR, Application date: Nov 26, Commodities: ADHESIVE TAPE, NOT SURGICAL, PLASTIC BACKING, Weight: 22.5 tons approx.)

### Reefer (RH)
- **用途**: 冷凍貨物
- **レート例**:
  - MUNDRA/NHAVA SHEVA-ECGYE: USD 4,500/40RH (2x40'REEFER per month, validity until Dec 31, 2025, 10 days free detention at destination)
  - Commodity: FROZEN FRENCH FRIES
- **Free Time**: 10 days free detention at destination
- **Volume**: 2x40'REEFER per month
- **Service Type**: YY (CY/CY)
- **Payment Terms**: COLLECT
- **Space Release例**: 
  - ONEYSZPFAH940300 (ETD: 2025-11-29, V.V.: ONE SPIRIT OITT2547E, 1X40RH)
  - ONEYTAOFL7207400 (ETD: 2025-11-24, V.V.: POSORJA EXPRESS AJRT2546E, 1X40RH)
  - ONEYSZPFZ1679500 (ETD: 2025-11-23, V.V.: MSC CANDIDA KDDT0546E, 1X40RH)

### AP (Allocation Plan) 処理

#### PECLL NOR制約
- **Capping**: PECLL NOR - please continue capping at 100 Units / WK
- **理由**: Equipment availability制約

#### Booking Release戦略
- **AX1**: Will release all for following 2 sailings, except GD4 to IQQ/PECLL NOR/MX NOR/PE+CL DG
- **AX2**: Will release all for following 2 sailings, except GD4 to PECLL NOR+heavy D2/MX NOR/COBUN heavy D2/PE+CL DG
- **AX3**: Will release common PODs for following 2 sailings, except GD4 to PECLL NOR+heavy D2/MX NOR/COBUN heavy D2/ DG
- **AX4**: Will release all for following 2 sailings, except MX NOR
- **SHA on WK49**: Open for SHA on WK49 OITT2547E first, as only 10 days before ETA

#### Market Situation
- **TAO**: Currently has 1000+TEUs on hold
- **Strategy**: Maintain aggressive booking release strategy across all 4 loops through end of November
- **Priority**: Release qualified bookings first to prevent massive rollovers
- **Hold Policy**: Temporarily hold certain heavy or restricted cargoes booked for Dec sailings

### 特殊貨物の制約
- **Non-DG Batteries**: Must be declared and get pre-approval before container gate-in
- **Heavy Cargo**: May be temporarily held for Dec sailings
- **Restricted Cargo**: May be temporarily held for Dec sailings

### Equipment確認の重要性
- **R5 Container**: Check availability at outports before quoting
- **CNSWA**: Enough R5 containers available
- **CNXIL**: Need to check R5 container availability
- **Reefer Equipment**: Make sure outport have reefer equipment before quoting; otherwise add-on fee is not sufficient to cover empty repo cost

## 次アクション
- [ ] 04_Memory/Work/ONE/Pricing/Ecuador/に移動を検討
- [ ] AP処理のベストプラクティスをまとめる

#inbox #ecuador #pricing #special-cargo #NOR #reefer #AP
