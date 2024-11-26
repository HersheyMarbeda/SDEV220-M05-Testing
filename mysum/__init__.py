def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

target = __import__("my_sum.py")
sum = target.sum

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6" # This is saying that the sum of 1, 2, 3 should be 6 or whatever inside the function should be equal to 6

def test_sum_tuple():
    assert sum((1, 2, 2)) == 5, "Should be 5" # This is saying that the sum of 1, 2, 2 should be 5 or whatever inside the function should be equal to 5
    test_sum()
    test_sum_tuple()

if __name__ == "__main__":
    test_sum()
    print("Everything passed")