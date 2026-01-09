from .base import *
import os
from decouple import config

# ==================== 鍩虹璁剧疆 ====================
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# ==================== 搴旂敤閰嶇疆 ====================
# 纭繚 INSTALLED_APPS 鏄垪琛?
if not isinstance(INSTALLED_APPS, list):
    INSTALLED_APPS = list(INSTALLED_APPS)

# 绉婚櫎鎵€鏈夊彲鑳介噸澶嶇殑搴旂敤
apps_to_remove = ['allauth', 'allauth.account', 'allauth.socialaccount', 'debug_toolbar']
INSTALLED_APPS = [app for app in INSTALLED_APPS if app not in apps_to_remove]

# 娣诲姞蹇呴渶鐨勫簲鐢紙纭繚椤哄簭鍜屽敮涓€鎬э級
required_apps = [
    'django.contrib.sessions',
    'django.contrib.messages',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

for app in required_apps:
    if app not in INSTALLED_APPS:
        INSTALLED_APPS.append(app)

# ==================== 涓棿浠堕厤缃?====================
# 姝ｇ‘鐨勪腑闂翠欢椤哄簭锛堥潪甯搁噸瑕侊紒锛?
MIDDLEWARE = [
    # Django 鏍稿績涓棿浠?
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # 绗笁鏂逛腑闂翠欢
    'allauth.account.middleware.AccountMiddleware',      # 蹇呴』鍦?AuthenticationMiddleware 涔嬪悗
    'debug_toolbar.middleware.DebugToolbarMiddleware',   # 閫氬父鏀惧湪鏈€鍚?
]

# ==================== 鏁版嵁搴撻厤缃?====================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ==================== Debug Toolbar 閰嶇疆 ====================
INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

def show_toolbar(request):
    """鎬绘槸鏄剧ず Debug Toolbar"""
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

# ==================== Django Allauth 閰嶇疆 ====================
# 纭繚 SITE_ID 宸茶缃?
if not hasattr(locals(), 'SITE_ID'):
    SITE_ID = 1

# 璁よ瘉鍚庣
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Allauth 璁剧疆
# ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # 已弃用
ACCOUNT_LOGIN_METHODS = {'email', 'username'}  # 鍏佽鐢ㄦ埛鍚嶆垨閭鐧诲綍
# ACCOUNT_EMAIL_REQUIRED = True  # 已弃用
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']                     # 闇€瑕侀偖绠?
ACCOUNT_EMAIL_VERIFICATION = 'optional'           # 閭楠岃瘉鍙€?
LOGIN_REDIRECT_URL = '/'                          # 鐧诲綍鍚庨噸瀹氬悜
LOGOUT_REDIRECT_URL = '/'                         # 鐧诲嚭鍚庨噸瀹氬悜

# ==================== Stripe 鏀粯閰嶇疆 ====================
STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default='')

# ==================== 闈欐€佹枃浠跺拰濯掍綋鏂囦欢 ====================
# 寮€鍙戠幆澧冮潤鎬佹枃浠惰缃?
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ==================== 瀹夊叏璁剧疆锛堝紑鍙戠幆澧冿級 ====================
# 寮€鍙戠幆澧冨厑璁告墍鏈変富鏈猴紙浠呯敤浜庡紑鍙戯級
if DEBUG:
    ALLOWED_HOSTS = ['*']
    # 绂佺敤 HTTPS 閲嶅畾鍚?
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

# ==================== 鏃ュ織閰嶇疆 ====================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
