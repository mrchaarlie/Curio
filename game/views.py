from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import os
import datetime

#current_dir = os.path.dirname(__file__)  # get current directory

@login_required
def index(request):
    return render_to_response('index.html', locals())

def game(request):
    return render_to_response('game.html', locals()) 
