# ipip-ipdb-hp
High performance IPIP.net unofficially database ipdb format parsing library

# Python Parse ipdb file

## Installing
```
python3 setup.py build
python3 setup.py install
```

## 官方库性能对比
### C Version
```
python3 ipdotnet_benchmark.py
Load: 0.034990s  List Used: 0.2513652s  QPS: 397826/s
Load: 0.286393s  Dict Used: 0.2991660s  QPS: 334262/s
```
### Py Version
```
Load: 0.074412s   List Used: 4.2106075s  QPS: 23750/s
Load: 4.285052s   Map  Used: 4.4340391s  QPS: 22553/s
```

## Code Example
### 适用于IPDB格式的每周高级版，每日标准版，每日高级版，每日专业版，每日旗舰版
  <pre><code>
import ipdb

db = ipdb.City("/path/to/city.ipv4.ipdb")
# db.reload("/path/to/city.ipv4.ipdb") # update ipdb database file reload data
print(db.is_ipv4(), db.is_ipv6())
print(db.languages()) # support language
print(db.fields()) #  support fields
print(db.build_time()) #  build database time
print(db.find("1.1.1.1", "CN")) #  query ip return array
# print(db.find(u"1.1.1.1", "CN")) #  Python 2.7
print(db.find_map("8.8.8.8", "CN")) #  query ip return dict
print(db.find_info("118.28.1.1", "CN").country_name) 
  </pre></code>

### 地级市精度库数据字段说明
<pre>
country_name : 国家名字 （每周高级版及其以上版本包含）
region_name  : 省名字   （每周高级版及其以上版本包含）
city_name    : 城市名字 （每周高级版及其以上版本包含）
owner_domain : 所有者   （每周高级版及其以上版本包含）
isp_domain  : 运营商 （每周高级版与每日高级版及其以上版本包含）
latitude  :  纬度   （每日标准版及其以上版本包含）
longitude : 经度    （每日标准版及其以上版本包含）
timezone : 时区     （每日标准版及其以上版本包含）
utc_offset : UTC时区    （每日标准版及其以上版本包含）
china_admin_code : 中国行政区划代码 （每日标准版及其以上版本包含）
idd_code : 国家电话号码前缀 （每日标准版及其以上版本包含）
country_code : 国家2位代码  （每日标准版及其以上版本包含）
continent_code : 大洲代码   （每日标准版及其以上版本包含）
idc : IDC |  VPN   （每日专业版及其以上版本包含）
base_station : 基站 | WIFI （每日专业版及其以上版本包含）
country_code3 : 国家3位代码 （每日专业版及其以上版本包含）
european_union : 是否为欧盟成员国： 1 | 0 （每日专业版及其以上版本包含）
currency_code : 当前国家货币代码    （每日旗舰版及其以上版本包含）
currency_name : 当前国家货币名称    （每日旗舰版及其以上版本包含）
anycast : ANYCAST       （每日旗舰版及其以上版本包含）
</pre>

### 适用于IPDB格式的中国地区 IPv4 区县库
  <pre>
import ipdb

db = ipdb.District("/path/to/china_district.ipdb")
print(db.is_ipv4(), db.is_ipv6())
print(db.languages())
print(db.fields())
print(db.build_time())
print(db.find("1.12.13.255", "CN"))
print(db.find_map("1.12.13.255", "CN"))
  </pre>

### 适用于IPDB格式的基站 IPv4 库
<pre>
import ipdb
db = ipdb.BaseStation("/path/to/base_station.ipdb")
print(db.is_ipv4(), db.is_ipv6())
print(db.languages())
print(db.fields())
print(db.build_time())
print(db.find_map("117.136.83.55", "CN"))
</pre>