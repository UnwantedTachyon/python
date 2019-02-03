chars = range(ord('a'), ord('z') + 1)

for a in chars:
    for b in chars:
        for c in chars:
            for d in chars:
                for e in chars:
                    for f in chars:
                        for g in chars:
                            for h in chars:
                                print(''.join(chr(a) + chr(b) + chr(c) + chr(d) + chr(e) + chr(f) + chr(g) + chr(h)))

                                