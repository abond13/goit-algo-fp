class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next
        print('None')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            cnext = current.next
            current.next = prev
            prev = current
            current = cnext
        self.head = prev

    def merge_sort(self, h):
        if h is None or h.next is None:
            return h

        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)

        return sorted_list


    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head
        while (fast.next is not None and
               fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow


    def sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result


    def merge_sorted_lists(self, llist1, llist2):
        if llist1.head is None:
            llist1 = llist2

        cur = llist1.head
        while cur.next:
            cur = cur.next
        cur.next = llist2.head

        llist1.merge_sort(llist1.head)

        return llist1


if __name__ == '__main__':

    first_list = LinkedList()

    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    print("Зв'язний список:")
    first_list.print_list()

    first_list.reverse()
    print("Зв'язний список після реверсування :")
    first_list.print_list()

    first_list.head = first_list.merge_sort(first_list.head)
    print("Зв'язний список відсортовано:")
    first_list.print_list()

    second_list = LinkedList()
    second_list.insert_at_beginning(59)
    second_list.insert_at_beginning(20)
    second_list.insert_at_beginning(35)

    first_list.merge_sorted_lists(first_list, second_list)
    print("Зв'язний список відсортовано та замерджено:")
    first_list.print_list()
