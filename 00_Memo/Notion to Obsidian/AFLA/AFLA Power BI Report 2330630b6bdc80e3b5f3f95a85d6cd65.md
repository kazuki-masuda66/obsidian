# AFLA Power BI Report

- **Supply Demand report**
    - [https://sites.google.com/one-line.com/ghqafla-supplydemand/home?authuser=0](https://sites.google.com/one-line.com/ghqafla-supplydemand/home?authuser=0)
    - Power BI location
        - G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan
            - AFLA Supply & Demand
    - Power BI Data source
        - G:\Shared drives\GHQ AFLA\Business Intelligence\Looker Reports - Transition Folder
            - AFLA Supply DB
    - Original data
        - eeSea Tableau(ONE→Weeky roundtrips explanation→ONE - voy v3)
            - Supply data
        - Alpaliner
            - Vessel Information
    
    （７／１７打ち合わせ）
    
    - Power BIは全社的にNG、どちらかに移行する
        - Looker
        - Looker Studio→Ad hocなデータ追加が可能
    - Supply Dmenadは比較的容易に移行可能
        - eeSeaのデータはLookerにSupply含めて存在している
        - eeSeaのデータで完結できるのであれば、AFLAが見ているチャートの中で、欲しいものを選択して、
            - Dejimaのダッシュボードで要件を満たせるか、満たせない場合は要件を追加して彼らにいれてもらう
        - eeSeaのデータで完結できない、マニュアル部分をどう補完するか？この部分が大きい場合、Lookerではなく、Looker Studioでしばらく対応するのも一案
    
- **Budget & Projection report**
    - https://sites.google.com/one-line.com/ghq-afla-budget-projection/home
    - Power BI location
        - G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan
            - GHQ AFLA FY23 Budget & Projection
    - Power BI Data source
        - G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan\Budget Segments\FY25 BP 1Half AFLA\Jun-Sep Proj\DB Output
    - Original data
        - [https://docs.google.com/spreadsheets/d/1EhqJiRADagE8UnRtB7BFyEAKjv3JHdoMHQuA56RLcCk/edit?gid=1172829103#gid=1172829103](https://docs.google.com/spreadsheets/d/1EhqJiRADagE8UnRtB7BFyEAKjv3JHdoMHQuA56RLcCk/edit?gid=1172829103#gid=1172829103)https://docs.google.com/spreadsheets/d/1EhqJiRADagE8UnRtB7BFyEAKjv3JHdoMHQuA56RLcCk/edit?gid=1172829103#gid=1172829103
        - Need to change the projection file from SYM to EXCEL from G-sheet
            - by using the below Power BI, export each data source
            - G:\Shared drives\GHQ AFLA\Business Intelligence\Actual, Forecast, Plan\Budget Segments\FY25 BP 1Half AFLA\Jun-Sep Proj
        

（７／１７打ち合わせ）

- Budget & ProjectionはLookerにはデータソースがない
    - 長期的にはKPI　PJに登録して、全Tradeをまたいでやる
    - 短期的には欲しいチャートを選択して、Looker Studioで実現する