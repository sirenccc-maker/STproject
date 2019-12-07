from . import views
from django.urls import path
urlpatterns=[
        path('',views.all_squirrel),
        path('add/',views.add_squirrel),
<<<<<<< HEAD
        path('stats/',views.stats),
=======
        path('<squirrel_id>/',views.edit_squirrel),
>>>>>>> 107d5314dcc8462956aec9e647c5c3725b95e22f
]

