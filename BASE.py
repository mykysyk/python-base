# coding: utf-8

class BASE(object):

    def __init__(self):
        pass

    def __setitem__(self, key, value):
        '''
        >>> b = BASE()
        >>> b['key1'] = 'value1'
        >>> b['key2'] = 'value2'
        >>> print(b.key1)
        value1

        '''
        self.__dict__[key] = value
        return (self.__dict__[key], value)

    def __getitem__(self, key):
        '''
        >>> b = BASE()
        >>> b['key1'] = 'value1'
        >>> b['key2'] = 'value2'
        >>> print(b['key2'])
        value2

        '''
        return self.__dict__[key]

    def __len__(self):
        '''
        >>> b = BASE()
        >>> b['key1'] = 'value1'
        >>> b['key2'] = 'value2'
        >>> len(b)
        2

        '''
        return len(self.__dict__)

    def __iter__(self):
        '''
        >>> b = BASE()
        >>> b['key1'] = 'value1'
        >>> b['key2'] = 'value2'
        >>> for i in b: print(i)
        ('key2', 'value2')
        ('key1', 'value1')

        '''
        return self.__dict__.iteritems()

    def __contains__(self, key):
        '''
        >>> b = BASE()
        >>> b['key1'] = 'value1'
        >>> b['key2'] = 'value2'
        >>> 'key' in b
        True

        '''
        if key in self.__dict__.keys(): return True
        else: return False

    def __str__(self):
        '''
        >>> b = BASE()
        >>> b['key3'] = 10.0 / 3
        >>> print(b.key3)
        3.33333333333
        >>> print(b['key3'])
        3.33333333333

        '''
        return str(self.__dict__)

    def __repr__(self):
        '''
        >>> b = BASE()
        >>> b['key1'] = 'value1'
        >>> b['key2'] = 'value2'
        >>> b['key3'] = 10.0 / 3
        >>> print(b)
        {'key3': 3.3333333333333335, 'key2': 'value2', 'key1': 'value1'}

        '''
        return repr(self.__dict__)

    def keys(self):
        '''
        >>> b = BASE()
        >>> b['key1'] = 'value1'
        >>> b['key2'] = 'value2'
        >>> b['key3'] = 10.0 / 3
        >>> b.keys()
        ['key3', 'key2', 'key1']

        '''
        return self.__dict__.keys()

    def values(self):
        '''
        >>> b = BASE()
        >>> b['key1'] = 'value1'
        >>> b['key2'] = 'value2'
        >>> b['key3'] = 10.0 / 3
        >>> b.values()
        [3.3333333333333335, 'value2', 'value1']

        '''
        return self.__dict__.values()

    def items(self):
        '''
        >>> b = BASE()
        >>> b['key1'] = 'value1'
        >>> b['key2'] = 'value2'
        >>> b['key3'] = 10.0 / 3
        >>> b.items()
        [('key3', 3.3333333333333335), ('key2', 'value2'), ('key1', 'value1')]

        '''
        return self.__dict__.items()

def usage():

    class Example(BASE): 
        pass

    ex = Example()

    ex['key1'] = 'value1'
    ex.key2    = 'value2'
    ex.key3    = 10.0 / 3

    print('''\n### usage ### \n\n'''
          '''class Example(BASE):\n'''
          '''    pass\n'''
          '''\n'''
          '''ex = Example()\n'''
          '''ex['key1'] = 'value1'\n'''
          '''ex.key2    = 'value2'\n'''
          '''ex.key3    = 10.0 / 3\n'''
          )

    print('print(type(ex))\n')
    print('    =>  %s\n' % type(ex))

    print('print(ex)\n')
    print('    =>  %s\n' % ex)

    print('print(ex.key1)\n')
    print('    =>  %s\n' % ex.key1)

    print('''print(ex['key2'])\n''')
    print('    =>  %s\n' % ex['key2'])

    print('''print(ex['key3'])\n''')
    print('    =>  %s\n' % ex['key3'])

    print('print(len(ex))\n')
    print('    =>  %d\n' % len(ex))

    print('print(ex.keys())\n')
    print('    =>  %s\n' % ex.keys())

    print('print(ex.values())\n')
    print('    =>  %s\n' % ex.values())

    print('print(ex.items())\n')
    print('    =>  %s\n' % ex.items())

    print('print([ i for i in ex ])\n')
    print('    =>  %s\n' % [ i for i in ex ])

    print('''print('key1' in ex)\n''')
    print('    =>  %s\n' % ('key1' in ex))

    print('''print('key4' in ex)\n''')
    print('    => %s\n'  % ('key4' in ex))

if __name__ == '__main__' : usage()
