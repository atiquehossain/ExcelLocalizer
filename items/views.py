from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from items.models import Item
from items.serializers import ItemSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_items(request):
    items = Item.objects.all()
    logger.debug(f"Retrieved {len(items)} items from database")
    serializer = ItemSerializer(items, many=True)
    return Response({
        "success": True,
        "items": serializer.data
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_item(request):
    name = request.data.get('name')
    description = request.data.get('description', '')
    if not name:
        return Response({"success": False, "error": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)
    item = Item.objects.create(name=name, description=description, user=request.user)
    logger.debug(f"Created new item: {item.name}")
    serializer = ItemSerializer(item)
    return Response({
        "success": True,
        "message": "Item created successfully",
        "item": serializer.data
    })