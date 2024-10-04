from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    #path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    #path('secretariat-dashboard/', views.secretariat_dashboard, name='secretariat_dashboard'),
    #path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('add-grade/', views.add_grade, name='add_grade'),         # Διαδρομή για την καταχώρηση βαθμολογίας
    path('add-grade-success/', views.add_grade_success, name='add_grade_success'),  # Νέο URL για την επιτυχή καταχώρηση
    path('confirm-grades/', views.confirm_grades, name='confirm_grades'),
    path('confirm-grade/<int:grade_id>/', views.confirm_grade, name='confirm_grade'),  # Διαδρομή για επιβεβαίωση βαθμολογίας
    path('view-grades/', views.view_grades, name='view_grades'),   # Διαδρομή για την προβολή αναλυτικής βαθμολογίας
]
