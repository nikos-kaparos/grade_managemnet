from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Grade
from .forms import GradeForm
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Επαλήθευση χρήστη
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Έλεγχος αν ο χρήστης είναι φοιτητής
            if user.groups.filter(name='Students').exists():
                # Ελέγχει αν το username των φοιτητών αρχίζει με "it"
                if username.startswith('it'):
                    login(request, user)
                    return redirect('view_grades')
                else:
                    return render(request, 'login.html', {'error': 'Το όνομα χρήστη των φοιτητών πρέπει να αρχίζει με "it"'})
            
            # Αν ο χρήστης είναι καθηγητής
            elif user.groups.filter(name='Teacher').exists():
                login(request, user)
                return redirect('add_grade')

            # Αν ο χρήστης είναι από τη γραμματεία
            elif user.groups.filter(name='Secretariat').exists():
                login(request, user)
                return redirect('confirm_grades')
            else:
                return render(request, 'login.html', {'error': 'Δεν έχετε αντιστοιχιστεί σε ομάδα'})
        
        # Επιστροφή μηνύματος σφάλματος αν τα credentials είναι λανθασμένα
        return render(request, 'login.html', {'error': 'Λανθασμένα στοιχεία εισόδου'})

    return render(request, 'login.html')

#def teacher_dashboard(request):
    #return render(request, 'add_grade.html')

#def secretariat_dashboard(request):
    #return render(request, 'confirm_grade.html')

#def student_dashboard(request):
    #return render(request, 'view_greades.html')


# 1. View για την Καταχώρηση Νέας Βαθμολογίας από τον Καθηγητή
@login_required
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_grade_success')  # Ανακατεύθυνση μετά την επιτυχία
    else:
        form = GradeForm()

    return render(request, 'add_grade.html', {'form': form})

def add_grade_success(request):
    return render(request, 'add_grade_success.html')

# 2. View για την Εμφάνιση των Βαθμολογιών προς Επιβεβαίωση από τη Γραμματεία
@login_required
def confirm_grades(request):
    grades = Grade.objects.filter(is_confirmed=False)  # Φέρνουμε μόνο μη επιβεβαιωμένες βαθμολογίες
    return render(request, 'confirm_grades.html', {'grades': grades})

# 3. View για την Επιβεβαίωση μιας Συγκεκριμένης Βαθμολογίας από τη Γραμματεία
@require_POST
@login_required
def confirm_grade(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)  # Φέρνουμε τη βαθμολογία με βάση το grade_id
    grade.is_confirmed = True  # Επιβεβαίωση της βαθμολογίας
    grade.save()
    return redirect('confirm_grades')  # Ανακατεύθυνση στη σελίδα επιβεβαίωσης

@login_required
def view_grades(request):
    student_grades = Grade.objects.filter(student=request.user)
    return render(request, 'view_grades.html', {'grades': student_grades})
