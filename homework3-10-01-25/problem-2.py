def find_unique_substrings(s, start=0, substrings=None):   
    if substrings is None:
        substrings = set()

    if start >= len(s):
        return substrings

    generate_substrings_from_position(s, start, start, substrings)
    
    return find_unique_substrings(s, start + 1, substrings)


def generate_substrings_from_position(s, start, end, substrings):
    if end >= len(s):
        return
    
    substring = s[start:end + 1]
    substrings.add(substring)
    
    generate_substrings_from_position(s, start, end + 1, substrings)



def main():
    input_string = input().strip()
    unique_substrings = find_unique_substrings(input_string)
    substring_list = sorted(list(unique_substrings))
    print(", ".join(substring_list))
    print(len(unique_substrings))
if __name__ == "__main__":
    main()