import webbrowser
import time
import psutil,os
from pykeyboard import PyKeyboard 

count = 0
  
url = 'URL of the blog needed to be visited'
k = PyKeyboard()


# k.press_key( k.alt_key )
# k.tap_key('d')
# k.release_key( k.alt_key )
# k.press_key( k.alt_key ) 
# k.tap_key(k.enter_key)
# k.release_key( k.alt_key )

while count< 200:
    webbrowser.get('C:/Users/ASUS/Desktop/Tor Browser/Browser/firefox.exe %s ').open(url, new=0) //Enter the location of TOR browser as stored on your PC

    # webbrowser.open(url, new=0)
    # k.press_key( k.alt_key )
    # k.tap_key('d')
    # k.release_key( k.alt_key )
    # k.press_key( k.alt_key ) 
    # k.tap_key(k.enter_key)
    # k.release_key( k.alt_key )
    
    count+=1
    time.sleep(20)
    k.press_key( k.alt_key)
    k.tap_key(k.function_keys[4])
    k.release_key(k.alt_key)
    #os.system("taskkill /im firefox.exe /f")
    time.sleep(5)
    
else:
    pass
