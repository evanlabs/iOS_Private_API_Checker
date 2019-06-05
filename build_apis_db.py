import os
from config import sqlite3_info, db_names
from db_helper import create_dbs, api_dbs
from config import sdks_configs
from api import api_utils


import sys


def rebuild_sdk_private_apis(sdk_info):
    print('SET_A')
    print(rebuild_dump_framework_api(sdk_info['sdk_version'], sdk_info['framework_path']))


def rebuild_dump_framework_api(sdk_version, framework_folder):
    """
    public-framework-dump-apis
    SET_A
    :param sdk_version: 版本
    :param framework_folder: public路径
    """
    table_name = db_names['SET_A']
    # 先清除已有版本的api
    api_dbs.delete_api_by_sdk_version(table_name, sdk_version)
    framework_dump_header_apis = api_utils.frame_work_dump_apis(sdk_version, framework_folder)

    # [{'class':'','methods':'','type':''},{},{}]
    return api_dbs.insert_apis_by_sdk(table_name, framework_dump_header_apis)


if __name__ == '__main__':
    if not os.path.exists(sqlite3_info['sqlite3']):
        print('sqlite3 db not exists, creating......')
        create_dbs.create_relate_tables()


    for sdk_info in sdks_configs:
        rebuild_sdk_private_apis(sdk_info)