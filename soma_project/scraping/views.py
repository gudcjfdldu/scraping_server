from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from bs4 import BeautifulSoup

from scraping.models import ScrapInformation  

import urllib
import requests

def index(request):
    if request.method == 'GET':
        if request.GET.get('url', '') and (request.GET.get('action', '') == 'Fetch'):
	    print 'run Fetch'
            print request.GET.get('action', '')
            context = {}

            url = urllib.quote(request.GET.get('url', ''))
	    decode_url = urllib.unquote(url)
          
            context.update({'request_url': decode_url})
 
            try:
                r = requests.get(decode_url)
            except requests.exceptions.RequestException as e:
                print e
                error_context = {'error_message': 'invalid request'}

                return render(request, 'scraping/index.html', error_context)
            
            
            status_code = r.status_code   

            context.update({'status_code': status_code})       
                    
            scrap = ScrapInformation.objects.create(request_url = context['request_url'],
                                                    status_code = context['status_code'])
            scrap.status_update(context['status_code'])	    
	    
	    plain_text = r.text
	    try:
                soup = BeautifulSoup(plain_text, 'lxml')
            except:
                error_context = {'error_message': 'invalid request'}
                return render(request, 'scraping/index.html', error_context)

	    for og in soup.select('head > meta'):
                
                if og.get('property'):
                    
		    if 'title' in og.get('property'):
                        context.update({'og_title': og.get('content')})
                        scrap.title_update(context['og_title'])

                    elif 'url' in og.get('property'):
                        context.update({'og_url': og.get('content')})
                        scrap.url_update(context['og_url'])            

                    elif 'image' in og.get('property'):
                        context.update({'og_image': og.get('content')})
                        scrap.image_update(context['og_image'])

                    elif 'description' in og.get('property'):
		        context.update({'og_description': og.get('content')})			
                        scrap.description_update(context['og_description'])
                         
		    elif 'type' in og.get('property'):
                        context.update({'og_type': og.get('content')})
                        scrap.type_update(context['og_type'])	   


            return render(request, 'scraping/index.html', context)

        elif request.GET.get('url', '') and (request.GET.get('action', '') == 'Exist'):
            print 'run Exist'
            print request.GET.get('action', '')
            context = {}            

            url = urllib.quote(request.GET.get('url', ''))
	    decode_url = urllib.unquote(url)
 
            info = get_object_or_404(ScrapInformation, request_url=decode_url)

	    context.update({'request_url': info.request_url})

            context.update({'status_code': info.status_code})

            if info.og_url:
   	        context.update({'og_url': info.og_url})

            if info.og_title:
                context.update({'og_title': info.og_title})
       
            if info.og_image:
                context.update({'og_image': info.og_image})
 
            if info.og_description:
                context.update({'og_description': info.og_description})

            if info.og_type:
                context.update({'og_type': info.og_type})

            return render(request, 'scraping/index.html', context)
	    

	return render(request, 'scraping/index.html')
