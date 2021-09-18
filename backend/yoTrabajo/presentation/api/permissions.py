from presentation.models import Presentation
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        else:
            id_info = view.kwargs['pk']
            info = Presentation.objects.get(pk = id_info)

            id_user = request.user.pk
            id_user_info = info.user_id
            if id_user == id_user_info:
                return True
            
            return False
