from config import settings

# Environment-specific settings
if settings.DEBUG_MODE:
    print(f"Running in debug mode for {settings.APP_NAME}")
else:
    print(f"Running in production mode for {settings.APP_NAME}")
