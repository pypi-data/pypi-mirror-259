from zcbot_web_core.lib import logger
from zcbot_web_core.client.mongo_client import Mongo

LOGGER = logger.get('配置')


class DynamicSettings(object):
    """
    简易配置管理器
    """
    big_map = {}

    def __init__(self, collection: str, primary_field: str, value_field: str, mongo: Mongo = None):
        self.collection = collection
        self.primary_field = primary_field
        self.value_field = value_field
        self.mongo = mongo or Mongo()
        self.reload()

    def get_value(self, key):
        row = self.big_map.get(key)
        if row:
            return row.get(self.value_field)

        return None

    def get_row(self, key):
        row = self.big_map.get(key)

        return row

    def reload(self):
        items = self._fetch_items()
        hot_map = {}
        for item in items:
            id = item.get(self.primary_field, None)
            if id:
                hot_map[id] = item
            else:
                LOGGER.warning(f'异常配置: id={id}, collection={self.collection}, primary_field={self.primary_field}, value_field={self.value_field}')

        self.big_map = hot_map

        LOGGER.info(f'更新配置: {len(self.big_map)}条, collection={self.collection}, primary_field={self.primary_field}, value_field={self.value_field}')

    def _fetch_items(self):
        try:
            rs = self.mongo.list(collection=self.collection, query={})
            return rs
        except Exception as e:
            LOGGER.error(e)

        return []
