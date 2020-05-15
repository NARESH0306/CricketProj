from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.http import HttpResponseRedirect
from .models import userregistrationmodel,pointstable,struture_of_teams,structure_of_players,matches_between_teams,points_between_teams
from .forms import userregistrationforms,points_tableforms,struture_of_teamforms,structure_of_playersforms,matches_between_teamsforms,points_between_teamsforms, userlogin
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def disp(request):
    return render(request, 'index.html')


def adminauthenticate(request):
    return render(request, 'adminloginform.html')

def adminloginaction(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return render(request,'adminhome.html')
            else:
                messages.success(request, 'Invalid user id and password')

    return render(request,'adminloginform.html')


def adminhome(request):
    return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'index.html')


def adminuserlist(request):
    form = userregistrationmodel.objects.all()

    return render(request, 'adminuserdisp.html', {'form': form})


def adminaddteam(request):
    if request.method == 'POST':

        form = struture_of_teamforms(request.POST,request.FILES)
        if form.is_valid():
            print('please register')
            form.save()
            messages.success(request, 'You have been successfully saved')
            return HttpResponseRedirect('adminaddteam')
        else:
            print("Invalid form")
    else:
        form = struture_of_teamforms()
    return render(request, 'adminaddteam.html', {'form':form})



def adminaddplayers(request):
    if request.method == 'POST':

        form = structure_of_playersforms(request.POST,request.FILES)
        if form.is_valid():
            print('please register')
            form.save()
            messages.success(request, 'You have been successfully saved')
            return HttpResponseRedirect('adminaddplayers')
        else:
            print("Invalid form")
    else:
        form = structure_of_playersforms()
    return render(request, 'adminaddplayer.html', {'form':form})


def adminaddmatch(request):
    if request.method == 'POST':

        form = matches_between_teamsforms(request.POST)
        if form.is_valid():
            print('please register')
            form.save()
            messages.success(request, 'You have been successfully saved')
            return HttpResponseRedirect('adminaddmatch')
        else:
            print("Invalid form")
    else:
        form = matches_between_teamsforms()
    return render(request, 'adminaddmatch.html', {'form':form})




def adminpointstable(request):

    if request.method == 'POST':

        form = points_tableforms(request.POST)
        if form.is_valid():
            print('please register')
            form.save()
            messages.success(request, 'You have been successfully saved')
            return HttpResponseRedirect('adminpointstable')
        else:
            print("Invalid form")
    else:
        form = points_tableforms()
    return render(request, 'adminpointstable.html', {'form':form})


##   user can see

def userregsitraion(request):
    Rform =userregistrationforms()
    if request.method=="POST":
        Rform = userregistrationforms(request.POST)
        if Rform.is_valid():
            print('naresh')
            Rform.save()
        return redirect('userregsitraion')
    return render(request,'userregist.html',{'Rform':Rform})

def userloginform(request):
    form=userlogin()
    if request.method == "POST":
        myloginform = userlogin(request.POST)
        if myloginform.is_valid():
            # username1 = myloginform.cleaned_data['name']
            # password1 = myloginform.cleaned_data['password']
            username1 = request.POST.get('name')
            password1 = request.POST.get('password')

            dbuser = userregistrationmodel.objects.filter(name=username1, password=password1)
            print(dbuser)
            if not dbuser:
                return HttpResponse('registration failed')
            else:
                return HttpResponse('login success')
        else:
            return HttpResponse("please enter valied data")
    return render(request, 'userlogin.html',{'form':form})




def signout(request):
    return render(request,"signout.html")


def teamsdisp(request):
    form = struture_of_teams.objects.all()

    return render(request, 'teams.html', {'form': form})

def playersdisp(request):
    form = structure_of_players.objects.all()

    return render(request, 'players.html', {'form': form})

def matchdisp(request):
    form = matches_between_teams.objects.all()

    return render(request, 'matches.html', {'form': form})
def pointstabledisp(request):

    form = pointstable.objects.all()

    return render(request, 'pointstable.html', {'form': form})
def playershistorydisp(request):
    form=player_history.objects.all()

    return render(request,'players.html',{'form':form})

def teamplayersdisps(request):
    naresh = request.GET.get('naresh')
    form=structure_of_players.objects.filter(country=naresh)
    for k in form:
        print(k)
    return render(request,'teamplayesdisp.html',{"form": form})



