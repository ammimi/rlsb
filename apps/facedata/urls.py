from django.urls import path

from .views import FaceDataView,FaceDataListView,FaceDataCreateView,FaceDataUpdateView,FaceDataDetailView,FaceDataDeleteView
from .views_api import SendFaceDataView,DeleteFaceDataView,UpdateFaceDataView,ManualClockView

app_name = 'facedata'


urlpatterns = [
    path('', FaceDataView.as_view(), name='facedata'),
    path('list/', FaceDataListView.as_view(), name='list'),
    path('create/', FaceDataCreateView.as_view(), name='create'),
    path('update/', FaceDataUpdateView.as_view(), name='update'),
    path('detail/', FaceDataDetailView.as_view(), name='detail'),
    path('delete/', FaceDataDeleteView.as_view(), name='delete'),
    # path('upload/', FaceDataUploadView.as_view(), name='upload'),

    path('sendfacedata/',SendFaceDataView.as_view(),name='sendfacedata'),
    path('deletefacedata/',DeleteFaceDataView.as_view(),name='deletefacedata'),
    path('updatefacedata/', UpdateFaceDataView.as_view(), name='updatefacedata'),

    path('manualclock/', ManualClockView.as_view(), name='manualclock'),
]
