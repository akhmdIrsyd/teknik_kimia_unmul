# teknik_kimia_unmul
install python
buka comand promt lalu arahkan ke folder kimia_unmul
```
pip install --upgrade pip
```
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
apabila sudah,ketik di comand promt:
```
python manage.py migrate
```
lalu
```
python manage.py createsuperuser
```
