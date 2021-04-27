# How to intercept GMail API calls via mitmproxy

GMail client must be installed first:

```
pip3 install --user google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

Now it is possible to send email (with credentials.json from service account):

```
./send.py
```

Next step is to run mitmproxy :

```
pip3 install --user mitmproxy
./intercept.py
```

Now we can add `ca_certs='/home/enp/.mitmproxy/mitmproxy-ca.pem'` param to httplib2.Http constructor in GMail API implementation and send email via mitmproxy:

```
vi $HOME/.local/lib/python3/site-packages/googleapiclient/http.py
https_proxy='http://127.0.0.1:8080' ./send.py
```
