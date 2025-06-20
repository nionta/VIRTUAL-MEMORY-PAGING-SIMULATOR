
# Virtual Memory Paging Simulator

## Overview
This project implements a Virtual Memory Paging Simulator in Python. It simulates three classic page replacement algorithms:
- FIFO (First-In-First-Out)
- LRU (Least Recently Used)
- Optimal Replacement

The simulator helps users understand how each algorithm handles memory pages and visually compares their behavior.

## Requirements
- Python 3.x
- matplotlib (install via `pip install matplotlib`)

## How to Run
1. Run the script using:
   python paging_simulator.py
2. Enter the number of memory frames.
3. Enter a reference string (space-separated page numbers).

## Output
- Total page faults and hits
- Page fault and hit rates
- Step-by-step memory states
- Visualization using matplotlib
