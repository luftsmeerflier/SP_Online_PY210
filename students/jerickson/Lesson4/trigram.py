import re
import random


def get_material(short=True):
    original_short = "I wish I may I wish I might"
    # Critical Role
    original_long = """
    the city of Zadash. Long in the Dwendalian Empire,
    you’ve made a small name for yourself in a few

    factions. You’ve done a deed or two for the King’s
    Hall here in service of the Crown. You’ve done a

    deed or two with the Knights of Requital, that
    involved getting caught up briefly in a manhunt,

    as you were loosely responsible for the death of
    the High-Richter, the high judge of the local

    court. Managed to make an introductory trade, a
    deal if you will, with The Gentleman, this

    subterranean figure of not the most legal of
    maneuvers. You delved deep into one of the

    subterranean river tunnels beneath the city of
    Zadash for him, managed to clear out and recover

    materials from a long-buried research facility
    from the Age of Arcanum.

    Upon returning, the deal was solid. You managed to
    smuggle out Horris, who needed to be away from the

    town for the time being while this investigation
    was happening. In doing so, also managed to clear

    your names of the death of the High-Richter. Upon
    returning back, getting a few deeds done, now

    waiting for this to blow over, and hearing word
    that there is no longer a manhunt for a number of

    you in cahoots to this, you begin to prepare for
    the coming Harvest Close Festival. Now we’re

    getting close to the third of the month of
    Fessuran, you’ve all managed to prepare in the

    ways you want, got a few things on your side.
    You’ve delved into some of the mysteries of the

    beacon that you maintain. You’ve retrieved your
    Forever Alcoholic Flask. That’s where we’ll begin

    today. Friends, as the early morning creeps up
    upon you, the chilled morning air has left a bit

    of ice and mist crawling across areas of the city
    floor, from outside your window here in the Leaky

    Tap tavern. However, though it is a gloomy
    morning, there is already a general air of

    celebration around. Glancing across, more people
    are now shifting out into the street and city

    around you. Music is beginning to creep into the
    vicinity, and you can hear muffling through the

    nearby walls.
    """
    if short:
        return original_short
    else:
        return original_long


def get_words(source_material):
    processed = re.sub(r"[^a-zA-Z ]+", "", source_material)  # strip all but letters
    processed = processed.lower()  # remove capitlization
    return processed.split()


def generate_xgram_strucutre(words, xgram_size=3):
    """
    Build up the Xgrams dict from the list of words. X being variable length.

    :param1 xgram_size: size of key words + 1. Default 3=tri-gram

    returns a dict with:
       keys: word sets of xgram_size-1
       values: list of followers
    """
    xgram_key_len = xgram_size - 1
    xgram_structure = {}
    for i in range(0, len(words) - xgram_key_len):
        xgram_list = words[i : i + xgram_key_len]
        i_xgram = xgram_structure.setdefault(tuple(xgram_list), [])
        i_xgram.append(words[i + xgram_key_len])
    return xgram_structure


def generate_multi_grams(words, xgram_seq):
    multi_gram_structures = {}
    for xgram_size in xgram_seq:
        multi_gram_structures[xgram_size] = generate_xgram_strucutre(
            words=words, xgram_size=xgram_size,
        )
    return multi_gram_structures


def generate_new_text(multi_grams):
    # TODO add missing key error correction
    # TODO search multiple x-grams
    new_story = ["of", "the"]
    new_words_to_gen = 80

    xgram_size = 3
    xgram_key_len = xgram_size - 1
    for _ in range(new_words_to_gen):
        word_key = tuple(new_story[-xgram_key_len:])
        new_word = random.choice(multi_grams[xgram_size][word_key])
        new_story.append(new_word)
        print(multi_grams[xgram_size][word_key])
        print(new_word)
    print(" ".join(new_story))


if __name__ == "__main__":
    raw = get_material(False)
    words = get_words(source_material=raw)
    xgram_list = [2, 3, 4, 5]
    multi_grams = generate_multi_grams(words, xgram_list)
    generate_new_text(multi_grams)
    # for gram_size, gram_structure in multi_grams.items():
    #     print(gram_size)
    #     for word_set, followers in gram_structure.items():
    #         print(word_set, followers)

