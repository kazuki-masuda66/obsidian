# AFLA Briefing-20250708-AP管理とエクアドルPricing

## 概要
AFLA部署でのブリーフィング（2025年7月8日）のメモ。AP（Allocation Plan）の管理方法、エクアドルPricingの運賃登録方法、Tigerの設定変更、Show up ratio、LAX（Los Angeles）でのデマレージ・ディテンション、MRGのダウンロード方法について記録しています。

## 内容

### APについて
- Pusan船がでることをClosing
  - その前までに満船にする、かつ、溢れたときにどれを切るかを明確にする
- G:\Shared drives\LW AP\3_Finalize_AP
  - ここで担当の国が終わってるか確認する
  - 基本は営業が直す
  - Warningが出ている場合はエラー箇所を指摘する
    - 先月と比べて大きな変化があるか
    - Actual liftingで実際に乗せているか
- AP Summary Standardのシート
  - TEU allocation/BSA→SimonがInputした。CGMで話し合われたTarget
  - 30％くらい多かったらSimonにシェア
- 船積み実績が全然ないケースがある
  - RFA No.が正しくない可能性がある、実際にはLiftingがある
  - Sales Officeに確認する（返信ないケースもある）
- AP→各国のBSAをOPUSにアップロードする
- AX1: HLC ８、ONE ３、HMM １
- 基本BSAは一番少ないキャパシティにあわせる
- ONEの船だと余分のスペースがある＝オーナーズメリット

### FAKはここ
- G:\Shared drives\Latin West Coast\LAWC Rates guideline
- 上記で作ったものがSimonがONE ForceでPublishしている
- ALL TM Directions→Created Byで並び替え→Simonを探す

### エクアドルPricingの話
- 運賃の登録はTiger
- TigerからのメールはTO 増田（担当者）でCCはAFLAにしたい
- Tigerの設定変更
- MAVIJYUのFilingのリクエストを受領
  - 過去のメールでやり取り確認
  - ZiyuはこれでOffer。StarcargoはTier1でこれに+100が本来のはず
  - 他のメールも確認して、StarcargoにいくらでOfferしているかは継続Watch
  - MRGのものはそのままでOK
  - MRG以外は上記のメールにアラインしているか確認する
- XingangとCNTSNは同じところを指す
  - CNTSN: UN/LOCODEでの正式コード。Tianjin（天津）を表す港コード
  - Xingang: 天津新港（Tianjin Xingang）。CNTSN内の主要なコンテナ港エリアの名称
  - 実務での使われ方: ブッキングやBLでは「CNTSN」を港コードに使い、現地CYなどの地名として「Xingang」と記載することが多い

### Tier運用
- COSCOはT1をMD
- CMAはDiamondと言ったりする
- HLC got 3 tier: FAK / Tier 1 / Tier 0
  - Tier1 -50 / Tier 0 -100
  - So their Tier 0 - similar to our Tier 1

### Show up ratio（ショーアップ率）
- 「Show up」は中国オフィスや前線オフィスによる予測のこと
- たとえば、確定予約が100TEUで、「show up」が50%と記載されていれば、それは50TEUがゲートインするという予想を意味します
- これが例えばBSA 50TEUに対してであれば、ロールオーバー（積み残し）はなしとなります
- もしショーアップ率が、積極的なレート調整などを背景に60%に上がると予想される場合、結果として10TEUのロールオーバーが発生することになります
- 通常、CY（コンテナヤード）のゲートオープンは船の到着の約3〜5日前なので、空コンテナのピックアップ状況により、より正確な予測ができるようになります

### Rate ValidityとOffer Validity
- Rate:1500
- Offer Validity: Filingの期限

### LAX（Los Angeles）
- メキシコは電気代などを船社ではなくお客さんに直接請求する
- 船がついて48時間以内だったら請求しません。それ以降だと蔵置料を請求する（デマレージ）
  - ターミナルは船社に請求する、それをお客さんに請求する
- お客さんのトラックがピックアップをしてそこから7日日以内だったら不要。それ以降だったらチャージ（ディテンション）
- 船から降ろされてから港においてて、返ってくるまでで14日間（Combined）：メキシコはCombined、南米はCombinedが多いがメキシコが有名
- DAR: D&D Approval？14日→21日にのばせる（14日にしていても、実態はお客さんの要求に応じて21日までは伸ばすのをOKにしていたりする）

### MRGのダウンロード方法
1. Go to sales force
2. Click follow ALL - WEST COAST SOUTH AMERICA (EB)
3. Go to related Trade and Mtkg Direction ; find the latest FAK MRG and download it

## 次アクション
- [ ] 関連ノートにリンク（[[AP管理]]、[[エクアドルPricing]]、[[Tiger]]、[[Show up ratio]]など）
- [ ] 必要に応じてMemory Noteに変換

#ap #pricing #ecuador #tiger #show-up-ratio`n#memory #work/one #work/one/afla
