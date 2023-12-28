from .intcode import Processor


class TestDay2:
    def test_one(self):
        program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        p = Processor(program=program)
        p.run()
        assert p.program == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

    def test_two(self):
        program = [1, 0, 0, 0, 99]
        p = Processor(program=program)
        p.run()
        assert p.program == [2, 0, 0, 0, 99]

    def test_three(self):
        program = [2, 3, 0, 3, 99]
        p = Processor(program=program)
        p.run()
        assert p.program == [2, 3, 0, 6, 99]

    def test_four(self):
        program = [2, 4, 4, 5, 99, 0]
        p = Processor(program=program)
        p.run()
        assert p.program == [2, 4, 4, 5, 99, 9801]

    def test_five(self):
        program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        p = Processor(program=program)
        p.run()
        assert p.program == [30, 1, 1, 4, 2, 5, 6, 0, 99]


class TestDay5:
    def test_input_output(self):
        program = [3, 0, 4, 0, 99]
        p = Processor(program=program)
        p.input = [1]
        p.run()
        assert p.output == "1"

    def test_jump_if_true_pos_mode(self):
        program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        p = Processor(program=program)
        p.input = [0]
        p.run()
        assert p.output == "0"

    def test_jump_if_false_pos_mode(self):
        program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        p = Processor(program=program)
        p.input = [5]
        p.run()
        assert p.output == "1"

    def test_jump_if_true_imm_mode(self):
        program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        p = Processor(program=program)
        p.input = [0]
        p.run()
        assert p.output == "0"

    def test_jump_if_false_imm_mode(self):
        program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        p = Processor(program=program)
        p.input = [5]
        p.run()
        assert p.output == "1"

    def test_equal_true_pos_mode(self):
        program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        p = Processor(program=program)
        p.input = [8]
        p.run()
        assert p.output == "1"

    def test_equal_false_pos_mode(self):
        program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        p = Processor(program=program)
        p.input = [1]
        p.run()
        assert p.output == "0"

    def test_equal_true_imm_mode(self):
        program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        p = Processor(program=program)
        p.input = [8]
        p.run()
        assert p.output == "1"

    def test_equal_false_imm_mode(self):
        program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        p = Processor(program=program)
        p.input = [7]
        p.run()
        assert p.output == "0"

    def test_less_than_true_pos_mode(self):
        program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        p = Processor(program=program)
        p.input = [7]
        p.run()
        assert p.output == "1"

    def test_less_than_false_pos_mode(self):
        program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        p = Processor(program=program)
        p.input = [8]
        p.run()
        assert p.output == "0"

    def test_less_than_true_imm_mode(self):
        program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        p = Processor(program=program)
        p.input = [7]
        p.run()
        assert p.output == "1"

    def test_less_than_false_imm_mode(self):
        program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        p = Processor(program=program)
        p.input = [8]
        p.run()
        assert p.output == "0"
