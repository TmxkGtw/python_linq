from linq.linq_methodchain import *


def main():
    linqed_list = Items([1, 2, 3, 4, 5]
    ).map([
        lambda index, value : index * value,
        lambda index, value : index + value,]
    ).filter([
        lambda index, value : index % 2 == 0,]
    ).reduce(
        lambda v1, v2 : v1 + v2,
        initial_value = 0
    )
    print(linqed_list)


if __name__ == "__main__":
    main()

