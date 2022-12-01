from django.urls import path
from . import views


app_name = 'curd'

urlpatterns = [

    path('index/', views.index, name='index'),
    # Chronos base
    path('chronos/performance/', views.chronos_performance, name='chronos_performance'),
    path('chronos/performance/view/', views.chronos_performance_view, name='chronos_performance_view'),
    path('chronos/accuracy/', views.chronos_accuracy, name='chronos_accuracy'),
    path('chronos/accuracy/view/', views.chronos_accuracy_view, name='chronos_accuracy_view'),
    # Chronos execl data
    path('chronos/upload/', views.chronos_upload, name='chronos_upload'),
    path('chronos/upload/view/', views.chronos_upload_view, name='chronos_upload_view'),
    path('chronos/download/', views.chronos_execl_download, name='chronos_download'),
    # Chronos compare
    path('chronos/performance/compare/', views.chronos_performance_compare, name='chronos_performance_compare'),
    path('chronos/performance/compare/view/', views.chronos_performance_compare_view, name='chronos_performance_compare_view'),
    path('chronos/accuracy/compare/', views.chronos_accuracy_compare, name='chronos_accuracy_compare'),
    path('chronos/accuracy/compare/view/', views.chronos_accuracy_compare_view, name='chronos_accuracy_compare_view'),
    # NAAL
    path('naal/performance/', views.naal_performance, name='naal_performance'),
    path('naal/performance/view/', views.naal_performance_view, name='naal_performance_view'),
]


