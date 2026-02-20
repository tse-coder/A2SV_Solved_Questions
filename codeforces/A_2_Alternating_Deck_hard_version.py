t = int(input())
for _ in range(t):
    alice = [0,0]
    bob = [0,0]
    remaining = int(input())
    step = 1

    while remaining > 0:
        if step == 1:
            player = "alice"
        else:
            block = (step - 2) // 2
            if block % 2 == 0:
                player = "bob"
            else:
                player = "alice"

        cards = min(step, remaining)

        if player == "alice":
            if cards%2 ==0:
                alice[0] += cards//2
                alice[1] += cards//2
            else:
                alice[0] += cards//2 + 1
                alice[1] += cards//2
        else:
            if cards % 2 == 0:
                bob[1] += cards//2
                bob[0] += cards//2
            else:
                bob[1] += cards//2 + 1
                bob[0] += cards//2

        remaining -= cards
        step += 1
    print(alice[0],alice[1],bob[0],bob[1])
