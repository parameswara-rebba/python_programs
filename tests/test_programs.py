"""Tests for the programs. Run from the repository root with:

    python -m unittest discover tests
"""

import importlib.util
import random
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(relative_path: str):
    """Import a program by file path (the folder names start with digits)."""
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BasicsTests(unittest.TestCase):
    def test_factorial(self):
        m = load("01_basics/factorial.py")
        self.assertEqual(m.factorial(0), 1)
        self.assertEqual(m.factorial(5), 120)
        self.assertEqual(m.factorial_recursive(6), 720)
        with self.assertRaises(ValueError):
            m.factorial(-1)

    def test_fibonacci(self):
        m = load("01_basics/fibonacci.py")
        self.assertEqual(m.fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(m.fibonacci(0), [])

    def test_primes(self):
        m = load("01_basics/prime_numbers.py")
        self.assertEqual(m.primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual([n for n in range(50) if m.is_prime(n)], m.primes_up_to(49))

    def test_fizzbuzz(self):
        m = load("01_basics/fizzbuzz.py")
        self.assertEqual([m.fizzbuzz(n) for n in (1, 3, 5, 15)], ["1", "Fizz", "Buzz", "FizzBuzz"])

    def test_gcd_lcm(self):
        m = load("01_basics/gcd_lcm.py")
        self.assertEqual(m.gcd(48, 18), 6)
        self.assertEqual(m.lcm(4, 6), 12)
        self.assertEqual(m.lcm(0, 5), 0)

    def test_leap_year(self):
        m = load("01_basics/leap_year.py")
        self.assertTrue(m.is_leap_year(2000))
        self.assertTrue(m.is_leap_year(2024))
        self.assertFalse(m.is_leap_year(1900))
        self.assertFalse(m.is_leap_year(2025))

    def test_temperature(self):
        m = load("01_basics/temperature_converter.py")
        self.assertEqual(m.celsius_to_fahrenheit(100), 212)
        self.assertEqual(m.fahrenheit_to_celsius(-40), -40)


class StringTests(unittest.TestCase):
    def test_palindrome(self):
        m = load("02_strings/palindrome.py")
        self.assertTrue(m.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(m.is_palindrome("python"))

    def test_anagram(self):
        m = load("02_strings/anagram.py")
        self.assertTrue(m.are_anagrams("Dormitory", "dirty room"))
        self.assertFalse(m.are_anagrams("hello", "world"))

    def test_count_vowels(self):
        m = load("02_strings/count_vowels.py")
        self.assertEqual(m.count_vowels_and_consonants("Hello, World!"), (3, 7))

    def test_word_frequency(self):
        m = load("02_strings/word_frequency.py")
        self.assertEqual(m.word_frequency("The cat. the CAT, a dog")["the"], 2)

    def test_reverse(self):
        m = load("02_strings/reverse_words.py")
        self.assertEqual(m.reverse_string("abc"), "cba")
        self.assertEqual(m.reverse_words("one two  three"), "three two one")

    def test_caesar(self):
        m = load("02_strings/caesar_cipher.py")
        self.assertEqual(m.encrypt("xyz ABC!", 3), "abc DEF!")
        self.assertEqual(m.decrypt(m.encrypt("Hello, World!", 11), 11), "Hello, World!")


class CollectionTests(unittest.TestCase):
    def test_lists(self):
        m = load("03_collections/list_operations.py")
        self.assertEqual(m.remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])
        self.assertEqual(m.flatten([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])
        self.assertEqual(m.chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(m.second_largest([10, 20, 20, 5]), 10)

    def test_dictionaries(self):
        m = load("03_collections/dictionary_operations.py")
        self.assertEqual(m.merge({"a": 1, "b": 2}, {"b": 3}), {"a": 1, "b": 3})
        self.assertEqual(m.invert({"a": 1}), {1: "a"})
        self.assertEqual(m.group_by_length(["hi", "to", "cat"]), {2: ["hi", "to"], 3: ["cat"]})
        self.assertEqual(list(m.sort_by_value({"x": 3, "y": 1})), ["y", "x"])

    def test_stack_and_queue(self):
        m = load("03_collections/stack_and_queue.py")
        stack, queue = m.Stack(), m.Queue()
        for n in (1, 2, 3):
            stack.push(n)
            queue.enqueue(n)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertTrue(m.is_balanced("{[()]}"))
        self.assertFalse(m.is_balanced("([)]"))
        self.assertFalse(m.is_balanced("(("))

    def test_matrix(self):
        m = load("03_collections/matrix_operations.py")
        a, b = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
        self.assertEqual(m.transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(m.add(a, b), [[6, 8], [10, 12]])
        self.assertEqual(m.multiply(a, b), [[19, 22], [43, 50]])


class AlgorithmTests(unittest.TestCase):
    def test_searching(self):
        m = load("04_algorithms/searching.py")
        data = [2, 5, 8, 12, 16, 23, 38, 56]
        for index, value in enumerate(data):
            self.assertEqual(m.linear_search(data, value), index)
            self.assertEqual(m.binary_search(data, value), index)
        self.assertEqual(m.binary_search(data, 7), -1)
        self.assertEqual(m.binary_search([], 1), -1)

    def test_sorting(self):
        m = load("04_algorithms/sorting.py")
        rng = random.Random(1)
        cases = [[], [1], [2, 1], [3, 3, 1, 2]] + [
            [rng.randint(-50, 50) for _ in range(rng.randint(0, 40))] for _ in range(20)
        ]
        for sort in (m.bubble_sort, m.selection_sort, m.insertion_sort, m.merge_sort, m.quick_sort):
            for case in cases:
                original = list(case)
                self.assertEqual(sort(case), sorted(case), sort.__name__)
                self.assertEqual(case, original, f"{sort.__name__} changed its input")

    def test_recursion(self):
        m = load("04_algorithms/recursion.py")
        self.assertEqual(len(m.hanoi(4)), 15)
        self.assertEqual(sorted(m.permutations("abc")), ["abc", "acb", "bac", "bca", "cab", "cba"])
        self.assertEqual(m.power(2, 10), 1024)
        self.assertEqual(m.digit_sum(12345), 15)


class OopTests(unittest.TestCase):
    def test_bank_account(self):
        m = load("05_oop/bank_account.py")
        account = m.BankAccount("Asha", 100)
        account.deposit(50)
        account.withdraw(30)
        self.assertEqual(account.balance, 120)
        with self.assertRaises(m.InsufficientFundsError):
            account.withdraw(1000)
        with self.assertRaises(ValueError):
            account.deposit(0)

    def test_shapes(self):
        m = load("05_oop/shapes.py")
        self.assertEqual(m.Rectangle(3, 4).area(), 12)
        self.assertEqual(m.Square(2).perimeter(), 8)
        self.assertAlmostEqual(m.Circle(1).area(), 3.14159265, places=6)
        with self.assertRaises(TypeError):
            m.Shape()

    def test_employee(self):
        m = load("05_oop/employee.py")
        staff = [m.Employee.from_csv_row(r) for r in ("A, X, 100", "B, X, 200", "C, Y, 50")]
        self.assertEqual(m.average_salary_by_department(staff), {"X": 150, "Y": 50})
        staff[2].give_raise(10)
        self.assertAlmostEqual(staff[2].salary, 55)


class FileAndAutomationTests(unittest.TestCase):
    def setUp(self):
        import tempfile

        self._folder = tempfile.TemporaryDirectory()
        self.folder = Path(self._folder.name)

    def tearDown(self):
        self._folder.cleanup()

    def test_file_read_write(self):
        m = load("06_files/file_read_write.py")
        path = self.folder / "notes.txt"
        m.write_lines(path, ["one two", "three"])
        m.append_line(path, "four")
        self.assertEqual(m.file_stats(path), {"lines": 3, "words": 4, "characters": 19})

    def test_csv(self):
        m = load("06_files/csv_example.py")
        path = self.folder / "servers.csv"
        m.write_csv(path, m.ROWS)
        rows = m.read_csv(path)
        self.assertEqual([row["name"] for row in rows], ["web-01", "web-02", "db-01"])
        self.assertEqual(m.average(rows, "cpu"), 59)

    def test_json(self):
        m = load("06_files/json_example.py")
        path = self.folder / "config.json"
        data = {"app": "demo", "ports": [80, 443]}
        m.save_json(path, data)
        self.assertEqual(m.load_json(path), data)

    def test_log_analyzer(self):
        m = load("07_automation/log_analyzer.py")
        levels, errors = m.analyze(m.SAMPLE)
        self.assertEqual(dict(levels), {"INFO": 3, "WARNING": 1, "ERROR": 2})
        self.assertEqual(errors["Connection to database timed out"], 2)

    def test_disk_usage(self):
        m = load("07_automation/disk_usage.py")
        self.assertTrue(0 <= m.usage_percent(str(self.folder)) <= 100)
        self.assertEqual(m.human_readable(1536), "1.5 KB")

    def test_password_generator(self):
        m = load("07_automation/password_generator.py")
        for length in (4, 16, 40):
            password = m.generate_password(length)
            self.assertEqual(len(password), length)
            self.assertTrue(any(c.islower() for c in password))
            self.assertTrue(any(c.isupper() for c in password))
            self.assertTrue(any(c.isdigit() for c in password))
            self.assertTrue(any(c in m.SYMBOLS for c in password))
        with self.assertRaises(ValueError):
            m.generate_password(3)

    def test_find_duplicates(self):
        m = load("07_automation/find_duplicate_files.py")
        (self.folder / "a.txt").write_text("same")
        (self.folder / "b.txt").write_text("same")
        (self.folder / "c.txt").write_text("different")
        groups = m.find_duplicates(self.folder)
        self.assertEqual([[p.name for p in g] for g in groups], [["a.txt", "b.txt"]])


if __name__ == "__main__":
    unittest.main()
