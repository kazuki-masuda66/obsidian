---
title: LA EagleX Email Groups - 設定と運用ノウハウ
tags: [eagle-x, latam, email-groups, laec, lawc, pricer-assignment]
created: 2025-11-22
source: ★スター付きメール抽出_Part4.md
---

# LA EagleX Email Groups - 設定と運用ノウハウ

## 概要

LATAM地域のEagleX関連メールグループの設定と運用について。LAEC（Latin America East Coast）とLAWC（Latin America West Coast）のPricingチームへの適切なメール配信を確保するための仕組み。

## 背景

- **日付**: 2024年6月5-6日
- **発信者**: Cassandra Peretto (LATAM RHQ Digital Yield Management)
- **受信者**: GHQ EagleX / LA EagleX teams
- **目的**: LATAM地域のEagleX関連メールグループの更新と、適切なメール配信の確保

## 主要ポイント

### 1. Email Groups一覧

#### LA EAGLEX
- **Email**: la.eaglex@one-line.com
- **Purpose**: EagleXに関する一般的なトピック（Tender process in EagleXには使用しない）
- **Group Admin**: Cassandra Peretto, Juliane Oliveira

#### LAEC EAGLEX PRICING
- **Email**: laec.eaglex.pricing@one-line.com
- **Purpose**: EagleXで処理されるTenderのPricing（LAEC scopes/Marketingのみ）
- **Group Admin**: Irving Najera, Natan Gonzalez, Tatiane Viana

#### LAWC EAGLEX PRICING
- **Email**: lawc.eaglex.pricing@one-line.com
- **Purpose**: EagleXで処理されるTenderのPricing（LAWC scopes/Marketingのみ）
- **Group Admin**: Irving Najera, Natan Gonzalez, Cristobal Ferron

### 2. 複数Scope対応

- **両方のScopeを含む場合**: LAECとLAWCの両方のScope/Marketingチームを含むTenderの場合、両方のPricingメールアドレスを追加
  - laec.eaglex.pricing@one-line.com **AND** lawc.eaglex.pricing@one-line.com

### 3. Service Scopesの定義

#### LAEC Marketing管轄
- **Service Scopes**: CSW, LAN, LEA, LEE, LEN
- **Pricer Assignment**:
  - BR.MKTG.LAEC.AS: LEE and CSW scopes
  - BR.MKTG.LAEC.LU: LEN scope
  - BR.MKTG.LAEC.AM: LEA / LAN scopes (TAE scope removed)

#### LAWC Marketing管轄
- **Service Scopes**: ILW, LWN, LWU, LWW
- **Pricer Assignment**:
  - Pricing America team: ILW, LWN, LWU
    - Group address: CL.MKTG.LAWC.AM@one-line.com
  - Pricing Asia team: LWW
    - Group address: cl.mktg.lawc.as@one-line.com

### 4. Conversion Toolの対応

- **コードリファクタリング**: Conversion Toolのコードリファクタリングを実施中
- **完了目標**: 2024年7月までに完了予定
- **対応内容**: 正しいグループアドレスを反映するまで時間がかかる可能性があるが、Tender processのメール配信を正確に保つよう努力

### 5. Controlling Country vs Service Scope

- **推奨方法**: Controlling Countryではなく、Tenderに含まれるService Scopeを考慮することを推奨
- **理由**: ChileがControlling Countryでも、LAEC MarketingチームがQuoteするルートがある場合がある（逆も同様）

## 実務上の注意点

### 1. メールグループの選択

- **一般的なトピック**: LA EAGLEXを使用（Tender processには使用しない）
- **Pricing関連**: 該当するService Scopeに応じて、LAECまたはLAWCのPricingグループを使用
- **複数Scope**: LAECとLAWCの両方のScopeを含む場合は、両方のPricingグループを追加

### 2. Service Scopeの確認

- **Conversion後**: Conversionプロセス後、各Tenderに含まれるService Scopeを特定
- **Pricer Assignment**: Service Scopeに応じて、適切なMKTGにEagle X Pricing Requestを送信
- **確認方法**: Pricer Assignment機能を使用して、正しいMKTGを特定

### 3. Conversion Toolの更新

- **リファクタリング中**: Conversion Toolのコードリファクタリングを実施中
- **完了まで**: 完了まで、手動でメールグループを確認・追加する必要がある場合がある
- **完了後の確認**: リファクタリング完了後、正しいグループアドレスが反映されていることを確認

## 関連情報

- **システム**: 
  - Conversion Tool
  - Pricer Assignment
  - Eagle X Pricing Request
- **担当者**: 
  - Cassandra Peretto (LATAM RHQ Digital Yield Management)
  - Irving Najera (LATAM CSM Tender Management)
  - Natan Gonzalez (LATAM CSM Tender Management)
  - Cristobal Ferron (LAWC Marketing)
  - Tatiane Viana (LAEC Marketing)
  - Flourance Tan (GHQ Eagle X)

## 今後の展開

1. **Conversion Tool更新**: 2024年7月までにConversion Toolのコードリファクタリングを完了
2. **メールグループの確認**: リファクタリング完了後、正しいグループアドレスが反映されていることを確認
3. **運用の継続**: 適切なメールグループへの配信を継続的に確認

## 関連ファイル

- [[Eagle-X-Email-Groups-Management]]
- [[LATAM-Pricer-Assignment]]
- [[Service-Scope-Management]]
- [[Conversion-Tool-Management]]

