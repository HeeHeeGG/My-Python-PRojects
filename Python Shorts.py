import random 

settings = {
    "theme": "light",
    "lang": "en",
    "alerts": False
}
user_settings = {
    "theme": "dark",
    "lang": "en",
    "alerts": True
}
settings |= user_settings
print(settings)


###########################################

#Lambda functions

spells = [# (spell, damage, mana cost)
    ("Fireball", 50, 40),
    ("Ice Shard", 30, 25),
    ("Lightning Bolt", 70, 50),
    ("Wind Slash", 20, 10),
    ("Dark Void", 55, 50)
]

def dmg_per_mana(s):
    return s[1]/s[2]

efficient_spells = sorted(
    spells,
    key=lambda s: s[1]/s[2],
    reverse=True
)
for s in efficient_spells:
    print(f'{s[0]}: {s[1]/s[2]}')

##################################################
