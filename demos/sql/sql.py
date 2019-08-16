from redis import ConnectionPool, StrictRedis
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.util.compat import contextmanager

from demos.sql import settings


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = settings.Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def init_db():
    """
    create all tables for database
    :return:
    """
    engine = get_engine()
    if engine:
        settings.Session = scoped_session(sessionmaker(bind=engine))
    # Base.metadata.create_all(engine)


def get_engine():
    """
    crate sqlalchemy connections
    :return: sqlalchemy engine
    """
    conf = settings.CONF
    engine_url = "mysql+pymysql://{}:{}@{}:3306/{}?charset=utf8".format(
        conf.db_info.user,
        conf.db_info.passwd,
        conf.db_info.ip,
        conf.db_info.db_name
    )
    engine = create_engine(
        engine_url,
        max_overflow=2,   # 超过连接池大小外最多创建的连接
        pool_size=8,
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=30   # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    # pool_pre_ping=True
    return engine


redis = StrictRedis(host='localhost', port=6379, db=0, password='foobared')