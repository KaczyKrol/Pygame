import delta_time as dt

bodies = [player, block1, block2, ...]

while True:
    dt.update()  # Twój deltaTime

    # 1. Update fizyki
    for b in bodies:
        b.update()

    # 2. Kolizje
    for i in range(len(bodies)):
        for j in range(i+1, len(bodies)):
            resolve_aabb_collision(bodies[i], bodies[j])
