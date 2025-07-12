import matplotlib.pyplot as plt
import time, json
start_reading = time.time() - 2 * 7 * 24 * 60 * 60 #day * hour * minute * sec
figure = []
with open("price_info.txt", "r") as f:
    while True:
        read_line = json.loads(f.readline())
        if read_line["time"] >= start_reading:
            figure.append(read_line["price_difference"])
        else:
            break
plt.plot(figure)
plt.title('Rune price', fontsize=15)
plt.show()