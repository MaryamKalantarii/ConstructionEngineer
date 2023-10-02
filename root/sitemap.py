from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Blog
from projects.models import Project
from services.models import Service

class StaticSiteMap(Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'root:home',
            'root:about',
            'root:contact',
            'blog:blog',
            'projects:projects',
            'services:services',
        ]
    
    def location(self,item):
        return reverse(item)
    
class DynamicSiteMap(Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Blog.objects.filter(status=True)
        return Project.objects.filter(status=True)
        return Service.objects.filter(status=True)
    
    def location(self,obj):
        return '/blog/blog_detail/%s' % obj.id
        # return '/projects/project_detail/%s' % obj.id
        # return '/services/service_detail/%s' % obj.id
    def location(self,obj):
         return '/projects/project_detail/%s' % obj.id
    def location(self,obj):
        return '/services/service_detail/%s' % obj.id