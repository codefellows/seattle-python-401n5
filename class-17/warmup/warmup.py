def get_age_range(people_tree):
    if not people_tree.root:
        return 0

    def walk(root, youngest=0, oldest=0):
        if not root:
            return youngest, oldest

        if root.value.age < youngest:
            youngest = root.value.age
        elif root.value.age > oldest:
            oldest = root.value.age

        youngest, oldest = walk(root.left, youngest, oldest)
        youngest, oldest = walk(root.right, youngest, oldest)

        return youngest, oldest

    first_person = people_tree.root.value

    youngest, oldest = walk(people_tree.root, first_person.age, first_person.age)

    return oldest - youngest

