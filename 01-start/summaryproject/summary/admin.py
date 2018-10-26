from django.contrib import admin

# Register your models here.

from .models import BookInfo, HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date']

class HerInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hgender', 'hcontent', 'hBook']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HerInfoAdmin)