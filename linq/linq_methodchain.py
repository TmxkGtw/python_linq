from typing import List, Dict, Callable, Union, Any
from copy   import deepcopy

class Items:
    def __init__(self, content : Union[List, Dict]):
        if type(content) is list:
            self.substance = enumerate(deepcopy(content))
        else:
            self.substance = deepcopy(content).items()

    def __str__(self):
        if type(content) is enumerate:
            return list(self.substance).__str__()
        else:
            return dict(self.substance).__str__()

    def show(self):
        if type(content) is enumerate:
            print(list(self.substance).__str__())
        else:
            print(dict(self.substance).__str__())
        return self

    def map(self, rules : List[Callable[[Any, Any], Any]]):
        transformed_items = self.substance

        for rule in rules:
            if type(transformed_items) is enumerate:
                transformed_items = enumerate([rule(index, value) for index, value in transformed_items])
            else:
                transformed_items = {key : rule(key, value) for key, value in transformed_items}.items()

        self.substance = transformed_items
        return self

    def filter(self, rules : List[Callable[[Any, Any], bool]]):
        transformed_items = self.substance

        for rule in rules:
            if type(transformed_items) is enumerate:
                transformed_items = enumerate([value for index, value in transformed_items if rule(index, value)])
            else:
                transformed_items = {key : value for key, value in transformed_items if rule(key, value)}.items()

        self.substance = transformed_items
        return self

    def reduce(self, rule : Callable[[Any, Any], Any], initial_value : Any):
        reduced_value = initial_value
        for accessor, value in self.substance:
            reduced_value = rule(reduced_value, value)

        return reduced_value

    def to_list(self):
        if type(self.substance) is enumerate:
            return list(self.substance)
        else:
            return [(key, value) for key, value in self.substance]

    def to_tuple(self):
        if type(self.substance) is enumerate:
            return tuple(self.substance)
        else:
            return tuple([(key, value) for key, value in self.substance])

    def to_dict(self):
        if type(self.substance) is enumerate:
            return {index : value for index, value in self.substance}
        else:
            return dict(self.substance)