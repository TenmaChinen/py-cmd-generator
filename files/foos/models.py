# from parents.models import Parent
from django.db import models

class Foo(models.Model):
  T_GENDERS = ((0,'Male'), (1, 'Female'), (2, 'Trans'))
  title = models.CharField(max_length=32)
  # parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
  idx = models.PositiveSmallIntegerField(blank=False, null=False)
  total_seconds = models.PositiveSmallIntegerField(blank=True, default=0)
  gender = models.PositiveSmallIntegerField(choices=T_GENDERS, blank=True, null=True, default=0)

  # Custom Methods
  def get_minutes(self):
    return self.total_seconds // 60