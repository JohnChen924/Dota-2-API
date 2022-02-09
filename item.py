import urllib, json
import socket

def item():
    url = 'http://api.steampowered.com/IEconDOTA2_570/GetGameItems/v1/?format=JSON&language=en_us&key=3A99C0D9D17ADD29409AB7700C6E9F6F'
    response = None
    connect = None 
    r = None 
    try:
        connect = urllib.request.urlopen('https://www.google.com')
    except:
        print("None internet connection")
        exit()
    try:
        response = urllib.request.urlopen(url)
        json_results = response.read()
        r = json.loads(json_results)
    except ConnectionError:
        print("Website does not exist")
        exit()
    except urllib.error.HTTPError as e:
        print("Failed to download contents")
        if e.code == 404:
            print("Forbidden url")
            exit()
        if e.code == 503:
            print("Overloaded website. Try again later")
            exit()
    except urllib.error.URLError as a:
        print("Invalid APIKEY or URL. Check again")
        exit()
        
    finally:
        if response != None:
            response.close()
        if r is not None:
            items = {}
            for i in r['result']['items']:
                items[i['localized_name']] = int(i['id'])
            return items
