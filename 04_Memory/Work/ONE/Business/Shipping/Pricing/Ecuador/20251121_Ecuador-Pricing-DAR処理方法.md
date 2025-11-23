# Ecuador-Pricing-DAR処理方法

## 概要
EcuadorにおけるDAR (Demurrage and Detention) 処理の方法、CTIC discountの承認プロセス、Free Time extensionの実例をまとめたノート。

## 内容

### DAR処理の基本フロー
1. **DARリクエスト受領**: 顧客またはEcuador officeからCTIC discount/waiverリクエストが来る
2. **状況確認**: コンテナの滞留理由、書類問題、税関問題などを確認
3. **判断**: ONEの責任か、顧客側の責任かを判断
4. **承認**: 承認権限内でwaiver/discountを承認
5. **DAR作成**: OPUSでDARを作成（例: GYEBB25110005A, GYEBB25110009A）

### CTIC Discountの実例

#### RESIQUIM S.A. ケース（Cargo Abandonment）
- **B/L**: ONEYTA4RP4449700
- **Route**: CNTAO-ECGYE
- **Containers**: 7x40'NOR (R5X7)
- **Shipper**: NINGBO TITAN UNICHEM CO., LTD.
- **CNEE**: RESIQUIM S.A.
- **NVO**: ODYSSEY INTERNATIONAL CO., LTD.
- **RA#**: TPEN01244A
- **CTIC**: USD 192,045 (after 50% discount; as of today)
- **問題**: 
  - Cargo was supposed to depart on February 14, but departed on February 9th
  - Import license approved on February 10th
  - VALOR 2504E sailed before expected
  - Customer asked for additional days but were rejected
- **リクエスト**: 50% discount initially, then total waiver request
- **承認**: 50% discount granted on 2nd September
- **結果**: Customer decided to abandon cargo even with 50% discount
- **Units Discharged**: March 30, 2025
- **Cargo Abandonment**: Customer declared cargo abandonment

#### ASIA SHIPPING ECUADOR S.A. ケース
- **B/L**: ONEYTA5PTF704400
- **Demurrage**: USD 25,620.00
- **問題**: Documentation issue requiring customer to obtain information from abroad
- **リクエスト**: 30% discount as commercial waiver
- **承認**: USD 5,000 waiver as exceptional commercial gesture
- **DAR**: 
  - GYEBB25110005A (最初は承認、後にキャンセル - Opus system applying USD 5,000 per container incorrectly)
  - GYEBB25110009A (USD 1,250 discount per container, total USD 5,000/BL)

### Free Time Extensionの実例

#### STARCARGO Free Time Request
- **B/Ls**: TPEF68645500, TPEF62814400, TPEF72577400, TPEF73924800
- **Total Containers**: 19 units
- **Arrival Date**: December 1st
- **Request**: 5 days additional per container
- **理由**: Due to delays and schedule changes, all shipments arrived within the same period
- **承認条件**: Before extending free time for all 19 containers, specify which units actually require the 5-day extension
- **承認**: 5-day additional free time for necessary containers approved

### DAR割引率の実例
- **50% Discount**: RESIQUIM case (USD 192,045 after 50% discount)
- **30% Discount Request**: ASIA SHIPPING (USD 25,620 demurrage, 30% = USD 7,686)
- **Fixed Amount Waiver**: ASIA SHIPPING (USD 5,000 waiver approved)
- **Per Container Discount**: ASIA SHIPPING (USD 1,250 per container, total USD 5,000/BL)

### 承認権限と判断基準
- **顧客側の責任**: Documentation issue requiring customer to obtain information from abroad → Limited waiver (USD 5,000)
- **ONE側の責任**: Vessel departure difference, rollover issues → More generous discount consideration
- **Cargo Abandonment Risk**: Consider total waiver to avoid abandonment (RESIQUIM case - 50% discount not sufficient)

### DAR作成時の注意点
- **Opus System Issue**: DAR GYEBB25110005A was applying USD 5,000 per container incorrectly, had to cancel and recreate as GYEBB25110009A with USD 1,250 per container
- **Per Container vs Per B/L**: Specify clearly whether discount is per container or per B/L

## 🔗 関連リンク

- [[../../../../../../.cursor/commands/dar.md]] - DAR業務支援コマンド（Cursor AI）

## 次アクション
- [ ] 04_Memory/Work/ONE/Pricing/Ecuador/に移動を検討
- [ ] DAR処理のベストプラクティスをまとめる

#inbox #ecuador #pricing #DAR #CTIC #free-time