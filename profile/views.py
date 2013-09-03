from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import (authenticate, login, views)
from django.contrib.auth.models import User
#from models import CustomUser 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _
from tastypie.models import ApiKey
from oppia.models import Points,Award, AwardCourse, Course
from oppia.profile.models import CustomUser
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from forms import RegisterForm, ResetForm, ProfileForm

def register(request):
    if request.method == 'POST': # if form submitted...
        form = RegisterForm(request.POST)        
        if form.is_valid(): # All validation rules pass
            # Create new user
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
        
            #OWC added new field
            phoneno = form.cleaned_data.get("phoneno")            
            professional = form.cleaned_data.get("professional")
            town = form.cleaned_data.get("town")
            city = form.cleaned_data.get("city")
            state = form.cleaned_data.get("state")
            country = form.cleaned_data.get("country")
            worktype = form.cleaned_data.get("worktype")
            currentlyworking = form.cleaned_data.get("currentlyworking")
            stafftype = form.cleaned_data.get("stafftype")
            familyplaning = form.cleaned_data.get("familyplaning")
            nurhitraining = form.cleaned_data.get("nurhitraining")
            education = form.cleaned_data.get("education")
            religion = form.cleaned_data.get("religion")
            sex = form.cleaned_data.get("sex")
            age = form.cleaned_data.get("age")
            providedit = form.cleaned_data.get("providedit")
            
            #OWC Derived from User Super Class and added new fields
            user = CustomUser.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.phoneno = phoneno            
            user.professional = professional            
            user.town = town
            user.city = city
            user.state = state
            user.country = country            
            user.worktype = worktype
            user.currentlyworking = currentlyworking
            user.stafftype = stafftype
            user.familyplaning = familyplaning
            user.nurhitraining = nurhitraining
            user.education = education
            user.religion = religion
            user.sex = sex
            user.age = age 
            user.providedit = providedit           
            user.save()
            u = authenticate(username=username, password=password)
            if u is not None:
                if u.is_active:
                    login(request, u)
                    return HttpResponseRedirect('thanks/') # Redirect after POST
            return HttpResponseRedirect('thanks/') # Redirect after POST
    else:
        form = RegisterForm() # An unbound form

    return render(request, 'oppia/profile/register.html', {'form': form,})

#Dump print
"""
           def dump(user):
               for attr in dir(user):
                   print "user.%s = %s" % (attr, getattr(user, attr))
"""
def reset(request):
    if request.method == 'POST': # if form submitted...
        form = ResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            user = User.objects.get(username__exact=username)
            newpass = User.objects.make_random_password(length=8)
            user.set_password(newpass)
            user.save()
            if request.is_secure():
                prefix = 'https://'
            else:
                prefix = 'http://'
            # TODO - better way to manage email message content
            send_mail('OppiaMobile: Password reset', 'Here is your new password for OppiaMobile: '+newpass 
                      + '\n\nWhen you next log in you can update your password to something more memorable.' 
                      + '\n\n' + prefix + request.META['SERVER_NAME'] , 
                      settings.SERVER_EMAIL, [user.email], fail_silently=False)
            return HttpResponseRedirect('sent')
    else:
        form = ResetForm() # An unbound form

    return render(request, 'oppia/profile/reset.html', {'form': form,})

def edit(request):    
    key = ApiKey.objects.get(user = request.user)
    if request.method == 'POST':
        
        form = ProfileForm(request.POST,request=request)
        if form.is_valid():
            # update basic data
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")            
            #OWC Additional fields are added
            phoneno = form.cleaned_data.get("phoneno")
            professional = form.cleaned_data.get("professional")
            town = form.cleaned_data.get("town")
            city = form.cleaned_data.get("city")
            state = form.cleaned_data.get("state")
            country = form.cleaned_data.get("country")
            worktype = form.cleaned_data.get("worktype")
            currentlyworking = form.cleaned_data.get("currentlyworking")
            stafftype = form.cleaned_data.get("stafftype")
            familyplaning = form.cleaned_data.get("familyplaning")
            nurhitraining = form.cleaned_data.get("nurhitraining")
            education = form.cleaned_data.get("education")
            religion = form.cleaned_data.get("religion")
            sex = form.cleaned_data.get("sex")
            age = form.cleaned_data.get("age")
            providedit = form.cleaned_data.get("providedit")
                       
            
            request.user.email = email
            request.user.first_name = first_name
            request.user.last_name = last_name
            #OWC Additional fields are added
            request.user.phoneno = phoneno
            request.user.professional = professional
            request.user.town = town
            request.user.city = city
            request.user.state = state
            request.user.country = country
            request.user.worktype = worktype
            request.user.currentlyworking = currentlyworking
            request.user.stafftype = stafftype
            request.user.familyplaning = familyplaning
            request.user.nurhitraining = nurhitraining
            request.user.education = education
            request.user.religion = religion
            request.user.sex = sex
            request.user.age = age
            request.user.providedit = providedit
            
            request.user.save()
            messages.success(request, _(u"Profile updated"))
            
            # if password should be changed
            password = form.cleaned_data.get("password")
            if password:
                request.user.set_password(password)
                request.user.save()
                messages.success(request, _(u"Password updated"))
    else:
        request.user= CustomUser.objects.get(pk=request.user.id)
        
        form = ProfileForm(initial={'username':request.user.username,
                                    'email':request.user.email,
                                    'first_name':request.user.first_name,
                                    'last_name':request.user.last_name,                                    
                                    'phoneno':request.user.phoneno,
                                    'professional':request.user.professional,
                                    'town':request.user.town,
                                    'city':request.user.city,
                                    'state':request.user.state,
                                    'country':request.user.country,
                                    'worktype':request.user.worktype,
                                    'currentlyworking':request.user.currentlyworking,
                                    'stafftype':request.user.stafftype,
                                    'familyplaning':request.user.familyplaning,
                                    'nurhitraining':request.user.nurhitraining,
                                    'education':request.user.education,
                                    'religion':request.user.religion,
                                    'sex':request.user.sex,
                                    'age':request.user.age,
                                    'providedit':request.user.providedit,                                                                                                          
                                    'api_key': key.key},request=request)
        
    return render(request, 'oppia/profile/profile.html', {'form': form,})

def points(request):
    points = Points.objects.filter(user=request.user).order_by('-date')
    paginator = Paginator(points, 25) # Show 25 contacts per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        mypoints = paginator.page(page)
    except (EmptyPage, InvalidPage):
        mypoints = paginator.page(paginator.num_pages)
    return render(request, 'oppia/profile/points.html', {'page': mypoints,})

def badges(request):
    awards = Award.objects.filter(user=request.user).order_by('-award_date')
    return render(request, 'oppia/profile/badges.html', {'awards': awards,})
