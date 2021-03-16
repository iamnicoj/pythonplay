def can_construct(target, word_bank):
    dashboard = [0 for _ in range(len(target) + 1 )]

    dashboard[0] = 1

    for i in range(len(dashboard)): 
        for word in word_bank:
            word_len =  len(word)
            if (len(target) >= i + word_len) and dashboard[i] > 0 and target.find(word, i) == i:
                dashboard[i + len(word)] += (dashboard[i])

    return dashboard

print(can_construct('', ['f', 'c', 's', 'as', 'd'])) # true
print(can_construct('asdf', ['f', 'c', 's', 'as', 'd'])) # true
print(can_construct('asdf', ['f', 'c', 's', 'as', 'd', 'sd'])) # true
print(can_construct('asdf', ['f', 's', 'as', 'd', 'sd', 'a'])) # true
print(can_construct('asdf', ['k', 'c', 's', 'as', 'd'])) # true
print(can_construct('asdfdasdfdasdfdasdfdasdfdasdfdasdfdasdfdasfasdfasdfasdfasdf', ['f', 'c', 's', 'as', 'd'])) # true


def how_construct(target, word_bank):
    dashboard = [ [] for _ in range(len(target) +1)]
    
    dashboard[0] = [['']]

    for i in range(len(dashboard)):
        if len(dashboard[i]) > 0:
            for word in word_bank:
                if (target.find(word, i) == i):
                    for option in dashboard[i]:
                        concatenated = option + [word]
                        dashboard[i + len(word)].append(concatenated)
                                
    return dashboard[i]

print('How Construct: ')
print(how_construct('', ['f', 'c', 's', 'as', 'd'])) # true
print(how_construct('asdf', ['f', 'c', 's', 'as', 'd'])) # true
print(how_construct('asdf', ['f', 'c', 's', 'as', 'd', 'sd'])) # true
print(how_construct('asdf', ['f', 's', 'as', 'd', 'sd', 'a'])) # true
print(how_construct('asdf', ['k', 'c', 's', 'as', 'd'])) # true
print(how_construct('asdfdasdfdasdfdasdfdasdfdasdfdasdfdasdfdasfasdfasdfasdfasdf', ['f', 'c', 's', 'as', 'd'])) # true
