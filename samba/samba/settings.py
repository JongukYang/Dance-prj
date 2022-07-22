"""
Django settings for samba project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from secret_data import s_SECRET_KEY

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 암호화를 위해 해시를 생성해주는 문자열, 패스워드 암호화, 배포시에 노출하면 안됨
SECRET_KEY = s_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
# 중요! 어떻게 서버를 킬것인지 정함, 개발자모드 또는 배포용으로 서버를 킬지 말지 정하는것
# DEBUT = True : 개발자모드, 많은 정보를 보여줌
# DEBUG = False : 사용자모드(배포시에), 정보가 적게 노출됨, 꼭 False로 배포할것
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'danceapp',
    'accounts',
    # The following apps are required:
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Social Login Provider Ex -> 네이버 카카오 등 해보기
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1  # 사이트 아이디 기본값

# 어떤 수단을 통해 로그인 진행할지 알려주는 것
AUTHENTICATION_BACKENDS = [
    # 기존 장고에 내장되어 있는 인증 기능
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # 소셜 로그인 기능
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# 로그인 성공했을 때 redirection 해주는 것
LOGIN_REDIRECT_URL = '/'

# 로그아웃 했을 때 redirection 해주는 것
LOGOUT_REDIRECT_URL = '/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'samba.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'samba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# 어떤 데이터베이스를 사용할것인지, 데이터베이스의 위치는 어디인지 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
# 디폴트 세팅 언어
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

import os
# static 파일에 접근 가능한 URL
STATIC_URL = '/static/'
# 사용자가 업로드한 미디어 파일이 저장되는 경로
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / 'static'
    ## 다른 방식의 경로 작성 방법
    # os.path.join(BASE_DIR, 'staticapp', 'static'),
]
# 미디어 파일에 접근 가능한 URL
MEDIA_URL = '/media/'
# 사용자가 업로드한 미디어 파일이 저장되는 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIAFILES_DIRS = [
#     BASE_DIR / 'media'
# ]



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
