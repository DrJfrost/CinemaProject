
from django.urls import path, include
from rest_framework_nested import routers
from movies.views import HeadquarterViewset, SpotTypeViewset, MovieGenreViewset, RoomViewset, SpotViewset, ShowViewset, MovieViewset

router = routers.SimpleRouter()

router.register(r"Headquarters", HeadquarterViewset)
router.register(r"SpotTypes", SpotTypeViewset)
router.register(r"MovieGenres", MovieGenreViewset)
router.register(r"Movies", MovieViewset)

headquarter_router = routers.NestedSimpleRouter(router, r'Headquarters', lookup='headquarter')
headquarter_router.register(r'Rooms', RoomViewset, basename='headquarters-rooms')
headquarter_router.register(r'Shows', ShowViewset, basename='headquarters-shows')

rooms_router = routers.NestedSimpleRouter(headquarter_router, r'Rooms', lookup='room')
rooms_router.register(r'Spots', SpotViewset, basename='headquarters-rooms-spots')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(headquarter_router.urls)),
    path('api/', include(rooms_router.urls)),
]
