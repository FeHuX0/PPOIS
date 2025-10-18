import unittest
from core.PostMachine import PostMachine


class TestPostMachine(unittest.TestCase):
    def setUp(self):
        self.pm = PostMachine(tape_size=5)

    def run_program(self, program, steps=50):
        """Утилита для выполнения программы целиком"""
        self.pm.reset()
        self.pm.load_program(program)
        for _ in range(steps):
            if not self.pm.running:
                break
            self.pm.step()
        return self.pm

    def test_mark_and_erase(self):
        program = [
            ("V", 2),   # ставим метку
            ("X", 3),   # стираем метку
            ("!",)      # стоп
        ]
        pm = self.run_program(program)
        self.assertEqual(pm.tape[0], 0)  # метки нет

    def test_right_and_left(self):
        program = [
            (">", 2),   # вправо
            ("<", 3),   # влево
            ("!",)      # стоп
        ]
        pm = self.run_program(program)
        self.assertEqual(pm.head, 0)  # вернулись в начало

    def test_right_expands_tape(self):
        program = [
            (">", 1),   # в цикле вправо
        ]
        pm = self.run_program(program, steps=15)
        self.assertGreater(pm.head, 10)     # ушли далеко вправо
        self.assertGreater(len(pm.tape), 5) # лента расширилась

    def test_jump0_on_empty(self):
        program = [
            ("?", 3, 2),   # если 0 → строка 3, иначе 2
            ("!",),        # строка 2
            ("!",)         # строка 3
        ]
        pm = self.run_program(program)
        self.assertEqual(pm.pc, 2)  # перешли на строку 3 (индекс 2)

    def test_jump0_on_marked(self):
        program = [
            ("V", 2),      # поставить метку
            ("?", 3, 4),   # проверка
            ("!",),        # строка 3
            ("!",)         # строка 4
        ]
        pm = self.run_program(program)
        # так как в ячейке "1", переход должен быть на строку 4 (индекс 3)
        self.assertEqual(pm.pc, 3)

    def test_stop(self):
        program = [("!",)]
        pm = self.run_program(program)
        self.assertFalse(pm.running)

    def test_invalid_command_raises(self):
        program = [("WTF",)]
        self.pm.load_program(program)
        with self.assertRaises(ValueError):
            self.pm.step()


if __name__ == "__main__":
    unittest.main()

