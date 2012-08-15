#!/usr/bin/python
import random

santas = ['chris', 'socrates', 'kami', 'chingu']
children = ['chris', 'socrates', 'kami', 'chingu']
chosen = []

def pick_child(santa, matches):
    # pick a random child
    for child in children:
        # check for match
        if santa != child and child not in chosen and (child, santa) not in matches:
            children.remove(child)
            chosen.append(santa)
            break

    return child

def match_santas():
    matches = []
    random.shuffle(children)

    # pair matches
    for santa in santas:
        child = pick_child(santa, matches)
        matches.append((santa, child))

    return matches

if __name__ == '__main__':
    print 'go santa go!'
    matches = match_santas()
    print matches
