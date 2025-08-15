from django import forms

class HeartForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.ChoiceField(choices=[(0, 'Female'), (1, 'Male')])
    cp = forms.ChoiceField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)])
    trestbps = forms.IntegerField()
    chol = forms.IntegerField()
    fbs = forms.ChoiceField(choices=[(0, 'False'), (1, 'True')])
    restecg = forms.ChoiceField(choices=[(0, 0), (1, 1), (2, 2)])
    thalach = forms.IntegerField()
    exang = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    oldpeak = forms.FloatField()
    slope = forms.ChoiceField(choices=[(0, 0), (1, 1), (2, 2)])
    ca = forms.ChoiceField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)])
    thal = forms.ChoiceField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)])
