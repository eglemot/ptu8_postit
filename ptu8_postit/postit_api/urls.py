from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:post_id>/comments/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('<int:post_id>/like/', views.PostLikeCreate.as_view()),
    path('comment/<int:comment_id>/like/', views.CommentLikeCreate.as_view()),
    path('signup/', views.UserCreate.as_view()),
]
