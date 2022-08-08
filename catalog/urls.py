from catalog import views
from django.urls import path

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name = "index"),
    path('CreateBook/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/',views.BookDetail.as_view(), name = 'book_detail'),
    path('my_view/',views.my_view, name="my-view"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('profile', views.CheckOutBooksByUserView.as_view(), name = 'profile')
]
