import random

def make_chains(text):
    words = text.split()
    d = {}
    for i in range(len(words)-2):
        w1 = words[i]
        w2 = words[i+1]
        v = words[i+2]

        key = (w1, w2)

        if key in d:
            l = d[key]
            l.append(v)
        else:
            d[key] = [v]

    return d


def make_text(chains_dict):

    all_keys = chains_dict.keys()
    starting_key = random.choice(all_keys)   #   ("the", "cat")
    output_list = list(starting_key)         #   ["the", "cat"]
    key = starting_key                       #   ("cat", "in")

    while key in chains_dict and len(output_list) < 15:
        possible_words = chains_dict[key]              #       ["the"]
        next_word = random.choice(possible_words)   #"the"
        output_list.append(next_word)               #["the", "cat", "in", "the"]
        key = (key[1], next_word)

    output_text = " ".join(output_list)
    return output_text


def main():
    f = open("would_you.txt")
    original_text = f.read()
    f.close()

    d = make_chains(original_text)
    markov_text = make_text(d)
    print markov_text

if __name__ == "__main__":
    main()
