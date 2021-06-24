from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_403_FORBIDDEN

from .models import Review, Comment
from .serializers import ReviewListSerializer, ReviewSerializer, CommentListSerializer, CommentSerializer

# JWT를 활용
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



# community/,  GET 전체 리뷰, POST 리뷰 추가
# 로그인 된 사용자만 권한 있음
# permission_classese => request.user 정보가 담긴다
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def reviews_list_create(request):
    if request.method == 'GET': # ok
        reviews = Review.objects.all()
        # print(reviews)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # DRF가 request.data 해주는거야
        # 장고에선 request.post ~ 처럼 씀
        serializer = ReviewSerializer(data=request.data) # 여기에 인스턴스 들어있으면 업데이트 동작
        # 유효성 검사
        if serializer.is_valid(raise_exception=True): # 유효하지 않으면 자동 리턴
            # 포스트맨에서 jwt 토큰 같이 보내는 법 https://emessell.tistory.com/210
            serializer.save(user=request.user)
            return Response(serializer.data, HTTP_201_CREATED) # 생성되면 201 넘어감



# community/<review_pk>/ GET, PUT, DELETE => 리뷰 조회, 수정, 삭제
# 로그인 된 사용자만 권한 있음
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_detail_put_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        review_serializer = ReviewSerializer(review)
        # # 리뷰 pk에 따른 comments 불러오기
        # comments = review.comment_set.all()
        # comment_serializer = CommentListSerializer(comments, many=True)
        # serializer = {'review_serializer': review_serializer.data, 'comment_serializer' :comment_serializer.data}
        return Response(review_serializer.data)

    elif request.method == 'PUT':
        if review.user == request.user:
            serializer = ReviewSerializer(review, request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data)
        return Response({'error':'수정 권한이 없습니다.'}, HTTP_403_FORBIDDEN) # 다른 사람이 수정을 시도할 경우

    elif request.method == 'DELETE':
        if review.user == request.user:
            review.delete()
            return Response({'id': review_pk}, HTTP_204_NO_CONTENT) # 삭제된 리뷰 pk 전달
        return Response({'error':'삭제 권한이 없습니다.'}, HTTP_403_FORBIDDEN) # 다른 사람이 삭제 시도할 경우




# community/<review_pk>/comments/ GET POST => 리뷰의 댓글 리스트 조회, 댓글 작성 
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_list_create(request, review_pk):
    if request.method == 'GET':
        review = get_object_or_404(Review, pk=review_pk)
        # 리뷰 pk에 따른 comments 불러오기
        comments = review.comment_set.all()
        comment_serializer = CommentListSerializer(comments, many=True)
        return Response(comment_serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(review_pk)
            review = get_object_or_404(Review, pk=review_pk)
            serializer.save(user=request.user, review=review)  # user이랑 review 지정하는 법 찾아보기
            # print(serializer)
            return Response(serializer.data, HTTP_201_CREATED)
    

# community/comments/<comment_pk> => 리뷰 수정 삭제
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_put_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        if request.method == 'PUT':
            serializer = CommentSerializer(comment, request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data)

        elif request.method == 'DELETE':
                comment.delete()
                return Response({'id': comment_pk}, HTTP_204_NO_CONTENT)
    return Response({'error':'권한이 없습니다.'}, HTTP_403_FORBIDDEN)