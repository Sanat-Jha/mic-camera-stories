from django.shortcuts import render,redirect

from contentmanagement.emailsending import send_email
from .models import StorySubmission, Video, Channel
from .youtubedatafetch import fetchchanneldetails
import threading


# Create your views here.
def home(request):
    topvideos = Video.objects.all().order_by('-views')[:3]
    latestvideos = Video.objects.all().order_by('-created_at')[:3]
    channel = Channel.objects.all()[0]
    context = {
        'topvideos': topvideos,
        'latestvideos': latestvideos,
        'channel': channel,
        'views': channel.views/1000,
        'subscribers': channel.subscribers/1000,
        "DMchannelsubs": channel.DMchannelsubs
        }
    return render(request, 'home.html',context)

def databaserefresh(request):
    fetchchanneldetails()
    return redirect('home')

def aboutus(request):
    channel = Channel.objects.all()[0]
    context = {
        'channel': channel
    }
    return render(request, 'about.html', context)

def yourstory(request):
    context = {
        "message": ""
    }
    if request.method == 'POST':
        try:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            organization = request.POST.get('organization')
            story = request.POST.get('story')
            feedback = request.POST.get('feedback')

            storysubmission = StorySubmission(firstname=firstname, lastname=lastname, email=email, mobile=mobile, address=address, organization=organization, story=story, feedback=feedback)
            storysubmission.save()
            threading.Thread(target=send_email, args=(firstname, [email])).start()
            context['message'] = "Your story has been submitted successfully. We will get back to you soon."
        except Exception as e:
            context['message'] = "There was an error submitting your story. Please try again later."

    return render(request, 'yourstoryform.html',context)

def stories(request):
    videos = Video.objects.all().order_by('-created_at')
    context = {
        'videos': videos
    }
    return render(request, 'allvideos.html', context)

def story(request):
    videoid = request.GET.get('videoid')
    video = Video.objects.get(videoId=videoid)
    # pick any random 3 videos from the videos list except the current video
    videos = Video.objects.exclude(videoId=videoid).order_by('?')[:3]
    context = {
        'video': video,
        'videos': videos
    }
    return render(request, 'video page.html', context)