SECRET_KEY = '5dc9b6c172f8f603c906457743a847e22196ff9d69dfcddcd11fc97bb8efc01e862408c29de2ac1703aff0adf9277da1c5c3d724cba6aac2aa83a534e7a99c3397fbd298c2706246160dcdf1a49521ef8d97a228c42268255f2e55efbbfa362b05ef857a'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'USER': 'user_mysite',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}