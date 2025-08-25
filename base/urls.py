from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name='home'),
    path('add',views.add,name='add'),
    path('edit/<int:id>',views.editning,name='edit'),
    path('delete/<int:id>',views.dele,name='delete'),
    path('history',views.history,name='history')
]
