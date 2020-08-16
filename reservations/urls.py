
from django.urls import path, include
from rest_framework_nested import routers
from reservations.views import BillViewset, BillTypeViewset, PaymentMethodViewset
from users.urls import router as routerUsers

router = routers.SimpleRouter()

router.register(r"BillTypes", BillTypeViewset)
router.register(r"PaymentMethods", PaymentMethodViewset)


client_router = routers.NestedSimpleRouter(routerUsers, r'Clients', lookup='client')
client_router.register(r'Billings', BillViewset, basename='client-billing')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(client_router.urls)),
]
