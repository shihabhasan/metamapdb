# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from mapping_stats import mapping_stats

# Create your views here.

def home(request):
   return render(request, 'index.html')

def manual(request):
   return render(request, 'help.html')

def contact(request):
   return render(request, 'contact.html')

def thanks(request):
   name=request.POST['name']
   email=request.POST['email']
   subject=request.POST['subject']
   message=request.POST['message']
   command = "echo 'Name: '"+name+"'\nEmail: '"+email+"'\nMessage: '"+message+" | mutt -s 'MathSpaceTasks Query: '"+subject+" -- pharm.shihab@gmail.com"
   subprocess.call(command, shell=(sys.platform!="Linux"))
   return render(request, 'thanks.html', { 'name': name })


# -----------UPDATE-----------------------------

def update(request):
   result=mapping_stats()
   context = {'result':result}
   return render(request, 'update.html', context)
