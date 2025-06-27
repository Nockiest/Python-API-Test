INSULTS = [
    "Thou art a boil, a plague sore!",
    "Thou pribbling ill-nurtured knave!",
    "Thou spongy hasty-witted miscreant!",
    "Thou art as loathsome as a toad.",
    "Thou fobbing sheep-biting scullion!",
    "Thou art unfit for any place but hell.",
    "Thou art a base, proud, shallow, beggarly, three-suited, hundred-pound, filthy, worsted-stocking knave.",
    "Thou art as fat as butter.",
    "Thou art a saucy, full-gorged pigeon-egg!",
    "Thou art a lumpish, idle-headed giglet!"
]

import random

ADJECTIVES = [
    "artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered",
    "clouted", "craven", "currish", "dankish", "dissembling", "droning",
    "errant", "fawning", "fobbing", "froward", "frothy", "gleeking",
    "goatish", "gorbellied", "impertinent", "infectious", "jarring",
    "loggerheaded", "lumpish", "mammering", "mangled", "mewling", "paunchy",
    "pribbling", "puking", "puny", "qualling", "rank", "reeky", "roguish",
    "ruttish", "saucy", "spleeny", "spongy", "surly", "tottering", "unmuzzled",
    "vain", "venomed", "villainous", "warped", "wayward", "weedy", "yeasty"
]

COMPOUND_ADJECTIVES = [
    "base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained",
    "clapper-clawed", "clay-brained", "common-kissing", "crook-pated",
    "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing",
    "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten",
    "folly-fallen", "fool-born", "full-gorged", "guts-griping", "half-faced",
    "hasty-witted", "hedge-born", "hell-hated", "idle-headed", "ill-breeding",
    "ill-nurtured", "knotty-pated", "milk-livered", "motley-minded", "onion-eyed",
    "plume-plucked", "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn",
    "rude-growing", "rump-fed", "shard-borne", "sheep-biting", "spur-galled",
    "swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted", "unchin-snouted",
    "weather-bitten"
]

NOUNS = [
    "apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear",
    "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb",
    "codpiece", "death-token", "dewberry", "flap-dragon", "flax-wench",
    "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon",
    "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger", "joithead",
    "lewdster", "lout", "maggot-pie", "malt-worm", "mammet", "measle",
    "minnow", "miscreant", "moldwarp", "mumble-news", "nut-hook", "pigeon-egg",
    "pignut", "puttock", "pumpion", "ratsbane", "scut", "skainsmate",
    "strumpet", "varlot", "vassal", "whey-face", "wagtail"
]

def generate_insult():
    return f"Thou {random.choice(ADJECTIVES)} {random.choice(COMPOUND_ADJECTIVES)} {random.choice(NOUNS)}!"