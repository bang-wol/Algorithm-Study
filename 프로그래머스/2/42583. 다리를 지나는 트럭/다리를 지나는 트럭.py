from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_queue = deque([0] * bridge_length)
    total_weight_on_bridge=0
    time=0
    truck_index=0
    
    while truck_index < len(truck_weights):
        time += 1
        total_weight_on_bridge -= bridge_queue.popleft()
        
        if truck_index < len(truck_weights) and total_weight_on_bridge + truck_weights[truck_index] <= weight:
            bridge_queue.append(truck_weights[truck_index])
            total_weight_on_bridge += truck_weights[truck_index]
            truck_index += 1
        else:
            bridge_queue.append(0)
    
    time += bridge_length
    
    return time