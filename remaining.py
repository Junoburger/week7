def remainingwords(words):
    arr = words.split()
    del arr[0]
    return ' '.join(arr)
