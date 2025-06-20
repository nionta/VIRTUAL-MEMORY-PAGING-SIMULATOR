import matplotlib.pyplot as plt

class PageReplacement:
    def __init__(self, frames, reference_string):
        self.frames = frames
        self.reference_string = reference_string

    def fifo(self):
        memory = []
        page_faults = 0
        page_hits = 0
        result = []

        for page in self.reference_string:
            if page in memory:
                page_hits += 1
            else:
                if len(memory) < self.frames:
                    memory.append(page)
                else:
                    memory.pop(0)
                    memory.append(page)
                page_faults += 1
            result.append(memory[:])

        return page_faults, page_hits, result

    def lru(self):
        memory = []
        page_faults = 0
        page_hits = 0
        recent_usage = []
        result = []

        for page in self.reference_string:
            if page in memory:
                page_hits += 1
                recent_usage.remove(page)
                recent_usage.append(page)
            else:
                if len(memory) < self.frames:
                    memory.append(page)
                else:
                    lru_page = recent_usage.pop(0)
                    memory[memory.index(lru_page)] = page
                recent_usage.append(page)
                page_faults += 1
            result.append(memory[:])

        return page_faults, page_hits, result

    def optimal(self):
        memory = []
        page_faults = 0
        page_hits = 0
        result = []

        for i, page in enumerate(self.reference_string):
            if page in memory:
                page_hits += 1
            else:
                if len(memory) < self.frames:
                    memory.append(page)
                else:
                    future_uses = {}
                    for p in memory:
                        if p in self.reference_string[i+1:]:
                            future_uses[p] = self.reference_string[i+1:].index(p)
                        else:
                            future_uses[p] = float('inf')
                    farthest_page = max(future_uses, key=future_uses.get)
                    memory[memory.index(farthest_page)] = page
                page_faults += 1
            result.append(memory[:])

        return page_faults, page_hits, result

    def display_results(self, algorithm, faults, hits, result):
        print(f"\n--- {algorithm} Page Replacement ---")
        print(f"Total Page Faults: {faults}")
        print(f"Total Page Hits: {hits}")
        print(f"Page Fault Rate: {faults / len(self.reference_string) * 100:.2f}%")
        print(f"Page Hit Rate: {hits / len(self.reference_string) * 100:.2f}%")
        print("\nStep-by-Step Memory State:")
        for i, state in enumerate(result):
            print(f"Step {i+1}: {state}")

    def visualize(self, algorithm, result):
        plt.figure(figsize=(10, 5))
        for i, state in enumerate(result):
            for j, val in enumerate(state):
                plt.scatter(i, val, s=100, label=f'Step {i+1}' if i == 0 else "")
        plt.xlabel("Steps")
        plt.ylabel("Pages in Memory")
        plt.title(f"{algorithm} Page Replacement Visualization")
        plt.grid(True)
        plt.show()

# === Main ===
if __name__ == "__main__":
    try:
        frames = int(input("Enter number of frames: "))
        ref_input = input("Enter reference string (space-separated): ")
        reference_string = list(map(int, ref_input.strip().split()))

        simulator = PageReplacement(frames, reference_string)

        # FIFO
        fifo_faults, fifo_hits, fifo_result = simulator.fifo()
        simulator.display_results("FIFO", fifo_faults, fifo_hits, fifo_result)
        simulator.visualize("FIFO", fifo_result)

        # LRU
        lru_faults, lru_hits, lru_result = simulator.lru()
        simulator.display_results("LRU", lru_faults, lru_hits, lru_result)
        simulator.visualize("LRU", lru_result)

        # Optimal
        opt_faults, opt_hits, opt_result = simulator.optimal()
        simulator.display_results("Optimal", opt_faults, opt_hits, opt_result)
        simulator.visualize("Optimal", opt_result)

    except Exception as e:
        print("Error:", e)
