#!/usr/bin/env -S mitmdump -s

import base64, re, json

from mitmproxy import ctx, http    

def response(flow: http.HTTPFlow) -> None:
    if flow.request.path == '/token':
        assertion = str(base64.urlsafe_b64decode(flow.request.urlencoded_form.get('assertion')))
        data = json.loads(re.findall(r'\{.+?\}(\{.+?\})', assertion)[0])
        ctx.log.info('REQUEST TOKEN FOR [%s] FROM [%s]' % (data.get('scope'), data.get('sub')))
        data = json.loads(flow.response.text)
        ctx.log.info('REQUEST TOKEN [%s]' % data.get('access_token'))
    elif flow.request.path == '/gmail/v1/users/me/messages/send?alt=json':
        ctx.log.info('REQUEST SEND WITH TOKEN [%s]' % flow.request.headers.get('authorization').replace('Bearer ',''))
        ctx.log.info('REQUEST SEND TEXT: %s' % base64.urlsafe_b64decode(json.loads(flow.request.text).get('raw')))
        ctx.log.info('RESPONSE SEND TEXT: %s' % json.loads(flow.response.text))
