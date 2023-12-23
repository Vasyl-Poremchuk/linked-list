class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next_node = None


class SinglyLinkedList:
    def __init__(self, value: int) -> None:
        self.head_node = Node(value=value)

    @staticmethod
    def get_node(value: int) -> Node:
        """Create a new Node with the given value.

        :param value: int: Specify the value of Node
        :return: A Node instance
        """
        node = Node(value=value)

        return node

    def display(self) -> list[int]:
        """Store the values of Nodes.

        :return: A list of integers
        """
        singly_linked_list_values = []
        current_node = self.head_node

        while current_node:
            singly_linked_list_values.append(current_node.value)
            current_node = current_node.next_node

        return singly_linked_list_values

    def insert_at_beginning(self, value: int) -> None:
        """Replace the Head Node with a new Node.

        :param value: int: Specify the value of Node
        :return: None
        """
        node = self.get_node(value=value)
        node.next_node = self.head_node
        self.head_node = node

    def insert_at_end(self, value: int) -> None:
        """Replace the Tail Node with a new Node.

        :param value: int: Specify the value of Node
        :return: None
        """
        node = self.get_node(value=value)
        current_node = self.head_node

        while current_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = node

    def insert_before_node(self, node_value: int, value: int) -> None:
        """Insert a new Node before the specified Node if it is available in
        the LinkedList.

        :param node_value: int: Specify the value of the search Node
        :param value: int: Specify the value of Node
        :return: None
        """
        node = self.get_node(value=value)
        previous_node = None
        current_node = self.head_node

        if current_node.value == node_value:
            self.insert_at_beginning(value=value)
            return

        while current_node:
            if current_node.value == node_value:
                previous_node.next_node = node
                node.next_node = current_node
                return

            previous_node = current_node
            current_node = current_node.next_node

    def insert_before_n_next_node(
        self, node_value: int, value: int, n_next_node: int
    ) -> None:
        """Insert a new Node before the N next occurrence of the specified Node
        value if it is available in the LinkedList.

        :param node_value: int: Specify the value of the search Node
        :param value: int: Specify the value of Node
        :param n_next_node: int: Specify the occurrence number
        :return: None
        """
        node = self.get_node(value=value)
        previous_node = None
        current_node = self.head_node
        number = 0

        if n_next_node == 1:
            self.insert_before_node(node_value=node_value, value=value)
            return

        while current_node:
            if current_node.value == node_value:
                number += 1

                if number == n_next_node:
                    previous_node.next_node = node
                    node.next_node = current_node
                    return

            previous_node = current_node
            current_node = current_node.next_node

    def insert_after_node(self, node_value: int, value: int) -> None:
        """Insert a new Node after the specified Node value if it is available
        in the LinkedList.

        :param node_value: int: Specify the value of the search Node
        :param value: int: Specify the value of Node
        :return: None
        """
        node = self.get_node(value=value)
        current_node = self.head_node

        while current_node:
            if current_node.value == node_value:
                node.next_node = current_node.next_node
                current_node.next_node = node
                return

            current_node = current_node.next_node

    def insert_after_n_next_node(
        self, node_value: int, value: int, n_next_node: int
    ) -> None:
        """Insert a new Node after the N next occurrence of the specified Node
        value if it is available in the LinkedList.

        :param node_value: int: Specify the value of the search Node
        :param value: int: Specify the value of Node
        :param n_next_node: int: Specify the occurrence number
        :return: None
        """
        node = self.get_node(value=value)
        current_node = self.head_node
        number = 0

        if n_next_node == 1:
            self.insert_after_node(node_value=node_value, value=value)
            return

        while current_node:
            if current_node.value == node_value:
                number += 1

                if number == n_next_node:
                    node.next_node = current_node.next_node
                    current_node.next_node = node
                    return

            current_node = current_node.next_node

    def insert_at_position(self, position: int, value: int) -> None:
        """Insert a new Node at the specified position.

        :param position: int: Specify the position of the Node
        :param value: int: Specify the value of Node
        :return: None
        """
        node = self.get_node(value=value)
        previous_node = None
        current_node = self.head_node

        if position == 0:
            self.insert_at_beginning(value=value)
            return

        for i in range(position):
            if current_node is None:
                return

            previous_node = current_node
            current_node = current_node.next_node

        previous_node.next_node = node
        node.next_node = current_node

    def delete_at_beginning(self) -> None:
        """Delete the current Head Node and replace it with the next Node.

        :return: None
        """
        self.head_node = self.head_node.next_node

    def delete_at_end(self) -> None:
        """Delete the Tail Node and replace it with the previous one.

        :return: None
        """
        current_node = self.head_node

        while current_node.next_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = None
        self.head_node = current_node

    def delete_before_node(self, node_value: int) -> None:
        """Delete the Node up to specified Node value if it is available in the
        LinkedList.

        :param node_value: int: Specify the value of Node
        :return: None
        """
        before_previous_node = None
        previous_node = None
        current_node = self.head_node

        if current_node.value == node_value:
            return

        while current_node:
            if current_node.value == node_value:
                before_previous_node.next_node = current_node
                return

            before_previous_node = previous_node
            previous_node = current_node
            current_node = current_node.next_node

    def delete_before_n_next_node(
        self, node_value: int, n_next_node: int
    ) -> None:
        """Delete a Node before the N next occurrence of the specified Node
        value if it is available in the LinkedList.

        :param node_value: int: Specify the value of the search Node
        :param n_next_node: int: Specify the occurrence number
        :return: None
        """
        before_previous_node = None
        previous_node = None
        current_node = self.head_node
        number = 0

        if n_next_node == 1:
            self.delete_before_node(node_value=node_value)
            return

        while current_node:
            if current_node.value == node_value:
                number += 1

                if number == n_next_node:
                    previous_node = before_previous_node
                    previous_node.next_node = current_node

            before_previous_node = previous_node
            previous_node = current_node
            current_node = current_node.next_node

    def delete_after_node(self, node_value: int) -> None:
        """Delete a Node after the specified Node value if it is available in
        the LinkedList.

        :param node_value: int: Specify the value of the search Node
        :return: None
        """
        current_node = self.head_node

        while current_node.next_node:
            if current_node.value == node_value:
                current_node.next_node = current_node.next_node.next_node

            current_node = current_node.next_node

    def delete_after_n_next_node(
        self, node_value: int, n_next_node: int
    ) -> None:
        """Delete a Node after the N next occurrence of the specified Node if
        it is available in the LinkedList.

        :param node_value: int: Specify the value of Node
        :param n_next_node: int: Specify the occurrence number
        :return: None
        """
        current_node = self.head_node
        number = 0

        while current_node.next_node:
            if current_node.value == node_value:
                number += 1

                if number == n_next_node:
                    current_node.next_node = current_node.next_node.next_node
                    return

            current_node = current_node.next_node

    def delete_at_position(self, position: int) -> None:
        """Delete the Node at the specified position if it is available in the
        LinkedList.

        :param position: int: Specify the position of the Node
        :return: None
        """
        previous_node = None
        current_node = self.head_node

        if position == 0:
            self.delete_at_beginning()

        while current_node:
            node_position = self.get_node_position(
                node_value=current_node.value
            )

            if position == node_position:
                current_node = current_node.next_node
                previous_node.next_node = current_node
                return

            previous_node = current_node
            current_node = current_node.next_node

    def get_node_position(self, node_value: int) -> int:
        """Get the position of the first occurrence of the specified Node
        value.

        :param node_value: Specify the value of the search Node
        :return: The position of the Node if found, otherwise -1
        """
        position = 0
        current_node = self.head_node

        if current_node.value == node_value:
            return position

        while current_node:
            if current_node.value == node_value:
                return position

            current_node = current_node.next_node
            position += 1

        return -1

    def get_all_node_positions(self, node_value: int) -> list[int]:
        """Get the positions of all occurrences of the specified Node value.

        :param node_value: Specify the value of the search Node
        :return: A list of positions of the specified Node value
        """
        position = 0
        node_positions = []
        current_node = self.head_node

        while current_node:
            if current_node.value == node_value:
                node_positions.append(position)

            position += 1
            current_node = current_node.next_node

        return node_positions

    def get_size(self) -> int:
        """Get the size (length) of the LinkedList.

        :return: A size of the LinkedList
        """
        size = 0
        current_node = self.head_node

        while current_node:
            current_node = current_node.next_node
            size += 1

        return size

    def is_empty(self) -> bool:
        """Check if the LinkedList is empty.

        :return: A True if the LinkedList is empty, otherwise False
        """
        empty = not bool(self.head_node)

        return empty

    def reverse_list(self) -> None:
        """Reverse the LinkedList in the other direction.

        :return: None
        """
        previous_node = None
        current_node = self.head_node

        while current_node is not None:
            last_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = last_node

        self.head_node = previous_node
