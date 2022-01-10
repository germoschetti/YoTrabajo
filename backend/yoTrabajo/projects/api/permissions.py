from rest_framework.permissions import BasePermission
from projects.models import Project

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        else:
            id_project = view.kwargs['pk']
            project = Project.objects.get(pk=id_project)
            
            id_user = request.user.pk
            id_user_project = project.user_id

            if id_user == id_user_project:
                return True

            return False
