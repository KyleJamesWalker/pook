import sys, os
sys.path.append(os.path.dirname(__name__))

import http.client
import pook


with pook.use():
    pook.get('http://httpbin.org/ip',
             reply=404, response_type='json',
             response_json={'error': 'not found'})

    conn = http.client.HTTPConnection('httpbin.org')
    conn.request('GET', '/ip')
    res = conn.getresponse()
    print('Status:', res.status, res.reason)
    print('Headers:', res.headers)
    print('Body:', res.read())

    print('Is done:', pook.isdone())
    print('Pending mocks:', pook.pending_mocks())
    print('Unmatched requests:', pook.unmatched_requests())
