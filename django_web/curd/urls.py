from django.urls import path
from . import views


app_name = 'curd'

urlpatterns = [

    path('index/', views.index, name='index'),
    path('chronos/performance/', views.chronos_performance, name='chronos_performance'),
    path('chronos/performance/view/', views.chronos_performance_view, name='chronos_performance_view'),
    path('chronos/accuracy/', views.chronos_accuracy, name='chronos_accuracy'),
    path('chronos/accuracy/view/', views.chronos_accuracy_view, name='chronos_accuracy_view'),
    path('naal/performance/', views.naal_performance, name='naal_performance'),
    path('naal/performance/view/', views.naal_performance_view, name='naal_performance_view'),
    path('charts/', views.charts, name='charts'),
    path('charts/view/', views.charts_view, name='charts_view'),

]


