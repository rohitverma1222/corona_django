from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.
def home(request):
    city="world"
    url=f'https://coronavirus-19-api.herokuapp.com/countries/{city}'
    data=requests.get(url).json()

    payload={'kity':data['country'], 'case':data['cases'], 'death':data['deaths'], 'recovered':data['recovered']}
    return render(request,'index.html', {'data':payload})

def search(request):
    searchcity=request.GET['box']
    url=f'https://coronavirus-19-api.herokuapp.com/countries/{searchcity}'
    data=requests.get(url).json()
    payload={'kity':data['country'], 'case':data['cases'], 'death':data['deaths'], 'recovered':data['recovered']}
    return render(request,'search.html', {'data':payload})