echo ====MIGRATING [START]====
python manage.py migrate
echo ====MIGRATING [END]====

echo ====LOADING DATA [START]====
python manage.py initadmin
echo ====LOADING DATA [END]====

echo ====RUNNING [START]====
python manage.py runserver 0.0.0.0:8080 --noreload
