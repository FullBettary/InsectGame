def draw(surface, player, *lists_for_draw):
    for l in lists_for_draw:
        for index in range(len(l)):
            data = l[index].action()
            if data is None:
                l[index] = 0
            else:
                surface.blit(data[0], data[1])

    for l in lists_for_draw:
        while 0 in l:
            l.remove(0)

    data = player.event_move_and_rot()
    surface.blit(data[0], data[1])
