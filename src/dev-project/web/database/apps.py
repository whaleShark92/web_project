from django.apps import AppConfig

#在網頁顯示中文
class VisitRecordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visitrecord'
    verbose_name = '參訪紀錄'

class LabMemberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'labmember'
    verbose_name = '實驗室成員介紹'

class LabEventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'labevent'
    verbose_name = '實驗室事件'

class CompetitionRecordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'competitionrecord'
    verbose_name = '競賽紀錄'

class CompositePhotoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'compositephoto'
    verbose_name = '合成照片'

class MeetingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meeting'
    verbose_name = '會議'

class AwardDisplayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'awarddisplay'
    verbose_name = '獎狀展示'

class EquipmentDisplayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'equipmentdisplay'
    verbose_name = '設備展示'

class MediaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'media'
    verbose_name = '多媒體'

class EventParticipantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventparticipant'
    verbose_name = '活動參與人員'

class TemplateHTMLConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'templatehtml'
    verbose_name = '範本html'
