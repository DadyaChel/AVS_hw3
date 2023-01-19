from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from API import views as v
from account import views as acc

# acc_router = DefaultRouter()
# acc_router.register('register', acc.ProfileRegisterAPIView)

acc_router = routers.DefaultRouter()
acc_router.register('reg', acc.AuthorRegisterViewSet)

posts_router = DefaultRouter()
posts_router.register('emp', v.EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('acc/', include(acc_router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', obtain_auth_token),
    path('acc/', include(acc_router.urls)),
    path('pos/', v.PositionListCreateAPIView.as_view()),
    path('pos/<int:pk>/', v.PositionRetrieveUpdateDestroy.as_view()),
    path('', include(posts_router.urls)),

]
