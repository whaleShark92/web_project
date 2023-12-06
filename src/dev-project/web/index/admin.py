from django.contrib import admin

# Register your models here.

admin.site.site_header = '智慧計算實驗室'  # 设置header
admin.site.site_title = '智慧計算實驗室'   # 设置title
admin.site.index_title = '智慧計算實驗室'

from .models import index
admin.site.register(index)