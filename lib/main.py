import requests
import sys


class ClickJacking:

    def verifyDomain(self,url, cookies=""):
        try:
            r = requests.get(url, timeout=10, cookies=cookies)
            if r.status_code == 500 or r.status_code == 404:
                return False # means that the page is not responding
            else:
                self.isVulnerable(url, cookies)
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.TooManyRedirects:
            print("[*] Too many redirects..")
        except requests.exceptions.RequestException as e:
            print(f"[*] Bad thing happened..{e}")
            sys.exit(1)
    

    def isVulnerable(self, url, cookies=""):
        try:
            r = requests.get(url, timeout=10, cookies=cookies)
            headers = r.headers
            if "X-Frame-Options" not in headers:
                anw = input("[*] Generate a POC? y/n: ")
                if anw.lower()[0] == "y":
                    self.genPoc(url)
                    return True # is vulnerable
                else:
                    return True
            else:
                if headers["X-Frame-Options"] == "SAMEORIGIN" or headers["X-Frame-Options"] == "DENY" or headers["X-Frame-Options"][0:10] == "Allow-from":
                    return False # not vulnerable

                elif headers["X-Frame-Options"] == "sameorigin" or headers["X-Frame-Options"] == "deny" or headers["X-Frame-Options"][0:10] == "allow-from":
                    return False # not vulnerable
                else:
                    anw = input("[*] Generate a POC? y/n: ")
                    if anw.lower()[0] == "y":
                        self.genPoc(url)
                        return True # vulnerable
                    else:
                        return True
            
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.TooManyRedirects:
            print("[*] Too many redirects..")
        except requests.exceptions.RequestException as e:
            print(f"[*] Bad thing happened..{e}")
            sys.exit(1)


    def genPoc(self, url):
        html_str = f"""
                    <html>
                        <title> ClickJakcing PoC </title>
                        <h1>ClickJacking PoC </h1>
                        <iframe src={url} width="800" height="600"></iframe> 
                        <footer>
                            fr0stnull
                        </footer>
                    </html>
                    """
        Html_file= open("poc.html","w")
        Html_file.write(html_str)
        Html_file.close()


def toCookies(lista):
    cookies = dict()
    for k in lista:
        keyCookie, valueCookie = k.split('=')
        cookies.update({keyCookie:valueCookie})
        return cookies


t = ClickJacking()

# if u pass a list of cookies
if len(sys.argv[1:]) >= 1:
    cookies = toCookies(sys.argv[1:])
    # pass a URL BELLOW
    t.verifyDomain('', cookies)
else:
    # pass a URL BELLOW
    t.verifyDomain('')

