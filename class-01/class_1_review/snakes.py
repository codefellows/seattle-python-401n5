# Print A Greeting
# Print a menu
# handle orders


items_dict = {
    "Wings": 0,
    "Cookies": 0,
    "Salmon": 0,
}

greeting = """
***********
* Welcome *
***********
"""

menu = """
Food
----
{}
{}

Appet
-----
{}
""".format(*items_dict)


def main():
    order = True
    print(greeting)
    print(menu)

# some loop quit
    while order:
        order = input("> ")
        if order == "quit":
            print("exit")
            break
        if order in items_dict:
            items_dict[order] += 1
            print(items_dict)


if __name__ == '__main__':
    main()
