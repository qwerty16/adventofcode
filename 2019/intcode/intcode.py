from icecream import ic


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            raw_line = line.split(",")
            output += [int(x) for x in raw_line]
    return output


class Processor:
    def __init__(self, program: list = []) -> None:
        self.program = program
        self.instruction_pointer = 0
        self.continue_processing = True
        self.instruction_map = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            8: self.is_equal,
            99: self.halt,
        }
        self.output = ""
        self.input = []

    def run(self):
        while self.continue_processing:
            self.process()

    def get_parameters(self, raw_instruction, n_parameters):
        parameters = []

        mode_1 = (raw_instruction // 100) % 10
        mode_2 = (raw_instruction // 1000) % 10
        mode_3 = (raw_instruction // 10000) % 10

        modes = [mode_1, mode_2, mode_3]

        for n in range(n_parameters):
            if modes[n] == 0:
                parameters += [
                    self.program[self.program[self.instruction_pointer + n + 1]]
                ]
            elif modes[n] == 1:
                parameters += [self.program[self.instruction_pointer + n + 1]]
            else:
                ValueError(f"Invalid mode {n}: {modes[n]}")

        return parameters

    def get_input(self):
        return self.input.pop()

    def process(self):
        ic(self.instruction_pointer)
        raw_instruction = self.program[self.instruction_pointer]
        instruction = raw_instruction % 100

        ic(instruction)

        self.instruction_map[instruction](raw_instruction)

    def add(self, raw_instruction):
        parameters = self.get_parameters(raw_instruction, 2)
        result = parameters[0] + parameters[1]
        self.program[self.program[self.instruction_pointer + 3]] = result
        self.instruction_pointer += 4
        ic(result)
        ic(self.program)

    def multiply(self, raw_instruction):
        parameters = self.get_parameters(raw_instruction, 2)
        result = parameters[0] * parameters[1]
        self.program[self.program[self.instruction_pointer + 3]] = result
        self.instruction_pointer += 4
        ic(result)
        ic(self.program)

    def input(self, raw_instruction):
        result = self.get_input()
        self.program[self.program[self.instruction_pointer + 1]] = result
        self.instruction_pointer += 2
        ic(result)
        ic(self.program)

    def output(self, raw_instruction):
        parameters = self.get_parameters(raw_instruction, 1)
        ic(parameters)
        output = str(parameters[0])
        self.instruction_pointer += 2
        self.output += output
        ic(output)
        ic(self.program)

    def jump_if_true(self, raw_instruction):
        parameters = self.get_parameters(raw_instruction, 2)
        ic(parameters)
        ic(f"jump if true {parameters[0]} != 0 : ")
        if parameters[0] != 0:
            ic("True")
            self.instruction_pointer = parameters[1]
        else:
            ic("False")
            self.instruction_pointer += 3

        ic(self.instruction_pointer)

    def jump_if_false(self, raw_instruction):
        parameters = self.get_parameters(raw_instruction, 2)
        ic(parameters)
        ic(f"jump if false {parameters[0]} == 0 : ")
        if parameters[0] == 0:
            ic("True")
            self.instruction_pointer = parameters[1]
        else:
            ic("False")
            self.instruction_pointer += 3
        ic(self.instruction_pointer)

    def is_equal(self, raw_instruction):
        parameters = self.get_parameters(raw_instruction, 3)
        ic(parameters)
        ic(f"equal {parameters[0]} == {parameters[1]} : ")
        if parameters[0] == parameters[1]:
            ic("True")
            self.program[parameters[2]] = 1
        else:
            ic("False")
            self.program[parameters[2]] = 0

        self.instruction_pointer += 4

        ic(self.program)
        ic(self.instruction_pointer)

    def halt(self, raw_instruction):
        self.continue_processing = False
