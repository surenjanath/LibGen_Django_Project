from bs4 import BeautifulSoup as bs
import pandas as pd

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

    if r.status_code == 200:
        soup = bs(r.content, 'lxml')
        df = pd.read_html(r.content)[-2]
        df.columns = df.iloc[0]
        df = df[1:]
        if df.__len__()>0:
            # Assuming the table you want has a specific ID, replace 'table_id' with the actual ID
            table = soup.find_all('table')[2]

            if table:
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
                            URLID = i.find('td', {'width':'500'}).find('a', {'id':id}).get('href')
                            data['Link'] =MAIN_URL + URLID
                            data['md5_ID'] = URLID.split('md5=')[-1]
                            print(data)
                            DAATA.append(data)
                    links= pd.DataFrame(DAATA)
                    df = df.merge(right=links, how='inner')
            else:
                return {'status':'403',"message":'No Data', 'results':[]} # No Results
        else:
            return {'status':'402',"message":'No Data', 'results':[]} # No Table Found

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