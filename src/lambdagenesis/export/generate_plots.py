import json
import os
import matplotlib.pyplot as plt

os.makedirs("media/plots", exist_ok=True)
with open("data/history.json") as f:
    history = json.load(f)

ticks = [x["tick"] for x in history]
complexity = [x["avg_complexity"] for x in history]
entropy = [x["entropy"] for x in history]
population = [x["population"] for x in history]

plt.figure(figsize=(10, 5))
plt.plot(ticks, complexity)
plt.xlabel("Tick")
plt.ylabel("Complexity")
plt.title("Complexity Growth")
plt.savefig("media/plots/complexity.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(ticks, entropy)
plt.xlabel("Tick")
plt.ylabel("Entropy")
plt.title("Entropy Dynamics")
plt.savefig("media/plots/entropy.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(ticks, population)
plt.xlabel("Tick")
plt.ylabel("Population")
plt.title("Population Dynamics")
plt.savefig("media/plots/population.png")
plt.close()
