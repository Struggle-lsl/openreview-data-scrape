import json
import requests
import urllib.request
import urllib.parse
from tqdm import tqdm
def creat_request(i,key):
    base_url='https://api2.openreview.net/notes?forum='
    if key=='oral':
        url=base_url+i+'&content.venue=ICLR%202024%20oral'
    elif key=='spotlight':
        url=base_url+i+'&content.venue=ICLR%202024%20spotlight'
    elif key=='poster':
        url=base_url+i+'&content.venue=ICLR%202024%20poster'
    elif key=='decisionPending':
        url=base_url+i+'&content.venue=Submitted%20to%20ICLR%202024'
    headers = {
                'cookie':'_ga=GA1.1.926646815.1652076197; __cuid=6e7a75c726ae4dd39d64b75000eba48a; amp_fef1e8=eec1aab1-0a18-42ea-8ce6-0d89117b5bf6R...1ha9bookf.1ha9bp5nc.4.1.5; _ga_3TRQ40799D=GS1.1.1694678934.1.1.1694679018.0.0.0; _ga_GTB25PBMVL=GS1.1.1706703827.4.1.1706704498.0.0.0',
                'origin':'https://openreview.net',
                'referer':'https://openreview.net/',
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                }    
    request=urllib.request.Request(url=url,headers=headers)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content
def down_load(content,key,id):
    path='/****/'+key+'/information/'+id+'.json'
    with open(path,'w',encoding='utf-8') as fp:
        fp.write(content)
if __name__ == '__main__':
    file_path = '/id_dict.json'
    with open(file_path, 'r') as json_file:
        id_dict = json.load(json_file) 
    for i in list(id_dict.keys()):
        for j in tqdm(id_dict[i]): 
            try:     
                request = creat_request(j,i)
                content = get_content(request)
                down_load(content,i,j)
            except:
                pass

