from bs4 import BeautifulSoup as bs
import pandas as pd
import re

def LibgenScraper(session, query, headers):

    ## Webscraping Variables

    MAIN_URL = 'http://libgen.rs/'
    RESULTS = []


    url = 'search.php'

    data = {
        "req": query,
        "lg_topic": "libgen",
        "open": 0,

        "view": "simple",
        "res": 100,
        "phrase": 1,
        "column": "def"
    }
    r = session.get(MAIN_URL + url, headers=headers,  params=data)
    print('req : ', r.content)
    if r.status_code == 200:
        soup = bs(r.content, 'lxml')
        table = soup.find('table', {'class':"c"})
        if table:
            df = pd.read_html(str(table))[0]
            df.columns = df.iloc[0]
            df = df[1:]
            df['Year'] = df['Year'].fillna("N/A")
            pattern = r'\[.*?\]|\b\d{3}-\d{1,5}-\d{1,7}-\d\b'

            df['Title'] = df['Title'].apply(lambda x : re.sub(pattern, '', x).strip())

            if df.__len__()>0:
                results = table.find_all('tr')[1:]
                if results != [] :
                    DAATA = []
                    for i in results:
                        data = {}
                        id = i.find('td').text
                        data['ID'] = id
                        if id is None:
                            pass
                        else:
                            print('[*] ID : ', id)
                            inf = i.find('td', {'width':'500'}).find('a', {'id':id})
                            URLID = inf.get('href')

                            data['Link'] =MAIN_URL + URLID
                            data['md5_ID'] = URLID.split('md5=')[-1]
                            print(data)
                            DAATA.append(data)
                    links= pd.DataFrame(DAATA)
                    df = df.merge(right=links, how='inner')

            else:
                return {'status':'402',"message":'No Data', 'results':[]} # No Table Found
        else:
            return {'status':'403',"message":'No Data', 'results':[]} # No Results

    if df.__len__()>0:
        return {'status':'200',"message":'success', 'results': df.to_dict('records')}

    return {'status':'404',"message":'No Data', 'results':[]} # No Table Found


def GET_DOWNLOADLINK(session, md5, headers ):
    dlpage = f'http://library.lol/main/{md5}'
    LINKS = []
    r = session.get(dlpage, headers=headers)
    if r.status_code == 200 :
        soup = bs(r.content, 'lxml')
        dl_container = soup.find('div',{'id':'download'})
        if dl_container != None:
            UL = dl_container.find('ul')

            for links in UL.find_all('li'):
                data = {'CLOUD':links.text,'LINK':links.find('a').get('href')}
                LINKS.append(data)
    return LINKS