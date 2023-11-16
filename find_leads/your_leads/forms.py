from django import forms
from .models import TeleModel


# choices = TeleModel.objects.all().values_list('name', 'name')

# choice_list = []

# for item in choices:
#     choice_list.append(item)


class TeleForm(forms.ModelForm):
    class Meta:
        model = TeleModel
        fields = [
            'first_name',
            'last_name',
            'address',
            'city',
            'county',
            'state',
            'zip',
            'phone',
            'carrier',
            'gender',
            'ethnicity',
            'ownrent',
            'latitude',
            'longitude',
            ]


        # widgets = {
        #         'title' : forms.TextInput(attrs={'class': 'form-control'}),
        #         'content' : forms.Textarea(attrs={'class': 'form-control'}),
        #         # 'category' : forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
        #     }