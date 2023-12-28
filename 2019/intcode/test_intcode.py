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

    def test_jump_zero(self):
        program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        p = Processor(program=program)
        p.input = [0]
        p.run()
        assert p.output == "0"

    def test_jump_one(self):
        program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        p = Processor(program=program)
        p.input = [5]
        p.run()
        assert p.output == "1"
