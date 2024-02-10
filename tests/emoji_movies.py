from evaluator import *

DESCRIPTION = "A for-fun test to see if the model can go movie title -> emoji -> movie title."

TAGS = ['fun']

question = """
For each of the following ten movies give at most 5 emoji that would best describe the movie.

Give your answer as a JSON array. So If I asked for
```["Finding Nemo", "Toy Story"]```

you might might answer

```json
{"Finding Nemo": ["🐠", "🐟", "🐡", "🐬", "🐳"],
"Toy Story": ["🚀", "⚔️,", "🤖", "👽", "🌌"]}
```.

Now give me answers for these movies:

```["The Lion King", "The Nightmare Before Christmas", "The Godfather", "The Matrix", "Casablanca", "Raiders of the Lost Ark", "V for Vendetta", "The Princess Bride", "Back to the Future", "Dune"]```

Give ONLY a JSON output. Nothing else.
"""

undo = """
For each of the following ten movies described by 5 emoji, give the movie title that best matches.

Give your answer as a JSON list. So If I asked for
```[["🐠", "🐟", "🐡", "🐬", "🐳"], ["🚀", "⚔️,", "🤖", "👽", "🌌"]]```

You might answer

```json
["Finding Nemo", "Toy Story"]]
```.

Now give me answers for these movies:

```<A>```

What are the names of the movie titles?
"""

def extract(x):
    x = json.loads(x)
    return str(list(x.values()))

def count(x):
    try:
        x = json.loads(x)
        count = 0
        for correct, guessed in zip(["The Lion King", "The Nightmare Before Christmas", "The Godfather", "The Matrix", "Casablanca", "Raiders of the Lost Ark", "V for Vendetta", "The Princess Bride", "Back to the Future", "Dune"], x):
            if correct == guessed:
                count += 1
        return count >= 8, "OK"
    except:
        return False, "Not a JSON list"


TestEmojiMovie = question >> LLMRun() >> ExtractJSON() >> PyFunc(extract) >> LLMRun(undo) >> ExtractJSON() >> PyFunc(count)

if __name__ == "__main__":
    print(run_test(TestEmojiMovie))
