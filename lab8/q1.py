def solve_cryptarithmetic(puzzle):
    letters = set("".join(puzzle))
    if len(letters) > 10:
        print("Invalid puzzle: More than 10 unique letters.")
        return

    def is_valid_assignment(assignment, word):
        return all(assignment[letter] is not None for letter in word)

    def evaluate_word(word, assignment):
        return int("".join(str(assignment[letter]) for letter in word))

    def check_solution(assignment, puzzle):
        first_sum = evaluate_word(puzzle[0], assignment)
        second_sum = evaluate_word(puzzle[1], assignment)
        result = evaluate_word(puzzle[2], assignment)
        return first_sum + second_sum == result

    def backtrack(assignment, remaining_letters):
        if not remaining_letters:
            if check_solution(assignment, puzzle):
                print("Solution found:")
                for letter, value in assignment.items():
                    print(f"{letter}: {value}")
                print()
                exit()
            return

        current_letter = remaining_letters.pop()
        for digit in range(10):
            if digit not in assignment.values():
                assignment[current_letter] = digit
                if is_valid_assignment(assignment, current_letter):
                    backtrack(assignment.copy(), remaining_letters.copy())
                assignment[current_letter] = None
        remaining_letters.append(current_letter)

    initial_assignment = {letter: None for letter in letters}
    initial_remaining_letters = list(letters)
    backtrack(initial_assignment, initial_remaining_letters)

# Example usage:
def main():
    puzzle = ["SEND", "MORE", "MONEY"]
    solve_cryptarithmetic(puzzle)

if __name__ == '__main__':
    main()
