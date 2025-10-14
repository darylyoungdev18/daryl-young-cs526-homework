def is_palindrome(s, left=0, right=None):
    
    if right is None:
        right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)


def main():
    palidrome_count = 0

    try:
        while True:
            line = input().strip()
            if not line:
                continue
            if is_palindrome(line):
                print("true")
                palidrome_count += 1
            else:
                print("false")
    except EOFError:
        print(palidrome_count)

if __name__ == "__main__":
    main()