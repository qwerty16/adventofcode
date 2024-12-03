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
        self.program = program.copy()
        self.instruction_pointer = 0
        self.continue_processing = True
        self.instruction_map = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.is_less_than,
            8: self.is_equal,
            99: self.halt,
        }
        self.output = ""
        self.input = []

    def __str__(self):
        return f"Processor: {self.program}"

    def __repr__(self):
        return str(self)

    def run(self):
        self.continue_processing = True
        while self.continue_processing:
            self.process()

    def get_parameters(self, n_parameters):
        parameters = []

        raw_instruction = self.program[self.instruction_pointer]

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
        self.instruction_map[instruction]()

    def add(self):
        parameters = self.get_parameters(2)
        result = parameters[0] + parameters[1]
        self.program[self.program[self.instruction_pointer + 3]] = result
        self.instruction_pointer += 4
        ic(result)
        ic(self.program)

    def multiply(self):
        parameters = self.get_parameters(2)
        result = parameters[0] * parameters[1]
        self.program[self.program[self.instruction_pointer + 3]] = result
        self.instruction_pointer += 4
        ic(result)
        ic(self.program)

    def input(self):
        result = self.get_input()
        self.program[self.program[self.instruction_pointer + 1]] = result
        self.instruction_pointer += 2
        ic(result)
        ic(self.program)

    def output(self):
        parameters = self.get_parameters(1)
        ic(parameters)
        output = str(parameters[0])
        self.instruction_pointer += 2
        self.output += output
        ic(output)
        ic(self.program)

    def jump_if_true(self):
        parameters = self.get_parameters(2)
        ic(parameters)
        ic(f"jump if true {parameters[0]} != 0 : ")
        if parameters[0] != 0:
            ic("True")
            self.instruction_pointer = parameters[1]
        else:
            ic("False")
            self.instruction_pointer += 3

        ic(self.instruction_pointer)

    def jump_if_false(self):
        parameters = self.get_parameters(2)
        ic(parameters)
        ic(f"jump if false {parameters[0]} == 0 : ")
        if parameters[0] == 0:
            ic("True")
            self.instruction_pointer = parameters[1]
        else:
            ic("False")
            self.instruction_pointer += 3
        ic(self.instruction_pointer)

    def is_less_than(self):
        parameters = self.get_parameters(2)
        ic(parameters)
        output_location = self.program[self.instruction_pointer + 3]
        ic(output_location)
        ic(f"less than {parameters[0]} < {parameters[1]} : ")
        if parameters[0] < parameters[1]:
            ic("True")
            self.program[output_location] = 1
        else:
            ic("False")
            self.program[output_location] = 0

        self.instruction_pointer += 4

        ic(self.program)
        ic(self.instruction_pointer)

    def is_equal(self):
        parameters = self.get_parameters(2)
        ic(parameters)
        output_location = self.program[self.instruction_pointer + 3]
        ic(output_location)
        ic(f"equal {parameters[0]} == {parameters[1]} : ")
        if parameters[0] == parameters[1]:
            ic("True")
            self.program[output_location] = 1
        else:
            ic("False")
            self.program[output_location] = 0

        self.instruction_pointer += 4

        ic(self.program)
        ic(self.instruction_pointer)

    def halt(self):
        self.continue_processing = False


class Amplifier(Processor):
    """An Amplifier is a Processor that waits after each
    time it outputs something to see what its next input will be"""

    def __str__(self):
        return f"Amplifier: {self.program}"

    def output(self):
        super().output()
        self.continue_processing = False


class AmplifierSequence:
    def __init__(self, programs, initial_inputs) -> None:
        self.programs = programs
        self.initial_inputs = initial_inputs
        self.max_output = 0
        self.max_output_input = []

        self.amplifiers = []
        self.finished = []

    def run(self):
        for inputs in self.initial_inputs:
            self.amplifiers = []
            self.finished = []
            for program, inp in zip(self.programs, inputs):
                a = Amplifier(program=program[0])
                a.input = [inp]
                self.amplifiers += [a]
                self.finished += [False]

            target = [True for i in inputs]

            steps = 0
            while self.finished != target:
                if steps > 50:
                    break
                current_program = steps % len(inputs)
                next_program = (steps + 1) % len(inputs)
                if steps == 0:
                    self.amplifiers[current_program].input = [0] + self.amplifiers[
                        current_program
                    ].input
                else:
                    self.amplifiers[current_program].input = [output] + self.amplifiers[
                        current_program
                    ].input

                ic.disable()
                self.amplifiers[current_program].run()
                ic.enable()
                output = self.amplifiers[current_program].output
                if output == "":
                    output = 0
                    self.finished[current_program] = True
                else:
                    output = int(output)
                self.amplifiers[current_program].output = ""
                self.amplifiers[next_program].input += [output]
                if output > self.max_output:
                    self.max_output = output
                    self.max_output_input = inputs

                steps += 1
            ic(inputs)
            ic(self.max_output)

        ic(self.max_output_input)
