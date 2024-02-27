from mhelper.enum_helper import VagueEnum


class MyEnum( VagueEnum ):
    ALPHA = 1
    BETA = 2
    GAMMA = 1


# We can compare to case insensitive name or value
assert (MyEnum.ALPHA == MyEnum.ALPHA)
assert (MyEnum.ALPHA == "ALPHA")
assert (MyEnum.ALPHA == "alpha")
assert (MyEnum.ALPHA == 1)

# This also works for aliases
assert (MyEnum.GAMMA == MyEnum.ALPHA)
assert (MyEnum.ALPHA == "GAMMA")
assert (MyEnum.ALPHA == "gamma")
assert (MyEnum.GAMMA == "alpha")

# ...check "not" case
assert (MyEnum.BETA != MyEnum.ALPHA)
assert (MyEnum.BETA != "ALPHA")
assert (MyEnum.BETA != 1)
assert (MyEnum.BETA != "gamma")

# We can check for existence
assert ("ALPHA" in MyEnum)
assert ("gamma" in MyEnum)

# ...check "not" case
assert ("DELTA" not in MyEnum)

print( "0 OK." )
