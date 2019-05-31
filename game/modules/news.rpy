init python:
    import io
    import re
    import urllib
    
    def news_catcher():
        def parse(data):
            data = evaluate(data)
            for item in data:
                item.append(None)
                if "{bg=" in item[1]:
                    img = re.search("\{bg=*.*\}", item[1]).group(0).strip("\{bg=").strip("\}")
                    img = urllib.urlretrieve(img, config.basedir+"/game/cache/"+str(item[0])+".png")  
                    item[4] = "cache/"+str(item[0])+".png"
                    item[1] = re.sub("\{bg=*.*\}", "", item[1])
            return data
        news_pull = urllib2.Request(binascii.unhexlify("687474703a2f2f3137322e3130342e3132392e36303a383038302f6e6577732f616c6c"))
        news_get = urllib2.urlopen(news_pull, timeout=10).read()
        news = parse(news_get) #news_get.read()
        return news