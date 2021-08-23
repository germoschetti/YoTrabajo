from skills.models import Skill
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        else:
            id_skill = view.kwargs['pk']
            skill = Skill.objects.get(pk = id_skill)

            id_user = request.user.pk
            id_user_skill = skill.user_id
            
            if id_user == id_user_skill:
                return True
            
            return False
