from pathlib import Path
import os

# ========================
# 📁 BASE CONFIG
# ========================

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-2pinri!ipu6^suqdw!@2(f-^x^*pi6a@)$nzoiki!ah##ur^%h'
DEBUG = True
ALLOWED_HOSTS = []

# ========================
# 🔌 APPS
# ========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # ton app principale
]

# ========================
# 🧱 MIDDLEWARE
# ========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mental_platform.urls'

# ========================
# 🎨 TEMPLATES
# ========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'core', 'templates', 'core'),  # pour registration/login.html
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # requis pour login/logout
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mental_platform.wsgi.application'

# ========================
# 🗃 DATABASE
# ========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ========================
# 🔐 PASSWORDS
# ========================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========================
# 🌍 I18N & TZ
# ========================

LANGUAGE_CODE = 'fr-fr'  # tu peux mettre 'en-us' si tu préfères
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ========================
# 🎨 STATIC FILES
# ========================

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core', 'static'),
]

# ========================
# 📧 EMAIL (dev)
# ========================

# ========================
# 📧 EMAIL (prod - Gmail)
# ========================
# ========================
# 📧 EMAIL (via Gmail SMTP)
# ========================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'bachirkarmeni@gmail.com'  # ✅ ton adresse Gmail
EMAIL_HOST_PASSWORD = ''       # ⚠️ mot de passe d'application


# ========================
# 🔐 LOGIN/LOGOUT
# ========================

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# ========================
# 🔑 DEFAULT PRIMARY KEY
# ========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
