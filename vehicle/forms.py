from django import forms
from django.forms import CharField
from vechicle.models import vitem


class vForm(forms.Form):
	mno = forms.CharField(max_length=50)
	img = forms.FileField()
	class Meta:
		model = vitem
		fields = [ 'vehid', 'mno','mname','color','scap','fea','mil','amt','img','status']