thisisaset = {2, 4, 67, 3, 46, 33}

print(type(thisisaset))
print(thisisaset)

thisisaset.add(2)
thisisaset.add(22)

thisisaset.update({76, 32})
print(thisisaset)

thisisaset.discard(67)
print(thisisaset)

thisisaset.remove(2)
print(thisisaset)

print(thisisaset.intersection({67, 32, 100, 99}))

thisisalsoatest = set([3])
thisisalsoatest.add(4)
thisisalsoatest.add(4)

print(thisisalsoatest)

teams = { [1,2], ["rew", "tesw"]}
