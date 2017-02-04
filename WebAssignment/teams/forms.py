from django import forms


#Just a django thing. Model goes into the HTMl
class PlayerForm(forms.Form):
    player_name = forms.CharField(label='Your name', max_length=250)
    player_position = forms.CharField(label='position', max_length=20)
