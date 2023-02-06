class Data(object):

    def __init__(self, string_date):
        self.string_date = string_date
        # self.string_date = '20-05-3903'

    @classmethod
    def extract(cls):
        cls.day, cls.month, cls.year = map(int, string_date.split('-'))
        return cls

    @staticmethod
    def validate(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 2050


if __name__ == '__main__':
    string_date = str(input('Введите дату в формате день-месяц-год: '))
    dateObj = Data(string_date).extract()
    is_valid = Data.validate(string_date)
    print('day: ', dateObj.day, ', month: ', dateObj.month, ', year: ', dateObj.year, ', is valid: ', is_valid)

