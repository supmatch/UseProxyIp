import requests
from pyquery import PyQuery


def get_ip_lists(num=1):
	url = 'https://www.xicidaili.com/nn/{}'.format(num)
	headers = {
		'User-Agent': 'Mozilla/5.0(Macintosh; Inter Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
	}
	html = requests.get(url, headers=headers).text
	html_table = PyQuery(html)('#ip_list tr')
	for items in html_table:
		ip = PyQuery(items)('td:nth-child(2)').text()
		port = PyQuery(items)('td:nth-child(3)').text()
		ip_http = PyQuery(items)('td:nth-child(6)').text()
		#这里的判断条件根据爬虫要访问的域名设定，访问https就用https的代理
		if ip_http == 'HTTP':
			continue
		else:
			key = 'https'
		value = '{}://{}:{}'.format(key, ip, port)
		proxy = {
			key: value
		}
		try:
			#headers看情况可以多弄几个进行随机，不然n多请求全是同样的headers可能会被反爬虫干掉
			response = requests.get('https://www.supmatch.xyz/', headers=headers, proxies=proxy, timeout=2)
			s = requests.session()
			print('{}---{}'.format(ip,response.status_code))
			s.keep_alive = False
		except:
			print('timeout')
#这里是循环页码，先跑个10页的ip	
for num in range(1,11):
	get_ip_lists(num)
