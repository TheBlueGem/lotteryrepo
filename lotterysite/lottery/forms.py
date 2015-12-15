from django import forms
from lottery import models

class PostModelForm(forms.ModelForm):
	class Meta:
		model = models.Contestant
		fields = '__all__'