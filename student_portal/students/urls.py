from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('students/',views.students_page, name='students-page'),
    path('add/',views.add_student, name='add-student'),
    path('delete/<int:id>/',views.delete_student, name='delete-student'),
    path('edit/<int:id>/',views.edit_student, name='edit-student'),
    path('login/',views.login_user, name='login-user'),
    path('logout/',views.logout_user, name='logout-user'),
    path('register/',views.register_user, name='register-user'),
    path('change_password/',views.change_password, name='change_password'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('reset_password/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('api/students/<int:id>/',views.StudentDetailAPI.as_view(), name='student-detail-api'),
]