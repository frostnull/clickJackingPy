# clickJackingPy
clickJackingPy is a way to automate and test whether a domain is vulnerable to an attack category called "ClickJacking" for more information here https://www.geeksforgeeks.org/clickjacking-ui-redressing/.

### Install / from PEPL
```
git clone https://github.com/frostnull/clickJackingPy/.git
$ pip install .
>>> import ClickJacking
>>> t = ClickJacking()
>>> t.verifyDomain('https://example.com') #if want use cookies pass a dict cookies like {"foo":"bar"}
>>> cookies = {"foo":"bar"}
>>> t.verifyDomain('https://example.com', cookies)
```

### Usage / from SRC
```
go to lib/main.py
1º Without cookies: type your URL inside t.verifyDomain('https://foo.bar')

2º With (cookies)!: type your URL inside t.verifyDomain('https://foo.bar') and when you execute the script, pass the cookies like
python3 lib/main.py cookieName=value1 cookieName2=value2 cookieName3=valu3

3º If the target is vulnerable, will asking you to generante a simple PoC just.. open the same browser that you're testing the application

```

###### TODO
argument command line
