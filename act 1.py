def calculate(arr, arr_size):
    profits = 0
    for i in range(1,arr_size):
        if arr[i] > arr[i-1]:
         profits += arr[i] - arr[i-1]
    return profits
arr = [13,844,58955,5895385,5389538,13189,389319]
arr_size = len(arr)
print(calculate(arr, arr_size))
    