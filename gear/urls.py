from django.urls import path
from . import views

app_name = 'gear'

urlpatterns = [
  path('', views.GearItems.as_view(), name='items'),
  # path('item/<int:pk>', views.gear_detail, name='gear_detail'),
  # path('item/<int:pk>/edit', views.gear_edit, name='gear_edit'),
]