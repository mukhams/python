class Devidebyzero(Exception):

    def __init__(self, delitel, message="Делитель не может быть равен 0"):
        self.delitel = delitel
        self.message = message
        super().__init__(self.message)


if __name__ == '__main__':
    delimoe = int(input("Введите делимое: "))
    delitel = int(input("Введите делитель: "))
    try:
        if delitel == 0:
            raise Devidebyzero(delitel)
    except Devidebyzero as e:
        print(e.message)
        print('Попробуйте еще раз')
    else:
        chastnoe = delimoe / delitel
        print('Частное: ', chastnoe)


