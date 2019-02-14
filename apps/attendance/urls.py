from django.urls import path

from .views import AttendanceInfoView,AttendanceInfoListView,AttendanceInfoCreateView,AttendanceInfoUpdateView,AttendanceInfoDetailView,AttendanceInfoDeleteView,AttendanceInfoExportView
from .views_api import RecognizeWithVideoFrame

app_name = 'attendance'

urlpatterns = [
    path('', AttendanceInfoView.as_view(), name='attendanceinfo'),
    path('list/', AttendanceInfoListView.as_view(), name='list'),
    path('export/', AttendanceInfoExportView.as_view(), name='export'),
    path('create/', AttendanceInfoCreateView.as_view(), name='create'),
    path('update/', AttendanceInfoUpdateView.as_view(), name='update'),
    path('detail/', AttendanceInfoDetailView.as_view(), name='detail'),
    path('delete/', AttendanceInfoDeleteView.as_view(), name='delete'),
    # path('upload/', AttendanceInfoUploadView.as_view(), name='upload'),

    path('recognizewithvideo/', RecognizeWithVideoFrame.as_view(), name='recognizewithvideo'),

]
