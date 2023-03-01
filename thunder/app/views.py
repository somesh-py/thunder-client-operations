from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    return render(request,'index.html')

def alldata(request):
    data=requests.get('http://tanveerpp.pythonanywhere.com/product/')
    data=data.json()
    print(data)
    return render(request,'showdata.html',{'data':data})

def showdata(request):
    return render(request,'showdata.html')

def showdataone(request):
    id=request.POST['id']
    data=requests.get('http://tanveerpp.pythonanywhere.com/product/'+id)
    data=data.json()
    print(data)
    return render(request,'showdata.html',{'data':[data]})

def adddetails(request):
    name=request.POST['name']
    price=request.POST['price']
    catagory=request.POST['cat']
    company=request.POST['cmp']
    res={'name':name,'price':price,'cat':catagory,'cmp':company}
    data=requests.post('http://tanveerpp.pythonanywhere.com/product/',res)
    data=data.json()
    print(data)
    return render(request,'showdata.html',{'data':data})