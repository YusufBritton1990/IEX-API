from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def transactions(request):
    return render(request, 'portfolio/transactions.html')
