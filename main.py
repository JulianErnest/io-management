#!/usr/bin/env python3
"""
IO Managaement algorithms calculator and visualizer
"""

__author__ = "Julian  Ernest Camello"
__version__ = "0.1.0"
__license__ = "MIT"

import matplotlib.pyplot as plt
import numpy as np
import inquirer

MAX = 200

def main():


    main_prompt = [
        inquirer.List('algorithm',
                    message="Select an algorithm",
                    carousel=True,
                    choices=[
                        'First-Come, First-Served (FCFS)', 
                        'Shortest Seek Time First (SSTF)', 
                        'SCAN (Elevator) Algorithm',
                        'C-SCAN Algorithm',
                        'LOOK Algorithm',
                        'C-LOOK Algorithm'
                        ]
        ),
        inquirer.Text('initial_track',message="Initial Track"),
        inquirer.Text('track_requests',message="Track Requests")
    ]
    
    answers = inquirer.prompt(main_prompt)
    algorithm = answers['algorithm']
    track_requests = answers['track_requests'].strip().split(' ')
    track_requests = [eval(i) for i in track_requests]
    initial_track = eval(answers['initial_track'])    
    print(algorithm == 'C-LOOK Algorithm')

    x = [i for i in range(0, len(track_requests) + 1)]

    if (algorithm == 'First-Come, First-Served (FCFS)'):
        y, total = fcfs(track_requests, initial_track)
        y.insert(0, initial_track)
    elif (algorithm == 'Shortest Seek Time First (SSTF)'):
        y, total = sstf(track_requests, initial_track)
        y.insert(0, initial_track)
    elif (algorithm == 'SCAN (Elevator) Algorithm'):
        if MAX - 1 not in track_requests:
            x.append(len(x))
        y, total = scan_a(track_requests, initial_track)
    elif (algorithm == 'C-SCAN Algorithm'):
        if 0 not in track_requests:
            x.append(len(x))
        if MAX - 1 not in track_requests:
            x.append(len(x))
        y, total = c_scan(track_requests, initial_track)
    elif (algorithm == 'LOOK Algorithm'):
        y, total = look(track_requests, initial_track)
    elif (algorithm == 'C-LOOK Algorithm'):
        y, total = c_look(track_requests, initial_track)
    

    # plot
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2.0)
    plt.title(f"Total track time: {total}")
    plt.xticks([])


    plt.yticks(range(min(y), max(y) + 1, 10))
    for i, txt in enumerate(y):
        plt.text(x[i], txt, str(txt), ha='center', va='bottom')

    plt.yticks(range(10, 200, 10))
    plt.show()



def fcfs(track_requests, head):
    total = 0
    for i in range(0, len(track_requests) - 1):
            total += abs(track_requests[i] - track_requests[i + 1]) 
    total += abs(track_requests[0] - head)
    return track_requests, total

def sstf(requests, head):
    total_track_time = 0
    current_head_position = head
    result_order = []

    while requests:
        # Calculate seek time for each request
        seek_times = [abs(request - current_head_position) for request in requests]

        # Find the request with the minimum seek time
        min_seek_time = min(seek_times)
        min_seek_index = seek_times.index(min_seek_time)
        selected_request = requests.pop(min_seek_index)

        # Update total track time
        total_track_time += min_seek_time

        # Update current head position
        current_head_position = selected_request

        # Add the selected request to the result order
        result_order.append(selected_request)

    print('total', total_track_time)
    return result_order, total_track_time

def scan_a(track_requests, head):
    total = 0
    if MAX - 1 not in track_requests:
        track_requests.append(MAX - 1)
    track_requests.sort();
    right = [req for req in track_requests if req <= head]
    right.reverse()
    left = [req for req in track_requests if req > head]
    left.insert(0, head)
    new_track = left + right
    print(new_track)
    for i in range(0, len(new_track) - 1):
        print(abs(new_track[i] - new_track[i + 1]))
        total += abs(new_track[i] - new_track[i + 1]) 

    return new_track, total

def c_scan(track_requests, head):
    total = 0
    if 0 not in track_requests:
        track_requests.append(0)
    if MAX - 1 not in track_requests:
        track_requests.append(MAX - 1)
    track_requests.sort();
    right = [req for req in track_requests if req <= head]
    left = [req for req in track_requests if req > head]
    left.insert(0, head)
    new_track = left + right

    for i in range(0, len(new_track) - 1):
        total += abs(new_track[i] - new_track[i + 1]) 
        print(total)

    return new_track, total

def look(track_requests, head):
    track_requests.sort();
    total = 0
    right = [req for req in track_requests if req <= head]
    left = [req for req in track_requests if req > head]
    left.insert(0, head)
    right.reverse()
    new_track = left + right

    print(new_track)
    for i in range(0, len(new_track) - 1):
        total += abs(new_track[i] - new_track[i + 1]) 

    return new_track, total

def c_look(track_requests, head):
    track_requests.sort();
    total = 0
    right = [req for req in track_requests if req <= head]
    left = [req for req in track_requests if req > head]
    left.insert(0, head)
    new_track = left + right

    print(new_track)
    for i in range(0, len(new_track) - 1):
        total += abs(new_track[i] - new_track[i + 1]) 

    print(new_track)
    return new_track, total


if __name__ == "__main__":
    main()