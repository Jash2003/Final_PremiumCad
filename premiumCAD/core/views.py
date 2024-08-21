from django.shortcuts import render,redirect
from django.urls import reverse
import json
from django.shortcuts import render, get_object_or_404
from core.forms import ApplicantForm
from .models import Blogpost,Applicant,Joblisting
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def pathways(request):
    return render(request, 'pathways.html')

def services(request):
    return render(request, 'services.html')

def career(request):  # sourcery skip: for-append-to-extend, list-comprehension
    joblistings = Joblisting.objects.all()
    total_jobs = joblistings.count()
    jobdata = []
    for job in joblistings:
        jobdata.append({
            'title': job.jobtitle,
            'image': job.jobimage.url,
            'details': job.jobdescription,
            'openPositions': job.openpositions,
            # 'link': reverse('job_details' ,args = [job.id] )
            'id' : job.id
            
        })

    jobdata_json = json.dumps(jobdata)
    context = {
        'joblistings': joblistings,
        'total_jobs': total_jobs,
        'jobdata_json' : jobdata_json  # jobdata_json to the template
    }
    return render(request, 'career.html', context)

def cadservices(request):
    return render(request, 'cadservices.html')

def gisservices(request):
    return render(request, 'gisservices.html')

def telecomservices(request):
    return render(request, 'telecomservices.html')

def solardesign(request):
    return render(request, 'solardesign.html')

def blogs(request):
    blogposts = Blogpost.objects.all()
    return render(request, 'blogs.html',{'blogposts': blogposts})

def blogdetails(request, id, title):
    blog = get_object_or_404(Blogpost, id=id, title=title)
    return render(request, 'blogdetails.html', {'blog': blog})

# def job_details(request, id ):
#     job = get_object_or_404(Joblisting, id=id)
#     return render(request, 'apply.html', {'job':job})

def job_details(request, id ):
    job = get_object_or_404(Joblisting, id=id)
    if request.method == 'POST':
        jobrole = request.POST.get('jobrole')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        experience = request.POST.get('experience')
        resume = request.FILES.get('resume')

        # Save the data to the Applicant model
        applicant = Applicant(
            jobrole=jobrole,
            name=name,
            email=email,
            phone=phone,
            location=location,
            experience=experience,
            resume=resume
        )
        applicant.save()

    return render(request, 'apply2.html', {'job': job})

