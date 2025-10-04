import time
from core.PostMachine import PostMachine

class PostMachineUI:

    def __init__(self):
        self.machine = PostMachine()
        self.running = True

        # Словарь-диспетчер для команд меню. Чисто, читаемо, расширяемо.
        self.menu_actions = {
            '1': ('Ввести программу', self._action_load_program),
            '2': ('Установить ленту', self._action_set_tape),
            '3': ('Показать текущее состояние', self.display_state),
            '4': ('Выполнить программу (быстро)', self._action_run_fast),
            '5': ('Выполнить программу (пошагово)', self._action_run_stepwise),
            '6': ('Сделать один шаг', self._action_step),
            '7': ('Сбросить машину', self._action_reset),
            '8': ('Выход', self._action_exit),
        }

    def _require_program(self):
        """Проверяет, загружена ли программа. Избавляет от дублирования кода."""
        if not self.machine.program:
            print("\n Сначала загрузите программу! (Пункт 1)")
            return False
        return True

    def _action_load_program(self):
        self.load_program_ui()

    def _action_set_tape(self):
        self.set_tape_ui()

    def _action_run_fast(self):
        if self._require_program():
            self.run_program(step_delay=0)

    def _action_run_stepwise(self):
        if self._require_program():
            self.run_program(step_delay=0.4)

    def _action_step(self):
        if not self._require_program():
            return

        if self.machine.running:
            print("Делаем один шаг...")
            self.machine.step()
            self.display_state()
        else:
            print("\n Программа уже завершена. Сбросьте машину для нового запуска.")

    def _action_reset(self):
        self.machine.reset()
        print("\n Машина сброшена к начальному состоянию.")
        self.display_state()

    def _action_exit(self):
        print("Завершение работы.")
        self.running = False

    def main_menu(self):
        """Основной цикл меню программы. Теперь он чистый и короткий."""
        while self.running:
            print("\n--- Меню Машины Поста ---")
            for key, (text, _) in self.menu_actions.items():
                print(f"{key}. {text}")

            choice = input("Выберите действие: ")

            action_tuple = self.menu_actions.get(choice)

            if action_tuple:
                action_function = action_tuple[1]
                action_function()  # Вызываем найденный метод
            else:
                print("\n Неверный выбор, попробуйте снова.")

    def display_state(self):
        """Наглядно отображает текущее состояние ленты и головки."""
        print("\n" + "=" * 50)
        tape_str = "Лента: |" + "|".join(map(str, self.machine.tape[:30])) + "|..."
        print(tape_str)
        head_str = "       " + " " * (self.machine.head * 2) + "^"
        print(head_str)
        print(f"Позиция головки: {self.machine.head}")

        if self.machine.running and 0 <= self.machine.pc < len(self.machine.program):
            print(f"Следующая команда (строка {self.machine.pc + 1}): {self.machine.program[self.machine.pc]}")
        else:
            print("Следующая команда: (программа не запущена или завершена)")
        print("=" * 50)

    def run_program(self, step_delay=0.1):
        """Цикл выполнения программы с отображением шагов."""
        self.machine.running = True
        while self.machine.running:
            self.display_state()
            self.machine.step()
            if step_delay > 0:
                time.sleep(step_delay)
        print("\n Программа завершена.")
        self.display_state()

    def load_program_ui(self):
        """Интерфейс для ввода программы пользователем."""
        print("\n--- Ввод программы ---")
        program = []
        line_num = 1
        while True:
            inp = input(f"{line_num}> ").upper().strip()
            if inp in ["ГОТОВО", "DONE", ""]: break
            parts = inp.split()
            cmd = parts[0]
            if cmd not in self.machine.commands:
                print(f"Ошибка: Неизвестная команда '{cmd}'.")
                continue
            try:
                args = [int(p) for p in parts[1:]]
                instruction = tuple([cmd] + args)
                program.append(instruction)
                line_num += 1
            except (ValueError, IndexError):
                print("Ошибка: неверные аргументы для команды.")
        self.machine.load_program(program)
        print("\nПрограмма успешно загружена!")

    def set_tape_ui(self):
        print("\n--- Установка ленты ---")
        tape_str = input("Введите начальное состояние ленты (например, 11101): ")
        try:
            tape_list = [int(char) for char in tape_str if char in '01']
            tape_size = len(self.machine.tape)
            self.machine.tape = tape_list + [0] * (tape_size - len(tape_list))
            self.machine.head = 0
            print("Лента установлена.")
            self.display_state()
        except ValueError:
            print("Ошибка: Лента должна состоять только из 0 и 1.")