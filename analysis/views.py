import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ExcelAnalysis
from .serializers import ExcelAnalysisSerializer
from pathlib import Path

class UploadExcelView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        analysis = ExcelAnalysis.objects.create(filename=file.name, file=file)
        return Response(ExcelAnalysisSerializer(analysis).data, status=status.HTTP_201_CREATED)

class ConfigureAnalysisView(APIView):
    def post(self, request, analysis_id):
        analysis = get_object_or_404(ExcelAnalysis, id=analysis_id)

        if analysis.status != 'pending':
            return Response({"error": "Configuration not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        analysis.config = request.data
        analysis.status = 'configured'
        analysis.save()

        return Response(ExcelAnalysisSerializer(analysis).data)

class ValidateAnalysisView(APIView):
    def post(self, request, analysis_id):
        analysis = get_object_or_404(ExcelAnalysis, id=analysis_id)
        
        if analysis.status != 'configured':
            return Response({"error": "Validation requires configuration"}, status=status.HTTP_400_BAD_REQUEST)

        file_path = analysis.file.path

        try:
            xls = pd.ExcelFile(file_path)
            sheets = xls.sheet_names

            # Example validation (checking required columns)
            required_columns = analysis.config.get("required_columns", [])
            results = {}

            for sheet in sheets:
                df = pd.read_excel(xls, sheet_name=sheet)
                missing = [col for col in required_columns if col not in df.columns]
                results[sheet] = {"status": "success" if not missing else "error", "missing_columns": missing}

            analysis.validation_results = results
            analysis.status = "completed"
            analysis.save()

            return Response(results)
        except Exception as e:
            analysis.status = "failed"
            analysis.error_message = str(e)
            analysis.save()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnalysisStatusView(APIView):
    def get(self, request, analysis_id):
        analysis = get_object_or_404(ExcelAnalysis, id=analysis_id)
        return Response(ExcelAnalysisSerializer(analysis).data)

class ListAnalysesView(APIView):
    def get(self, request):
        analyses = ExcelAnalysis.objects.all()
        return Response(ExcelAnalysisSerializer(analyses, many=True).data)
