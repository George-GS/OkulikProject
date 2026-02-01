response_times = [45, 120, 800, 1500, 75, 6000, 320, 1200, 5, 2800, 95, 4300]

valid_times = [x for x in response_times if 10 <= x <= 5000]

avg_time = sum(valid_times)/len(valid_times)

slow_requests = [x for x in response_times if x > 1000]

valid_times_sec = [round(x/1000, 2) for x in valid_times]
slow_requests_sec = [round(x/1000, 2) for x in slow_requests]

print(f"Валидные времена (мс): {valid_times}")
print(f"Валидные времена (сек): {valid_times_sec}")
print(f"Среднее время: {avg_time:.1f} мс")
print(f"Медленные запросы (>1000 мс): {slow_requests}")
print(f"Медленные запросы (в сек): {slow_requests_sec}")
