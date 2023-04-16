import types
import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        with open('task3.log', 'a') as file:
            name = f'Function: {old_function.__name__}\n'
            file.write(name)
            start = str(datetime.datetime.now())
            file.write(f'{start}\n')
            items = f'Arguments: {args}{kwargs}\n'
            file.write(items)
            result = old_function(*args, **kwargs)
            file.write(f'Result: {result}\n')
            return result
    return new_function
@logger
def flat_generator(list_of_lists):
    for item in list_of_lists:
        for i in item:
            yield i


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    print("Operation is complete")


if __name__ == '__main__':
    test_2()