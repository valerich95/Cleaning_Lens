import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from .utils import get_image_bytes 
import re



def google_shop(input_query_model):
    session = requests.Session()
    url = "https://consent.google.com/save"
    payload = 'bl=boq_identityfrontenduiserver_20231024.06_p0&x=8&gl=NL&m=0&app=0&pc=srp&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Ftbm%3Dshop%26q%3DMidwest%2BSL54DD%2BDog%2BBed%2BLarge%26start%3D0%26hl%3Den&hl=en&uxe=eomcrt&cm=4&set_eom=true'
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'NID=511=WmWxhoF_A8ufnA94OEChvW1Rl2Tz6MZZ42orbP1WOQG3qDzz0YMOHWLI7o3dgBn05oskcpDlmLc54VkJgW0syuM_c_sXqACKXJyR9lDhfiDI2PV25Eqv_H7ottD9SOgzgJ0Bhj9j36qh7pPCa_2bmolrTRLt2TxA5nOuDL1PWLlq9z1M6akVuAAlm-eU70qQ25KpNqiPitV8q9ydq4_hYg4gHI1TldPTBZtWLX60tORvqViB9j5Pr36Wks1p6iGpfld9Jiv0lULUaYtEIni0A2MznIGfvQsVCj5mp4sU5GAy4hM; SID=cQij1XZTyTp4HLV0hJCRZxeAZGYFgK9_8Lkx3boJW2v5216V3FTY6Sof23GXdUD8dSqZCw.; __Secure-3PSID=cQij1XZTyTp4HLV0hJCRZxeAZGYFgK9_8Lkx3boJW2v5216VENLG5ldCQHq3pc825hPKXQ.; HSID=AcmsXIbmMRg28olRQ; SSID=AtUl69CN-nETaCVyL; APISID=kzCKCe-rTqze3ypd/Aln08ulFRMqCBWRh-; SAPISID=OZCHhU0feFROv6Jk/A8voFyFpfveKHT8uF; __Secure-3PAPISID=OZCHhU0feFROv6Jk/A8voFyFpfveKHT8uF; SIDCC=ACA-OxN76CoeAuvJreQwm-j8m2GQWgmDbz6BF3IcY3FXnwgtdywgt8nM7LeeLfsMCidlAW0BRCPA; __Secure-3PSIDCC=ACA-OxPzk6fD_YzLl1vUfPTrWphJMA0ykcrYUUCSKVhL4Th0j3I8MWJjidVXPCm2SwnSyHO3egw; 1P_JAR=2023-10-28-17; CONSENT=PENDING+757; __Secure-1PSID=cQij1XZTyTp4HLV0hJCRZxeAZGYFgK9_8Lkx3boJW2v5216VrTvYSVDKOGoPodPVFHEnXQ.; __Secure-1PAPISID=OZCHhU0feFROv6Jk/A8voFyFpfveKHT8uF; __Secure-1PSIDCC=ACA-OxO_dHE0k4ASlfMiPUccnb3lKSLXrKCgJY5DGpB-SUdAv2KkA3fjxzGRUAq4_6YzniIc1JI; __Secure-1PSIDTS=sidts-CjIBNiGH7qLePQbXsyFJ4v9wU-ZpzLGcI4qg6guY5hLwTf3yDA3tJ9GI6mKGiW1rCzezwBAA; __Secure-3PSIDTS=sidts-CjIBNiGH7qLePQbXsyFJ4v9wU-ZpzLGcI4qg6guY5hLwTf3yDA3tJ9GI6mKGiW1rCzezwBAA; AEC=Ackid1QfNTtzVNqX8HIPPSYg-VbcYXf08W3OOK-hLvkv950qy-jxmY79Bj0; NID=511=oLzpfsjZMm9Xtfi5Q_KYghLSluruk1xE5ExDfeF6CrON7X8efdPMtfExnSDrcmMSeAfxxokbQucCWrKIOc_VBI3TEbMVDKIQhMlcaLm5mte7b7AywJekCvOOX3sU4zZ-CGhwab9hdIwAc5IF-Vl6zNsdEkyF7IlJUnY8BnAlnl4eKcidd7rw6HPX_W849Sb5s0_xXVXncDEtqNx-R3j5kf35qXjLuarCywOgoyHk7FB3nfja-StghJMKtreVu8X3oNaV',

    }
    session.post( url, headers=headers1, data=payload)
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",  # Do Not Track
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "Sec-GPC": "1",  # Google's privacy settings
    }
    product_list = []
    start = 0
    product_qty = input_query_model.product_qty
    page_counter = 0
    while (page_counter<product_qty//20):
        params = {
        'tbm': 'shop',
        'q': input_query_model.search_query,
        'start':start,
        'hl' : 'en',
        }
        cookies = {'CONSENT':"YES+cb.20220419-08-p0.cs+FX+111"}
        try:
            page = session.get('https://www.google.com/search',
                                params=params,
                                headers=headers,
                                cookies=cookies)
            page.status_code ==200
        except Exception as e:
            return(e)
        # with open('./t.html' , 'r') as file:
        #     page = file.read()
        # soup = BeautifulSoup(page , 'html.parser')
        soup = BeautifulSoup(page.text , 'html.parser')

        try:
            next = soup.find_all(class_='lYtaR')
        except Exception:
            return( 'google may recognize you as a bot, please try again later')
        if not next:
            next = None
            print ('Cant find next page')
        else:
            next = next[len(next)-1]
        if next:
            new_start_point= int(re.findall('(?<=start=)\d+' , (next['href']))[0])
            if new_start_point>start:
                start = new_start_point
                print(f'\t\t{start} ====> start\n')
            else:
                print(f'new_start_point is not find : {new_start_point}')
                print('End of Products')
                break

        elements = soup.find_all('div' , class_='u30d4')
        if not len(elements):
            return ('Not Found')
            break
        for element in elements:
            # seller_link
            try:
                link = element.find(class_='rgHvZc').a['href']
                link = re.findall('http.*' , link)[0]
            except:
                link =None
            # image_link
            try:
                image_link = element.find(class_='oR27Gd').img['src']
            except:
                image_link = None
            # text
            try:
                description =element.find(class_ = 'rgHvZc').text
            except Exception as e:
                description = e
            try:
                price_text = element.find(class_='HRLxBb').text
            except:
                price_text = None
            try:
                get_price=re.search(r'[.,\d]+' , price_text)

                price = price_text[0:get_price.end()].replace(',' ,'')
                specs = price_text[get_price.end():].strip()
            except:
                price = None
                specs = None

            product ={
                'description' : description,
                'website' : link,
                'image' : image_link,
                'specs': specs,
                'estimated_price' : price,
            }

            product_list.append(product)
        with ThreadPoolExecutor(40) as executor:
                for product in product_list:
                    executor.submit(get_image_bytes, product)
        page_counter +=1
    return product_list


