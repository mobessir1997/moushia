from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from accounts.serializers import UserSerializer


# Create your views here.
class ParentProfileApi(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]  # noqa: RUF012
    queryset = User.objects.filter()
    serializer_class = UserSerializer