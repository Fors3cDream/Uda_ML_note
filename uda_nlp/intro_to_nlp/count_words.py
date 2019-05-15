"""
Create by Killer at 2019-05-13 13:37
"""
import re


"""Count words."""
def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict() # dictionary of {<word>: <count>} pairs to return

    # TODO: Covert to lowercase
    text_lower = text.lower()

    # TODO: Split text into tokens(words),leaving out punctuation
    # (Hint: Use regex to split on non-alphanumeric characters)
    rgx = re.compile("(\w+)")
    text_list = rgx.findall(text_lower)

    # TODO: Aggregate word counts using a dictionary
    for words in text_list:
        if words not in counts.keys():
            counts[words] = 1
        else:
            counts[words] += 1

    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair:pair[1], reverse=True)

        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))

        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()