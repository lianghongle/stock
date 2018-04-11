#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime, timedelta
import sys

from common.model.Test import Test


@shared_task
def analysis_enter(game_id, date=None):
    date = date or (datetime.now() - timedelta(days=1)).strftime('%F')
    test.apply_async(kwargs={'game_id': game_id, 'date': date}, queue='{}_offline_queue'.format(game_id))
    test1.apply_async(kwargs={'game_id': game_id, 'date': date}, queue='{}_offline_queue'.format(game_id))

# from test.tasks import test
# test(100000020, '2000-10-10')
@shared_task
def test(game_id, date):
    """
    # 生产 自定义事件 数据分析
    :param game_id: 游戏Id
    :param date: 计算日期
    :return: 生产结果
    """

    funs = ['test1','test2']
    for fun in funs:
        funs(game_id, date)

    return True


@shared_task
def test3(game_id, date):

    print(sys._getframe().f_code.co_name)

    return True

@shared_task
def test1(game_id, date):

    print(sys._getframe().f_code.co_name)

    return True

@shared_task
def test2(game_id, date):

    print(sys._getframe().f_code.co_name)

    return True

# ********************************************************************************************
# import game_systems.x as x
#
# def test():
#     print('test')
#
#     x.xxx()
# ********************************************************************************************


def xxx(game_id, date):

    print(sys._getframe().f_code.co_name)

    return True


# ********************************************************************************************

# 2.增
# Model.objects.create(**kwargs)
# 3.查
# Model.objects.all()
# 4.改
# m = Model.objects.get(id=1)
# m.name = 'new_name'
# m.save()
# 5.删
# m = Model.objects.get(id=1)
# m.delete()
# from test.tasks import test_db
# test_db()
def test_db():
    test = Test.objects.get(id=1)
    print(test)

# ********************************************************************************************



# if __name__=='__main__':
#     print('xxx')
#     test_db()