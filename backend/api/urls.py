# backend/api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health_check, name='health_check'),
    path('vandermeulen', views.vandermeulen_data, name='vandermeulen_data'),
    path('test-roi', views.test_roi_analysis, name='test_roi_analysis'),
    
    # CSV Upload endpoints
    path('upload-csv', views.upload_csv_data, name='upload_csv_data'),
    path('uploaded-tables', views.get_uploaded_tables, name='get_uploaded_tables'),
    path('table-data', views.get_table_data, name='get_table_data'),
    path('delete-table', views.delete_uploaded_table, name='delete_uploaded_table'),
]