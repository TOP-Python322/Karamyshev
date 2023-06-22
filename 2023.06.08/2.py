def taxi_cost(distance: int, waiting_time: int = 0) -> int | None:
    if distance < 0 or waiting_time < 0:
        return None

    if distance == 0:
        cost = 80 + waiting_time * 3
    else:
        base_cost = 80
        distance_cost = (distance // 150) * 6
        waiting_cost = waiting_time * 3
        cost = base_cost + distance_cost + waiting_cost

    return int(cost)


distance = int(input("Enter the distance: "))
waiting_time_input = input("Enter your waiting time (optional): ")

if waiting_time_input:
    waiting_time = int(waiting_time_input)
else:
    waiting_time = 0

print(taxi_cost(distance, waiting_time))


