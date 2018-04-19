from django.contrib import admin
from basket.models import *
from easy_thumbnails.files import get_thumbnailer
from django.utils.safestring import mark_safe

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display =('name', 'team_description','_thumbnail','team_code',)
    list_filter =('name', 'team_description','team_img','team_code',)
    search_fields =['name', 'team_description','team_img','team_code']
    
    def _thumbnail(self, obj):
        if obj.team_img:
            return mark_safe(u'<img src="/MEDIA/%s" alt="" style=\'width: 70px;height: 70px;\'  />' % (obj.team_img))z
        else:
            return "[No Image]"


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display =('name', 'last_name', 'nick_name','age','birth_date','rut','height','weight','mail','position','team','_thumbnail')
    list_filter =('name', 'last_name', 'nick_name','age','birth_date','rut','height','weight','mail','position','team','photo')
    search_fields =['name', 'last_name', 'nick_name','age','birth_date','rut','height','weight','position','photo']
    
    def _thumbnail(self, obj):
        if obj.photo:
            return mark_safe(u'<img src="/MEDIA/%s" alt="" style=\'width: 70px;height: 70px;\'  />' % (obj.photo))
        else:
            return "[No Image]"

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display =('name', 'mail', 'age', 'nick_name', 'rut')
    list_filter =('name', 'mail', 'age', 'nick_name', 'rut')
    search_fields =['name', 'mail', 'age', 'nick_name', 'rut']

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display =('match',)
    list_filter =('match',)
    search_fields =['match']
    
    


