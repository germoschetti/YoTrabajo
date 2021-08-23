from contact.models import Contact
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        else:
            id_contact = view.kwargs['pk']
            contact = Contact.objects.get(pk=id_contact)

            id_user = request.user.pk
            id_user_contact = contact.user_id
            if id_user == id_user_contact:
                return True
            
            return False
