from hackip import hack_ip
from requests import get

ip = get('https://chat.openai.com/').text
# print(ip)
a = hack_ip()
print(a.my_ip_location(ip))


# try:
#     ip = get('https://chat.openai.com/').text
#     a = hack_ip()
#     print(a.my_ip_location(ip))
# except Exception as e:
#     print('Error occurred:', e)