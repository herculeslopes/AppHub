from django.contrib import admin

# Register your models here.
from .models import Platform, Software, SoftwarePlatform
from .models import Comment

# admin.site.register(Software)
# admin.site.register(Platform)
# admin.site.register(SoftwarePlatform)

admin.site.register(Comment)

class SoftwarePlatformInline(admin.TabularInline):
    model = SoftwarePlatform
    min_num = 1
    extra = 2
    max_num = 3


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    inlines = [SoftwarePlatformInline]