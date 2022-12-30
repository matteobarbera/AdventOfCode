from Day8.game_console import GameConsole


class ModifiedGameConsole(GameConsole):
    def __init__(self):
        super(ModifiedGameConsole, self).__init__()

    def execute(self):
        self.reset()
        is_fixed = False
        while self.instr_idx in self.idx_set:
            self.idx_set.remove(self.instr_idx)
            instruction, value = self.instructions[self.instr_idx].split(' ')
            self.instr_idx += self.instr_dict[instruction](int(value))
            if self.instr_idx == self.instr_tot:
                is_fixed = True
                break
        return is_fixed

    def execute_bugged(self):
        while self.instr_idx in self.idx_set:
            self.idx_set.remove(self.instr_idx)
            instruction, value = self.instructions[self.instr_idx].split(' ')
            self.instr_idx += self.instr_dict[instruction](int(value))
        other_instr = []
        for idx in self.idx_set_static - self.idx_set:
            instr = self.instructions[idx]
            if instr[:3] != 'acc':
                other_instr.append(idx)
        return other_instr, self.accumulator

    def brute_force_fix(self):
        possible_culprits, _ = self.execute_bugged()
        tmp_instr = self.instructions[:]
        for sus in possible_culprits:
            self.instructions = tmp_instr[:]
            instr = tmp_instr[sus]
            if instr[:3] == 'jmp':
                instr = 'nop' + instr[3:]
            else:
                instr = 'jmp' + instr[3:]
            self.instructions[sus] = instr
            if self.execute():
                print('Fix found!')
                break
        return self.accumulator


def day8_part1(c: ModifiedGameConsole):
    _, repeated_idx = c.execute_bugged()
    return repeated_idx


def day8_part2(c: ModifiedGameConsole):
    acc = c.brute_force_fix()
    return acc


if __name__ == "__main__":
    console = ModifiedGameConsole()
    console.load_program('day8_input.txt')
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Repeated idx: {day8_part1(console)}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Accumulator value of fixed program: {day8_part2(console)}")
