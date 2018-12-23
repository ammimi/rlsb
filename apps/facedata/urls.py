from django.urls import path

from .views import FaceDataView,FaceDataListView,FaceDataCreateView,FaceDataUpdateView,FaceDataDetailView,FaceDataDeleteView


app_name = 'system'

urlpatterns = [
    path('', FaceDataView.as_view(), name='facedata'),
    path('list/', FaceDataListView.as_view(), name='list'),
    path('create/', FaceDataCreateView.as_view(), name='create'),
    path('update/', FaceDataUpdateView.as_view(), name='update'),
    path('detail/', FaceDataDetailView.as_view(), name='detail'),
    path('delete/', FaceDataDeleteView.as_view(), name='delete'),
    # path('upload/', FaceDataUploadView.as_view(), name='upload'),


]
