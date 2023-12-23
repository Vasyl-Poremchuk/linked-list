from unittest import TestCase, main

from singly_linked_list.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(TestCase):
    def setUp(self) -> None:
        self.singly_linked_list = SinglyLinkedList(value=1)

    def test_display(self) -> None:
        self.assertEqual(first=[1], second=self.singly_linked_list.display())

    def test_insert_at_beginning(self) -> None:
        self.singly_linked_list.insert_at_beginning(value=2)

        self.assertEqual(
            first=[2, 1], second=self.singly_linked_list.display()
        )

    def test_insert_at_end(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)

        self.assertEqual(
            first=[1, 3], second=self.singly_linked_list.display()
        )

    def test_insert_before_node(self) -> None:
        self.singly_linked_list.insert_at_end(value=2)
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=5)

        self.singly_linked_list.insert_before_node(node_value=3, value=6)

        self.assertEqual(
            first=[1, 2, 6, 3, 4, 5], second=self.singly_linked_list.display()
        )

    def test_insert_before_node_at_beginning(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=23)

        self.singly_linked_list.insert_before_node(node_value=1, value=48)

        self.assertEqual(
            first=[48, 1, 3, 7, 23], second=self.singly_linked_list.display()
        )

    def test_insert_before_node_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=9)
        self.singly_linked_list.insert_at_end(value=14)
        self.singly_linked_list.insert_at_end(value=5)

        self.singly_linked_list.insert_before_node(node_value=7, value=33)

        self.assertEqual(
            first=[1, 9, 14, 5], second=self.singly_linked_list.display()
        )

    def test_insert_before_n_next_node(self) -> None:
        self.singly_linked_list.insert_at_end(value=2)
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=3)

        self.singly_linked_list.insert_before_n_next_node(
            node_value=3, value=7, n_next_node=2
        )

        self.assertEqual(
            first=[1, 2, 3, 4, 7, 3], second=self.singly_linked_list.display()
        )

    def test_insert_before_n_next_node_first(self) -> None:
        self.singly_linked_list.insert_at_end(value=2)
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=3)

        self.singly_linked_list.insert_before_n_next_node(
            node_value=3, value=7, n_next_node=1
        )

        self.assertEqual(
            first=[1, 2, 7, 3, 4, 3], second=self.singly_linked_list.display()
        )

    def test_insert_before_n_next_node_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=2)
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=3)

        self.singly_linked_list.insert_before_n_next_node(
            node_value=3, value=7, n_next_node=3
        )

        self.assertEqual(
            first=[1, 2, 3, 4, 3], second=self.singly_linked_list.display()
        )

    def test_insert_after_node(self) -> None:
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=2)
        self.singly_linked_list.insert_at_end(value=9)

        self.singly_linked_list.insert_after_node(node_value=4, value=11)

        self.assertEqual(
            first=[1, 7, 4, 11, 2, 9], second=self.singly_linked_list.display()
        )

    def test_insert_after_node_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=6)
        self.singly_linked_list.insert_at_end(value=17)
        self.singly_linked_list.insert_at_end(value=8)

        self.singly_linked_list.insert_after_node(node_value=13, value=12)

        self.assertEqual(
            first=[1, 6, 17, 8], second=self.singly_linked_list.display()
        )

    def test_insert_after_node_n_next_node(self) -> None:
        self.singly_linked_list.insert_at_end(value=6)
        self.singly_linked_list.insert_at_end(value=17)
        self.singly_linked_list.insert_at_end(value=8)
        self.singly_linked_list.insert_at_end(value=8)
        self.singly_linked_list.insert_at_end(value=23)

        self.singly_linked_list.insert_after_n_next_node(
            node_value=8, value=49, n_next_node=2
        )

        self.assertEqual(
            first=[1, 6, 17, 8, 8, 49, 23],
            second=self.singly_linked_list.display(),
        )

    def test_insert_after_node_n_next_node_first(self) -> None:
        self.singly_linked_list.insert_at_end(value=14)
        self.singly_linked_list.insert_at_end(value=17)
        self.singly_linked_list.insert_at_end(value=8)
        self.singly_linked_list.insert_at_end(value=8)
        self.singly_linked_list.insert_at_end(value=23)

        self.singly_linked_list.insert_after_n_next_node(
            node_value=8, value=49, n_next_node=1
        )

        self.assertEqual(
            first=[1, 14, 17, 8, 49, 8, 23],
            second=self.singly_linked_list.display(),
        )

    def test_insert_after_node_n_next_node_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=15)
        self.singly_linked_list.insert_at_end(value=15)
        self.singly_linked_list.insert_at_end(value=23)

        self.singly_linked_list.insert_after_n_next_node(
            node_value=15, value=49, n_next_node=3
        )

        self.assertEqual(
            first=[1, 7, 15, 15, 23],
            second=self.singly_linked_list.display(),
        )

    def test_insert_at_position(self) -> None:
        self.singly_linked_list.insert_at_end(value=19)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=33)

        self.singly_linked_list.insert_at_position(position=2, value=17)

        self.assertEqual(
            first=[1, 19, 17, 11, 33], second=self.singly_linked_list.display()
        )

    def test_insert_at_position_zero_position(self) -> None:
        self.singly_linked_list.insert_at_end(value=9)
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=16)

        self.singly_linked_list.insert_at_position(position=0, value=7)

        self.assertEqual(
            first=[7, 1, 9, 4, 16], second=self.singly_linked_list.display()
        )

    def test_insert_at_position_at_end(self) -> None:
        self.singly_linked_list.insert_at_end(value=89)
        self.singly_linked_list.insert_at_end(value=45)
        self.singly_linked_list.insert_at_end(value=18)

        self.singly_linked_list.insert_at_position(position=4, value=27)

        self.assertEqual(
            first=[1, 89, 45, 18, 27], second=self.singly_linked_list.display()
        )

    def test_insert_at_position_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.insert_at_position(position=44, value=5)

        self.assertEqual(
            first=[1, 3, 11, 7], second=self.singly_linked_list.display()
        )

    def test_delete_at_beginning(self) -> None:
        self.singly_linked_list.delete_at_beginning()

        self.assertEqual(first=[], second=self.singly_linked_list.display())

    def test_delete_at_end(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)

        self.singly_linked_list.delete_at_end()

        self.assertEqual(first=[1], second=self.singly_linked_list.display())

    def test_delete_before_node(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.delete_before_node(node_value=11)

        self.assertEqual(
            first=[1, 11, 7], second=self.singly_linked_list.display()
        )

    def test_delete_before_node_zero_position(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.delete_before_node(node_value=1)

        self.assertEqual(
            first=[1, 3, 11, 7], second=self.singly_linked_list.display()
        )

    def test_delete_before_node_end_position(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.delete_before_node(node_value=7)

        self.assertEqual(
            first=[1, 3, 7], second=self.singly_linked_list.display()
        )

    def test_delete_before_node_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.delete_before_node(node_value=13)

        self.assertEqual(
            first=[1, 3, 11, 7], second=self.singly_linked_list.display()
        )

    def test_delete_before_n_next_node(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=3)

        self.singly_linked_list.delete_before_n_next_node(
            node_value=3, n_next_node=2
        )

        self.assertEqual(
            first=[1, 3, 11, 3], second=self.singly_linked_list.display()
        )

    def test_delete_before_n_next_node_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.delete_before_n_next_node(
            node_value=1, n_next_node=1
        )

        self.assertEqual(
            first=[1, 3, 11, 7], second=self.singly_linked_list.display()
        )

    def test_delete_after_node(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.delete_after_node(node_value=3)

        self.assertEqual(
            first=[1, 3, 7], second=self.singly_linked_list.display()
        )

    def test_delete_after_node_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.delete_after_node(node_value=7)

        self.assertEqual(
            first=[1, 3, 11, 7], second=self.singly_linked_list.display()
        )

    def test_delete_after_n_next_node(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.delete_after_n_next_node(
            node_value=3, n_next_node=2
        )

        self.assertEqual(
            first=[1, 3, 11, 3], second=self.singly_linked_list.display()
        )

    def test_delete_after_n_next_node_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=7)

        self.singly_linked_list.delete_after_n_next_node(
            node_value=3, n_next_node=3
        )

        self.assertEqual(
            first=[1, 3, 11, 3, 7], second=self.singly_linked_list.display()
        )

    def test_delete_at_position(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=13)

        self.singly_linked_list.delete_at_position(position=2)

        self.assertEqual(
            first=[1, 3, 7, 13], second=self.singly_linked_list.display()
        )

    def test_delete_at_position_zero_position(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=13)

        self.singly_linked_list.delete_at_position(position=0)

        self.assertEqual(
            first=[3, 11, 7, 13], second=self.singly_linked_list.display()
        )

    def test_delete_at_position_do_nothing(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=11)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=13)

        self.singly_linked_list.delete_at_position(position=5)

        self.assertEqual(
            first=[1, 3, 11, 7, 13], second=self.singly_linked_list.display()
        )

    def test_get_node_position(self) -> None:
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=2)

        position = self.singly_linked_list.get_node_position(node_value=7)

        self.assertEqual(first=2, second=position)

    def test_get_node_position_zero_position(self) -> None:
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=2)

        position = self.singly_linked_list.get_node_position(node_value=1)

        self.assertEqual(first=0, second=position)

    def test_get_node_position_end_position(self) -> None:
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=2)

        position = self.singly_linked_list.get_node_position(node_value=2)

        self.assertEqual(first=3, second=position)

    def test_get_node_position_negative_one(self) -> None:
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=2)

        position = self.singly_linked_list.get_node_position(node_value=17)

        self.assertEqual(first=-1, second=position)

    def test_get_all_node_positions(self) -> None:
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=4)

        positions = self.singly_linked_list.get_all_node_positions(
            node_value=4
        )

        self.assertEqual(first=[1, 3], second=positions)

    def test_get_all_node_positions_empty_list(self) -> None:
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=7)
        self.singly_linked_list.insert_at_end(value=4)

        positions = self.singly_linked_list.get_all_node_positions(
            node_value=5
        )

        self.assertEqual(first=[], second=positions)

    def test_get_size(self) -> None:
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=1)
        self.singly_linked_list.insert_at_end(value=14)

        size = self.singly_linked_list.get_size()

        self.assertEqual(first=4, second=size)

    def test_get_size_empty(self) -> None:
        self.singly_linked_list.delete_at_beginning()

        size = self.singly_linked_list.get_size()

        self.assertEqual(first=0, second=size)

    def test_is_empty_false(self) -> None:
        empty = self.singly_linked_list.is_empty()

        self.assertEqual(first=False, second=empty)

    def test_is_empty_true(self) -> None:
        self.singly_linked_list.delete_at_beginning()

        empty = self.singly_linked_list.is_empty()

        self.assertEqual(first=True, second=empty)

    def test_reverse_list(self) -> None:
        self.singly_linked_list.insert_at_end(value=2)
        self.singly_linked_list.insert_at_end(value=3)
        self.singly_linked_list.insert_at_end(value=4)
        self.singly_linked_list.insert_at_end(value=5)

        self.singly_linked_list.reverse_list()

        self.assertEqual(
            first=[5, 4, 3, 2, 1], second=self.singly_linked_list.display()
        )


if __name__ == "__main__":
    main()
