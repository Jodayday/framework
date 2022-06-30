from django.urls import path


from accountapp.views import index
from accountapp.views import AccountCreateView
app_name = "accountapp"

urlpatterns = [
    path('hi/',index, name='hi'),
    path('create/',AccountCreateView.as_view(), name='create'),

]