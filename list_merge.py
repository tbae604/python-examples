def merge_lists(orig, add, rem):
    """
    Takes orig (list of str), adds str from add (list of str), and removes str from rem (list of str).

    Returns list of unique values ordered by desc str char count. If a tie, reverse alphabetical.
    """
    result = list(dict.fromkeys(orig + add))
    for word in rem:
        result.remove(word)
    return sorted(result, key=lambda word: (len(word), word), reverse=True)


if __name__ == "__main__":
    print("Welcome. This takes a list of string, adds another list of string to it, and removes a third list of string. The returned list will be ordered by descending char count.\n")
    orig = str(raw_input("Please provide the first list of str:\n")).strip('][').split(', ')
    add = str(raw_input("Please provide a list of str to add to the first:\n")).strip('][').split(', ')
    rem = str(raw_input("Please provide a list of str to remove from the first:\n")).strip('][').split(', ')
    print("Result:")
    print(merge_lists(orig, add, rem))