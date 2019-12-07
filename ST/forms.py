from django.form import ModelForm
 from .models import Squirrel

Class SquirrelForm(ModelForm):
	class Meta:
		model=Squirrel
		fields=‘__all__’
