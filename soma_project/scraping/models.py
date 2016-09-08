from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ScrapInformation(models.Model):
    request_url = models.CharField(max_length=500, blank=False)
    status_code = models.CharField(max_length=10, blank=False)
    og_url = models.CharField(max_length=500, blank=False)
    og_title = models.CharField(max_length=50, blank=True)
    og_image = models.TextField(max_length=500, blank=True)
    og_description = models.CharField(max_length=100, blank=True)
    og_type = models.CharField(max_length=50, blank=True)


    def status_update(self, status_code):
        self.status_code = status_code
	self.save()

    def url_update(self, og_url):
        self.og_url = og_url
        self.save()

    def title_update(self, og_title):
        self.og_title = og_title
        self.save()
 
    def image_update(self, og_image):
        self.og_image = og_image
        self.save()

    def description_update(self, og_description):
        self.og_description = og_description
        self.save()

    def type_update(self, og_type):
        self.og_type = og_type 
        self.save()
