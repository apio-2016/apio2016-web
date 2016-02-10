# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.static import serve

from .settings import BASE_DIR

import os

def bad_request(request):
    return render(request, '400.html', {'path': request.get_host()+request.get_full_path()})

def page_not_found(request):
    return render(request, '404.html', {'path': request.get_host()+request.get_full_path()})

def server_error(request):
    return render(request, '500.html', {'path': request.get_host()+request.get_full_path()})

def static_serve(request, path):
    return serve(request, path, os.path.join(BASE_DIR, 'static'), False)

def main(request):
	return render(request, 'main.html', {})

def results(request):
	return render(request, 'results.html', {})

def about(request):
	return render(request, 'about.html', {})
	
def schedules(request):
	return render(request, 'schedules.html', {})
	
def regulations(request):
	return render(request, 'regulations.html', {})

def register(request):
	return render(request, 'register.html', {})

def callfortasks(request):
	return render(request, 'callfortasks.html', {})

def environment(request):
	return render(request, 'environment.html', {})

def rules(request):
	return render(request, 'rules.html', {})

def host(request):
	return render(request, 'host.html', {})

def links(request):
	return render(request, 'links.html', {})