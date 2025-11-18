# Almir Handover (Power BI report)

- 2つのレポート
- Supply Demand report
    - 手順
        - eeSeaにアクセスする（GSEからシェア）
        - Tableauにログインする（GSEのアカウント＋Authenticaterでワンタイムパスワード）
        - ONEフォルダ→Weeky roundtrips explanation→ONE - voy v3
        - G:\Shared drives\GHQ AFLA\Business Intelligence\Looker Reports - Transition Folder
        - AFLA Supply DBというExcelファイルを開く
        - 1列目のService - master nameの列を全コピー
        - 違う新しいシートに全貼り付け
        - Remove Duplicateをして対象のAFLAに関連するサービスを取得する
        - Tableauに戻り、右上のService - master nameからまず全文の選択肢を外し、そのあと一つずつ対象を選択する
        - 選択できたらApplyを押す
        - Service Versionで3つを選択しApply
        - 
        
        ![image.png](Almir%20Handover%20(Power%20BI%20report)/image.png)
        
        - 右上のダウンロードからデータをダウンロード
        - ONE - voy v3_data (2)みたいなデータがダウンロードできる
        - ダウンロードをしたファイルからカラムAだけをコピーしてDuplicationをRemoveする
        - もとのやつと比較してなにか抜けていないか確認する
        - ダウンロードしたデータのA列からL列までをAFLA Supply DBに貼り付ける
        - A列にMexicaで検索して、Vessel NameがNullのものがないかチェック（これは不要かも）
        - SaveしてExcelを閉じる
        - Power BIを開く
        - G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan
        - AFLA Supply & Demand
        - Dataをリフレッシュする
        - Vessel Nameタブにいき、データがうまっていないものがあるか確認する
        - データが埋まっていないものがある場合はそのVesselをAlphalinerで検索して、TEUとWeightを調べて、データに追加する
        - Publishする
    
    - DBを用意する必要がある
        - Supplyのみ準備している
        - ECC ration
    - ON TIME Report
        - Serivce Qualityをるのによい
            - BkankはOmission
- Budget & Projection
    - SYM→MarketingチームがProjectionのデータを確定させる
    - ProjectionのファイルをGシートからExcelでダウンロードする
    - Budget & Projectionを開く
    - G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan
    - 毎月行う
    - 大本のPower BIとは別にそのもとのデータソースのPower BIが存在する
    - G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan\Budget Segments\FY25 BP 1Half AFLA\Jun-Sep Proj
    - 上から順にPower BIファイルを開く
    - BSA & Liftings FY25 1H Jun-Sep Proj
    - Transform data
    - 個別ファイルをここに吐き出す
    - G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan\Budget Segments\FY25 BP 1Half AFLA\Jun-Sep Proj\DB Output
    - 対象のSales Weekだけを選ぶ
    - Sepの場合はWK３９まで
    - My workspaceにPublishして、My workspaceからExcelでダウンロード→DB outputにフォルダ移動
    - RevenueのBIからFAKとRevenueのデータを出力する

- どうやってデータをもってくるか
- eeSeaのにGSEのアドレスでサインインする
    - TableauのモバイルでVerification Codeを取得する
- ONEフォルダのWeeky roundtrips explnaation
- Voy Ver3
    - Serviceを選択する
- Everyweek updateしている
    - Duplicateをなくす
- Alphlinerから落としていたが、とても大変だった
-