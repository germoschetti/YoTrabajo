from users.models import User
from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        else:
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)

            id_user = request.user.pk
            id_user_coment = comment.user_id
            if id_user == id_user_coment:
                return True
            
            return False