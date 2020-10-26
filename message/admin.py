from django.contrib import admin

# Register your models here.
from django.contrib import admin
from message import models


class MessageAdmin(admin.ModelAdmin):
    list_display = ("time", 'name', 'grade', 'classNum',
                    'title', 'message_text', 'isShow')    # 显示的列
    fields = ('time','name', 'grade', 'classNum', 'title',
              'message_text', 'isShow')  # 添加时出现的字段
    search_fields = ("time", 'name', 'grade', 'classNum',
                     'title', 'message_text', 'isShow')      # 可以搜索的字段
    list_per_page = 25

admin.site.register(models.Message, MessageAdmin)
