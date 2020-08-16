from django.urls import path, include
from rest_framework import routers
from users.views import EmployeeViewset, ClientViewset, PositionViewset

router = routers.SimpleRouter()
router.register(r'Empleyees', EmployeeViewset)
router.register(r'Clients', ClientViewset)
router.register(r'Positions', PositionViewset)


urlpatterns = [
    path('api/', include(router.urls))
]