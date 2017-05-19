#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html

html = requests.get("http://rekvizitai.vz.lt/imone/uab_2it_baltic/").content
dom = lxml.html.fromstring(html)

#for entry in dom.cssselect('.theentry'):
#    post = {
#        'įmonės_kodas': entry.cssselect('.entry-title')[0].text_content(),
#        'pvm_kodas': entry.cssselect('.the-meta a')[0].text_content(),
#        'vadovas': entry.cssselect('a')[0].get('href'),
#        'adresas': int( entry.cssselect('.comment-number')[0].text_content() ),
#        'telefonas': entry.cssselect('table a')[0].text_content()
#    }
#    print post
for tr in root.cssselect("div[class='info'] tr"): 
    tds = tr.cssselect("td") 
        if len(tds)==12: 
            data = { 
                'įmonės_kodas': tds[0].text_content(), 
                'pvm_kodas': int(tds[4].text_content()) 
            } 
    print data

    #scraperwiki.sql.save(['url'], post)
