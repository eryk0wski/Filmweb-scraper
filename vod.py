#URL_vod = 'https://www.filmweb.pl/search#/films?vodProviderIds=' + str(vod_dictionary[''])
#URL_min_reviews = 'https://www.filmweb.pl/search#/films?count=' + str(min_amount_reviews)
#URL_min_and_vod = 'https://www.filmweb.pl/search#/films?count=' + str(min_amount_reviews) + '%2C&vodProviderIds=' + str(vod_dictionary[''])

def GetUrlVod(streaming_service, minimum_reviews=0):

    vod_dictionary = {
    'Netflix': 2,
    'HboMax' : 1,
    'Disney' : 42, 
    'PremieryCanalPlus' : 5,
    'Player': 6,
    'PrimeVideo': 8,
    'SkyShowtime': 44,
    'Viaplay' : 31,
    'PlayNow' : 4,
    'AppleTV' : 9,
    'Cineman' : 28,
    'Ninateka': 18,
    'Rakuten' : 47,
    'Chili' : 11,
    'Megogo' : 50
    }
    URL = 'https://www.filmweb.pl/search#/films?count=' + str(minimum_reviews) + '%2C&vodProviderIds=' + str(vod_dictionary[str(streaming_service)])
    return URL

