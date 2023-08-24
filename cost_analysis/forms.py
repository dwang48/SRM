from django import forms
from .models import CostAnalysis

class CostAnalysisForm(forms.ModelForm):
    class Meta:
        model = CostAnalysis
        fields = ['excel_file']
