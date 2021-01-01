snowballs_count = int(input())
best_result, \
    best_snow, \
    best_time, \
    best_quality = 0, 0, 0, 0
for snowball in range(0, snowballs_count):
    snow = int(input())
    time = int(input())
    quality = int(input())
    result = (snow/time)**quality
    if result >= best_result:
        best_result = result
        best_snow = snow
        best_time = time
        best_quality = quality

print(f"{best_snow} : {best_time} = {int(best_result)} ({best_quality})")
