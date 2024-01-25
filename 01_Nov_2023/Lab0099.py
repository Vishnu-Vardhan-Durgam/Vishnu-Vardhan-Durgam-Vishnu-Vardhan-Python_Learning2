words = ["vishnu", "vardhan", "durgamedQECA", "YUYacfAzx"]
min_len = 6


def check_len(word):
    return len(word)> min_len


# op = list(filter(check_len, words))
op = list(map(check_len, words)) # op : [False, True, True, True]
print(op) # OP : ['vardhan', 'durgamedQECA', 'YUYacfAzx']
