class MySqlConfig(object):

    pass


class RedisConfig(object):
    pass


sql_config = {
    'MySqlConfig': MySqlConfig,
    'RedisConfig': RedisConfig,
    'default': MySqlConfig,
}