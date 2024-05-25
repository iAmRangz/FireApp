from django.contrib import admin
from django.urls import path
from fire.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('stations', map_station, name='map-station'),
    path('incidents', map_incidents, name='map-incidents'),
    path('weather_list', WeatherConditionsList.as_view(), name='weather-list'),
    path('weather_list/add', WeatherConditionsAdd.as_view(), name='weather-add'),
    path('weather_list/edit/<int:pk>', WeatherConditionsUpdate.as_view(), name='weather-update'),
    path('weather_list/delete/<int:pk>', WeatherConditionsDelete.as_view(), name='weather-delete'),
]
