from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class VisitRecord(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="編號")
    event_name = models.CharField(max_length=255, verbose_name="活動名稱")
    date = models.DateField(verbose_name="日期", null=True)
    content = models.TextField(verbose_name="介紹內容", null=True)

    class Meta:
        verbose_name = "參訪紀錄"
        verbose_name_plural = "參訪紀錄"

    def __str__(self):
        return self.event_name

class LabMember(models.Model):
    STUDENT_LEVEL_CHOICES = [
        (1, '大學部'),
        (2, '研究生'),
        (3, '博士後'),
        (4, '研究助理'),
        (5, '教授'),
    ]

    id = models.AutoField(primary_key=True, verbose_name="編號")
    name = models.CharField(max_length=255, verbose_name="姓名")
    student_id = models.CharField(max_length=10, verbose_name="學號")
    department = models.CharField(max_length=255, verbose_name="系所")
    position = models.CharField(max_length=255, verbose_name="職位")
    introduction = models.TextField(verbose_name="介紹", null=True)
    student_level = models.IntegerField(choices=STUDENT_LEVEL_CHOICES, default=1, verbose_name="學級")

    class Meta:
        verbose_name = "實驗室成員介紹"
        verbose_name_plural = "實驗室成員介紹"

    def __str__(self):
        return self.name

class LabEvent(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="編號")
    title = models.CharField(max_length=255, verbose_name="標題")
    date = models.DateField(verbose_name="日期")
    event = models.TextField(verbose_name="事件", null=True)
    content = models.TextField(verbose_name="介紹內容", null=True)

    class Meta:
        verbose_name = "實驗室事件"
        verbose_name_plural = "實驗室事件"

    def __str__(self):
        return self.title

class CompetitionRecord(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="編號")
    competition_name = models.CharField(max_length=255, verbose_name="競賽名稱")
    date = models.DateField(verbose_name="日期")
    content = models.TextField(verbose_name="介紹內容", null=True)

    class Meta:
        verbose_name = "競賽紀錄"
        verbose_name_plural = "競賽紀錄"

    def __str__(self):
        return self.competition_name

class CompositePhoto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="編號")
    template_html = models.ForeignKey('TemplateHTML', on_delete=models.CASCADE, null=True, blank=True, verbose_name="模板 HTML")
    content_title = models.TextField(verbose_name="主題", null=True)
    content_event = models.TextField(verbose_name="事件", null=True)
    content_a = models.TextField(verbose_name="內容區域A", null=True)
    content_b = models.TextField(verbose_name="內容區域B", null=True)
    content_c = models.TextField(verbose_name="內容區域C", null=True)
    content_d = models.TextField(verbose_name="內容區域D", null=True)

    class Meta:
        verbose_name = "合成照片"
        verbose_name_plural = "合成照片"

    def __str__(self):
        return str(self.id)


class Meeting(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="編號")
    meeting_name = models.CharField(max_length=255, verbose_name="會議名稱")
    date = models.DateField(verbose_name="日期", null=True)
    meeting_link = models.URLField(verbose_name="會議連結", null=True)
    content = models.TextField(verbose_name="會議內容", null=True)

    class Meta:
        verbose_name = "會議"
        verbose_name_plural = "會議"

    def __str__(self):
        return self.meeting_name

class AwardDisplay(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="編號")
    award_name = models.CharField(max_length=255, verbose_name="獎項名稱")
    date = models.DateField(verbose_name="日期", null=True)
    content = models.TextField(verbose_name="介紹內容", null=True)

    class Meta:
        verbose_name = "獎狀展示"
        verbose_name_plural = "獎狀展示"

    def __str__(self):
        return self.award_name

class EquipmentDisplay(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="編號")
    equipment_name = models.CharField(max_length=255, verbose_name="設備名稱")
    content = models.TextField(verbose_name="介紹內容", null=True)
    
    class Meta:
        verbose_name = "設備展示"
        verbose_name_plural = "設備展示"

    def __str__(self):
        return self.equipment_name


# 多媒體
class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', '圖片'),
        ('video', '影片'),
        # 添加其他媒體類型...
    ]

    id = models.AutoField(primary_key=True, verbose_name="編號")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, verbose_name="內容類型")
    object_id = models.PositiveIntegerField(null=True, blank=True, verbose_name="物件 ID")
    content_object = GenericForeignKey('content_type', 'object_id')
    media_type = models.CharField(max_length=255, choices=MEDIA_TYPE_CHOICES, blank=True, verbose_name="多媒體類型")
    content = models.TextField(verbose_name="內容")
    path = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name="路徑")

    def save(self, *args, **kwargs):
        if self.path and self.path.url:
            if self.path.url.lower().endswith(('.png', '.jpg', '.jpeg')):
                self.media_type = 'image'
            elif self.path.url.lower().endswith(('.mp4', '.avi', '.mov')):
                self.media_type = 'video'
            else:
                self.media_type = 'unknown'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "多媒體"
        verbose_name_plural = "多媒體"

    def __str__(self):
        return str(self.id)

class EventParticipant(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="編號")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, verbose_name="內容類型")
    object_id = models.PositiveIntegerField(null=True, blank=True, verbose_name="物件 ID")
    content_object = GenericForeignKey('content_type', 'object_id')
    participant_id = models.ForeignKey('LabMember', on_delete=models.CASCADE, null=True, blank=True, verbose_name="參與者 ID")

    class Meta:
        verbose_name = "活動參與人員"
        verbose_name_plural = "活動參與人員"

    def __str__(self):
        return str(self.id)

class TemplateHTML(models.Model):
    id=models.AutoField(primary_key=True, verbose_name="編號") 
    template_path=models.FileField(upload_to='templates/',null=True,blank=True, verbose_name="模板路徑")

    class Meta:
        verbose_name= "範本html"
        verbose_name_plural= "範本html"

    def __str__(self):
        return str(self.id)
