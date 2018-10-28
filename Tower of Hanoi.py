def hanoi(circle, first_stack, free_stack, sorted_stack):
    if circle == 1:
        print "Moving circle", circle,"to", sorted_stack
        return

    hanoi(circle - 1, first_stack, sorted_stack, free_stack)
    print "Moving circle", circle, "from", first_stack, "to", sorted_stack
    hanoi(circle - 1, free_stack, first_stack, sorted_stack)


circle = int(input('How many circles do you have?(only integers): '))
hanoi(circle, 'A', 'B', 'C')
