# Eagle-X-Pricing-tool-EUA-IOPとBase-Port-Out-Port

## 概要
Pricing toolに関するメモ。EuropeとAfricaのSeparate IOP tool、IOPのロジック、マッチバック、India Inland haulage、Base PortとOut Portの定義、コンテナタイプの変換、CM/teuの計算について記録されています。

## 内容

### EuropeとAfricaはSeparate IOP toolがある
- **IOPのロジック**
- **マッチバック**
  - InとOut上海でだして上海に戻ってきたらマッチバック100%

### Pricing toolに出てくるのはEUAのIOP offerだが、ここに出てくるのはEUA IOPだけではない

### India Inland haulage
- **インドの内陸のコスト（主にRail）はインドMarketingが決めている**
- **このデータをPricing toolで読込できるようにしている**
- **PODを変更するたたびにデータが変わる**
- **全Tradeで使用可能**
- **SoC=Shipper Own Container**
- **CoC＝Career Own Container (こちらが通常)**

### Base Port（ベースポート）
- **定義**：主要航路上の拠点となる港で、船会社が標準的な運賃を設定している港。
- **特徴**：
  - 定期航路で頻繁に寄港する港。
  - 運賃（基本海上運賃）はこの港を基準に設定される。
  - 例：**シンガポール、釜山、横浜、ロッテルダム、ロサンゼルス**など。

### Out Port（アウトポート）
- **定義**：Base Port以外の港で、追加コスト（追加運賃）が発生する可能性がある港。
- **特徴**：
  - 通常の定期航路から外れた場所にある。
  - サービス頻度が低く、接続が複雑な場合が多い。
  - Base Portからのフィーダーサービス（支線輸送）が必要なケースが多い。
  - 通常、**Outport Surcharge（追加費用）**が発生する。

### コンテナタイプの変換
- **D2=20**
- **D4=40**
- **D5=HC**
- **D7=45**

### CM/teuの計算
- **D2以外は割る２する**

## 次アクション
- [ ] 関連ノートにリンク（[[Eagle X]]、[[Pricing tool]]、[[Base Port]]、[[Out Port]]など）
- [ ] 必要に応じてMemory Noteに変換

#inbox #one #eagle-x #pricing-tool #base-port #out-port
