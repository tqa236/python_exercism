def find(search_list: list[int], value: int) -> None:
    start = 0
    end = len(search_list)
    while start < end:
        index = (start + end) // 2
        if search_list[index] == value:
            return index
        elif search_list[index] > value:
            end = index
        else:
            start = index + 1
    raise ValueError("value not in array")
