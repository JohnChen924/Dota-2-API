import urllib, json
import socket

def history(hero = None, req = None, i = None):
    base = f"https://api.steampowered.com/IDOTA2Match_570/"
    url = base+'GetMatchHistory/V001/?format=JSON&language=en_us&key=3A99C0D9D17ADD29409AB7700C6E9F6F&account_id=' + str(i) +'&matches_requested=18'

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
            for i in r['result']['matches']:
                a.append(i['match_id'])
            return a
