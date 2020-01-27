from django.shortcuts import render
from django.conf import settings #Needed to get enviromental variable
from django.http import HttpResponse

import requests

# Create your views here.
def quote(request):

    """Prod"""
    # api_key = settings.IEX_API_KEY
    # secret_key = settings.IEX_SECRET #optional, only if requested

    # base_url = "https://cloud.iexapis.com/"

    """Test"""
    api_key = settings.IEX_API_KEY_TEST
    # secret_key = settings.IEX_SECRET_TEST #optional, only if requested

    base_url = "https://sandbox.iexapis.com/"

    """API Call"""
    symbol = "IBM"
    field = "" #optional, begin with a "/" if using

    iex_url = f"{base_url}stable/stock/{symbol}/quote{field}?token={api_key}"

    r = requests.get(
        iex_url
        # headers = {'Content-type': 'application/json'}
    )

    return HttpResponse(r)
