import json
import requests
import jsonpath
import urllib.request
import urllib.parse
path_oral='https://api2.openreview.net/notes?content.venue=ICLR%202024%20oral&details=replyCount%2Cpresentation&domain=ICLR.cc%2F2024%2FConference&limit=25&'
path_spotlight='https://api2.openreview.net/notes?content.venue=ICLR%202024%20spotlight&details=replyCount%2Cpresentation&domain=ICLR.cc%2F2024%2FConference&limit=25&'
path_poster='https://api2.openreview.net/notes?content.venue=ICLR%202024%20poster&details=replyCount%2Cpresentation&domain=ICLR.cc%2F2024%2FConference&limit=25&'
path_decisionPending='https://api2.openreview.net/notes?content.venue=Submitted%20to%20ICLR%202024&details=replyCount%2Cpresentation&domain=ICLR.cc%2F2024%2FConference&limit=25&'
def get_id(url,offset):
    headers = {
                'cookie':'_ga=GA1.1.926646815.1652076197; __cuid=6e7a75c726ae4dd39d64b75000eba48a; amp_fef1e8=eec1aab1-0a18-42ea-8ce6-0d89117b5bf6R...1ha9bookf.1ha9bp5nc.4.1.5; _ga_3TRQ40799D=GS1.1.1694678934.1.1.1694679018.0.0.0; _ga_GTB25PBMVL=GS1.1.1706703827.4.1.1706704498.0.0.0',
                'origin':'https://openreview.net',
                'referer':'https://openreview.net/',
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                }
    id_list=[]
    for i in range(offset):
        response = requests.get(url+'offset='+str(i*25), headers=headers)
        html_str = json.loads(response.content.decode())
        id_list.extend(jsonpath.jsonpath(html_str, '$..id')) 
    return id_list
id_dict={}
id_dict['oral']=get_id(path_oral,4)
id_dict['spotlight']=get_id(path_spotlight,15)
id_dict['poster']=get_id(path_poster,72)
id_dict['decisionPending']=get_id(path_decisionPending,142)
for i in id_dict.values():
    print(len(i))
    
output_file_path = '/*****/id_dict.json'
with open(output_file_path, 'w') as json_file:
    json.dump(id_dict, json_file)
print(f'JSON file "{output_file_path}" has been created successfully.')