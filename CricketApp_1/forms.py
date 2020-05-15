from django import forms
from .models import userregistrationmodel,pointstable,struture_of_teams,structure_of_players,matches_between_teams,points_between_teams

class userregistrationforms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True,max_length=100)
    email = forms.EmailField(widget=forms.TextInput(), required=True,max_length=100)



    class Meta():
        model = userregistrationmodel
        fields=['name','password','email']


class userlogin(forms.ModelForm):
    class Meta:
        model = userregistrationmodel
        fields = ['name','password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class struture_of_teamforms(forms.ModelForm):
    class Meta():
        model=struture_of_teams
        fields= "__all__"
class structure_of_playersforms(forms.ModelForm):
    class Meta():
        model=structure_of_players
        fields= "__all__"

class matches_between_teamsforms(forms.ModelForm):
    class Meta():
        model=matches_between_teams
        fields= "__all__"


class points_between_teamsforms(forms.ModelForm):
    class Meta():
        model = points_between_teams
        fields = "__all__"
class  points_tableforms(forms.ModelForm):
    class Meta():
        model=pointstable
        fields="__all__"



