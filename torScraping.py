from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from torrequest import TorRequest
import random
import time
from fake_useragent import UserAgent
import pickle

with open('founderDetails.pickle', 'rb') as founderDetails:
    b = pickle.load(founderDetails)
ua = UserAgent()

user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    # 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    # 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    # 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    # 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # #Firefox
    # 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    # 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    # 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    # 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    # 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    # 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    # 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    # 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    # 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    # 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    # 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    # 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    # 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
]

cookie_list = [
'__cfduid=d63103a23911b6586d60636d5bd3c3a241580982979; _pxhd=61487ace6980357cf9a64dcc03b7a12b6fec626d34ee8a04bbdd690aa11194c9:ec8adf31-48c6-11ea-91b1-8ba0e36f2b83; cid=rBsAml488HlrUgAtBRSwAg==; _pxvid=ec8adf31-48c6-11ea-91b1-8ba0e36f2b83; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _hp2_id.973801186=%7B%22userId%22%3A%221898666675396062%22%2C%22pageviewId%22%3A%222211643164967162%22%2C%22sessionId%22%3A%227173270544524748%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga=GA1.2.637854430.1580983000; _gid=GA1.2.1929749373.1580983000; _fbp=fb.1.1580983001098.1346634639; _pxff_wa=1; _px3=7c606f0756ff04d5d955a60f8cf22a17559e28acbd504afe542ba11744b6adc5:tfgQmS5U9iYQUQHGGSJZag1I7X7kv3NGj+1rkl/4JfKWKpSiizt5N9iddQtEYuSvzuW8ou9xwiQIMN5fJHzXOg==:1000:Mv9AxcJdfudmo0arDROIziECiEU58i3YtNXeJOV5o7lzxoQcLpyn8dO0Ol889cYkJq8OaleIE7oAaDhrw5ZXUQtgipgZ5hLnv0mgW+EtW2oFU0q9wU6/f50asMfsH+5HENJlA/+gTp8D5pEAQ0A4l7WUZ3uS1oGocLl8db84o3E=; _hp2_ses_props.973801186=%7B%22ts%22%3A1581052024967%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fbrian-marshal%22%7D; _gat_UA-60854465-1=1',
'__cfduid=dbe4883bb21964e36566a6c02160925c61581052209; _pxhd=b75177d4956478e01dc99b330508f6d4aaee0a1cbbc10fe777c83c2ad85c9a36:1cf38811-4968-11ea-9fd7-5522d8731b5d; cid=rBsRdl488UOiOAAwBQUyAg==; _pxvid=1cf38811-4968-11ea-9fd7-5522d8731b5d; _pxff_wa=1; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _hp2_ses_props.973801186=%7B%22ts%22%3A1581052214423%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fbrian-marshal%22%7D; _hp2_id.973801186=%7B%22userId%22%3A%221300013350074804%22%2C%22pageviewId%22%3A%221224380967581933%22%2C%22sessionId%22%3A%227133636706607583%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _px3=6427678a3a061993c79cd805b8a154169c9d9b2e629f98f3ada33b9c2e820a3e:l11+rDdVYE2THODdLHGVoVhEVb7MiUcr8YWutE1+wgzNg8Eokw5dz5rLeIz7QY3OJyaHtCf7bMkk2/AHZpHZHg==:1000:6wG2PsN8i+LThj98/mD0mJbMzV/WLWn9czFkums8AAriE9oSaq2/RLUhiInYYdfx4HbHOLMt9nXEJbw4P4Z5mGnwwTmIRAhaAt0LNC0lZXVx7aY28hFFm1xIEwEF0hauBbYzE9SjsOxnlQrnYQ2hCi7a8RUrZXV0ogFmuXeKxPQ=',
# IE
'_px3=72e9860225612d52af9c98ec87ed5796dba24b5c7ef7b281f8f965185305fb77:/8DJ/fpJMBCTTDC9kodwsBCXNKg/mL6rCjkep7t+S//0vvHewcojLWwkrTCUPFahawWFSEH750ikoaMf1kc7UQ==:1000:uGIadi/KPlORiQmOX8wjPkCwL9G781Np/3Hg+AlPDvRjy+1qPpas3j1jSCg6b3/XbcURddFvn0340yO02OlyslNG/03AMxBNQRbYctW6E8Tjxge4O+RWcs5OHXrMC6h2LW9+4LUKt8IaZMqxrzwDP9UGpwq4zfVzcwiSOxRFAgM=; cid=rBsIHF49AZSXTQAwB+8gAg==; _hp2_id.973801186=%7B%22userId%22%3A%226024373890856327%22%2C%22pageviewId%22%3A%221978321788804081%22%2C%22sessionId%22%3A%226830375570021912%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.973801186=%7B%22ts%22%3A1581056154793%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fjose-calderon%22%7D; _gid=GA1.2.111870463.1581056160; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _ga=GA1.2.2038405085.1581056160; __cfduid=d91932b7f5cf7fd137aa83e0d7344e5311581056136; _fbp=fb.1.1581056155739.1445468280; _pxvid=41a20251-4971-11ea-bf20-434ec49f234b; _pxhd=fe5fdaec25653c700f178a7f0fcefb16ee7f4164f13607b9a72b2a6be8d50bcc:41a20251-4971-11ea-bf20-434ec49f234b',
'__cfduid=dd23cfa15563594b59474020075c1240e1581056761; cid=rBsRdl49A0qiOAAwBViAAg==; _pxvid=b60965b1-4972-11ea-8582-677f4b782595; _ga=GA1.2.1413593090.1581056787; _gid=GA1.2.82370889.1581056787; _gat_UA-60854465-1=1; _px3=1f1c5af2a3914e4605bf96c65e69471513baf6b9284dcc438476d0ba8508850c:P7EOPOmdguIwqd/sDxIXST4FdNOs8S34d6oa0GYOCdVrcFRwZh/AUq/sG/jrvxmU5/RWOZh0CROIhn47HWHCnA==:1000:xe87jd9ZUdAAAP55JyEH1l2sqsXYJwD2cgqe1/1ewjgYkt+zyk/h75V02IcaLKnpm8Kgr6nOuEHMLcdoPRGByTLediwgMiR6IUblsOHl9cy7tS4gYuDJzAc1w++W5gmQIQE+UkhjN1qI/U4XUuKVF8+5LtRgYtaKWZm6GpvDs+E=; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _hp2_ses_props.973801186=%7B%22ts%22%3A1581056794164%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fjose-calderon%22%7D; _hp2_id.973801186=%7B%22userId%22%3A%224332950280930744%22%2C%22pageviewId%22%3A%227318260657457309%22%2C%22sessionId%22%3A%225281494773061247%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _fbp=fb.1.1581056798730.369134177; _pxhd=801755b06470aa19dd33f93f0ac807449e0d346e41cae498e715fd3f194f56bf:b60965b1-4972-11ea-8582-677f4b782595; _pxff_ne=1; _pxff_wa=1',
'cid=rBsAml49CQ9reAAvCHt/Ag==; __cfduid=d0e9d28be2d30b0e344aeed1f36a5e0dc1581058315; _pxvid=3eb661d1-4976-11ea-8dbf-3bbb0fb16bd7; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _ga=GA1.2.1927318105.1581058305; _gid=GA1.2.1167145260.1581058305; _gat_UA-60854465-1=1; _hp2_ses_props.973801186=%7B%22ts%22%3A1581058306668%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fariane-goldman%22%2C%22g%22%3A%22%23section-overview%22%7D; _hp2_id.973801186=%7B%22userId%22%3A%227730547364312001%22%2C%22pageviewId%22%3A%226381741712854217%22%2C%22sessionId%22%3A%221072417730352375%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _px3=576c37f5f0abb83f3297113800acba9df0cfef590920afa8b51cd286899538f4:dKyO/44GSjdmwuK7iw+DJwzj8kZ/7c3rPzp2g5YQsaDTDb1UDCu2XW2p/cjcmU/2z34VRGylOyz4AA5o5RJnQA==:1000:qN3u6IDBal5YLbLzhq92sxjb4XfgXW1VHZhPCWd7cibYDB2V71KZLKb6aVGiRrIBQSLBgf/Y9Z2IS8YYs5OGUZ+jC0/Zobip+xqoXq0PqdVQCCW+LNygwJABZEEREw//2kuyV8I8iJF3z0Y463czYkbQ/uOd3/3TH1zOuQhTA8E=; _fbp=fb.1.1581058313186.1657791799; _pxhd=a1e03306808a19148bbd004c61ce4de3deecf198ce682c338e00e3a59cd57da8:3eb661d1-4976-11ea-8dbf-3bbb0fb16bd7; _pxff_wa=1',
'__cfduid=d7766aeefb0781996c29c6931483be0fc1581058457; cid=rBsAml49CZlreAAvCH5uAg==; _pxvid=8f3cb371-4976-11ea-93de-bd5bef7cea81; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _hp2_ses_props.973801186=%7B%22ts%22%3A1581058444239%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fariane-goldman%22%7D; _hp2_id.973801186=%7B%22userId%22%3A%225167357719664228%22%2C%22pageviewId%22%3A%227227754425569457%22%2C%22sessionId%22%3A%224204245250212284%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _px3=82f70f8c9a81aab93ecaa8ef071cd1f5bf685a60ecdfe03cd75558f1bc197fda:6xpBCEpOuUHwqauDm0rBJtgc9iO2Ky1r74DRGtqY07HCLDxkx71rG67UyErtQszjHZZSMSlosQiH8Ft8SPqSwQ==:1000:UXnwRjsx/qy9Y36/3rxqy7CzFi8henh4yad5D32V6Yzjn9bUp8U4T85NLfoL40SWrq8Fk+Qgjkwq5cKH8beI7HxD8zxjOJicfFIB5ez6CdsNIdkBn8GMzJ/kmzXIBCgW9RRNzEBOi2z7Kq7SBMdRZBlrpCJzgYW52zTGX8sPENA=; _ga=GA1.2.1154045230.1581058459; _gid=GA1.2.923402773.1581058459; _gat_UA-60854465-1=1; _pxhd=81271d1768ce72dc975ddf0840d69eadebe31ff6e72e4ea0d860633b1ae5d5d0:8f3cb371-4976-11ea-93de-bd5bef7cea81; _pxff_wa=1',
# chrome
'__cfduid=d38bee50c1369edd0e2f59aeec73a538c1580903222; _pxhd=595bb66a01fcfd6ea7ac605a6604e4e92a369cfbd43bf5f5de61d8512af6babd:396f4670-480d-11ea-9268-07bd5f5f5af9; _pxvid=396f4670-480d-11ea-9268-07bd5f5f5af9; _ga=GA1.2.1342162083.1580903226; _fbp=fb.1.1580903226621.2005885991; cid=rBsRdl49A++g4wAuA07nAg==; _pxff_ne=1; _gid=GA1.2.158092137.1581057073; _hp2_ses_props.973801186=%7B%22ts%22%3A1581057074794%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fjose-calderon%22%7D; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJmMzYyN2I1OC04YzQ1LTQzMDEtODkwZC0zNTZiZTg1YjdhOTEiLCJpc3MiOiJ1c2Vyc2VydmljZV9mMDg0MGI2OV8xODkiLCJzdWIiOiIyNzE0ZjVkMC01NTNkLTQ3NGYtODE1ZC1hMWZiYzM1ZGM3YTUiLCJleHAiOjE1ODEwNTc0NDUsImlhdCI6MTU4MTA1NzE0NSwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTRuUjNoQ01tN0wvczVwaGdQekpFZDZwMFM1MW9nWkRpNE5jVU9yNmQ0a2hIdnF0cDc2bDFMc3dBc1paZ21yOTVHYzYrTi9rSFhOTk15S0p6aHdWc3BINml3dm0zd3NYSW54YzFEQjFqRS93VlVPSGw5WFBiNTJmS29HWEdqMktCd01yQTBUTkE3T0lqRG9wZWlRR0tTVjczOVZTOWpZc2ZSZTY1Y04xSlVteXhxcVlDeGV6cFZ6emViZDJpQkdTeHE1anlSL1NLWFdCZWJuelhmOXdkWEVNVytWbGZMYm1nR0lJQzA4NWpVQmkxbEZoRnFXWWJqSFg0ZHkxb2xERGVmYzBsSTVrbmJoQlZLc3dURktwTWo5azM0UityQ1plY3hhc2FDZytzaXBXIn0.KjMte7ROESy7f5J3s97YG3LCOf_Qcwn5n_DLnT25vkdPnV3xB3l6eRzkfb2zy4K0IG891P3OwG5W_xRO3oyc2Q; _hp2_id.973801186=%7B%22userId%22%3A%22243685083507237%22%2C%22pageviewId%22%3A%225195149793517989%22%2C%22sessionId%22%3A%224039868582475717%22%2C%22identity%22%3A%22sportyrish96%40yahoo.in%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; _hp2_props.973801186=%7B%22Logged%20In%22%3Atrue%7D',
'__cfduid=dc431a79e60da13b8cf495d9a857eb6751581057255; _pxhd=0923ee0603295f314fa426bcc39c6edc67b45d900f59d98a6c958474cc891817:dc346771-4973-11ea-b095-bf58a66ad1aa; _pxvid=dc346771-4973-11ea-b095-bf58a66ad1aa; _pxff_wa=1; _px3=f5398d05355d0c92eb4bd3220beaefe54864e7e2324db722c6185a39eeb5c8ca:pxB8oTW5CVyCyqQnbzH6dWKK6lhvz7InPQbmFGm2JVdYJPd6ml+mBcJXPpIBBne73BD4MJWTYzmVAlOXY69VfQ==:1000:yZt8klbc0DCx32NFwznIBFBck8SNikGIMi2wesrFblOg/5I6A2zS+NWCMgvd3RVd0LwGw8mqsN50+eyTr8HrxFgrnBHUqUXR8NcpIVemp8MI0R4f27dp2pR/WhiQafNOjhbMzYYAIbrF6x9x/8/Dg5OW9FYTHQjYiR2WE248sfo=; cid=rBsRql49BRIVzAA0CC/gAg==',
'__cfduid=d38bee50c1369edd0e2f59aeec73a538c1580903222; _pxhd=595bb66a01fcfd6ea7ac605a6604e4e92a369cfbd43bf5f5de61d8512af6babd:396f4670-480d-11ea-9268-07bd5f5f5af9; _pxvid=396f4670-480d-11ea-9268-07bd5f5f5af9; _ga=GA1.2.1342162083.1580903226; _fbp=fb.1.1580903226621.2005885991; _gid=GA1.2.158092137.1581057073; _hp2_ses_props.973801186=%7B%22ts%22%3A1581057074794%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fjose-calderon%22%7D; _hp2_props.973801186=%7B%22Logged%20In%22%3Atrue%7D; _hp2_id.973801186=%7B%22userId%22%3A%22243685083507237%22%2C%22pageviewId%22%3A%228062364566735579%22%2C%22sessionId%22%3A%224039868582475717%22%2C%22identity%22%3A%22sportyrish96%40yahoo.in%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJmMzYyN2I1OC04YzQ1LTQzMDEtODkwZC0zNTZiZTg1YjdhOTEiLCJpc3MiOiJ1c2Vyc2VydmljZV9mMDg0MGI2OV8xODkiLCJzdWIiOiIyNzE0ZjVkMC01NTNkLTQ3NGYtODE1ZC1hMWZiYzM1ZGM3YTUiLCJleHAiOjE1ODEwNTc5MzMsImlhdCI6MTU4MTA1NzYzMywicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTRuUjNoQ01tN0wvczVwaGdQekpFZDZwMFM1MW9nWkRpNE5jVU9yNmQ0a2hIdnF0cDc2bDFMc3dBc1paZ21yOTVHYzYrTi9rSFhOTk15S0p6aHdWc3BINml3dm0zd3NYSW54YzFEQjFqRS93VlVPSGw5WFBiNTJmS29HWEdqMktCL1pZbXlFSU9mU3JFV2t1MDRhTFEvM1ZwTnMveUR4alFLTDcxNkliTXN6WDlnWXZ2NHJJVEgzcWRyQm8rZnFkTjZQaEFZKzNRWjRSeUMxa3hjK2tESm1qMTZIR3YwQTI3S3I2Ui8ydVdrUzJCUDdGSGdMMlkveS9WUjREekpMQm15Tmo4VzNnQkhrNXpaVVhQVENNaWRVU2svajBxT2FSL2RXOWE3K05oL2grUzJHQ1p0Y0ZHMjZrWnVFTE8rNW83UT09In0.Z0JsKa-2jUpexCTQissB-RQ1JX55-LKUDhZAsk_wHqTF5yeIHoudWMTsmePWVNEcpE4sM5MrCuj_CJTi1SUxFg; _pxff_wa=1; _gat_UA-60854465-1=1; cid=rBsd1l49BmxAQQAwCDKIAg==; _px3=916d1b7a8bbd42d684f90bc5c6565b4ca202b2091ec9adc3148f0bd343576f12:nup0P1noEnIZ2H2aGld1w7hOWaWcvEUOI9vF3hRf1gowK6+DGjxJT+kdlBURyAFnsNMPFwI5xds7+gGbFl5tzw==:1000:S6zGexaGcdLi3iSwiGAUX/P2xT0uaM3d9EqvltnMhXvWAwFZbdINfXdv8cLk+iTwzY5lnccNwjNg731/oUNjILlBj6eGlvd0dhW47YrwBcGFIHYOwVg+fB+LDizCehpW3VnL/EvHDuzsoP27+W+lONXR8uPFZNH4/WeSpJodZgk=',
'__cfduid=dc431a79e60da13b8cf495d9a857eb6751581057255; _pxhd=0923ee0603295f314fa426bcc39c6edc67b45d900f59d98a6c958474cc891817:dc346771-4973-11ea-b095-bf58a66ad1aa; _pxvid=dc346771-4973-11ea-b095-bf58a66ad1aa; _px3=f5398d05355d0c92eb4bd3220beaefe54864e7e2324db722c6185a39eeb5c8ca:pxB8oTW5CVyCyqQnbzH6dWKK6lhvz7InPQbmFGm2JVdYJPd6ml+mBcJXPpIBBne73BD4MJWTYzmVAlOXY69VfQ==:1000:yZt8klbc0DCx32NFwznIBFBck8SNikGIMi2wesrFblOg/5I6A2zS+NWCMgvd3RVd0LwGw8mqsN50+eyTr8HrxFgrnBHUqUXR8NcpIVemp8MI0R4f27dp2pR/WhiQafNOjhbMzYYAIbrF6x9x/8/Dg5OW9FYTHQjYiR2WE248sfo=; cid=rBsLO149BS6lggAwCGi4Ag==; _pxff_ne=1; _pxff_tm=1; _ga=GA1.2.1590708953.1581057327; _gid=GA1.2.2079308424.1581057327; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _hp2_id.973801186=%7B%22userId%22%3A%226402932174157627%22%2C%22pageviewId%22%3A%228779524215646485%22%2C%22sessionId%22%3A%227260558729441410%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.973801186=%7B%22ts%22%3A1581057331994%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fjose-calderon%22%7D; _fbp=fb.1.1581057406192.1293584495; _gat_UA-60854465-1=1',




]

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Content-Type': 'application/json; charset=utf-8'}
headers1 = {
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
# cache-control: max-age=0
# dnt: 1
# sec-fetch-mode: navigate
# sec-fetch-site: same-origin
# sec-fetch-user: ?1
# upgrade-insecure-requests: 1
'user-agent': 
# 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'}
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

headers2 = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
# cache-control: max-age=0
'dnt': '1',
# sec-fetch-mode: navigate
# sec-fetch-site: same-origin
# sec-fetch-user: ?1
# upgrade-insecure-requests: 1
# 'cookie' : '__cfduid=d63103a23911b6586d60636d5bd3c3a241580982979; _pxhd=61487ace6980357cf9a64dcc03b7a12b6fec626d34ee8a04bbdd690aa11194c9:ec8adf31-48c6-11ea-91b1-8ba0e36f2b83; cid=rBsFWl474tmFvAAwINzfAg==; _px3=b1fe3560c2d4bff4df24672e217d2c2598b6ee7bd14b87b725f30786a4bc0e31:IAqaQ4znepmP0MGW2QMTouxBA+f+HJ4s7z72bnMAXS2rUgkgPQagDO35CS0QF7Z1V93jwf6m42/4DxmiIAh4BA==:1000:9zHejld38akhbaMBCjtk2ZxTVXcvQ8v+MGSnMWu3zKoJh4RpmJ/PC14gxqDgAhr5McTBm5aFVFmN1GVqMkiMuZKZTkCwFw1xZGEgx3gizO6JBS3Fq3QxOjPIyhEkNTedV1j8fTjAZIo1e3TmkjK8t/yX/OMSlKU1lX+IyrOJOMY=; _pxvid=ec8adf31-48c6-11ea-91b1-8ba0e36f2b83; _pxff_wa=1; _pxff_tm=1; _pxff_ne=1; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _hp2_ses_props.973801186=%7B%22ts%22%3A1580982999595%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fjiby-thomas%22%2C%22g%22%3A%22%23section-overview%22%7D; _hp2_id.973801186=%7B%22userId%22%3A%221898666675396062%22%2C%22pageviewId%22%3A%224289803178933498%22%2C%22sessionId%22%3A%223916880317364292%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga=GA1.2.637854430.1580983000; _gid=GA1.2.1929749373.1580983000; _gat_UA-60854465-1=1; _fbp=fb.1.1580983001098.1346634639',
# 'cookie': '__cfduid=dc8e9afe0d514432a5409c5257eaf980f1580891053; _pxhd=71118eac2817d141d6521b5614023ae582f06925e8b9c567f97c245af9a1a832:e4305f81-47f0-11ea-a852-b37908212520; _pxvid=e4305f81-47f0-11ea-a852-b37908212520; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%7D; _ga=GA1.2.1007903799.1580891064; _gid=GA1.2.2065855134.1580891064; _fbp=fb.1.1580891064747.1394099720; cid=rBsL3146rJ0IcAAvGzbUAg==; _pxff_wa=1; _gat_UA-60854465-1=1; _hp2_id.973801186=%7B%22userId%22%3A%228983544961729747%22%2C%22pageviewId%22%3A%221383448139880665%22%2C%22sessionId%22%3A%226302847062768594%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _px3=7f35ab2b50838a116058a7975d3172289535474f2203943aa88827d2e6117bea:PpPKTfUVb4wSfBuOJFdAErtUmwKdALO8jMcUvqZR9ylzKEzUr2lwHEX3XXeYNL+pwNSpQcEKDwFHyoxN6FhzyA==:1000:UkdH/b73sJZ6Iex94bcQTV9aJm3YyE4oaub67vfHb/5sDu+sv/m6sViq55dy75VijALEzzgFl+FZ7dHymd7tvyLNhlJ+e1XoE9cJ+AAtdninWu2KUtz8kZgZ8wLPCdkAa7CJ8FjqD0wReg01zA6Y/Hh7uWvuISratY0vpr0W2dA=; _hp2_ses_props.973801186=%7B%22ts%22%3A1580903582727%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fperson%2Fjiby-thomas%22%7D',
# 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}

# 'https://www.crunchbase.com/person/jiby-thomas'
# 'https://www.crunchbase.com/person/pranay-chulet'


path  = 'ecommerce/'
headers = headers1

import glob, os
files = glob.glob("ecommerce/*.htm") + glob.glob("ecommerce/*.html")
founderRows = []
founderRowsHeading = [['founderName','companyName', 'companyWebsite', 'founderTitle', 'foundersLocation', 'linkedinLink', 'facebookLink', 'twitterLink']]

counter = b['totalRowsExtracted']
brk = False
maxTries = 4
tryNumber = 0
totalFoundersLinks = len(b['data'])-1
for file in sorted(files)[3:5]:

    
    print(file, '   file in the process....\n')
    f = open(file, "r").read()
    soup = BeautifulSoup(f, 'html.parser')
    companyRows = soup.find_all('grid-row', class_='ng-star-inserted')
    for companyRow in companyRows[b['totalRowsExtracted']:]:
        with open('founderDetails.pickle', 'rb') as founderDetails:
            b = pickle.load(founderDetails)
        counter+=1
        print('\n\n\n\n\n============================================================================================Row No : {} ===================================================='.format(counter))
        try:
            companyName = companyRow.find('grid-cell', class_='column-id-identifier ng-star-inserted').find('div', class_='flex-no-grow cb-overflow-ellipsis identifier-label').text
            print('companyName : ', companyName, '\n')
        except:
            print('companyName not found')
        try:
            companyWebsite = companyRow.find('grid-cell', class_='column-id-website ng-star-inserted').find('a', class_='cb-link component--field-formatter field-type-link layout-row layout-align-start-end ng-star-inserted')['href']
            print('companyWebsite : ', companyWebsite, '\n')
        except:
            print('companyWebsite not found')
        foundersLinks = companyRow.find('grid-cell', class_="column-id-founder_identifiers ng-star-inserted")
        # print('companys founders crunch links : ',foundersLinks, '\n')
        if foundersLinks:
            foundersLinks = foundersLinks.find_all('a', class_='cb-link ng-star-inserted')
        if len(foundersLinks) != 0:
            print('total number of founders : {}'.format(len(foundersLinks)))
            # foundersLink.append([a['href'] for a in a])
            # for foundersLink in foundersLinks:
            i=0
            founderRowsTemp = []
            while i < len(foundersLinks):
                foundersLink = foundersLinks[i]

                print('\n\n..........................................................founders crunch link to be hit  : {}......................................\n'.format(foundersLink['href']))
                totalFoundersLinks+=1
                print('founder number : .....    {}\n'.format(totalFoundersLinks))
                with TorRequest(proxy_port=9050, ctrl_port=9051, password=None) as tr:
                  tr=TorRequest(password='linux')
                  print('headers. used : {}\n'.format(headers))
                  resp = tr.get(foundersLink['href'], headers = headers)
                  response = tr.get('http://ipecho.net/plain')
                  print(response.text)
                  print(resp.status_code)
                  # print(resp.headers)
                  # headers2['cookie'] = resp.headers['Set-Cookie'] 
                  # print(resp.headers)
                  print('Holding to reset_identity IP .....\n')
                  tr.reset_identity()
                # html = requests.get(foundersLink['href'])
                # print('\n\nhtml response : {}\n\n'.format(html))
                # bs = BeautifulSoup(driver.page_source,"html.parser")
                # bs = BeautifulSoup(html,"html.parser")
                if resp.status_code == 200:
                    # user_agent = ua.random
                    # headers = {'user-agent': user_agent}
                    headers = headers1
                    tryNumber = 0
                    # headers2['cookie'] = resp.headers['Set-Cookie']
                    i += 1
                    
                    bs = BeautifulSoup(resp.text,"html.parser")
                    founderName = bs.find('image-with-fields-card').find('span', class_='ng-star-inserted').text
                    try:
                        founderTitle = bs.find('image-with-fields-card').find('span', class_='component--field-formatter field-type-text_short ng-star-inserted').text
                    except:
                        print('founderTitle not found\n')
                        founderTitle = 'NA'
                    else:
                        print("Nothing went wrong founderTitle : ", founderTitle)
                    try:
                        foundersLocation = bs.find('span', class_='component--field-formatter field-type-identifier-multi').find_all('a')
                        foundersLocation = (', ').join([a.text for a in foundersLocation])
                    except:
                        print('Location not found\n\n')
                        foundersLocation = 'NA'
                    else:
                        print("Nothing went wrong foundersLocation : ", foundersLocation)
                    links = bs.find_all('a', class_="cb-link component--field-formatter field-type-link layout-row layout-align-start-end ng-star-inserted")
                    # founderTitle = bs.find_all('span', class_='component--field-formatter field-type-text_short ng-star-inserted')
                    # foundersLocation = bs.find_all('span', class_='component--field-formatter field-type-identifier-multi')
                    linkedinLink = 'NA'
                    facebookLink = 'NA'
                    twitterLink = 'NA'
                    for l in links:
                        if 'linkedin.com' in l['href']:
                            print('link in for loop : ',l['href'])
                            linkedinLink = l['href']
                        if 'facebook.com' in l['href']:
                            print('link in for loop : ',l['href'])
                            facebookLink = l['href']
                        if 'twitter.com' in l['href']:
                            print('link in for loop : ',l['href'])
                            twitterLink = l['href']
                    # driver.close()
                    founderDetailRow = [founderName, companyName, companyWebsite, founderTitle, foundersLocation, linkedinLink, facebookLink, twitterLink] 
                    print(founderDetailRow, '\n')
                    founderRowsTemp.append(founderDetailRow) 
                    sleepTime =  4+(1*random.random() + 1*random.random())*random.random()
                    print('SLEEPING for {} seconds.....'.format(sleepTime))
                    time.sleep(sleepTime)
                else:
                    if tryNumber == 4:
                        print('Automation Detected at Row no. : {} and founder link : {}'.format(companyRows.index(companyRow), foundersLink['href']))
                        brk = True
                        tryNumber = 0
                        break
                        i+=1
                    # user_agent = random.choice(user_agent_list)
                    setCookie = random.choice(cookie_list)
                    print('!! .......... ........... .... cookie  changed to  : {}. Try number : ............ {}  \n'.format(setCookie, tryNumber))
                    # headers2['user-agent'] = user_agent
                    headers2['cookie'] = setCookie 
                    headers = headers2
                    # sleepTime =  (1*random.random() + 1*random.random())*(tryNumber+1)*random.random()
                    sleepTime =  1*random.random() + 1*random.random()
                    print('SLEEPING for {} seconds.....'.format(sleepTime))
                    time.sleep(sleepTime)
                    
                    
                    
                    tryNumber +=1
                    
                    # founderRowsTemp.append([str(foundersLink['href']), 'NOT SCRAPED']) 
                    
                    # user_agent = ua.random
                    # headers = {'User-Agent': user_agent}
                    # sleepTime = 1*random.random() + 1*random.random() + 1*random.random()
                    # print('\nSLEEPING for {} seconds due to SERVER ERROR .....\n'.format(sleepTime))
                    # founderRows.append([])
                    # time.sleep(sleepTime)
            if len(foundersLinks) == len(founderRowsTemp):
                founderRows = founderRows + founderRowsTemp
                haltRowIndex = companyRows.index(companyRow)
                print('successful parsed upto  : ', haltRowIndex)
            else:
                haltRowIndex = companyRows.index(companyRow)
                print('unsuccessful parsed upto  : ', haltRowIndex)
            if brk:
                break

                    
                
        else:
            
            print('---- No founders found -----')
            founderRows.append([companyRows.index(companyRow),'Row - No Founders','NA','NA','NA','NA','NA','NA']) 
        b = {'data': b['data'] + founderRows,
            'totalRowsExtracted' : companyRows.index(companyRow)}
        # with open('founderDetails.pickle', 'wb') as founderDetails:
        #     pickle.dump(b, founderDetails, protocol=pickle.HIGHEST_PROTOCOL)
    if not brk:
        with open('founderDetails_'+file.split('.')[0].split('/')[1]+'.pickle', 'wb') as founderDetails:
            pickle.dump(b, founderDetails, protocol=pickle.HIGHEST_PROTOCOL)
        b = {'data': founderRowsHeading,
            'totalRowsExtracted' : 0}
        with open('founderDetails.pickle', 'wb') as founderDetails:
            pickle.dump(b, founderDetails, protocol=pickle.HIGHEST_PROTOCOL)
        print('\n\n\nALL ROWS DONE IN {}\n'.format(file))
        
# founderRowsHeading = founderRowsHeading + founderRows

# b = {'data': b['data'] + founderRows,
# 'totalRowsExtracted' : companyRows.index(companyRow)}


# import pandas as pd
# # df = pandas.read_csv('hrdata.csv', 
# #             index_col='Employee', 
# #             parse_dates=['Hired'],
# #             header=0, 
# #             names=['Employee', 'Hired', 'Salary', 'Sick Days'])
# # df.to_csv('hrdata_modified.csv')
# df = pd.DataFrame(founderRowsHeading)
# df.to_excel("foundersDetails.xlsx") 
