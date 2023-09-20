
from django.contrib import admin
from django.urls import include, path

from api.v1.forum.urls import router, forum_answer_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(forum_answer_router.urls)),
    path('api/v1/', include('api.v1.accounts.urls')),
]
