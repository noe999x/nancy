# JANGAN UBAH APAPUN...
import os, time
from time import sleep
try:
	os.system('git pull')
except:pass
try:
    os.system('clear')
    print('Tools sedang dalam pemeliharaan');time.sleep(4)
    print('Untuk info selanjutnya bisa hubungi saya!');time.sleep(3)
except:pass
def atmin():
    print('\nKetik oke untuk menuju profile facebook author')
    nancy = input('\nTekan enter untuk exit program\n\n')
    if nancy in ['oke','ok']:
        print('Anda akan diarahkan ke halaman profile facebook author')
        time.sleep(2)
        os.system('xdg-open https://www.facebook.com/bagasekaapr')
    elif nancy in['',' ']:
        print('\nTerimakasih sudah mau menunggu~\n Maaf atas ketidaknyamanannya ya!');exit()
    else:print('asu lo!');exit()
atmin()
