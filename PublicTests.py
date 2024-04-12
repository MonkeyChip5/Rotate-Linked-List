import unittest
from cmsc389OHW8.solution import rotate_list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        head = Node(1)
        curr = head
        for i in range (2,4):
            curr.next = Node(i)
            curr = curr.next

        head = rotate_list(head, 2)
        ans = [3, 1, 2]
        for val in ans:
            self.assertEqual(val, head.data)
            head = head.next
        self.assertEqual(None, head)

    def test2(self):
        head = Node(1)
        curr = head
        for i in range (2,4):
            curr.next = Node(i)
            curr = curr.next

        head = rotate_list(head, 7)
        ans = [1, 2, 3]
        for val in ans:
            self.assertEqual(val, head.data)
            head = head.next
        self.assertEqual(None, head)

    def test3(self):
        head = Node(1)
        curr = head
        for i in range (2,3):
            curr.next = Node(i)
            curr = curr.next

        head = rotate_list(head, 1)
        ans = [2, 1]
        for val in ans:
            self.assertEqual(val, head.data)
            head = head.next
        self.assertEqual(None, head)

    def test4(self):
        head = Node(1)
        curr = head
        for i in range (2,4):
            curr.next = Node(i)
            curr = curr.next

        head = rotate_list(head, 0)
        ans = [1, 2, 3]
        for val in ans:
            self.assertEqual(val, head.data)
            head = head.next
        self.assertEqual(None, head)
        

if __name__ == "__main__":
    unittest.main()
