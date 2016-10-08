# -*- coding: utf-8 -*-

from BASE import BASE
from operator import attrgetter

# 汎用基底クラスを継承して名簿クラス作成
class Persons(BASE):
    pass

# 汎用基底クラスを継承して成績データクラスの作成
class Data(BASE):
    def __init__(self, id, name, kokugo, eigo):
        self.id     = id
        self.name   = name
        self.kokugo = kokugo
        self.eigo   = eigo

# 成績データオブジェクトリストを返す
def get_persons():
    '''
    >>> get_persons()
    [{'eigo': 10, 'id': '0004', 'kokugo': 20, 'name': 'C'},
     {'eigo': 40, 'id': '0001', 'kokugo': 10, 'name': 'A'},
     {'eigo': 30, 'id': '0002', 'kokugo': 40, 'name': 'D'},
     {'eigo': 20, 'id': '0003', 'kokugo': 30, 'name': 'B'}]
    ]
    '''
    # 名簿オブジェクト作成
    p = Persons()
    # 名簿オブジェクトに成績データオブジェクトを入れる
    p['0001'] = Data('0001', 'A', 10, 40)
    p['0003'] = Data('0003', 'B', 30, 20)
    p['0002'] = Data('0002', 'D', 40, 30)
    p['0004'] = Data('0004', 'C', 20, 10)
    persons   = p.values()
    return persons

# 出力時のデコレーション用
def output_decoration(func):
    def wrapper(*args,**kwargs):
        print('# sort_key: %(sort_key)s' % kwargs)
        print('+----+-----+------+------+')
        print('|%-4s|%-5s|%-6s|%-6s|' % ('id', 'name', 'kokugo', 'eigo'))
        print('+----+-----+------+------+')
        func(*args,**kwargs)
        print('+----+-----+------+------+')
    return wrapper

# sorted の keyパラメータに operator モジュールの attrgetter() を指定したソート
@output_decoration
def output_use_operator(persons, sort_key):
    for person_data in sorted(persons, reverse=False, key=attrgetter(sort_key)):
        print('|%(id)4s|%(name)-5s|%(kokugo)6d|%(eigo)6d|' % person_data)

# sorted の keyパラメータに lambda を指定したソート
@output_decoration
def output_use_lambda(persons, sort_key):
    for person_data in sorted(persons, reverse=False, key=lambda x: x[sort_key]):
        print('|%(id)4s|%(name)-5s|%(kokugo)6d|%(eigo)6d|' % person_data)

if __name__ == '__main__' :

    # 成績データオブジェクトリスト取得
    persons = get_persons()
    # 国語の点数をソートキーとして出力する (sortedのkeyパラメータは attrgetter() )
    print "\n# sort_parameter: operator.attrgetter"
    output_use_operator(persons, sort_key='kokugo')
    # 英語の点数をソートキーとして出力する (sortedのkeyパラメータは lambda)
    print "\n# sort_parameter: lambda"
    output_use_lambda(persons, sort_key='eigo')
