from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.MemoIndexView.as_view(), name='index'),
    path('<int:pk>', views.MemoDetailView.as_view(), name='detail'),
    path('new_memo', views.MemoCreateView.as_view(), name='create'),
    path('delete_memo/<int:pk>', views.MemoDeleteView.as_view(), name='delete')
]