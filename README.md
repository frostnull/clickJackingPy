# clickJackingPy
clickJackingPy is a way to automate and test whether a domain is vulnerable to an attack category called "ClickJacking" for more information here https://www.geeksforgeeks.org/clickjacking-ui-redressing/.


### Usage
```
go to lib/main.py
1º Without cookies: type your URL inside t.verifyDomain('https://foo.bar')

2º With (cookies)!: type your URL inside t.verifyDomain('https://foo.bar') and when you execute the script, pass the cookies like
python3 lib/main.py cookieName=value1 cookieName2=value2 cookieName3=valu3

3º If the target is vulnerable, will asking you to generante a simple PoC just.. open the same browser that you're testing the application

```

###### TODO
argument command line
