from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from board.models import Board

from board.serializers import BoardSerializer

# Create your views here.


# @api_view(['POST', 'GET'])
# def route_def(request, board_id=None):
#     print(board_id)
#     if (request.method == 'GET'):
#         get_boards(request)
#     elif (request.method == 'POST'):
#         create_board(request)
#     return Response({})


@api_view(['post'])
def create_board(req):
    serializer = BoardSerializer(data=req.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['get'])
def read_boards(req):
    boards = Board.objects.all().order_by('-create_date')
    serializer = BoardSerializer(boards, many=True)

    # content = JSONRenderer().render(serializer.data)
    # return Response(content, status=200)

    return Response(serializer.data, status=200)


@api_view(['get'])
def read_board(req, board_id):
    board = get_object_or_404(Board, pk=board_id)
    serializer = BoardSerializer(board)

    return Response(serializer.data, status=200)


@api_view(['put'])
def update_board(req, board_id):
    board = get_object_or_404(Board, pk=board_id)
    serializer = BoardSerializer(board, data=req.data, partial=True)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=200)

    return Response(serializer.errors, status=400)


@api_view(['delete'])
def delete_board(req, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.delete()

    return Response(status=200)
