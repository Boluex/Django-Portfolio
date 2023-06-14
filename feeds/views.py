from django.shortcuts import render
from .models import *
from django.http import FileResponse,Http404

# Create your views here.


def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = Projects.objects.all()
    skills = Skills.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "skills": myskills,
        "know": skills
    }

    return render(request, 'home_page.html', context)


# def display_files(request,id):
#     get_info=PersonalInformation.objects.get(id=id)
#     get_file=get_info.cv
#     try:
#          with open(str(get_file.path), 'rb') as pdf:
#             response = FileResponse(pdf.read(), content_type='application/pdf')
#             response['Content-Disposition'] = 'filename=a.pdf'
#             return response
#          pdf.closed
#     #    return FileResponse(open(get_file,'r'),content_type='application/pdf')
#     except FileNotFoundError:
#         return Http404()




# from django.http import FileResponse, Http404
# from django.shortcuts import get_object_or_404
# from .models import PersonalInformation

# def display_files(request, id):
#     get_info = get_object_or_404(PersonalInformation, id=id)
#     get_file = get_info.cv

#     try:
#         with open(str(get_file.path), 'rb') as pdf:
#             response = FileResponse(pdf.read(), content_type='application/pdf')
#             response['Content-Disposition'] = 'filename=a.docx'
#             return response

#     except FileNotFoundError:
#         raise Http404()




from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import PersonalInformation

def display_files(request, id):
    get_info = get_object_or_404(PersonalInformation, id=id)
    get_file = get_info.cv

    try:
        with open(str(get_file.path), 'rb') as docx:
            response = FileResponse(docx.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=a.docx'
            return response

    except FileNotFoundError:
        raise Http404()
