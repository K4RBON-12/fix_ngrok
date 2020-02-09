

from requests import get
import os
import re


def get_https_proxys():
  global https_proxys
  global head

  head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.4; en-us; Nexus 4 Build/JOP24G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
  res = get(url="https://www.proxy-list.download/api/v1/get?type=https",headers=head)
  html = res.text
  https_proxys = re.findall(r"[\w\.?\:?]+",html)


def check_proxy():
  global http_proxy

  print("FIXING NGROK (Consertando ngrok) ...")
  working = []
  for prox in https_proxys:
    https_proxy = {"https":"https://"+prox}
    print(https_proxy)
    try:
      res = get(url="https://www.google.com/",headers=head,proxies=https_proxy,timeout=3)
      if res.status_code == 200:
        if not https_proxy in working:
          try:
            http_proxy = {"http":"http://"+prox}
            print(http_proxy)
            res = get(url="http://spys.one/",headers=head,proxies=http_proxy,timeout=3)
            if res.status_code == 200:
              print(res.status_code)
              http_proxy = http_proxy["http"]
              break
          except:
            None
    except:
      None

get_https_proxys()
check_proxy()

os.system("echo 'export http_proxy=\"{}\"' >> $HOME/.bashrc".format(http_proxy))

print("[+] NGROK FIXED AS SUCESS! (ngrok consertado com sucesso!)\n")
print("[*] TYPE 'bash' FOR IT WORK IN THIS TERMINAL! (digite bash para funcionar nesse terminal)")
