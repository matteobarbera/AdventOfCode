class GameConsole:

    def __init__(self):
        self.accumulator = 0
        self.instr_idx = 0
        self.instr_tot = 0
        self.instructions = []
        self.idx_set = set()
        self.idx_set_static = set()
        self.instr_dict = {'acc': self.accumulate, 'jmp': self.jump_to, 'nop': self.no_op}

    def load_program(self, program: str):
        with open(program) as p_f:
            self.instructions = [line.rstrip() for line in p_f]
            self.instr_tot = len(self.instructions)
            self.idx_set = set(range(self.instr_tot))
            self.idx_set_static = self.idx_set.copy()

    def reset(self):
        self.accumulator = 0
        self.instr_idx = 0
        self.idx_set = self.idx_set_static.copy()

    def accumulate(self, val: int):
        self.accumulator += val
        return 1

    @staticmethod
    def jump_to(val):
        return val

    @staticmethod
    def no_op(val):
        return 1
