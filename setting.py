import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# MYSQL
MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '1234')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '3306')
DB_NAME = os.environ.get('DB_NAME', 'demo')
DB_CONNECT_STRING_FORMAT = 'mysql+mysqldb://{username}:{password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'


# MYSQL 配置
MYSQL_CONF = {
    'connect_string': DB_CONNECT_STRING_FORMAT.format(
        username=MYSQL_USERNAME,
        password=MYSQL_PASSWORD,
        db_host=DB_HOST,
        db_port=DB_PORT,
        db_name=DB_NAME
    ),
    'host': DB_HOST,
    'port': DB_PORT,
    'username': MYSQL_USERNAME,
    'password': MYSQL_PASSWORD,
}