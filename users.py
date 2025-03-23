from werkzeug.security import generate_password_hash

# На проде это должно храниться в базе данных, но чтоьы показать, что мвп работает, сделали так
# Пароли захешированы для безопасности
USERS = {
    "admin@s7.ru": {
        "password": generate_password_hash("s7admin"),
        "name": "Администратор S7"
    },
    "analyst@s7.ru": {
        "password": generate_password_hash("s7analyst"),
        "name": "Аналитик S7"
    }
}
