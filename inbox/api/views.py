from inbox.api.serializers import NotificationSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class NotificationViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.ListModelMixin,
):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)
    # ListModeMixin提供的list方法会在quetryset中默认使用下面的filter
    filterset_fields = ('unread',)
    def get_queryset(self):
        # 只给出这个用户的notifications, 此处用到了django的反查机制
        # 与Notifications.objects.filter(recipient=self.request.user)等价
        return self.request.user.notifications.all()

    # 因为url规则使用-而不是_,所以这里用url_path重载
    @action(methods=['GET'], detail=False, url_path='unread-count')
    def unread_count(self, request, *args, **kwargs):
        count = self.get_queryset().filter(unread=True).count()
        return Response({'unread_count': count}, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, url_path='mark-all-as-read')
    def mark_all_as_read(self, request, *args, **kwargs):
        # 这里使用的是query set的update方法
        updated_count = self.get_queryset().update(unread=False)
        return Response({'marked_count': updated_count}, status=status.HTTP_200_OK)
