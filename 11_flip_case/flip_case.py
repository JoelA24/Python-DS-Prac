def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    to_swap = to_swap.lower()

    fixed = [(char.swapcasae() if char.lower() == to_swap else char) for char in phrase]

    return "".join(fixed)

#  converts the to_swap string to lowercase using the lower() method. 

#  swaps the case of the character, and an if statement that checks if the lowercase version of the character matches the to_swap string.

#  modified list is joined back into a string using the join() method and returned from the function.