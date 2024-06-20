def MinWindowSubstring(strArr):
    # Extract the two strings from strArr
    N, K = strArr

    # Initialize variables
    start, minLength = 0, float('inf')
    charCount = {}
    requiredChars = set(K)

    # Helper function to check if all required characters are present
    def allCharsPresent():
        return all(charCount[char] >= K.count(char) for char in requiredChars)

    for end, char in enumerate(N):
        # Update character count
        charCount[char] = charCount.get(char, 0) + 1

        # Check if the current window contains all required characters
        while allCharsPresent():
            # Update the minimum length and starting index of the window
            if end - start + 1 < minLength:
                minLength = end - start + 1
                minWindowStart = start

            # Move the window start to the right
            charCount[N[start]] -= 1
            start += 1

    # Return the smallest substring
    return N[minWindowStart:minWindowStart + minLength]

# Examples:
print(MinWindowSubstring(["aaabaaddae", "aed"]))    # Output: "dae"
print(MinWindowSubstring(["aabdccdbcacd", "aad"]))  # Output: "aabd"
