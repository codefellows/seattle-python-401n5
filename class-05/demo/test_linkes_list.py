import pytest
from linked_list import Node, LinkedList


def test_create_node():
    node1 = Node(5)
    assert node1.value == 5


def test_create_node_not_pass():
    node1 = Node(5)
    assert node1.value != 6


def test_create_node_test_next():
    node1 = Node(5)
    assert node1.next is None


def test_new_ll():
    ll = LinkedList()
    assert ll.head is None


def test_new_ll_with_node():
    node1 = Node(100)
    node2 = Node(99, node1)
    ll = LinkedList(node2)
    assert ll.head is node2
    assert ll.head.next is node1
