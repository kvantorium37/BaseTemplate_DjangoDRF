from rest_framework.routers import SimpleRouter

from tasks.api import views

app_name = 'tasks'

router = SimpleRouter()
router.register('users', views.UserViewSet)
router.register('', views.TasksViewSet)

urlpatterns = router.urls
