nums = [1, 2]
index = 3
try:
    print(nums[index])
except IndexError:
    print("Wrong index!")
finally:
    print("A value from nums was accessed!")

