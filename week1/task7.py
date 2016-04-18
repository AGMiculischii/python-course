'''
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от
одного класса до другого.
Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке
указано от каких классов наследуется i-й класс. Обратите внимание, что класс
может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам
от себя (прямо или косвенно), что класс не наследуется явно от одного класса
более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в
формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1
является предком класса 2, и "No", если не является.
'''
#!/usr/bin/env python3
# coding=utf-8

import sys

def build_tree(classes):
    tree = {}

    # build classes' relationship tree
    for relation in classes:
        child, *parents = relation

        if len(parents) == 0:
            tree[child] = []
        else:
            tree[child] = parents.pop().split()

    return tree

def is_parent(tree, start, end, path=[]):
    path = path + [start]

    if start not in tree:
        return None
    if start == end:
        return path

    for cl in tree[start]:
        if cl not in path:
            newpath = is_parent(tree, cl, end, path)

            if newpath:
                return newpath

    return None

def read_int():
    return int(sys.stdin.readline())

# read n classes relationship queries from stdin
def read_classes(n):
    reader = (tuple(map(str.strip, line.split(':'))) for line in sys.stdin)
    classes = []

    for i in range(n):
        classes.append(next(reader))

    return classes

# read q check queries from stdin
def read_queries(q):
    reader = (tuple(map(str, line.split())) for line in sys.stdin)
    queries = []

    for i in range(q):
        queries.append(next(reader))

    return queries

def main():
    n = read_int()

    classes = read_classes(n)
    relationships = build_tree(classes)

    q = read_int()
    queries = read_queries(q)

    for query in queries:
        base, child = query
        if is_parent(relationships, child, base):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
