from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.disp, name='home'),
    path('userregsitraion', views.userregsitraion, name='userregsitraion'),
    path('userloginform', views.userloginform, name='userloginform'),
    path('adminauth', views.adminauthenticate, name='adminauth'),
    path('adminloginaction', views.adminloginaction, name='adminloginaction'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('adminuserdisp', views.adminuserlist, name='adminuserlist'),
    path('teams', views.teamsdisp, name='teams'),
    path('players', views.playersdisp, name='players'),
    path('matches', views.matchdisp, name='matches'),
    path('pointstable', views.pointstabledisp, name='pointstable'),
    path('playershistory', views.playershistorydisp, name='playershistory'),
    path('adminuserdisp', views.adminuserlist, name='adminuserdisp'),
    path('adminaddteam', views.adminaddteam, name='adminaddteam'),
    path('adminaddplayers', views.adminaddplayers, name='adminaddplayers'),
    path('adminaddmatch', views.adminaddmatch, name='adminaddmatch'),
    # path('adminplayershistory', views.adminplayershistory, name='adminplayershistory'),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('adminpointstable', views.adminpointstable, name='adminpointstable'),
    # path('teamplayersdisps', views.teamplayersdisps, name='teamplayersdisps'),
    url(r'^teamplayersdisps/$', views.teamplayersdisps, name="teamplayersdisps"),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)