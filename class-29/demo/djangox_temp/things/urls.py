from django.urls import path

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="things_home"),
    # localhost:8000/things
    # path("widgets", WidgetPageView.as_view(), name="things_widget")
    # localhost:8000/things/widgets

]
