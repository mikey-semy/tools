# Основные настройки
SERVER_MODE = False
MASTER_PASSWORD_REQUIRED = False
UPGRADE_CHECK_ENABLED = False

# Настройки безопасности
ENHANCED_COOKIE_PROTECTION = True
CONSOLE_LOG_LEVEL = 30

# Настройки сессий
SESSION_EXPIRATION_TIME = 24 * 60
SESSION_COOKIE_NAME = 'pgadmin4_session'

# Настройки UI
DEFAULT_BINARY_PATHS = {
    'pg': '/usr/local/bin',
    'ppas': '/usr/local/bin'
}
