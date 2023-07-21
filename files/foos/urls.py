from django.urls import path, include
from foos import views

app_name = 'foos'

urlpatterns = [
    path('list/',views.FooListView.as_view(), name='list'),
    path('create/',views.FooCreateView.as_view(), name='create'),
    path('detail/<int:pk>',views.FooDetailView.as_view(), name='detail'),
    path('update/<int:pk>',views.FooUpdateView.as_view(), name='update'),
    path('delete/<int:pk>',views.FooDeleteView.as_view(), name='delete'),
]