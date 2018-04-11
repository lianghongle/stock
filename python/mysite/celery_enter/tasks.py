#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import sys
import importlib
from datetime import datetime
from datetime import timedelta
from django.conf import settings


# @shared_task
# def offline_analysis_enter(game_id, date=None):
#     """
#     离线分析入口
#     由offline_run函数执行后最后触发，不需要手动触发
#     :param game_id:
#     :param date:
#     :return:
#     """
#
#     # 传日期，使用指定日期；不传，使用脚本运行前一天
#     date = date or (datetime.now() - timedelta(days=1)).strftime('%F')
#
#     game_id_list = game_id if isinstance(game_id, list) else [game_id]
#     offline_module_list = [
#         i for i in settings.INSTALLED_APPS
#         if not i.startswith('django')
#         and hasattr(sys.modules[i], '__analysis_type__')
#         and sys.modules[i].__analysis_type__ == 'offline'
#     ]
#     for game_id in game_id_list:
#         for m in offline_module_list:
#             try:
#                 tasks = importlib.import_module(m + u'.tasks')
#                 # tasks.analysis_enter.delay(game_id, date)
#                 tasks.analysis_enter.apply_async(args=[game_id, date], queue='{}_offline_queue'.format(game_id))
#             except ImportError:
#                 continue


@shared_task
def enter_1_min():

    return True

@shared_task
def realtime_analysis_enter(game_id, date=None):
    """
    实时分析入口
    手动触发，5分钟分析一次缓存数据并写入result库
    :param game_id: 
    :param date: 
    :return: 
    """
    now_time = datetime.now()
    now_time_str = now_time.strftime('%F %T')
    game_id_list = game_id if isinstance(game_id, list) else [game_id]
    realtime_module_list = [
        i for i in settings.INSTALLED_APPS
        if not i.startswith('django')
        and hasattr(sys.modules[i], '__analysis_type__')
        and sys.modules[i].__analysis_type__ == 'realtime'
    ]
    for game_id in game_id_list:
        for m in realtime_module_list:
            try:
                tasks = importlib.import_module(m + u'.tasks')
                # tasks.analysis_enter.delay(game_id, now_time_str)
                tasks.analysis_enter.apply_async(args=[game_id, now_time_str], queue='{}_realtime_analysis_queue'.format(game_id))
            except ImportError:
                continue
