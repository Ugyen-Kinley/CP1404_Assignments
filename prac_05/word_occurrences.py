"""
Word Occurrences
Estimate: 25 minutes
Actual:   30 minutes
"""


def main():
    text = input("Text: ")
    word_counts = count_of_word_occurrences(text)
    max_length = max(len(word) for word in word_counts)

    sorted_word_counts = dict(sorted(word_counts.items()))

    for word, count in sorted_word_counts.items():
        print(f"{word:{max_length}} : {count}")


def count_of_word_occurrences(text):
    words = text.split()
    word_counts = {}
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


if __name__ == "__main__":
    main()
