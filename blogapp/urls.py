from . import views 
from django.urls import path


app_name='blogapp'

urlpatterns=[
    
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail , 
    # name='post_detail'),
    # path('' ,views.post_list , name='post_list' ),
    path('',	views.post_list,	name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',
									views.post_detail,
									name='post_detail'),

    path ('' , views.PostListView.as_view(), name='post_list'),
#    path('<int:post_id/share/', views.post_share,name='post_share'),
#    path(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),

    path('<int:post_id>/share/',views.post_share,name='post_share'),

]