import os
import re
import operator
from math import prod


class Monkey:
    def __init__(self, number, starting_items, operation, test, throw_to):
        self.number = number
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.throw_to = throw_to
        self.total_inspections = 0

    def inspect(self, item, big_mod):
        self.total_inspections += 1
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        op = operations[self.operation[0]]

        if "old" in self.operation:
            self.starting_items[0] = op(item, item) % big_mod
            return True if self.starting_items[0] % self.test == 0 else False
        self.starting_items[0] = op(item, int(self.operation[2:])) % big_mod
        return True if self.starting_items[0] % self.test == 0 else False

    def throw(self, monkey):
        item = self.starting_items[0]
        monkey.starting_items.append(item)
        self.starting_items.pop(0)


def read_data(loc):
    data = {}
    with open (loc, "r") as file:
        raw_data = file.read().split("\n\n")
        raw_data = [line.split("\n") for line in raw_data]
        for line in raw_data:
            monkey_number = re.search(r"[0-9]+", line[0]).group(0)
            starting_items = [int(item) for item in re.findall(r"[0-9]+", line[1])]
            operation = line[2][23:]
            test = int(re.search(r"[0-9]+", line[3]).group(0))
            throw_to = [int(monkey) for monkey in re.findall(r"[0-9]+", line[4] + line[5])]
            data[monkey_number] = (starting_items, operation, test, throw_to)
    return data


def main():
    data = read_data(os.getcwd() + r"/day11.txt")
    monkeys = []
    for k, v in data.items():
        monkeys.append(Monkey(k, *v))

    big_mod = 1
    for monkey in monkeys:
        big_mod *= monkey.test

    monkey_business = []
    for i in range(10000):
        for monkey in monkeys:
            items = []
            for item in monkey.starting_items:
                items.append(item)
            for item in items:
                test = monkey.inspect(item, big_mod)
                if test:
                    to_monkey = monkey.throw_to[0]
                else:
                    to_monkey = monkey.throw_to[1]
                monkey.throw(monkeys[to_monkey])

            if i == 9999:
                monkey_business.append(monkey.total_inspections)
        
    print(monkey_business)
    print(prod(sorted(monkey_business)[-2:]))


if __name__ == "__main__":
    main()
