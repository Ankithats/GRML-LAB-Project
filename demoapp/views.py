from django.shortcuts import render


# Create your views here.
def home(req):
    return render(req,'index.html')
def contact(req):
    return render(req,'contact.html')
def test(req):
    return render(req,'test.html')
def about(req):
    return render(req,'about.html')
def branch(req):
    return render(req,'branch.html')
def package(req):
    return render(req,'package.html')
def blog(req):
    return render(req,'blog.html')

def gal(req):
    return render(req,'gal.html')

def make(req):
    return render(req,'make.html')
def dep(req):
    return render(req,'dep.html')
def mon(req):
    return render(req,'mon.html')



