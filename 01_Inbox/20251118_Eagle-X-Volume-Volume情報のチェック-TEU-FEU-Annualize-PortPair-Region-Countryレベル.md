# Eagle-X-Volume-Volume情報のチェック-TEU-FEU-Annualize-PortPair-Region-Countryレベル

## 概要
Volumeに関するメモ。Volume情報のチェック、Volume情報があるか、VolumeがRateと同じシートにある、Volumeの粒度がPortPairのレベル、TEU/FEUの確認、文字情報があるか、VolumeがAnnualizeされているか、Volumeの粒度がPortPairのレベルでない、Regionレベル、Countryレベル、VolumeがRateと同じシートにない、Volume情報がない場合について記録されています。

## 内容

### Volume情報のチェック
- **Volume情報があるか？**
  - **ある場合:**
    - **VolumeがRateと同じシートにある**
      - **Volumeの粒度がPortPairのレベルになっている**
        - **下記の観点を確認してマッピングする**
        - **1. TEU/FEUの確認**
          - **TEUの場合: マッピング**
          - **FEUの場合: 列を追加して2倍にしてからマッピング**
        - **2. 文字情報があるか？**
          - **ある場合: 列を追加して文字情報をなくした数値のみをマッピング**
          - **ない場合: マッピング**
        - **3. VolumeがAnnualizeされているか？**
          - **Annualizeされている：マッピング**
          - **Annualizeされていない：要検討（Contract Periodを元に自動算出する？）**
        - **上記情報が不明瞭の場合：Salesに確認する**
      - **Volumeの粒度がPortPairのレベルでない**
        - **Regionレベル：上記3点を確認した上で、マッピングを行い、その後に裏で分割ロジックを入れる？（過去のLifitingに基づいて）**
        - **Countryレベル：上記3点を確認した上で、マッピングを行い、その後に裏で分割ロジックを入れる？（過去のLifitingに基づいて）**
    - **VolumeがRateと同じシートにない**
      - **RateにVlookupなどで情報をもってこれるものはもってきてマッピングする**
      - **データ粒度が異なり持ってこれない場合：要検討**
  - **ない場合：要検討（数値の制約があるので、ありえない数値999999や0などで表現して、Game planやPricing側でデータがないなど表現しないといけない）**

### Check Volume Information (English)
- **Is there volume information?**
  - **If yes:**
    - **Volume is on the same sheet as Rate**
      - **The granularity of Volume is at the PortPair level**
        - **Confirm and map based on the following aspects**
        - **1. Check TEU/FEU**
          - **If TEU: Map it**
          - **If FEU: Add a column, double the value, and then map it**
        - **2. Is there any text information?**
          - **If yes: Add a column to remove the text and map only the numerical value**
          - **If no: Map it**
        - **3. Is the Volume Annualized?**
          - **If annualized: Map it**
          - **If not annualized: Need to consider (Automatically calculate based on Contract Period?)**
        - **If the above information is unclear: Confirm with Sales**
      - **The granularity of Volume is not at the PortPair level**
        - **At the Region level: Confirm the above three points, map it, and then consider adding a splitting logic based on past Lifting?**
        - **At the Country level: Confirm the above three points, map it, and then consider adding a splitting logic based on past Lifting?**
    - **Volume is not on the same sheet as Rate**
      - **Bring over the information to Rate using Vlookup or similar, and map it**
      - **If the data granularity is different and it cannot be brought over: Need to consider**
  - **If no: Need to consider (No data on the Game plan or Pricing side)**

## 次アクション
- [ ] 関連ノートにリンク（[[Eagle X]]、[[Volume]]など）
- [ ] 必要に応じてMemory Noteに変換

#inbox #one #eagle-x #volume

