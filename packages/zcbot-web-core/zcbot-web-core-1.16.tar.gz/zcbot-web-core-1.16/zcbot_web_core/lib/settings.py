from typing import List

from zcbot_web_core.lib import logger
from zcbot_web_core.client.mongo_client import Mongo

LOGGER = logger.get('配置')


class DynamicSettings(object):
    """
    简易配置管理器
    """
    # 主键索引
    row_map = {}
    # 组索引
    group_map = {}

    def __init__(self, collection: str, primary_field: str, value_field: str, group_field: str = None, mongo: Mongo = None):
        self.collection = collection
        self.primary_field = primary_field or '_id'
        self.value_field = value_field or 'value'
        self.group_field = group_field or 'group'
        self.mongo = mongo or Mongo()
        self.reload()

    def get_value(self, key):
        row = self.row_map.get(key)
        if row:
            return row.get(self.value_field)

        return None

    def get_row(self, key):
        row = self.row_map.get(key)

        return row

    def get_rows_by_group(self, group_key):
        rows = self.group_map.get(group_key)

        return rows

    def reload(self):
        items = self._fetch_items()
        hot_row_map = {}
        hot_group_map = {}
        for item in items:
            # 主键索引
            id = item.get(self.primary_field, None)
            if id:
                hot_row_map[id] = item
            else:
                LOGGER.warning(f'异常配置: id={id}, collection={self.collection}, primary_field={self.primary_field}, value_field={self.value_field}')

            # 分组索引
            group_key = item.get(self.group_field, None)
            if group_key:
                if group_key not in hot_group_map:
                    hot_group_map[group_key] = list()
                rows = hot_group_map.get(group_key)
                rows.append(item)

        self.row_map = hot_row_map
        self.group_map = hot_group_map

        LOGGER.info(f'更新配置: row={len(self.row_map.keys())}条 group={len(self.group_map.keys())}条, collection={self.collection}, primary_field={self.primary_field}, value_field={self.value_field}, group_field={self.group_field}')

    def _fetch_items(self):
        try:
            rs = self.mongo.list(collection=self.collection, query={})
            return rs
        except Exception as e:
            LOGGER.error(e)

        return []
