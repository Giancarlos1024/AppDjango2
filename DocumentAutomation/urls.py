from django.urls import path, include

urlpatterns = [
    path('', include('Administration.urls')),
    path('', include('Dashboard.urls'))
]
