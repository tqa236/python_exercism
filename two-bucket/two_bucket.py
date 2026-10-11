from collections import deque


def measure(bucket_one: int, bucket_two: int, goal: int, start_bucket: str):
    start_bucket = start_bucket.lower()
    if start_bucket not in {"one", "two"}:
        raise ValueError("invalid start bucket")
    if goal == 0:
        return (0, start_bucket, 0)
    if goal > max(bucket_one, bucket_two):
        raise ValueError("goal is impossible")

    start_state = (bucket_one, 0) if start_bucket == "one" else (0, bucket_two)
    queue = deque([(start_state, 1)])
    seen = {start_state}

    def is_legal_state(state):
        a, b = state
        if start_bucket == "one":
            return not (a == 0 and b == bucket_two)
        return not (a == bucket_one and b == 0)

    def neighbors(state):
        a, b = state
        options = []

        if a < bucket_one:
            nxt = (bucket_one, b)
            if is_legal_state(nxt):
                options.append(nxt)
        if b < bucket_two:
            nxt = (a, bucket_two)
            if is_legal_state(nxt):
                options.append(nxt)
        if a > 0:
            nxt = (0, b)
            if is_legal_state(nxt):
                options.append(nxt)
        if b > 0:
            nxt = (a, 0)
            if is_legal_state(nxt):
                options.append(nxt)

        if a > 0:
            pour = min(a, bucket_two - b)
            if pour > 0:
                nxt = (a - pour, b + pour)
                if is_legal_state(nxt):
                    options.append(nxt)
        if b > 0:
            pour = min(b, bucket_one - a)
            if pour > 0:
                nxt = (a + pour, b - pour)
                if is_legal_state(nxt):
                    options.append(nxt)

        return options

    while queue:
        state, steps = queue.popleft()
        a, b = state
        if a == goal:
            return (steps, "one", b)
        if b == goal:
            return (steps, "two", a)

        for nxt in neighbors(state):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, steps + 1))

    raise ValueError("goal is impossible")
