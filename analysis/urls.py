from django.urls import path
from .views import UploadExcelView, ConfigureAnalysisView, ValidateAnalysisView, AnalysisStatusView, ListAnalysesView

urlpatterns = [
    path('upload/', UploadExcelView.as_view(), name='upload-excel'),
    path('configure/<int:analysis_id>/', ConfigureAnalysisView.as_view(), name='configure-analysis'),
    path('validate/<int:analysis_id>/', ValidateAnalysisView.as_view(), name='validate-analysis'),
    path('status/<int:analysis_id>/', AnalysisStatusView.as_view(), name='analysis-status'),
    path('analyses/', ListAnalysesView.as_view(), name='list-analyses'),
]
