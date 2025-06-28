from django.contrib import admin
from .models import Board

# Register your models here.
class AdminBoard(admin.ModelAdmin):
    list_display = ['board_name', 'owner', 'visibility', 'date_created']
    prepopulated_fields = {"slug":["board_name"]}
admin.site.register(Board, AdminBoard)
