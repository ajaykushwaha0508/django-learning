from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


dummyData = [
  {
    "id": 1,
    "title": "Getting Started with Django",
   "content": "This article explains the basics of setting up a Django project, creating apps, and running the development server."
  },
  {
    "id": 2,
    "title": "Understanding REST APIs",
   "content": "Learn how REST APIs work, why they are used, and how to build secure APIs using Django REST Framework."
  },
  {
    "id": 3,
    "title": "Deploying Applications to Production",
   "content": "This guide covers best practices for deploying web applications, including environment variables, security, and server configuration."
  }
]


def helloWorld (request) : 
    return HttpResponse("Hello World")

def home (request):
    html  = ''

    for data in dummyData: 
          html += f'''
               <div>
               <a href='/posts_app/home/{data['id']}'>
               <h1>{data['id']} - {data['title']}</h1>
               </a>
               <p>{data['content']}</p>
               </div>
'''
    return HttpResponse(html)


def getContent(request ,id):
      html  = ''
      validId = False
      for data in dummyData: 
           if data['id'] == id :
                foundedData = data
                validId = True
                break

      if validId:
            html += f'''
                    <div>
                    <h1>{foundedData['id']} - {foundedData['title']}</h1>
                    <p>{foundedData['content']}</p>
                    </div>
        '''
            return HttpResponse(html)
      else:
            return HttpResponseNotFound("Post Not Found")
      


def redirectTo(request ,id):
     url = reverse("posts" ,args=[id])
     return HttpResponseRedirect(url)


def blog(request):
     return render(request ,'blog.html' ,{"name" : "Ajay" ,"posts" : dummyData})

def about(request):
     return render(request ,'about.html' ,{"name" : "Ajay" ,"work" : "developer" ,"posts" : [] })