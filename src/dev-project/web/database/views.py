from django.shortcuts import render
from .models import VisitRecord, LabMember, LabEvent, CompetitionRecord, CompositePhoto, Meeting, AwardDisplay, EquipmentDisplay, Media, EventParticipant, TemplateHTML
# from index.views import home

# def menu(request):
#     result = home(request)

def imgs_show_list(request):
    nav_items = [
{"name": "設備展示", "url": "visit_record_list"},
        {"name": "參訪活動", "url": "visit_record_list"},
        {"name": "影音展示", "url": "imgs_show_list"},
        {"name": "時間軸", "url": "visit_record_list"},
        {"name": "實驗室項目Demo", "url": "visit_record_list"},
        {"name": "實驗室成員", "url": "lab_member_list"}
    ]
    imgs_show = Media.objects.all()
    return render(request, 'imgs_show_list.html', {'imgs_show': imgs_show_list, 'nav_items': nav_items})

def visit_record_list(request):
    nav_items = [
        {"name": "設備展示", "url": "visit_record_list"},
        {"name": "參訪活動", "url": "visit_record_list"},
        {"name": "影音展示", "url": "imgs_show_list"},
        {"name": "時間軸", "url": "visit_record_list"},
        {"name": "實驗室項目Demo", "url": "visit_record_list"},
        {"name": "實驗室成員", "url": "lab_member_list"}
    ]
    visit_records = VisitRecord.objects.all()
    return render(request, 'visit_record_list.html', {'visit_records': visit_records, 'nav_items': nav_items})


def lab_member_list(request):
    nav_items = [
        {"name": "設備展示", "url": "visit_record_list"},
        {"name": "參訪活動", "url": "visit_record_list"},
        {"name": "影音展示", "url": "imgs_show_list"},
        {"name": "時間軸", "url": "visit_record_list"},
        {"name": "實驗室項目Demo", "url": "visit_record_list"},
        {"name": "實驗室成員", "url": "lab_member_list"}
    ]
    lab_members = LabMember.objects.all()
    return render(request, 'lab_member_list.html', {'lab_members': lab_members, 'nav_items': nav_items})

def database_view(request):
    visit_records = VisitRecord.objects.all()
    lab_members = LabMember.objects.all()
    lab_events = LabEvent.objects.all()
    competition_records = CompetitionRecord.objects.all()
    composite_photos = CompositePhoto.objects.all()
    meetings = Meeting.objects.all()
    award_displays = AwardDisplay.objects.all()
    equipment_displays = EquipmentDisplay.objects.all()
    medias = Media.objects.all()
    event_participants = EventParticipant.objects.all()
    template_htmls = TemplateHTML.objects.all()

    context = {
        'visit_records': visit_records,
        'lab_members': lab_members,
        'lab_events': lab_events,
        'competition_records': competition_records,
        'composite_photos': composite_photos,
        'meetings': meetings,
        'award_displays': award_displays,
        'equipment_displays': equipment_displays,
        'medias': medias,
        'event_participants': event_participants,
        'template_htmls': template_htmls
    }

    return render(request, 'database_index.html', context)
