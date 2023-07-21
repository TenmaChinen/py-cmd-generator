from foos.models import Foo
from django import forms

class FooForm(forms.ModelForm):
  
  # Create New Fields if Needed
  minutes = forms.IntegerField(min_value=0, initial=0)
  seconds = forms.IntegerField(min_value=0, max_value=59, initial=0)
  
  class Meta:
    model = Foo
    # fields = '__all__'
    # fields = ('title', 'idx')
    exclude = ('idx', 'total_seconds' )

  def clean(self):
    cleaned_data = super().clean()
    minutes = cleaned_data.get('minutes')
    seconds = cleaned_data.get('seconds')
    total_seconds = minutes * 60 + seconds
    cleaned_data['total_seconds'] = total_seconds
    return cleaned_data

