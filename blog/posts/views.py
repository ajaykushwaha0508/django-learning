from django.shortcuts import render
from django.http import HttpResponse

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
               <h1>{data['id']} - {data['title']}</h1>
               <p>{data['content']}</p>
               </div>
'''
    return HttpResponse(html)