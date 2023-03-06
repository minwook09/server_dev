from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password,check_password
from .serializer import LoginUserSerializer


class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")
        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(dict(msg="None User"))
        if check_password(user_pw, user.user_pw):
            return Response(LoginUserSerializer(user).data )
        else:
            return Response(dict(msg="Wrong password"))


class RegistUser(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(request.data)

        if LoginUser.objects.filter(user_id=serializer.data['user_id']).exists():
            users=LoginUser.objects.filter(user_id=serializer.data['user_id']).first()
            data = dict(
                msg="Already existed id",
                user_id=users.user_id,
                user_pw=users.user_pw,
            )
            return Response(data)

        user = serializer.create(request.data)

        return Response(data=LoginUserSerializer(user).data)

