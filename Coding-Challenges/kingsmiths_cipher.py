""" 
Problem statement: 

In the land of Cryptonia, ancient vaults hold secrets to eternal knowledge, hidden behind locks that no brute force can open.

Only one thing can—a Perfect Key, crafted using a precise sequence of magical runes. These runes are always distinct, each holding a unique elemental power: wind, flame, stone, shadow…

The Keysmith Guild has entrusted their youngest apprentice, Arin, with an urgent mission: generate every possible arrangement of a set of unique runes to try unlocking a sealed vault that’s been dormant for a thousand years.

But the vault is a trickster. It accepts only one permutation of the rune sequence, and nobody knows which.

Arin’s job: forge all permutations of the given rune sequence and hand them to the Oracle (the test system) who will verify the correct one.

🔐 Your Mission
Write a function:
def forge_keys(runes: str) -> List[str]:

Given a string of n distinct characters (e.g., "ABCD"), return all possible permutations of the string.

Each character must be used exactly once per key

Keys can be returned in any order

All characters in the input will be unique

"""

class ForgeKeys:
    def __init__(self):
        self.num = 0
        self.keys = []

    def forge_keys(self, rune):
        self.num = 0
        self.keys = []
        self.construct_key(rune, "")
        return self.keys

    def construct_key(self, remaining_runes, current_key):
        if len(remaining_runes) == 0:
            self.num += 1
            self.keys.append(current_key)
            return
        for i in range(len(remaining_runes)):
            self.construct_key(
                remaining_runes[:i] + remaining_runes[i+1:], 
                current_key + remaining_runes[i]
            )

if __name__ == "__main__":
    fK = ForgeKeys()
    result = fK.forge_keys("ABCD")
    print(f"Total keys Arin forged: {fK.num}")
    for key in result:
        print(key)