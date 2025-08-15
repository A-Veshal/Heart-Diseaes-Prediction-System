from django.urls import path
from .views import predict_view, result_view, cholesterol_chart

urlpatterns = [
    path('', predict_view, name='predict'),
    path('results/', result_view, name='result'),
    path('cholesterol-chart/', cholesterol_chart, name='cholesterol_chart'),
]
