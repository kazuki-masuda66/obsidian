# Eagle-X-HONDA-memo-R1-R2-Lane-ID-課題とアクション

## 概要
HONDA memoに関するメモ。Eagle XではR1とR2の紐づき（Lane ID）を取る必要がある、R2 Supplemental tool、HONDAのケースでの問題、OMMCのConversionの誤り、今後のアクションについて記録されています。

## 内容

### R1とR2の紐づき
- **Eagle XではR1とR2の紐づき（Lane ID（どのLaneがNewでどのLaneがDeleteされた等を特定する））を取る必要がある**
- **通常、このLane IDを簡易に特定するためにR2 Supplemental toolという補助ToolをEagle Xは提供しており、問題なければ、時間がかからずLane IDの整理が可能**

### HONDAのケースでの問題
- **HONDAのケースの場合は通常と異なり、R1のコンバージョンのあとにOMMCのConversionの誤り（Field Mapping for POR）が発見され、この修正時にエラーに関連する部分（Field Mappingを修正後にPlace mappingも合わせて修正する必要があった）のUpdateを漏らしてしまい、それが原因でR1のLane IDがぐちゃぐちゃになってしまっていた（このことにR2が来るまで気づくことができなかった）**
- **R2のConversion実施時に、R1のLane IDがぐちゃぐちゃになっていたため、R2 Supplemental toolを使用できず、Eagle Xチーム担当者がマニュアルでLane IDの整合をとるよう努めたものの、R1のLane IDの整理から、かつフルマニュアルで実施する必要があり、通常よりも大幅に時間がかかってしまうことから、Deadlineを考慮し、ASISへの切り替えの判断となった**

### 詳細な経緯
- **Pricing tool was created based on above wrong extracted file and overwritten POR in Pricing Tool**
- **Eagle X requested OMMC to update R1 Conversion Tool's Field Mapping**
- **OMMC updated it but forgot to update Place Mapping and almost R1 Converted data was wrong**
- **therefore Ben conducted R2 Conversion by manual**

### 今後に向けたアクション
- **Eagle Xのレビューの徹底（Field mappingの指摘漏れを防ぐ）**
- **OMMCチームにR2のやり方、及びR2 Supplemental toolの使い方を再トレーニング**
- **OMMCチームにConversion toolを修正するときに関連する箇所についてトレーニング**

## 次アクション
- [ ] 関連ノートにリンク（[[Eagle X]]、[[HONDA]]、[[Lane ID]]など）
- [ ] 必要に応じてMemory Noteに変換

#inbox #one #eagle-x #honda #lane-id

