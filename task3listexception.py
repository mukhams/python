class NotIntTypeException(ValueError):

    def __init__(self, elem, message='Ошибка. Элемент списка должен быть числом'):
        self.elem = elem
        self.message = message
        super().__init__(self.message)


if __name__ == '__main__':

    print('Вводите элементы списка, нажимайте enter')
    print(' для окончания ввода просто нажмите enter')

    elems = []
    while True:
        s = input('-->> ')
        if s == '':
            break
        try:
            try:
                elems.append(int(s))
            except ValueError:
                raise NotIntTypeException(s)
        except NotIntTypeException as e:
            print(e.message)

    print('Список: ', elems)
