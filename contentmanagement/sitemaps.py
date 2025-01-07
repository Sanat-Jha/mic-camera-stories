# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Video

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'yourstory', 'stories']

    def location(self, item):
        return reverse(item)

class VideoSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return Video.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at