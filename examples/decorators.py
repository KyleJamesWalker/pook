import pook
import requests


@pook.get('http://httpbin.org/status/500', reply=204)
@pook.get('http://httpbin.org/status/400', reply=200)
def fetch(url):
    return requests.get(url)

res = fetch('http://httpbin.org/status/400')
print('#1 status:', res.status_code)

res = fetch('http://httpbin.org/status/500')
print('#2 status:', res.status_code)

print('Is done:', pook.isdone())
print('Pending mocks:', pook.pending_mocks())
