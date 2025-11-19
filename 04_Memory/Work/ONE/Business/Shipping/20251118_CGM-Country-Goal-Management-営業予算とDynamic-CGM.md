# CGM-Country Goal Management-営業予算とDynamic CGM

## 概要
CGM（Country Goal Management）について記録したメモ。CGMの定義、Dynamic CGM Target、Individual Sales Budget、営業予算（輸出・輸入・JOA）、FY25予実対比Weekly Report、実績振り分けルールについて詳細に記載されています。

## 内容

### CGMとは？
CGM（Country Goal Management）とは、GHQ Trade Managementが策定しているもので、Fiscal Year毎のTrade Budgetを各国に分配した予算値となります。期初と下期の年2回見直しが行われます。予算値として「TEU」、「CM/TEU」、「Gross CM」が設定され、Globalレベルで各国に分配されたCGM予算値をすべての国が達成したとき、Trade Budgetを達成できる仕組みになっています。

### CGMには2種類あり
- **Loading Office Country CGM**: 積み国が日本となっているCGM予算値
- **Contract Office Country CGM**: 契約国が日本となっているCGM予算値

ONE JAPANでは「Loading Office Country CGM」をベースに達成率をモニターしています。

### Dynamic CGMについて
FY2025より、CGM達成状況のモニタリングを強化するために、Dynamic CGM Targetが導入されています。

Dynamic CGM Targetは、各Trunk VVDのFinal BSA情報を反映し、本船のアップサイズ／ダウンサイズも考慮したターゲット値を指します。VMS時にはBSAがゼロとなるため、ターゲットはゼロに設定されます。これまで、VMSの影響やBSAの変動を反映することは困難でしたが、Dynamic CGM Targetの導入により実態に即したCGM達成率のモニタリングが可能となっています。

### Dynamic CGM TEU Target計算方法
"Final BSA" x "Trade Budget Utilization %" x "Country Proportion" per each Trunk VVD Lane Domi / N-Domi respectively.

※Country Proportion (Country Allocation Ratio) は月次平均に基づいており、季節要因を反映しています。一方、本船は季節性に関係なく満船にする必要があるため、Utilizationは1H/2H半期平均を用いてDynamic CGM TEU Targetを算出しています。

### Individual Sales Budgetについて
FY2025より、Contract CGM達成のために導入されています。

前年度のパフォーマンスに基づいてセールス担当者個人(C-KAM、あるいはC-KAMに該当するONECareセールス担当)に割り当てられるターゲット値で、Service Scope Group/Dominant Flag毎、1H/2Hに分割されて割り当てられます。

CVAがCustomer Performanceをモニターする指標であるのに対して、Individual Sales Budgetはセールス個人のPerformanceをモニターする指標となります。

Trade Budget (GHQ) -> Contract CGM (Country/Office) -> Individual Sales Budget (Person) -> CVA (Customer) + Opportunity -> Actual Lifting

※ONE JapanとしてはOriginal POR CGM Target数値（＝Japan Pipeline）の輸出(CIF)/輸入(FOB)/JOAのTarget数値を使用し、全社共通指標の営業予算としてモニタリングしています。

### 営業予算とは？
輸出・輸入・JOAすべてにおいて、「Weekly TEU」、「CM/TEU」、「Weekly Gross CM」の営業予算を設定しています。輸入CIFだけは「Weekly TEU」のみの予算設定としています。毎年期初に営業予算を策定した後、下期のCGM見直しの変動幅に応じて、必要に応じて下期の営業予算値を見直します（年によっては下期見直しがない場合あり）。

### 輸出営業予算
Original POR CGM Targetと同じ値を使用しています。積み上げ営業予算の合計値（Mark Up値含む）がCGMと同じ値です。一点異なる点としては、CGMは週毎にTEU Targetが異なる値で設定されていますが、輸出営業予算はCGMを年間52週(年によっては53週)で割ったWeekly Average TEU Targetを定めてパフォーマンスをモニターしています。CM値については、CGMのAverage CM/TEUを営業予算とし、Weekly Average TEUを乗じた数値がWeekly Gross CM営業予算となります。

### 輸入営業予算
ONE JAPANが独自で定めている予算値となります。日本契約に加えて、外地契約のCIFを足しこんで予算値を策定し、Weekly TEU Targetを定めてパフォーマンスをモニターしています。CM値については、FOB分のWeekly TEU TargetにCM/TEU営業予算値を乗じた数値がWeekly Gross CM営業予算となります。

### JOA営業予算
ONE JAPANが独自で定めている予算値となります。Weekly TEU Targetを定めてパフォーマンスをモニターしています。CM値については、Weekly TEU Target値にCM/TEU営業予算値を乗じた数値がWeekly Gross CM営業予算となります。

### FY25予実対比Weekly Report
営業予算と実績の週次対比ReportをSYM課より毎週金曜日に配信しています。ONE BESTでは、All Japan全体の予算達成率に焦点を当てていますが、予実対比Weekly Reportでは、営業課、営業担当者、顧客単位での予実対比をモニターすることを目的としています。

### 実績振り分けルール
※①から順に優先適用します。

1. **SC/RFA SVC Scope Sales Rep code**
2. **SC/RFA Request Sales Rep code**
3. **予算申告時のSC/RFA Customer Code** (CIF・FOB共に)
4. **予算申告されていない場合**:
   - a) まず日本取り決め案件については、SC/RFA Customer latest sales rep code (=OPUS Customer Integration上のSales rep)から営業課を判定
   - b) 輸出FOB BKGはPipelineシート上でご申告頂いた営業課から判定
   - c) それでも判定できないものは、輸出案件であれば「KA Type、BKG Office(ONEQの場合はContract Office)、BCO/NVO、Trade」4つの情報から実績を営業部課へ割り振ります。輸入とJOA案件についてはKA TypeとContract Officeから営業部課を判定します。

### Tigerを用いてSC/RFA Filingを行う場合
Tiger Filing時にRequest Officeで選択されたSales RepがSC/RFA SVC Scope Sales Repに紐づけられます。Tiger Filing時にRequest Officeボタンから正しいSales Repを指定してください。

### ONEQuoteで入ったBKGの場合
SC/RFA Customer Code(=BKG Party)に紐付くSales Rep code（Customer Integration上の情報）がSC/RFA SVC Scope Sales Repに引用され、そちらを参照することになりますので、Customer Integration上でSales person（個人名）を紐付けて頂いている場合は各営業課に実績が正しく振り分けられます。

## 関連ノート
- [[CGMとAPの関係-Country-Goal-Managementとアカウントプラン]]
- [[APとは何か-Account-Planの基本概念]]
- [[Sales-TargetとAPの比較-営業目標と計画の整合性]]

#cgm #sales-budget #dynamic-cgm #work/one #work/one/afla

