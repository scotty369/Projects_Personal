import random 

# Lists of words I have that the program will create basic sentences from
determiners = ['The', 'A', 'One', 'Some', 'Any']
nouns = ['boy', 'girl', 'dog', 'town', 'car']
verbs = ['drove', 'jumped', 'ran', 'walked', 'skipped']
prepositions = ['to', 'from', 'over', 'under', 'on']
adjectives = ['angry', 'happy', 'sad', 'pretty', 'ugly']
adverbs = ['quickly', 'slowly', 'carefully', 'well', 'badly']

# This function will randomly select a word from the above list
def get_word(word_list):
    return random.choice(word_list)

# This function will make a prepositional phrase
def get_prepositional_phrase():
    return f"{get_word(prepositions)} {get_word(determiners).lower()} {get_word(nouns)}"

# Using this function, it will then make a complete yet basic sentence
def make_sentence():
    return f"{get_word(determiners)} {get_word(adjectives)} {get_word(nouns)} {get_word(adverbs)} {get_word(verbs)} {get_prepositional_phrase()}."

#The below function will construct 6 sentences using the word list and def make_sentence function
for _ in range(6):
    print(make_sentence())

def get_determiner(quantity):
    if quantity == 1:
        return random.choice(['A', 'One', 'The'])
    else:
        return random.choice(['Some', 'Any'])

def get_noun(quantity):
    if quantity == 1:
        return random.choice(["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"])
    else:
        return random.choice(["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"])

def get_verb(quantity, tense):
    if tense == "past":
        return random.choice(["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"])
    elif tense == "present" and quantity == 1:
        return random.choice(["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"])
    else:
        return random.choice(["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"])

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    return f"{determiner} {noun} {verb}"

sentence = make_sentence(2, 'past')
print(sentence)

def get_preposition():
    prepositions = ['to', 'from', 'over', 'under', 'on']
    return random.choice(prepositions)

def get_adjective():
    adjectives = ['angry', 'happy', 'sad', 'pretty', 'ugly']
    return random.choice(adjectives)
