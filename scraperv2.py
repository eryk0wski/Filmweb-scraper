from playwright.sync_api import sync_playwright
import time
from rich import print
import pandas as pd
import json

def scrolling():
    def check_json(response):
        try:
            if "preview" in response.url:
                #print({"url": response.url, "body": response.json()})
                json_file = response.json()

                genres = []
                for genre in range(len(json_file['genres'])):
                    genres.append(json_file['genres'][genre]['name']['text'])


                columns = [json_file['year'], json_file['entityName'],json_file['description']['synopsis'],
                               json_file['description']['sourceType'],json_file['originalTitle']['title'],genre,json_file['plotOrDescriptionSynopsis']]
                df.loc[len(df)] = columns
            if "rating" in response.url:
                json_file = response.json()

                columns = [json_file['count'], json_file['rate'], json_file['countWantToSee']]
                rating.loc[len(rating)] = columns
                
        except ValueError:
            print('Value_Error')

        except:
            print('Other error')


    def json_to_pandas(json_file, row_number):
        
        genres = []
        for genre in range(len(json_file['genres'])):
            genres.append(json_file['genres'][genre]['name']['text'])
        df.loc[row_number] = [json_file['year'], json_file['entity_name'],json_file['description']['synopsis'],
                               json_file['description']['sourceType'],json_file['original_title']['title'],genre,json_file['plotOrDescriptionSynopsis']]
  
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size(
            {"width":1280, "height": 1080}
        )
        rating = pd.DataFrame(columns = ['count','rating','want_to_see'])
        df = pd.DataFrame(columns = ['year','entity_name','summary','source_type', 'original_title','genre', 'plot_describtion'])
        page.on("response", lambda response: check_json(response))
        page.goto("https://www.filmweb.pl/films/search")
        time.sleep(2)
        page.click("#didomi-notice-agree-button", timeout=2_000)

        page.wait_for_load_state("networkidle")

        for i in range(20):

            page.mouse.wheel(0, 7000)
            print("Scrolling")
            time.sleep(1)
            #if bottom_header:



        time.sleep(5)
        browser.close() 

        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())

        data_file = moment + 'filmweb.csv'
        rating_file = moment + 'ratings.csv'


        df.to_csv(data_file, index=False, encoding='utf-8')
        rating.to_csv(rating_file, index = False, encoding ='utf-8')



def main():
    scrolling()

if __name__ == "__main__":
    main()