from django import forms 
from FBVApp.models import PlayerModel
class PlayerForm(forms.ModelForm): 

    class Meta: 
        model = PlayerModel

        fields = ['name','description']