def gale_shapley(men_preferences, women_preferences):
    # Initialize all men and women as free 
    free_men = list(men_preferences.keys())
    matches = {}  # woman -> man mapping 
    proposals = {man: [] for man in men_preferences}  # track proposals made by each man

    while free_men:
        man = free_men.pop(0)

        # Get the next woman to propose to
        for woman in men_preferences[man]:
            if woman not in proposals[man]: # if not yet proposed
                proposals[man].append(woman)
                # If woman is free, match them
                if woman not in matches:
                    matches[woman] = man
                    break
                else:
                    current_man = matches[woman]
                    # Check if she prefers the new man
                    if women_preferences[woman].index(man) < women_preferences[woman].index(current_man):
                        matches[woman] = man
                        free_men.append(current_man)
                        break
                # If she rejects, continue to next woman
    return matches

if __name__ == "__main__":
    import sys
    from pathlib import Path

    raw_text = ""
    input_name = "stdin"
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        input_name = input_path.name
        raw_text = input_path.read_text()
    else:
        raw_text = sys.stdin.read()

    lines = raw_text.splitlines()
    if not lines:
        print("No input provided.")
        sys.exit(1)

    n = int(lines[0].strip())
    
    # Extract all unique women's names from men's preferences (lines 1 to n)
    women_names_set = set()
    for i in range(1, n + 1):
        names = lines[i].split()
        for name in names:
            women_names_set.add(name)
    
    # Extract all unique men's names from women's preferences (lines n+1 to 2n)
    men_names_set = set()
    for i in range(n + 1, 2 * n + 1):
        names = lines[i].split()
        for name in names:
            men_names_set.add(name)
    
    # Sort for consistent ordering
    women_names = sorted(list(women_names_set))
    men_names = sorted(list(men_names_set))
    
    # Parse men's preferences
    men_preferences = {}
    for i in range(1, n + 1):
        preferences = lines[i].split()
        man_index = i - 1
        man_name = men_names[man_index]
        men_preferences[man_name] = preferences
    
    # Parse women's preferences
    women_preferences = {}
    for i in range(n + 1, 2 * n + 1):
        preferences = lines[i].split()
        woman_index = i - n - 1
        woman_name = women_names[woman_index]
        women_preferences[woman_name] = preferences
    
    # Run the algorithm
    matches = gale_shapley(men_preferences, women_preferences)
    
    # Print results
    print("\n" + "=" * 60)
    print("File Input: " + input_name)
    print("=" * 60 + "\n")
    
    print("MEN'S PREFERENCES:")
    for man in sorted(men_preferences.keys()):
        prefs = " > ".join(men_preferences[man])
        print("  " + man + ": " + prefs)
    
    print("\nWOMEN'S PREFERENCES:")
    for woman in sorted(women_preferences.keys()):
        prefs = " > ".join(women_preferences[woman])
        print("  " + woman + ": " + prefs)
    
    print("\n" + "=" * 60)
    print("STABLE MATCHING RESULTS:")
    print("=" * 60)
    
    # Convert matches from woman->man to man->woman for display
    man_to_woman = {}
    for woman, man in matches.items():
        man_to_woman[man] = woman
    
    for man in sorted(man_to_woman.keys()):
        woman = man_to_woman[man]
        print("  " + man + " <---> " + woman)
    
    print("\n" + "=" * 60)
    print("✓ MATCHING COMPLETE")
    print("=" * 60 + "\n")