from django.db import models

# Create your models here.

# we need to add this to admin.py for admin site
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    
    #STR funtion is used to make it string
    def __str__(self) -> str:
        return '{}'.format(self.search)
    
    class Meta:
        verbose_name_plural = 'Searches'