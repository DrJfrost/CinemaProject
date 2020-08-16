from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from movies.models import Room

class CheckRoom(BasePermission):

    """
    permission to only allow owners of an auditor account to list its relations.
    """
    message = "the room sent in data does not belong to the headquarter specified on the URL"

    def has_permission(self, request, view):
        has_permission = False
        if 'room' in request.data:
            room_id = (int)(request.data['room'])
            room_obj = get_object_or_404(Room, pk=room_id)
            if room_obj.headquarter.id == (int)(view.kwargs["headquarter_pk"]):
                has_permission = True
        else:
            has_permission = True
        return has_permission