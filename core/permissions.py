from rest_framework.permissions import BasePermission


class IsAuthorStaffEditOrReadonly(BasePermission):
	WRITE_METHODS = ("PUT", "POST", "DELETE")
	READ_METHODS = ('GET', 'HEAD', 'OPTIONS')

	def has_permission(self, request, view):
		return bool(request.method in self.READ_METHODS or request.user and request.user.is_authenticated)

	def has_object_permission(self, request, view, obj):
		if request.method not in self.READ_METHODS and \
			(not request.user or not request.user.is_authenticated):
			if request.user.is_superuser:
				return True

			if request.user.is_staff and request.method not in self.WRITE_METHODS:
				return True

			if obj.owner == request.user:
				return True
			return False
		return True
