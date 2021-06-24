# from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from .models import User
from .serializers import UserSerializers
from community.serializers import ReviewListSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import logout as auth_logout



@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        # 1. 
        password = request.data.get('password')
        #postman에 쓸때 passwordConfirmation 이걸 key값으로 넣어야 함
        password_confirmation = request.data.get('passwordConfirmation')

        # 2.
        if password != password_confirmation:
            return Response({'error':'비밀번호가 일치하지 않습니다.'}, HTTP_400_BAD_REQUEST)
        ## 원래는 1,2 를 장고에서 제공되는 기능으로 했는데, vue로 넘기면서 직접 해줘야 함

        # 3. 인스턴스 준비
        serializer = UserSerializers(data=request.data)

        # 4. 유효성 검사
        if serializer.is_valid(raise_exception=True):
            user = serializer.save() # 여기서 끝나면 비밀번호가 그대로 저장됨
            # 5. 비밀번호 해싱
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data, HTTP_201_CREATED)


## 프로필 내용 보여주고싶은뎅
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def profile(request, user_pk):
    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_pk)
        myreviews = user.reviews.all()
        # reviews = user.reviews.all()
        # reviews_serializer = ReviewListSerializer(reviews, many=True)  
        # print(reviews_serializer.data)
        # return Response(reviews_serializer.data)
        return Response({'error':'휴'})

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_update_delete(request):
    if request.method == 'PUT':
        user = request.user
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        request.user.delete()
        auth_logout(request)
        return Response({'성공':'삭제되었습니다.'})

