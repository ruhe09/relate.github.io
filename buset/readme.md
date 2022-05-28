#1

django-admin startproject bst
py manage.py startapp buset
settings.py

Untuk kontrol database gunakan models.py, rules nya disitu, jangan lupa untuk masukkan ke apps.py dan ke main settings.py




Run python manage.py makemigrations untuk dijadikan migration-able.
ex py .\manage.py makemigrations buset 
Run python manage.py migrate untuk migrate db.
check what happen: py .\manage.py sqlmigrate buset 0001 
django.contrib.admin – The admin site. You’ll use it shortly.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.

view --> url -->

#3

template
get_object_or_404(Posting, pk=title_id)
url spacing

#4

form demo
generic view

#5

automated test

#6

static files handle django

#7

customize django package

#8 

step allauth
settings.py di set untuk melibatkan allauth

SITE_ID = 1

LOGIN_REDIRECT_URL = '/buset/'

installed apps dibawah ini di include

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.google',

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

AUTHENTICATION_BACKENDS = (
 #used for default signin such as loggin into admin panel
 'django.contrib.auth.backends.ModelBackend', 
  
 #used for social authentications
 'allauth.account.auth_backends.AuthenticationBackend',
 )

 jangan lupa set url apps
 path('accounts/', include('allauth.urls')),

 setting token di admin page

 buat ui untuk redirect ke accounts

 daftarkan callback ke oauth