from django.urls import path
from django.contrib import admin
from .views import task
from .views import event
from .views import user
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [
    path('admin/', user.admin, name='admin'),
    path('home/', user.home, name='home'),
    path('signup/', user.signup, name='signup'),
    path('logout/', user.signout, name='logout'),
    path('', user.signin, name='signin'),
    path('signin/', user.signin, name='signin'),
    path('event/checklist/<int:event_id>',
         event.event_checklist, name='event_checklist'),
    path('create/event/', event.create_event, name='create_event'),
    path('create/task/', task.create_task, name='create_task'),
    path('edit/event/<int:event_id>/', event.edit_event, name='edit_event'),
    path('edit/event/<int:event_id>/complete', event.complete_event, name='event_complete'),
    path('edit/event/<int:event_id>/delete', event.delete_event, name='event_delete'),
    path('home/search/', user.search_user, name='users_search'),
    path('edit/task/<int:task_id>/', task.edit_task, name='edit_task'),
    path('edit/task/<int:task_id>/delete', task.delete_task, name='task_delete'),
    path('password_reset', PasswordResetView.as_view(template_name='password_reset_form.html', email_template_name='password_reset.html'), name="password_reset"),
    path('password_reset_done', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/done', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
