partyA = set(["Park", "Kim", "Lee"])

partyB = set(["Park", "Choi"])


print("파티 A,B에 참석한 사람들:",partyA.union(partyB))
print("파티 A,B에 중복없이 참석한 사람:",partyA.symmetric_difference(partyB))
print("파티 A에만 참석한 사람:",partyA.difference(partyB))