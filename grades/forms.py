from django import forms
from .models import Grade
from django.contrib.auth.models import User

class GradeForm(forms.Form):
    student_username = forms.CharField(label="Student Username")
    subject = forms.CharField(max_length=100)
    score = forms.FloatField()
    
    def save(self, commit=True):
        student_username = self.cleaned_data['student_username']
        subject = self.cleaned_data['subject']
        score = self.cleaned_data['score']
        """"
        # Βρίσκουμε τον φοιτητή με βάση το username
        student = User.objects.get(username=student_username)
        """
         # Ελέγχουμε αν υπάρχει ο χρήστης με το username
        try:
            student = User.objects.get(username=student_username)
        except User.DoesNotExist:
            # Δημιουργούμε νέο χρήστη αν δεν υπάρχει
            student = User.objects.create_user(username=student_username)
        
        # Δημιουργούμε τη βαθμολογία
        grade = Grade(student=student, subject=subject, score=score)
        if commit:
            grade.save()
        return grade
