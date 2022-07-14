from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path("",views.home_page, name="homepage"),
    path("create",views.create_post,name="create"),
    path("detail/<int:id>", views.detail_post, name="detail"),
    path("delete/<int:id>",views.delete_post,name="delete"),
    path("update/<int:id>",views.update_post,name = "update"),

]
