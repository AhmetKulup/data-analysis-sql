# data-analysis-sql
A collection of SQL practice queries focusing on inventory analysis, sales insights, and supplier performance — based on realistic operational data scenarios.


 **inventory_analysis.sql** | Düşük stok, hızlı dönen ürünler gibi depo yönetimi içgörülerini çıkaran sorgular. |
| **sales_summary.sql** | Aylık gelir, en çok satan ürünler, müşteri analizleri gibi temel satış KPI’larını hesaplar. |
| **supplier_performance.sql** | Tedarikçilerin zamanında teslim oranı ve maliyet performansını analiz eder. |





 The data model I used

Bu SQL sorgularını yazarken şu üç temel tabloyu baz aldım.  
Gerçek veri yok, ancak veri modeli tamamen iş mantığına dayanıyor:

### **1. sales**
Satış hareketlerini temsil eder.

| Column | Meaning |

| `sale_date` | Satış tarihi |
| `product_id` | Ürün ID |
| `customer_id` | Müşteri ID |
| `quantity_sold` | Satılan adet |
| `total_amount` | Toplam satış tutarı |
| `category` | Ürün kategorisi |

-

### **2. inventory**
Depodaki ürün stok bilgileri.

| Column | Meaning |

| `product_id` | Ürün ID |
| `product_name` | Ürün adı |
| `stock_quantity` | Mevcut stok |
| `reorder_level` | Yeniden sipariş seviyesi |


### **3. purchase_orders**
Tedarikçi ve satın alma süreçleri.

| Column | Meaning |

| `supplier_id` | Tedarikçi ID |
| `product_id` | Ürün ID |
| `unit_cost` | Birim maliyet |
| `expected_delivery_date` | Beklenen teslim tarihi |
| `delivery_date` | Gerçek teslim tarihi |


Phyton için;
The repository includes a mini data pipeline demonstrating beginner-friendly 
data analysis:

1. data_cleaning.py → handles nulls, fixes types, creates new columns
2. basic_analysis.py → computes KPIs such as monthly revenue and top products
3. visualization.py → turns the KPIs into clear charts (line, bar, pie)
