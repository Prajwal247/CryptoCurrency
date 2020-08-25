from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    # grab crpto price
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    # grad crypto news
    api_requests = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_requests.content)
    return render(request, 'home.html', {'api':api,'price':price})



def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        import requests
        import json
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote,'crypto':crypto})
    else:
        not_found = 'Search a CryptoCurrencyy above.....'
        return render(request, 'prices.html',{'not_found':not_found})
