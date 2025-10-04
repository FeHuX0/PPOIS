class PostMachine:

    def __init__(self, tape_size=20):
        self.__initial_tape_size = tape_size
        self.tape = [0] * self.__initial_tape_size  # лента
        self.head = 0  # положение головки
        self.pc = 0  # счётчик команд (program counter)
        self.running = True
        self.program = []  # список инструкций

        # Таблица команд
        self.commands = {
            "V": self.cmd_mark,  # 'V' для установки метки (Mark)
            "X": self.cmd_erase,  # 'X' для стирания метки (Erase)
            ">": self.cmd_right,  # '>' для сдвига вправо (Right)
            "<": self.cmd_left,  # '<' для сдвига влево (Left)
            "?": self.cmd_jump0,  # '?' для условного перехода (Jump if zero)
            "!": self.cmd_stop  # '!' для остановки (Stop)
        }

    def reset(self):
        """Сбрасывает состояние машины к начальному."""
        self.tape = [0] * self.__initial_tape_size
        self.head = 0
        self.pc = 0
        self.running = True

    def load_program(self, program):
        """Загрузить список инструкций в формате [(команда, arg1, arg2,...), ...]"""
        self.program = program

    def step(self):
        """Выполнить одну инструкцию"""
        if not self.running or not (0 <= self.pc < len(self.program)):
            self.running = False
            return

        instr = self.program[self.pc]
        cmd = instr[0]

        if cmd not in self.commands:
            self.running = False
            raise ValueError(f"Неизвестная команда: {cmd}")

        # Вызов обработчика команды
        self.commands[cmd](instr)

    # ==== Команды ====
    def cmd_mark(self, instr):
        self.tape[self.head] = 1
        self.pc = instr[1] - 1  # Переход на строку N (индекс N-1)

    def cmd_erase(self, instr):
        self.tape[self.head] = 0
        self.pc = instr[1] - 1  # Переход на строку N (индекс N-1)

    def cmd_right(self, instr):
        self.head += 1
        if self.head >= len(self.tape):
            self.tape.extend([0] * 10)  # Динамически расширяем ленту
        self.pc = instr[1] - 1  # Переход на строку N (индекс N-1)

    def cmd_left(self, instr):
        if self.head > 0:
            self.head -= 1
        self.pc = instr[1] - 1  # Переход на строку N (индекс N-1)

    def cmd_jump0(self, instr):
        # Переход на строку N1, если ячейка пуста (0), иначе на N2
        self.pc = (instr[1] - 1) if self.tape[self.head] == 0 else (instr[2] - 1)

    def cmd_stop(self, instr):
        self.running = False