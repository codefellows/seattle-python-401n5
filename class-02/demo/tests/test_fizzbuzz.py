import pytest

from fizz_buzz.fiz_buzz import fizz_buzz_function


def test_number_three():
    actual = fizz_buzz_function(3)  # 'Fizz'
    expected = "Fizz"
    assert actual == expected


def test_number_six():
    actual = fizz_buzz_function(6)
    expected = 'Fizz'
    assert actual == expected


def test_number_four_fail():
    actual = fizz_buzz_function(4)
    expected = 'Fizz'
    assert actual != expected


def test_number_four():
    actual = fizz_buzz_function(4)
    expected = 4
    assert actual == expected


def test_number_five():
    actual = fizz_buzz_function(5)
    expected = "Buzz"
    assert actual == expected


def test_number_ten():
    actual = fizz_buzz_function(10)
    expected = "Buzz"
    assert actual == expected


def test_number_fifteen():
    assert fizz_buzz_function(15) == 'FizzBuzz'


def test_number_one_hundred_fifty():
    assert fizz_buzz_function(150) == 'FizzBuzz'
