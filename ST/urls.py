from django.urls import path
from. import views
urlpatterns=[
        path('',views.all_squirrel),
        path('<squirrel_id>/',views.edit_squirrel),
        path('add/',views.add_squirrel),
]

