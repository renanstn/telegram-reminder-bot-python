from playhouse.db_url import connect

from settings import DATABASE_URL
from models import Reminder, database_proxy


def init_database():
    """
    Faz a conexão com o banco, e cria as models
    iniciais se necessário.
    """
    db = connect(DATABASE_URL)
    database_proxy.initialize(db)
    Reminder.create_table()
