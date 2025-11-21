# Broken Route Booking更新フロー

## 概要
Broken route（破損ルート）のBooking更新フローについてまとめました。SHA TS（Shanghai Transhipment）がタイなどのBooking Officeの更新を直前になる場合の処理方法です。

## 内容

### 基本フロー

#### 状況
- **SHA TS**: Shanghai Transhipment Teamが担当
- **対象**: タイなどのBooking Officeの更新を直前になる場合
- **処理**: SHA TSがBooking更新を担当

### 実際のケース: GS2 HMMT0021E / Broken Route / BKK Bookings

#### ケース概要
- **Service**: AX4
- **Vessel**: HMMT0021E
- **問題**: Broken route
- **Booking**: BKKFAX449600、BKKFAV726900
- **対応**: BrokenをRemove（解除）

#### 処理フロー

**Step 1: Broken Routeの確認**
- **Cenhong Yang**（OPS Transhipment Team）からリクエスト
- **内容**: Broken routeのBookingをRemoveしてほしい
- **Booking**: BKKFAX449600、BKKFAV726900

**Step 2: Booking更新の実施**
- **Paweena Singsoongnoen**（Marketing and Planning 2、Thailand）が対応
- **対応内容**: 
  - TH bookings already BDRed（Booking already released）
  - MV name（Vessel name）の更新が必要
  - AX4 WK47: HYUNDAI PREMIUM V.0102E-HYPT0102E → HMM PREMIUM V.0102E-PMXT0102E

**Step 3: Vessel変更の更新**
- **Cenhong Yang**が更新を実施
- **更新内容**: PMXT0102Eに更新完了

### Vessel変更時の注意点

#### タイミング
- **Vessel変更**: 直前になる場合がある
- **対応**: SHA TSがBooking更新を担当
- **期限**: 迅速に対応が必要

#### 更新内容
- **MV name**: Vessel nameの更新
- **VVD**: Vessel Voyage Dateの更新
- **Booking status**: Broken routeの解除

### 連携のポイント

#### 関係者
- **Cenhong Yang** (`cenhong.yang@one-line.com`): OPS Transhipment Team、Booking更新リクエスト
- **Paweena Singsoongnoen** (`paweena.singsoongnoen@one-line.com`): Marketing and Planning 2、Thailand、Booking更新実施
- **GHQ LAWC/Masuda san**: Vessel変更の指示

#### 連絡先
- **グループメール**: `GHQ.LAWC.MKTG@one-line.com` をCCに入れる
- **迅速な対応**: Vessel変更は迅速に対応が必要

### ベストプラクティス

#### 1. 迅速な対応
- Vessel変更は迅速に対応
- Booking更新は即座に実施

#### 2. 明確な連絡
- Vessel変更の理由を明確に説明
- 更新内容を明確に伝える

#### 3. 確認
- 更新後、Bookingが正しく更新されているか確認
- Broken routeが解除されているか確認

## 次アクション
- [ ] 必要に応じてMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/]]）
- [ ] 他のBroken routeケースがないか確認

#lawc #pricing #booking #broken-route #vessel-change #inbox

