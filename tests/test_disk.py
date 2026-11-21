import unittest
from disk_check import check_disk

class TestDisk(unittest.TestCase):
    def test_warning_starts_at_threshold(self):
        self.assertEqual(check_disk(79), "ok")
        self.assertEqual(check_disk(80), "warning")
        self.assertEqual(check_disk(81), "warning")

    def test_zero_is_ok(self):
        self.assertEqual(check_disk(0), "ok")

    def test_max_value_is_warning(self):
        self.assertEqual(check_disk(100), "warning")

    def test_negative_is_ok(self):
        self.assertEqual(check_disk(-10), "ok")

    def test_half_is_ok(self):
        self.assertEqual(check_disk(50), "ok")

    def test_ninety_nine_is_warning(self):
        self.assertEqual(check_disk(99), "warning")

    def test_one_is_ok(self):
        self.assertEqual(check_disk(1), "ok")

    def test_twenty_is_ok(self):
        self.assertEqual(check_disk(20), "ok")

    def test_sixty_is_ok(self):
        self.assertEqual(check_disk(60), "ok")

    def test_seventy_nine_is_ok(self):
        self.assertEqual(check_disk(79), "ok")

if __name__ == '__main__':
    unittest.main()
