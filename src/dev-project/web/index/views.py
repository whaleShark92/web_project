from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render

# def lab_member_list(request):
#     lab_members = LabMember.objects.all()
#     return render(request, 'imgshow.html', {'lab_members': lab_members})

def home(request):
    nav_items = [
        {"name": "設備展示", "url": "visit_record_list"},
        {"name": "參訪活動", "url": "visit_record_list"},
        {"name": "影音展示", "url": "imgs_show_list"},
        {"name": "時間軸", "url": "visit_record_list"},
        {"name": "實驗室項目Demo", "url": "visit_record_list"},
        {"name": "實驗室成員", "url": "lab_member_list"}
    ]
    return render(request, 'index.html', {'nav_items': nav_items})



# def equipment(request):
#     # 處理設備展示頁面的邏輯...
#     pass

# def visit(request):
#     # 處理參訪活動頁面的邏輯...
#     pass

# # 其他視圖...
