def check_collide(bullet_list, mob_list):
    for bullet_index in range(0, len(bullet_list)):
        for mob_index in range(0, len(mob_list)):
            if bullet_list[bullet_index].rect.colliderect(mob_list[mob_index].rect):
                bullet_list[bullet_index].collide()
                bullet_list[bullet_index] = 0
                mob_list[mob_index].get_damage()
                break

    while 0 in bullet_list:
        bullet_list.remove(0)
    while 0 in mob_list:
        mob_list.remove(0)

    shift = 0.8
    for i in range(len(mob_list) - 1):
        for j in range(i + 1, len(mob_list)):
            if mob_list[i].rect.colliderect(mob_list[j].rect):
                mob_list[i].move(-shift, -shift)
                mob_list[j].move(shift, shift)





