import datetime
import smtplib
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from evenetManagementApp.models import event_tbl, participant_tbl
from twilio.rest import Client

def index(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {}
    if request.method == "POST":
        hostemail = request.POST['hostEmail']
        hostpass = request.POST['hostPass']
        events_list = event_tbl.objects.filter(host_email=hostemail, host_password=hostpass)
        if events_list:
            request.session['hostEmail'] = hostemail
            return redirect('event')
        else:
            context={
                "error": "Invalid Host email or password."
            }
            return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))

def logout(request):
    del request.session['hostEmail']
    return redirect('login')

def event(request):
    template = loader.get_template('viewEvent.html')
    if 'hostEmail' in request.session:
        print(request.session['hostEmail'])
        hostEmail = request.session['hostEmail']
        context = {
            "events": event_tbl.objects.filter(host_email=hostEmail, deadLine__gte=datetime.datetime.now()),
        }
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('login.html')
        context = {
            "error": "Please Login first."
        }
        return HttpResponse(template.render(context, request))

def eventReg(request):

    template = loader.get_template('eventReg.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def sendEmail(email, msg):
    sender_email = "email@gmail.com"
    receiver_email = email
    password = "*******"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg)

def sendSms(pnumber, msg):
    account_sid = "SID"
    auth_token = "TOCKEN"
    client = Client(account_sid, auth_token)
    sms = client.messages.create(
        body=msg,
        from_='phone number',
        to=pnumber
    )
    print(sms.sid)

def eventInsert(request):
    if request.method == "POST":
        eventName = request.POST['eventName']
        eventDesc = request.POST['eventDesc']
        posterLink = request.POST['posterLink']
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']
        deadLine_Date = request.POST['deadLine']
        hostEmail = request.POST['hostEmail']
        hostPass = request.POST['hostPass']

        # print(eventName + " " + eventDesc + " " + posterLink + " " + startDate + " " + endDate)

        data = event_tbl(name=eventName, description=eventDesc, poster_link=posterLink, start_date=startDate, end_date=endDate,
                         deadLine=deadLine_Date, host_email=hostEmail, host_password=hostPass)
        data.save()
        sendEmail(hostEmail, "Your Event Registration has been done successfully")
        sendSms("+919979017121", "Your Event Registration has been done\n Host Email: "+ hostEmail +" and password: " + hostPass + " \nThank you")
    return render(request, 'index.html')

def participantReg(request):

    template = loader.get_template('participentReg.html')
    context = {
        "events": event_tbl.objects.filter(deadLine__gte=datetime.datetime.now())
    }
    return HttpResponse(template.render(context, request))

def participantInsert(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact_no']
        email = request.POST['email']
        event_n = request.POST['events_t']
        regType = request.POST['regType']
        noOfPeople = request.POST['no_of_people']
        data = participant_tbl(name=name, contact_no=contact, email=email, event_name=event_n, registration_type=regType, no_of_people=noOfPeople)
        data.save()
        sendEmail(email, "Your Registration has been successfully. \n Thanks and Regards \n Event Management App.co")
        # sendSms(contact,"Your Registration has been done\n Thank you")
    return render(request, 'index.html')

def participant(request):
    template = loader.get_template('viewEvent.html')
    context = {
        "par": participant_tbl.objects.all()
    }
    return HttpResponse(template.render(context, request))

