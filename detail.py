import urllib, json
import socket

def detail(acc = None, id = None):
    base = f"https://api.steampowered.com/IDOTA2Match_570/"
    url = base+'GetMatchDetails/V001/?format=JSON&language=en_us&key=3A99C0D9D17ADD29409AB7700C6E9F6F&match_id=' + str(id)

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
            a = []
            for i in r['result']['players']:
                if str(i['account_id']) == str(acc):
                    kda = int(i['kills']) + int(i['assists'])
                    kda = float('{:.2f}'.format(kda/int(i['deaths'])))
                    a.append((i['hero_id'],kda))
            return a
