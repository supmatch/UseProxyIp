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

		if ip_http == 'HTTPS':
			key = 'https'
		else:
			continue
		value = '{}://{}:{}'.format(key, ip, port)
		proxy = {
			key: value
		}
		try:
			response = requests.get('https://www.supmatch.xyz/', headers=headers, proxies=proxy, timeout=2)
			print('{}---{}'.format(ip_list,response.status_code))
		except:
			print('timeout')
			
for num in range(1,11):
	get_ip_lists(num)
