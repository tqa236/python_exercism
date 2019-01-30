def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError("length is not suitable")
    return [series[i:i+length] for i in range(len(series) - length + 1)]
