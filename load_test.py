import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "http://localhost:8000"
NUM_USERS = 10  # количество "пользователей"
REQUESTS_PER_USER = 10  # запросов от каждого

def simulate_user(user_id):
    results = []
    for i in range(REQUESTS_PER_USER):
        # POST — создать товар
        start = time.time()
        requests.post(f"{URL}/items/", json={
            "category": "Тест",
            "name": f"Товар_{user_id}_{i}",
            "quantity": 10,
            "minimum_quantity": 2
        })
        post_time = time.time() - start

        # GET — получить все товары
        start = time.time()
        requests.get(f"{URL}/items/")
        get_time = time.time() - start

        results.append({"post": post_time, "get": get_time})
    return results

# Запуск
print(f"Запуск: {NUM_USERS} пользователей, {REQUESTS_PER_USER} запросов каждый")
all_results = []

start_total = time.time()
with ThreadPoolExecutor(max_workers=NUM_USERS) as executor:
    futures = [executor.submit(simulate_user, i) for i in range(NUM_USERS)]
    for future in as_completed(futures):
        all_results.extend(future.result())
total_time = time.time() - start_total

# Статистика
post_times = [r["post"] for r in all_results]
get_times = [r["get"] for r in all_results]

print(f"\n--- Результаты ---")
print(f"Всего запросов: {len(all_results) * 2}")
print(f"Общее время: {total_time:.2f}с")
print(f"\nPOST (создание):")
print(f"  Средняя: {sum(post_times)/len(post_times)*1000:.0f}мс")
print(f"  Макс:    {max(post_times)*1000:.0f}мс")
print(f"  Мин:     {min(post_times)*1000:.0f}мс")
print(f"\nGET (чтение):")
print(f"  Средняя: {sum(get_times)/len(get_times)*1000:.0f}мс")
print(f"  Макс:    {max(get_times)*1000:.0f}мс")
print(f"  Мін:     {min(get_times)*1000:.0f}мс")
