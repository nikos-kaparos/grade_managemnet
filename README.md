# Grading System Project

## Περιγραφή

Αυτό το project είναι ένα σύστημα διαχείρισης βαθμολογιών για εκπαιδευτικά ιδρύματα. Οι καθηγητές μπορούν να καταχωρούν βαθμολογίες για τους φοιτητές, η γραμματεία μπορεί να επιβεβαιώνει αυτές τις βαθμολογίες και οι φοιτητές μπορούν να βλέπουν την αναλυτική τους βαθμολογία.

## Τεχνολογίες

- **Django**: Web framework για την ανάπτυξη της εφαρμογής.
- **PostgreSQL**: Βάση δεδομένων για την αποθήκευση δεδομένων.
- **Docker**: Για την απομόνωση του περιβάλλοντος ανάπτυξης και παραγωγής.
- **Docker Compose**: Για την ευκολότερη διαχείριση των υπηρεσιών Docker.

## Απαιτήσεις

Πριν ξεκινήσεις, βεβαιώσου ότι έχεις εγκαταστήσει:

- Docker
- Docker Compose
- Python 3.x
- pip

## Εγκατάσταση

1. **Clone το repository:**
   ```bash
   git clone https://github.com/nikos-kaparos/grade_managemnet/tree/main
   cd grading_system
2. **Δημιουργία του περιβάλλοντος Docker:**
    ```bash
   docker-compose up --build
3. **Eκτέλεση migrations για τη βάση δεδομένων:**
   ```bash
   docker-compose run web python manage.py makemigrations
   docker-compose run web python manage.py migrate
4. Δημιουργία superuser (προαιρετικό):
   ```bash
   docker-compose run web python manage.py createsuperuser
## Πρόσβαση στην εφαρμογή:
Άνοιξε τον browser σου και πήγαινε στο http://localhost:8000
## Χρήση
Σύνδεση:
Για να συνδεθείς, θα πρέπει να έχεις έναν λογαριασμό. Οι φοιτητές πρέπει να έχουν username που αρχίζει με "it".
Οι ομάδες χρηστών περιλαμβάνουν:
Teacher
Secretariat
Students
Λειτουργίες:

Οι καθηγητές μπορούν να προσθέσουν βαθμολογίες.
Η γραμματεία μπορεί να επιβεβαιώσει τις βαθμολογίες.
Οι φοιτητές μπορούν να δουν τις αναλυτικές τους βαθμολογίες.
