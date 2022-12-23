
char_H: list = []; [char_H.append(1) for _ in range(1, ord("H") + 1)]
char_e: list = []; [char_e.append(1) for _ in range(1, ord("e") + 1)]
char_l: list = []; [char_l.append(1) for _ in range(1, ord("l") + 1)]
char_o: list = []; [char_o.append(1) for _ in range(1, ord("o") + 1)]
char_space: list = []; [char_space.append(1) for _ in range(1, ord(" ") + 1)]
char_W: list = []; [char_W.append(1) for _ in range(1, ord("W") + 1)]
char_r: list = []; [char_r.append(1) for _ in range(1, ord("r") + 1)]
char_d: list = []; [char_d.append(1) for _ in range(1, ord("d") + 1)]

helloworld: list = [char_H, char_e, char_l, char_l, char_o, char_space, char_W, char_o, char_r, char_l, char_d]

for char in helloworld:
    print(chr(sum(char)), end="")
