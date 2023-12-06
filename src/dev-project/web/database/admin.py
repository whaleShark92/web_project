from django.contrib import admin
from .models import VisitRecord, LabMember, LabEvent, CompetitionRecord, CompositePhoto, Meeting, AwardDisplay, EquipmentDisplay, Media, EventParticipant, TemplateHTML

admin.site.site_header = '智慧計算實驗室'  # 设置header
admin.site.site_title = '智慧計算實驗室'   # 设置title
admin.site.index_title = '智慧計算實驗室'

class VisitRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name', 'date', 'content')
    search_fields = ('event_name',)
    ordering = ('date',)
    # 在這裡添加您的說明
    VisitRecord.__doc__ = '這是參訪紀錄的說明'

class LabMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'student_id', 'department', 'position', 'introduction')
    search_fields = ('name', 'student_id')
    ordering = ('name',)
    # 在這裡添加您的說明
    LabMember.__doc__ = '這是實驗室成員介紹的說明'

# 類似地，您可以為其他的資料庫類別建立相對應的 ModelAdmin 類別，並在其中添加您的說明

admin.site.register(VisitRecord, VisitRecordAdmin)
admin.site.register(LabMember, LabMemberAdmin)
admin.site.register(LabEvent)
admin.site.register(CompetitionRecord)
admin.site.register(CompositePhoto)
admin.site.register(Meeting)
admin.site.register(AwardDisplay)
admin.site.register(EquipmentDisplay)
admin.site.register(Media)
admin.site.register(EventParticipant)
admin.site.register(TemplateHTML)