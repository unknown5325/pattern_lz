def main3():
    class VisitableDict(dict):
        def accept(self, visitor):
            visitor.visit_dict(self)

    class VisitableList(list):
        def accept(self, visitor):
            visitor.visit_list(self)

    class Printer():
        def visit_dict(self, instance):
            print('dict keys: {}'.format(', '.join(instance.keys())))

        def visit_list(self, instance):
            print('list = {} '.format(instance))


    visitable_dict = VisitableDict({'one': 1, 'two': 2, 'three': 3})
    visitable_dict.accept(Printer())

    visitable_list = VisitableList([1,2,4,3,4,1,31,24,412,1412,312,4])
    visitable_list.accept(Printer())


if __name__ == "__main__":
    main3()