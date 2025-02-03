import os
import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            s = ''
            name = old_function.__name__
            now = datetime.datetime.now()
            now = now.strftime('%Y-%m-%d %H:%M:%S')
            result = old_function(*args, **kwargs)  # результат вызова функции
            ## сохренение элементов args, kwargs  сначала в лист, потом преобразование в кортеж
            args_kwargs_list = []
            [args_kwargs_list.append(i) for i in args]

            if kwargs:  # если kwargs не пусто
                args_kwargs_list.extend(list(kwargs.values()))
            args_kwargs_list = tuple(args_kwargs_list)  # преобразование в кортеж

            s += f'{now, name, args_kwargs_list, result}\n'  # строка для записи
            with open(path, 'a',  encoding='utf-8') as f_write:  # файл  в режиме дополнения записей
                f_write.write(s)
            return result
        return new_function

    return __logger


def test_3():
    path = ('log_3task.log')

    if os.path.exists(path):
        os.remove(path)

    def discriminant(a, b, c):
        D = b ** 2 - 4 * a * c
        return D

    @logger(path)
    def solution(a, b, c):
        D = discriminant(a, b, c)
        if D < 0:
            return 'корней нет'
        elif D == 0:
            return (-b - D ** (0.5)) / (2 * a)
        else:
            return ((-b + D ** (0.5)) / (2 * a), (-b - D ** (0.5)) / (2 * a))

    result = solution(1, -2, 14)
    assert result == 'корней нет'

    result = solution(1, -2, 1)
    assert result == 1

    result = solution(1, 5, 6)
    assert result == (-2, -3)



    assert os.path.exists(path), f'файл {path} должен существовать'

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'solution' in log_file_content, 'должно записаться имя функции'

    for item in (1, -2, 14):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_3()