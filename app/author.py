#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: author.py
@time: 16-1-17 上午12:05
"""


from database import db_session
from models import Author


def get_row_by_id(author_id):
    """
    通过 id 获取作者信息
    :param author_id:
    :return: None/object
    """
    row = db_session.query(Author).filter(Author.id == author_id).first()
    return row


def get_row(*args, **kwargs):
    """
    获取作者信息
    Usage:
        # 方式一
        get_row(Author.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        get_row(**test_condition)
    :param args:
    :param kwargs:
    :return: None/object
    """
    if args:
        row = db_session.query(Author).filter(*args).first()
        return row
    if kwargs:
        row = db_session.query(Author).filter_by(**kwargs).first()
        return row
    return None


def add(author_data):
    """
    添加作者信息
    :param author_data:
    :return: None/Value of author.id
    """
    author = Author(**author_data)
    db_session.add(author)
    db_session.commit()
    return author.id


def edit(author_id, author_info):
    """
    修改作者信息
    :param author_id:
    :param author_info:
    :return: Number of affected rows (Example: 0/1)
    """
    author = db_session.query(Author).filter(Author.id == author_id)
    result = author.update(author_info)
    db_session.commit()
    return result


def delete(author_id):
    """
    删除作者信息
    :param author_id:
    :return: Number of affected rows (Example: 0/1)
    """
    author = db_session.query(Author).filter(Author.id == author_id)
    result = author.delete()
    db_session.commit()
    return result


def get_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取作者列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return: None/object
    """
    if args:
        rows = Author.query.filter(*args).paginate(page, per_page, False)
        return rows
    if kwargs:
        rows = Author.query.filter_by(**kwargs).paginate(page, per_page, False)
        return rows
    return None


def test():
    """
    测试
    :return:
    """
    print '测试增删改查'
    # 测试获取
    row = get_row_by_id(5)
    print row
    if row:
        print row.id, row.name, row.email
    # 测试添加
    author_info = {
        'name': 'Bob',
        'email': 'bob@gmail.com'
    }
    result = add(author_info)
    print result
    # 测试修改
    result = edit(6, {'name': 'Emma'})
    print result
    # 测试删除
    result = delete(6)
    print result


def test_get_row():
    """
    测试信息获取
    :return:
    """
    print '测试单条信息'
    test_condition = {
        'name': "Larry"
    }
    row = get_row(**test_condition)
    print row
    if row:
        print row.id, row.name, row.email

    row = get_row(Author.id > 1)
    print row
    if row:
        print row.id, row.name, row.email


def test_get_rows():
    """
    测试列表获取
    :return:
    """
    print '测试列表信息'
    rows = get_rows(1, 10, Author.id > 2, Author.id < 5)
    for item in rows.items:
        print item.id, item.name, item.email

    rows = get_rows(1, 10, **{'name': "Larry"})
    for item in rows.items:
        print item.id, item.name, item.email


if __name__ == '__main__':
    # test()
    test_get_row()
    test_get_rows()
