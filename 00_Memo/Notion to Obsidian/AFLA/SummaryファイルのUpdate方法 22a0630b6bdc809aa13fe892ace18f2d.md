# SummaryファイルのUpdate方法

- Summaryファイル

G:\Shared drives\Latin West Coast\Space Control

- Summaryファイル更新のためのLookerファイル

G:\Shared drives\Latin West Coast\Space Control\Looker\5. Summary File Update

- グループにOpen Summaryという→Notify each other
- 週次のアップデートは月曜日、遅くとも火曜の午前までに行う→BCP
- 各PICがその後状況をUpdateする

- Lookerファイル
- Reeferの数値はここを使う
- G:\Shared drives\Latin West Coast\Space Control\Looker\5. Summary File Update\1.Reefer

![image.png](Summary%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AEUpdate%E6%96%B9%E6%B3%95/image.png)

- TEUを２で割ってUnitにする

![image.png](Summary%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AEUpdate%E6%96%B9%E6%B3%95/image%201.png)

- Pivotを作って各週に貼り付ける

![image.png](Summary%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AEUpdate%E6%96%B9%E6%B3%95/image%202.png)

- NOR/Live RH　下の表を更新する
- **SAOHQ - Reefer Container TrackingのLookerを開く**
    
    [](https://oneline.cloud.looker.com/dashboards/29978?Arrival+Date=&Arrival+Month=&Is+Firm+%28Yes+%2F+No%29=Yes&DEL+RHQ=SAOHQ&Booking+Cargo+Type+Name=Full+cargo&1st+POL+ETD+Date=&DEL+Country+Code=CL%2CEC%2CMX%2CNI%2CPE%2CCO%2CCR%2CGT%2CSV&POR+RHQ=&Service+Scope+Code=&POR+Country+Code=&Trade+Code=&Revenue+Lane+Code=&Last+Service+Code=&Service+Scope+Group+Code=&Is+Dominant+%28Yes+%2F+No%29=&Sales+Month=&Sales+Fiscal+Year=2025&Container+Type+Size+Code=R5&DEL+RCC=BRSAO%2CPAMIT%2CCLSCL)
    
- DEL countryでフィルター
    - CL EC　MX NI PE CO CR GT SV
- 2つのチャートをスクリーンショットしてSummaryファイルに貼り付ける

- このテーブルをLookerの数値を使って更新する
- 

![image.png](Summary%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AEUpdate%E6%96%B9%E6%B3%95/image%203.png)

![image.png](Summary%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AEUpdate%E6%96%B9%E6%B3%95/image%204.png)

- WCCAのUpdate
    - このフォルダから一番最新のファイルを開く
    - G:\Shared drives\Latin West Coast\Space Control\Looker\5. Summary File Update\2.Marex
    - RPBとCMの列はHideする
    - SVAQJとそれ以外をわけて集計する
    - 
    
    ![image.png](Summary%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AEUpdate%E6%96%B9%E6%B3%95/image%205.png)
    

- **SV/CR/NI liftingsから3つのチャートを切り取りコピーする**
- 

### 週次アップデート作業をざっくり説明すると…

| 作業の流れ | 目的・ポイント | コツ・注意点 |
| --- | --- | --- |
| **1. 週次データを入力（Excel）**  - その週に対応する列（例：W31）を追加し、前週の値をコピーして更新  - 古い週の列は非表示にして見やすくする | ・WCCA（中米西岸）／WCSA（南米西岸）の実績と目標の進捗を見える化 | **Excel は同時編集不可**。最初に開いた人が「開けたよ」とチャットで共有し、二重更新を防ぐ |
| **2. 「NOR live refer numbers」を貼り付け**  - ローカルレポート（ピン留め済）から数値をコピー  - ピボットテーブルで週別・サービス別に並べ替え | ・冷凍コンテナ（リーファー）の投入実績を把握し、今後2週の見込みを立てる | ピボットは「T-uses」「Sales Week」「Shipment Lane Revenue」を行・列にドラッグするだけ |
| **3. 空コンテナ(Empties)とAXラインの手入力**  - Busan/Yokohama→ラ米向け等、スペースプランナーが把握している空バン移動を追加 | ・総ユニット数を正確に出すため | AX4は隔週運航。バンチング時は週連続表示になるので要チェック |
| **4. 先読み用の簡易予測**  - 未入力週は前週実績÷2で仮置き → 船積2週前に需要を掴む | ・船がガラ空きなら営業に「もっと詰めて」とアラート、満杯なら「抑えよう」と指示 | YQ など特定PODの動向もここで確認 |
| **5. リーファートラッキングレポートを見る**  - POD別の積載／需要を可視化。特に輸出好調なQなどを攻める | ・どこにリーファーを多く送るべきか瞬時に判断 | VBA／Google Apps Scriptで自動化する案あり |
| **6. 国別フィルタリング（WCCA／WCSA）**  - Chile, Colombia, Ecuador, Mexico など該当国だけ抽出 | ・RHQ／上層部が見る数値とずれないようにする | Mexicoはドラフト制限でクレーム多。数字管理を厳密に |
| **7. ECN & WCCA 目標チェック**  - ECN（北米東岸）実績を週1で手入力  - MarxレポートでAX1-4実績を拾い、CM/RPB除外 | ・達成度を即座に上司へ報告し、スロットコストの赤字を防止 | 例：WCCA目標 256 TU、コミット550 TU（Simon）／870 TU（Marx） |
| **8. 火・木の会議用資料化**  - 火曜14:00までに更新 → Simon チームのデータ（15-16時）を取り込み、17時会議へ | ・意思決定をスムーズに | 月曜 or 火曜午前に更新すると週末更新分まで反映できて確実 |

---

### 一言でまとめると…

> 「週次で Excel を更新 → 冷凍・空バン・サービス別実績を整理 → 目標と先2週の見込みを出し、会議で即判断できる状態にする」 - これが WCCA 数字管理の核心です。
> 

これさえ押さえれば、「どの港・どのサービスを攻めるか」「どこで空きを抑えるか」をタイムリーに指示でき、スロットコストの損失も回避できます。