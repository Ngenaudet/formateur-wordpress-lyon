"""Test d'intégration : python3 tests/course-access.py URL (code lu sur stdin)."""
import http.client
import re
import sys
from http.cookies import SimpleCookie
from urllib.parse import urlsplit, urlencode

url = urlsplit(sys.argv[1])
code = sys.stdin.readline().strip()
assert re.fullmatch(r'[0-9]{4}', code)
cookies = SimpleCookie()

def request(path='', method='GET', data=None, cookie=True):
    cls = http.client.HTTPSConnection if url.scheme == 'https' else http.client.HTTPConnection
    con = cls(url.hostname, url.port, timeout=10)
    headers = {}
    if cookie and cookies:
        headers['Cookie'] = '; '.join(f'{k}={v.value}' for k, v in cookies.items())
    body = urlencode(data) if data else None
    if body:
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
    con.request(method, url.path + path, body=body, headers=headers)
    r = con.getresponse()
    content = r.read()
    for k, v in r.getheaders():
        if cookie and k.lower() == 'set-cookie':
            assert 'httponly' in v.lower() and 'secure' in v.lower() and 'samesite=lax' in v.lower()
            cookies.load(v)
    result = r.status, dict(r.getheaders()), content
    con.close()
    return result

status, headers, body = request()
assert status == 200 and b'name="code"' in body and b'LE FIL ROUGE' not in body
assert 'no-store' in headers['Cache-Control']
csrf = re.search(rb'name="csrf" value="([a-f0-9]+)"', body)[1].decode()
assert request('assets/diapo-01.jpg', cookie=False)[0] == 403
assert request('assets/visuel-lumiere.png', cookie=False)[0] == 403
assert request('index.html', cookie=False)[2].find(b'name="code"') >= 0
assert request('access-config.php')[0] == 404
assert request('contenu-source.json')[0] == 404
assert request('slides.json')[0] == 404
assert request('LISEZ-MOI.md')[0] == 404
assert request('../index.html')[0] == 404
assert request(method='POST', data={'csrf': 'wrong', 'code': code})[0] == 403
assert request(method='POST', data={'csrf': csrf, 'code': '12345'})[0] == 401
status, headers, body = request(method='POST', data={'csrf': csrf, 'code': code})
assert status == 303 and headers['Location'] == url.path
assert b'LE FIL ROUGE' in request()[2]
status, headers, body = request('assets/diapo-01.jpg')
assert status == 200 and body[:2] == b'\xff\xd8'
assert request('assets/visuel-lumiere.png')[0] == 200
assert request('style.css')[0] == 200 and request('app.js')[0] == 200
assert request('assets/diapo-01.jpg', cookie=False)[0] == 403
cookies.clear()
_, _, body = request()
csrf = re.search(rb'name="csrf" value="([a-f0-9]+)"', body)[1].decode()
wrong = '0000' if code != '0000' else '1111'
for _ in range(5):
    assert request(method='POST', data={'csrf': csrf, 'code': wrong})[0] == 401
assert request(method='POST', data={'csrf': csrf, 'code': code})[0] == 429
cookies.clear()
_, _, body = request()
csrf = re.search(rb'name="csrf" value="([a-f0-9]+)"', body)[1].decode()
assert request(method='POST', data={'csrf': csrf, 'code': code})[0] == 429
print('Accès, ressources, cookies, CSRF et limite persistante de tentatives vérifiés.')
