from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('services/', views.services_page, name='services'),
    path('events/', views.events_page, name='events'),
    path('events/<int:event_id>/', views.event_detail_view, name='event-detail'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('feedback/', views.feedback, name='feedback'),

    path('register/', views.user_register, name='user-register'),
    path('login/', views.user_login, name='user-login'),  # Ensure this matches LOGIN_URL
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('admin-register/', views.admin_register, name='admin-register'),
    path('admin-login/', views.admin_login, name='admin-login'),
    path('admin-panel/', views.admin_panel, name='admin-panel'),
    path('admin-panel/carousel-images/', views.admin_panel_carousel_images, name='admin-panel-carousel-images'),
    path('admin-panel/more-events/', views.admin_panel_more_events, name='admin-panel-more-events'),
    path('admin-register/verify-email/', views.verify_email, name='verify-email'),

    path('password-reset/', views.password_reset_request, name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/pages/password-reset/password_reset_done.html'), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/pages/password-reset/password_reset_complete.html'), name='password-reset-complete'),
    path('reset/invalid/', auth_views.PasswordResetConfirmView.as_view(template_name='main/pages/password-reset/password_reset_invalid.html'), name='password-reset-invalid'),

    path('admin-panel/more-events/add-event/', views.add_event, name='add-event'),
    path('admin-panel/more-events/update-event/<int:event_id>/', views.update_event, name='update-event'),
    path('admin-panel/more-events/delete-event/<int:event_id>/', views.delete_event, name='delete-event'),

    path('admin-panel/carousel-images/add-upcoming-events/', views.add_carousel_image, name='add-carousel-image'),
    path('admin-panel/carousel-images/update-upcoming-events/<int:image_id>/', views.update_carousel_image, name='update-upcoming-event'),
    path('admin-panel/carousel-images/delete-upcoming-events/<int:image_id>/', views.delete_carousel_image, name='delete-upcoming-event'),

    path('admin-panel/add-question/', views.add_question, name='add-question'),
    path('admin-panel/update-question/<int:question_id>/', views.update_question, name='update-question'),
    path('admin-panel/delete-question/<int:question_id>/', views.delete_question, name='delete-question'),
    path('admin-panel/delete-response/<int:user_id>/', views.delete_response, name='delete-response'),
    path('admin-panel/delete-all-responses/', views.delete_all_responses, name='delete-all-responses'),
    path('admin-panel/export-responses/', views.export_responses, name='export-responses'),
]
