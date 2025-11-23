# Peru-Pricing-DAR処理方法

## 概要
PeruにおけるDAR (Demurrage and Detention) 処理の方法、CTIC discountの承認プロセス、実例をまとめたノート。

## 内容

### DAR処理の基本フロー
1. **DARリクエスト受領**: 顧客またはPeru officeからCTIC discountリクエストが来る
2. **状況確認**: コンテナの滞留理由、書類問題、税関問題などを確認
3. **判断**: ONEの責任か、顧客側の責任かを判断
4. **承認**: 承認権限内でwaiver/discountを承認
5. **DAR作成**: OPUSでDARを作成（例: LIMBB25100029）

### CTIC Discountの実例

#### JP & INSUTEXTIL E.I.R.L. ケース
- **B/L**: ONEYNBOF43558300
- **ルート**: CNNGB - PECLL
- **Shipper**: NINGBO MH SHINE INDUSTRY CO., LTD
- **CNEE**: JP & INSUTEXTIL E.I.R.L.
- **CNPT**: NINGBO DEEPLY CONVICE SUPPLY CHAIN MANAGEMENT CO.,LTD
- **RFA**: R00006621E5 - ONE QUOTE
- **貨物価値**: USD 7,500 (polyester sewing thread woven label tape)
- **問題**: 書類不足によりコンテナをピックアップできず
- **状況**: ペルー税関が書類OKを承認し、full containerのピックアップを許可
- **リクエスト**: CTIC discount USD 10,000（顧客はUSD 5,500しか残していない）
- **発生したdetention**: October/27thまで
- **承認**: USD 5,000 waiver承認
- **条件**: 顧客が残額を迅速かつ完全に決済すること
- **DAR**: LIMBB25100029承認
- **結果**: 顧客がUSD 5,000 discountを受け入れ、10月29日水曜日にfull containerをピックアップ

### Free Time設定の実例

#### 標準Free Time
- **CTOC (Container Terminal Origin Charges)**: 14 days
- **CTIC (Container Terminal Import Charges)**: 21 days
- **NOR (Non-Operating Reefer)**: 14 days free line detention at POD

#### 顧客別Free Time設定
- **Geodis Project**: 14 days CTOC / 21 days CTIC
- **Marinasol**: MRG freetimeに合わせるためのDMT F/T Exception

### DAR承認の判断基準
1. **責任の所在**: ONEの責任でない場合（顧客の書類問題など）は、長期関係を考慮して部分的なwaiverを検討
2. **顧客との関係**: 長期的な関係を維持するための判断
3. **金額**: 承認権限内での判断（例: USD 5,000まで）
4. **条件**: 残額の迅速な決済を条件とする

### DAR処理の注意点
- **迅速な対応**: コンテナの早期返却を促進するため、迅速な判断が必要
- **記録**: DAR番号を記録し、OPUSでの承認を確認
- **フォローアップ**: 空コンテナの返却状況を確認

## 🔗 関連リンク

- [[../../../../../../.cursor/commands/dar.md]] - DAR業務支援コマンド（Cursor AI）

## 次アクション
- [ ] DAR処理の標準プロセスを文書化
- [ ] 承認権限の明確化
- [ ] 類似ケースのデータベース化

#inbox #peru #pricing #DAR #CTIC #detention #waiver
