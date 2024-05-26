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

    path('firetruck_list', FireTruckList.as_view(), name='firetruck-list'),
    path('firetruck_list/add', FireTruckAdd.as_view(), name='firetruck-add'),
    path('firetruck_list/edit/<int:pk>', FireTruckUpdate.as_view(), name='firetruck-update'),
    path('firetruck_list/delete/<int:pk>', FireTruckDelete.as_view(), name='firetruck-delete'),

    path('incident_list', IncidentList.as_view(), name='incident-list'),
    path('incident_list/add', IncidentAdd.as_view(), name='incident-add'),
    path('incident_list/edit/<int:pk>', IncidentUpdate.as_view(), name='incident-update'),
    path('incident_list/delete/<int:pk>', IncidentDelete.as_view(), name='incident-delete'),

]
