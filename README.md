# teknik_kimia_unmul
install python

update pip
```
pip install --upgrade pip
```
buka command prompt lalu arahkan ke folder kimia_unmul

arahkan ke folder kimia_unmul, lalu ketik:
```
pip install -r requirements.py
```
buat database
```
pip install mysqlclient
```
ubah settingan database di kimia_unmul/setting.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': <Database_name>,
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT': '3306',
    }
}
```
apabila gagal coba 
```
pip install mysql-connector-python
```
ubah setting.py 
```
DATABASES = {
    'default': {
        'NAME': 'user_data',
        'ENGINE': 'mysql.connector.django',
        'USER': 'mysql_user',
        'PASSWORD': 'password',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}
```
apabila sudah,ketik di command prompt:
```
python manage.py migrate
```
lalu, untuk membuat akun, ketik:
```
python manage.py createsuperuser
```

apabila sudah, coba jalankan website:
```
python manage.py runserver ip-address_atau_domain:8000
```
buka website dengan mengetik url berikut pada browser
```
python manage.py runserver ip-address_atau_domain:8000
```
untuk mengakses admin, ketik:
```
python manage.py runserver ip-address_atau_domain:8000/admin
```
