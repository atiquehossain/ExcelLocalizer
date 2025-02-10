from rest_framework import serializers
from .models import ExcelAnalysis

class ExcelAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelAnalysis
        fields = '__all__'
