import re

class Operation:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
    def execute(self, value):
        temp = 0
        if self.operator == 'add':
            temp = value + self.operand
        elif self.operator == 'subtract':
            temp = value - self.operand
        elif self.operator == 'multiply':
            temp = value * self.operand
        elif self.operator == 'divide':
            temp = value // self.operand
        elif self.operator == 'raise_to':
            temp = value ** self.operand
        return temp

class Test:
    def __init__(self, test_val, true_monkey, false_monkey):
        self.test_val = test_val
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
    def evaluate(self, value):
        if value % self.test_val:
            return self.false_monkey
        else:
            return self.true_monkey

class Monkey:
    all_monkeys = []
    denominator = 1
    def get_monkey(name):
        for monkey in Monkey.all_monkeys:
            if name == monkey.name:
                return monkey
        return None
    def compute_denominator():
        if Monkey.denominator == 1:
            for monkey in Monkey.all_monkeys:
                Monkey.denominator *= monkey.test.test_val
        return Monkey.denominator
    def __init__(self, name, items, operation, test):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.num_inspections = 0
        Monkey.all_monkeys.append(self)
    def inspect_and_throw(self, verbose=True):
        if verbose:
            print('Monkey {}:'.format(self.name))
        while self.items:
            item = self.items.pop(0)
            if verbose:
                print('...inspects an item with worry level {}.'.format(item))
            item = self.operation.execute(item)
            #item //= 3
            item %= Monkey.compute_denominator()
            if verbose:
                print('...transformed worry level is {}.'.format(item))
            dest_monkey_name = self.test.evaluate(item)
            if verbose:
                print('...throws item with worry level {} to monkey {}'.format(item, dest_monkey_name))
            dest_monkey = Monkey.get_monkey(dest_monkey_name)
            dest_monkey.catch(item, verbose)
            self.num_inspections += 1
    def catch(self, item, verbose=True):
        if verbose:
            print('Monkey {} catches an item with worry level {}'.format(self.name, item))
        self.items.append(item)
        if verbose:
            print('...new item list is: {}'.format(self.items))

def make_monkeys(infile='aoc11_input.txt'):
    monkeys = []
    with open(infile) as f:
        while True:
            line1 = f.readline().strip()
            print(line1)
            monkey_name = int(line1.split()[1][:-1])
            #monkey_name = re.search(r'Monkey (0-9+):', line1).group(0)
            print('Monkey name = {}'.format(monkey_name))
            line2 = f.readline().strip()
            print(line2)
            monkey_items_str_list = line2.split()
            monkey_items = []
            if len(monkey_items_str_list) >= 2:
                for item in monkey_items_str_list[2:]:
                    print(item)
                    if item[-1] == ',':
                        item = item[:-1]
                    monkey_items.append(int(item))
            #monkey_items_re = re.match(r'Starting items: (0-9+)[,(0-9)+]*)', line2)
            #monkey_items = []
            #for item in monkey_items_re:
            #    print('...holds item {}'.format(item))
            #    monkey_items.append(int(item))
            line3 = f.readline().strip()
            print(line3)
            line3_parts = line3.split()
            monkey_op_re = line3_parts[4]
            monkey_operand_re = line3_parts[5]
            #monkey_operation_re = re.match(r'Operation: new = old (+-*/) (0-9+))', line3)
            #monkey_op_re = monkey_operation_re.group(0)
            #monkey_operand_re = monkey_operation_re.group(1)
            monkey_op = None
            monkey_operand = 0
            if monkey_op_re == '+':
                monkey_op = 'add'
                monkey_operand = int(monkey_operand_re)
            elif monkey_op_re == '-':
                monkey_op = 'subtract'
                monkey_operand = int(monkey_operand_re)
            elif monkey_op_re == '*':
                if monkey_operand_re == 'old':
                    monkey_op = 'raise_to'
                    monkey_operand = 2
                else:
                    monkey_op = 'multiply'
                    monkey_operand = int(monkey_operand_re)
            else:
                monkey_op = 'divide'
                monkey_operand = int(monkey_operand_re)
            line4 = f.readline().strip()
            print(line4)
            monkey_test = int(line4.split()[3])
            #monkey_test_re = re.match(r'Test: divisible by (0-9+))', line4)
            #monkey_test = int(monkey_test_re.group(0))
            line5 = f.readline().strip()
            print(line5)
            monkey_true = int(line5.split()[5])
            #monkey_true_re = re.match(r'If true: throw to monkey (0-9+))', line5)
            #monkey_true = int(monkey_true_re)
            line6 = f.readline().strip()
            print(line6)
            monkey_false = int(line6.split()[5])
            #monkey_false_re = re.match(r'If false: throw to monkey (0-9+))', line6)
            #monkey_false = int(monkey_false_re)
            line7 = f.readline()

            new_monkey = Monkey(monkey_name, monkey_items, Operation(monkey_op, monkey_operand), Test(monkey_test, monkey_true, monkey_false))
            monkeys.append(new_monkey)
            if not line7:
                break
        return monkeys

if __name__ == '__main__':
    #monkeys = make_monkeys('aoc11_sample.txt')
    monkeys = make_monkeys()
    for i in range(1, 10001):
        for monkey in monkeys:
            monkey.inspect_and_throw(False)
    num_inspections = []
    for monkey in monkeys:
        print('Monkey {} inspected items {} times'.format(monkey.name, monkey.num_inspections))
        num_inspections.append(monkey.num_inspections)
    num_inspections.sort()
    print('The answer is: {}'.format(num_inspections[-1] * num_inspections[-2]))

