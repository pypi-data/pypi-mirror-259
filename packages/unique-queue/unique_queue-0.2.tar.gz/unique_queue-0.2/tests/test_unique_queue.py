import unittest
from src.unique_queue import UniqueQueue

class TestUniqueQueue(unittest.TestCase):

    def test_push_pop(self):
        q = UniqueQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)

    def test_push_duplicate(self):
        q = UniqueQueue()
        q.push(1)
        q.push(2)
        q.push(1)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)

    def test_extend(self):
        q = UniqueQueue()
        q.extend([1, 2, 3])
        self.assertEqual(len(q), 3)
        q.extend([3, 4, 5])
        self.assertEqual(len(q), 5)

    def test_total_count(self):
        q = UniqueQueue()
        q.extend([1, 2, 3])
        self.assertEqual(q.total_count(), 3)

    def test_completed_count(self):
        q = UniqueQueue()
        q.extend([1, 2, 3])
        q.pop()
        self.assertEqual(q.completed_count(), 1)

    def test_remaining_count(self):
        q = UniqueQueue()
        q.extend([1, 2, 3])
        q.pop()
        self.assertEqual(q.remaining_count(), 2)

    def test_empty(self):
        q = UniqueQueue()
        self.assertTrue(q.empty())
        q.push(1)
        self.assertFalse(q.empty())
        q.pop()
        self.assertTrue(q.empty())

    def test_pop_when_empty(self):
        q = UniqueQueue()
        with self.assertRaises(IndexError):
            q.pop()

if __name__ == '__main__':
    unittest.main()
