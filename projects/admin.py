from django.contrib import admin

from . import models

class ProjectAdmin(admin.ModelAdmin): pass
class EndorsementAdmin(admin.ModelAdmin): pass
class TechnologyAdmin(admin.ModelAdmin): pass
class CollectionAdmin(admin.ModelAdmin): pass
class ClientAdmin(admin.ModelAdmin): pass
class ImageAdmin(admin.ModelAdmin): pass


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Endorsement, EndorsementAdmin)	
admin.site.register(models.Technology, TechnologyAdmin)	
admin.site.register(models.Collection, CollectionAdmin)	
admin.site.register(models.Client, ClientAdmin)	
admin.site.register(models.Image, ImageAdmin)	