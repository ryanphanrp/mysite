from django.urls import path
from .views import view_list, view_detail, view_result, view_vote

app_name = "polls"

urlpatterns = [
   path('', view_list, name='index'),
   path('list', view_list, name='list'),
   path('detail/<int:poll_id>', view_detail, name='detail'),
   path('result/<int:poll_id>', view_result, name='result'),
   path('vote/<int:poll_id>', view_vote, name='vote'),
]