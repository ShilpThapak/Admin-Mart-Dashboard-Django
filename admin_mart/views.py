from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Incident


def index_view(request):
    return render(request, "admin_mart/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "admin_mart/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "admin_mart/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "admin_mart/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "admin_mart/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "admin_mart/register.html")


@login_required(login_url='/login')
def report_view(request):
    if request.method == 'POST':
        location = request.POST['location']
        department = request.POST.get('department')
        datetime = request.POST.get('datetime')
        incident_location = request.POST.get('incident_location')
        severity = request.POST.get('severity')
        cause = request.POST.get('cause')
        action = request.POST.get('action')
        user_id = request.POST.get('user_id')
        user = User.objects.get(pk=user_id)

        env = request.POST.get('Environmental Incident')
        ill = request.POST.get('Injury')
        pd = request.POST.get('Property Damage')
        veh = request.POST.get('Vehicle')

        inc_type = []
        if env  == 'on': inc_type.append('Environmental Incident')
        if ill  == 'on': inc_type.append('Injury/Illness')
        if pd  == 'on': inc_type.append('Property Damage')
        if veh  == 'on': inc_type.append('Property Damage')

        button = request.POST.get('button')
        if button == 'Save for Later':
            saved = True
        else:
            saved = False

        new_incident = Incident(
            location=location, 
            department=department,
            datetime=datetime,
            incident_location=incident_location,
            initial_severity=severity,
            suspected_cause=cause,
            immediate_action_taken=action,
            sub_incident_types=inc_type,
            saved=saved,
            reported_by=user,
            )
        new_incident.save()
        # print(list(request.POST.items()))
        # print(request)
    return render(request, "admin_mart/report.html")


@login_required(login_url='/login')
def saved_view(request):
    return render(request, "admin_mart/saved.html")


@login_required(login_url='/login')
def sent_view(request):
    return render(request, "admin_mart/sent.html")