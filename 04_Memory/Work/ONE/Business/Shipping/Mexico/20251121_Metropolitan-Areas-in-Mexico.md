# Metropolitan Areas of Mexico - メキシコ大都市圏とロケーションコード

## 概要
メキシコの大都市圏（Metropolitan Areas）に関する資料です。IOP México 2022のデータに基づき、メキシコの主要都市圏とそのロケーションコード、大都市圏に含まれる周辺地域について詳細にまとめました。

## 内容

### ファイル情報
- **元ファイル**: `Metropolitan_Areas_in_Mexico_(1).pptx`
- **形式**: PowerPointプレゼンテーション
- **データソース**: IOP México. 2022
- **場所**: 00_Memo内に保存されていた資料

### Mexico City（メキシコシティ大都市圏）

#### メイン都市
- **Mexico City (MXMEX)**: メキシコシティ

#### メキシコシティ内の地区（16地区）
1. **ALVARO OBREGON**
2. **BENITO JUAREZ**
3. **AZCAPOTZALCO**
4. **COYOACAN**
5. **CUAJIMALPA**
6. **CUAUHTEMOC**
7. **GUSTAVO A MADERO**
8. **IZTACALCO**
9. **IZTAPALAPA**
10. **MAGADALENA CONTRERAS**
11. **MIGUEL HIDALGO**
12. **VENUSTIANO CARRANZA**
13. **MILPA ALTA**
14. **TLAHUAC**
15. **TLALPAN**
16. **XOCHIMILCO**

#### メキシコシティ大都市圏のその他の地域
| Name | Code |
|------|------|
| NAUCALPAN | MXNDJ |
| TLALNEPANTLA | MXTLP |
| CUAUTITLAN IZCALLI | MXCUT |
| TULTITLAN | MXTLL |
| NEZAHUALCOYOTL | MXNHY |
| COACALCO | MXCDB |
| ECATEPEC | MXEPC |
| LOS REYES | MXRYA |
| HUEHUETOCA | MXHUE |
| SATELITE | MXNDJ |
| ATIZAPAN | MXAZP |
| TEPOTZOTLAN | MXTPZ |
| TULTEPEC | MXTTP |
| CHIMALHUACAN | MXCMH |

**合計**: メキシコシティ大都市圏には、メキシコシティ内16地区 + 周辺14地域 = 合計30地域が含まれる

### Guadalajara（グアダラハラ大都市圏）

#### メイン都市
- **Guadalajara (MXGDL)**: グアダラハラ
  - **GUADALAJARA**

#### グアダラハラ大都市圏のその他の地域
| Name | Code |
|------|------|
| TLAQUEPAQUE | MXTLQ |
| ZAPOPAN | MXZAP |
| TLAJOMULCO DE ZUÑIGA | MXTLZ |
| TONALA | MXTON |
| EL SALTO, JALISCO | MXESO |

**合計**: グアダラハラ大都市圏には、グアダラハラ + 周辺5地域 = 合計6地域が含まれる

### Monterrey（モンテレイ大都市圏）

#### メイン都市
- **Monterrey (MXMTY)**: モンテレイ
  - **MONTERREY**

#### モンテレイ大都市圏のその他の地域
| Name | Code |
|------|------|
| APODACA | MXAPD |
| GENERAL ESCOBEDO | MXGEO |
| GUADALUPE | MXGLP |
| SALINAS VICTORIA | MXSAV |
| SAN PEDRO GARZA GARCIA | MXSPG |
| SAN NICOLAS DE LOS GARZA | MXSND |
| GARCIA | MXGCA |
| SANTA CATARINA | MXSTC |

**合計**: モンテレイ大都市圏には、モンテレイ + 周辺8地域 = 合計9地域が含まれる

### Querétaro（ケレタロ大都市圏）

#### メイン都市
- **Querétaro (MXQRO)**: ケレタロ
  - **SANTIAGO DE QUERETARO**

#### ケレタロ大都市圏のその他の地域
| Name | Code |
|------|------|
| SANTA ROSA DE JAUREGUI | MXSRO |
| EL MARQUES DE QUERETARO | MXELM |
| JURIQUILLA | MXJRQ |

**合計**: ケレタロ大都市圏には、ケレタロ + 周辺3地域 = 合計4地域が含まれる

### Toluca（トルカ大都市圏）

#### メイン都市
- **Toluca (MXTLC)**: トルカ
  - **TOLUCA**

#### トルカ大都市圏のその他の地域
| Name | Code |
|------|------|
| LERMA | MXLER |
| SAN MATEO ATENCO | MXSMA |
| OCOYOACAC | MXOYO |
| METEPEC | MXMPC |

**合計**: トルカ大都市圏には、トルカ + 周辺4地域 = 合計5地域が含まれる

### 大都市圏別サマリー

| 大都市圏 | メイン都市コード | メイン都市名 | 周辺地域数 | 合計地域数 |
|---------|----------------|------------|-----------|-----------|
| Mexico City | MXMEX | Mexico City | 14 | 30 |
| Guadalajara | MXGDL | Guadalajara | 5 | 6 |
| Monterrey | MXMTY | Monterrey | 8 | 9 |
| Querétaro | MXQRO | Santiago de Queretaro | 3 | 4 |
| Toluca | MXTLC | Toluca | 4 | 5 |

**合計**: 5大都市圏、合計54地域

### ロケーションコードの使用例

#### Pricing業務での使用
- **POR (Place of Receipt)**: 大都市圏内のロケーションコードを使用
- **DEL (Place of Delivery)**: 大都市圏内のロケーションコードを使用
- **Inland Haulage**: 大都市圏へのInland輸送の計算に使用

#### 例: Mexico Cityへの配送
- **メイン都市**: MXMEX（Mexico City）
- **周辺地域**: MXNDJ（Naucalpan）、MXTLP（Tlalnepantla）など
- **Inland Haulage**: 港（例：Lazaro Cardenas、Manzanillo）からMXMEXへのInland輸送

#### 例: Guadalajaraへの配送
- **メイン都市**: MXGDL（Guadalajara）
- **周辺地域**: MXZAP（Zapopan）、MXTLQ（Tlaquepaque）など
- **Inland Haulage**: 港からMXGDLへのInland輸送

### 関連情報
- [[20251121_Mexico-Pricing-メキシコ特有の港とルール]]: メキシコの港情報
- [[20251121_Mexico-Pricing-基本ルールとTigerシステム]]: MX Inlandの確認フロー
- **MX Inland**: メキシコ内陸輸送はカルロスに確認すること
- **IOP México**: メキシコのIOP（Inland Operations）チーム

### 確認事項
- [ ] 各大都市圏のロケーションコードを確認
- [ ] Inland Haulageの計算方法を確認
- [ ] 港から各大都市圏への配送時間を確認

## 次アクション
- [ ] 都市圏情報をMemory Noteに変換（[[04_Memory/Work/ONE/Business/Shipping/Mexico/]]）
- [ ] MX Inlandのルールと統合
- [ ] Pricing業務で使用する際の参考資料として活用

#mexico #metropolitan-areas #inland #logistics #location-codes #iop #inbox

