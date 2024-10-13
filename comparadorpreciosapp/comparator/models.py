from django.db import models

class Query(models.Model):
    query_text = models.CharField(max_length=200)
    # query_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_text
    # counter = models.PositiveIntegerField(default=0)



# from django import forms
# class Query(forms.Form):
#     query_text = forms.CharField(label="Query to search", max_length=200)