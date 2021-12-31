from os.path import abspath, dirname


BASE_DIR = dirname(dirname(abspath(__file__)))

APP_ENV_DEV = 'development'
APP_ENV_PROD = 'production'
APP_ENV_TEST = 'test'


JWT_SECRET_KEY = 'qwqelr]!"#$)!"]#$!"#${]~qwer!"#$1239487awerasodfe([[([([([9213847s})^d~]{!"#:cvkdsfjwqekeksdfe'


DATABASE_URI_LOCAL = 'mysql+mysqldb://orders_dev:orders_dev_pwd@localhost/orders'
DATABASE_URI_JAWSDB = 'mysql://cmhuw3zgryz6bgxe:tn7c6dx0i8565zr9@l6glqt8gsx37y4hs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/l0rhxvw3bxojgkns'
DATABASE_URI_CLEARDB = 'mysql://b56eb1d1b77a1b:1aff9528@us-cdbr-east-05.cleardb.net/heroku_048e25c9e1bcb3e?reconnect=true'
