import os
import re
from django import forms

class Seminario(forms.Form):
    events = forms.CharField(widget=forms.HiddenInput())
    