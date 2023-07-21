# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'

# This needed to have a global static templates - css - js files.
STATICFILES_DIRS = [ BASE_DIR / 'staticfiles',]

# ADDED TO GET CSS STYLES AND RESOURCES FROM STATIC FOLDER
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'