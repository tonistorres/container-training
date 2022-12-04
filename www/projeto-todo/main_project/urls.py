from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # -------
    # gambis #
    # --------
    #  no fim do dia essa rota aponta para rota about logo acima
    path("about/", include("abouts.urls")),
    path("user/about/", include("abouts.urls")),
    path("editask/about/", include("abouts.urls")),
    # -----------------------------------------------------------
    path("user/", include("users.urls")),
    path("admin/", admin.site.urls),
    # path("editask/<int:id>", include("tasks.urls")),
    path("", include("tasks.urls")),
]
