from _Lessons_learned import linked_list


def remove_dups(l):
    seen = set()
    current = l.head
    prev = l.head
    if current:
        seen.add(current.data)
        current = current.next
    else:
        raise Exception("List is empty")
    while current:
        # found dup
        if current.data in seen:
            # skip over dup. prev stays the same
            prev.next = current.next
            current = current.next
        else:
            seen.add(current.data)
            prev = current
            current = current.next
    return l

if __name__ == '__main__':
    l = linked_list.LinkedList(["a", "b", "b", "c"])
    print(remove_dups(l))