t = int(input())
for _ in range(t):
    alice = 0
    bob = 0
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
            alice += cards
        else:
            bob += cards

        remaining -= cards
        step += 1
    print(alice,bob)
