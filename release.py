import os
import json
import requests
import configparser
from urllib3 import *

disable_warnings()

path = "/Users/james/Pictures/测试样品/NO3/"

"""
TODO
批量并发上传
鞋子不同品牌尺码选择
文件夹迁移模块
错误重试
✅ cookies 解析模块
cookies 有效性验证
商品爬虫
其他商品的ID
"""

# 全局配置文件
config = configparser.ConfigParser()
config.read('/Users/james/Code/shopee/config.txt', encoding='utf-8')
# 常用变量定义
price = config.get('data', 'price')
sellable_stock = config.getint('data', 'sellable_stock')
# 商品类别映射
mapper = {
    '篮球鞋': [100637,100726,101298]
}
# cookies 文件解析
data_cookie = {}
header_cookies = ""
with open('cookies.txt', 'r') as content:
    cookies = json.loads(content.read())
for i in range(len(cookies)):
    data = json.loads(json.dumps(cookies[i]))
    temp = {data['name']: data['value']}
    data_cookie.update(temp)
    header_cookies += f"{data['name']}={data['value']}; "
header_cookies = header_cookies.replace('"', '\\"')
# 商品详情文件
with open(path + 'detail.json', 'r') as content:
    output = json.loads(content.read())
    
# 上传图片
def upload(image_path):
    image_encode = open(image_path, 'rb').read().decode("latin-1",errors='ignore')
    req = requests.post("https://seller.shopee.cn/api/v3/general/upload_image/",
        params={
            "SPC_CDS": "d05d282f-3101-4864-b375-66621f6584b4",
            "SPC_CDS_VER": "2",
            "cnsc_shop_id": f"{config.get('data', 'shopid')}",
        },
        data=f"""------WebKitFormBoundaryJBDkf5fKShesvHzh
Content-Disposition: form-data; name="file"; filename="blob"
Content-Type: image/jpeg

{image_encode}
------WebKitFormBoundaryJBDkf5fKShesvHzh--

""",
        headers={
            "Host": "seller.shopee.cn",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryJBDkf5fKShesvHzh",
            "origin": "https://seller.shopee.cn",
            "referer": "https://seller.shopee.cn/portal/product/mtsku/new?cnsc_shop_id=821694597",
            "sc-fe-session": "9ea406c5-c0ec-45f9-aef5-c2aaf2d213f1",
            "sc-fe-ver": "56878",
            "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
            "sec-ch-ua-mobile": "?0", 
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        },
        cookies=data_cookie,
        auth=(),
        verify=False
    )
    # 返回图片的 resource_id 列表
    return json.loads(req.text)['data']['resource_id']

image_linklist = []
files = os.listdir(path)
for file in files:
    if file.endswith(('.jpg', '.png', 'jpeg')):
        result = upload(path + file)
        image_linklist.append(result)

data = {
    "description": output['description'],
    "tier_variation": [
        {
            "images": [
                
            ],
            "name": "size",
            "options": [
                "BR34=EU36=22.5CM=US5.5",
                "BR34.5=EU36.5=23CM=US6",
                "BR35.5=EU37.5=23.5CM=US6.5",
                "BR36=EU38=24CM=US7",
                "BR36.5=EU38.5=24.5CM=US7.5",
                "BR37=EU39=25CM=US8",
                "BR38=EU40=25CM=US7",
                "BR38.5=EU40.5=25.5cm=US7.5",
                "BR39=EU41=26CM=US8",
                "BR40=EU42=26.5CM=US8.5",
                "BR40.5=EU42.5=27CM=US9",
                "BR41=EU43=27.5CM=US9.5",
                "BR42=EU44=28CM=US10",
                "BR42.5=EU44.5=28.5CM=US10.5",
                "BR43=EU45=29CM=US11"
            ]
        }
    ],
    "video_list": [
        
    ],
    "model_list": [
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                0
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                1
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                2
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                3
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                4
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                5
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                6
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                7
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                8
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                9
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                10
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                11
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                12
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                13
            ]
        },
        {
            "mtsku_model_id": 0,
            "seller_sku": "",
            "stock_setting_list": [
                {
                    "sellable_stock": sellable_stock
                }
            ],
            "normal_price": price,
            "is_default": False,
            "tier_index": [
                14
            ]
        }
    ],
    "condition": 1,
    "category_path": mapper[config.get('data', 'category_path')],
    "seller_sku": "",
    "ds_cat_rcmd_id": "",
    "description_type": "normal",
    "weight": config.get('data', 'weight'),
    "ds_attr_rcmd_id": "15cd68dc-e2b5-4a7c-86fe-618ab2a6ee75|a|EN",
    "brand_id": config.getint('data', 'brand_id'),
    "days_to_ship": config.getint('data', 'days_to_ship'),
    "size_chart": "",
    "attributes": [
        {
            "attribute_id": 100022,
            "attribute_value_id": 674
        }
    ],
    "dimension": {},
    "images": image_linklist,
    "mtsku_item_id": 0,
    "name": output['name']
}

# 构造请求发布商品
response = requests.post(
    url="https://seller.shopee.cn/api/v3/mtsku/create_mtsku/",
    params={
        "cnsc_shop_id": {config.get('data', 'shopid')},
    },
    headers={
        "Cookie": f"{header_cookies}",
        "Content-Type": "application/json; charset=utf-8",
    },
    data=json.dumps(data),
    verify=False
)

print("✅ 上架成功") if(json.loads(response.text)['code'] == 0) else print("失败")
#print(json.loads(response.text))
