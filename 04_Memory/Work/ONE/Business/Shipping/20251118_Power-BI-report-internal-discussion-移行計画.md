# Power BI report internal discussion-移行計画

## 概要
Power BI reportの内部ディスカッションのメモ。Power BIが社内全体で許可されなくなり、LookerまたはLooker Studioへの移行が必要になったこと、Supply DemandコンポーネントとBudget & Projectionの移行計画について記録しています。

## 内容

### Power BI is no longer permitted company-wide
- Power BIは社内全体で許可されなくなり、以下のいずれかに置き換える必要がある:
  - **Looker** (Managed by DDE) → 出力したいデータはLooker Exploreで利用可能である必要がある
  - **Looker Studio** → アドホックなデータ追加が可能

### Supply Demandコンポーネントの移行
- eeSea data、Supply情報を含めて、既にLookerで利用可能
- すべてがeeSea dataでカバーできる場合、現在AFLAが使用している希望のチャートを選択し:
  - Dejimaのダッシュボードで要件を満たせるか確認。満たせない場合は、実装のための追加要件を提出
- eeSea dataだけでは不十分で手動補完が必要な場合、その部分が相当な場合は、一時的にLooker Studioを使用することも選択肢

### Budget & Projection
- Lookerには利用可能なデータソースがない
- **長期的には**: KPIプロジェクトの下に登録し、すべてのTradesで管理 → **Looker**に移行
- **短期的には**: 希望のチャートを選択し、**Looker Studio**で実装

### Supply & Demand
- 1st page: このデータはeeSea scheduleからのもの
- Looker（eeSea）からこのデータをダウンロードしたい
- P4-6

### Budget & Projection
- 1st 4 pages in December (budget)
- 1H budget set up in the beginning

## 次アクション
- [ ] 関連ノートにリンク（[[Power BI]]、[[Looker]]、[[Looker Studio]]、[[データ移行]]など）
- [ ] 必要に応じてMemory Noteに変換

#power-bi #looker #data-migration #reporting`n#memory #work/one #work/one/afla
