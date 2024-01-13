from django.contrib import admin
from .models import ResponseDataModel , InputQueryModel

class ResponseInline(admin.TabularInline):
    model = ResponseDataModel
    extra = 1

class InputQueryAdmin(admin.ModelAdmin):
    list_display = ['date' ,'search_query' ]
    inlines = [ResponseInline]

admin.site.register(InputQueryModel , InputQueryAdmin)
admin.site.register(ResponseDataModel)
# Register your models here.
