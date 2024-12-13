from itertools import permutations
def calculate_total_distance(tour, distances): 
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]] 
        total_distance += distances[tour[-1]][tour[0]] # Return to the starting city # 
        #print(total_distance)
    return total_distance

def traveling_salesman_bruteforce(distances): 
    cities = range(len(distances)) 
    min_distance = float('inf') 
    optimal_tour = None 
    for tour in permutations(cities): 
        # print(tour) 
        distance = calculate_total_distance(tour, distances) 
        if distance < min_distance: 
            min_distance = distance 
            optimal_tour = tour
            # print(tour, distance)
    return optimal_tour, min_distance 
# Example usage:
# Replace the distances matrix with your own data 
distances_matrix = [[0, 10, 15, 20],
                    [10, 0, 35, 25],
                    [15, 35, 0, 30],
                    [20, 25, 30, 0]
                    ]
optimal_tour, min_distance = traveling_salesman_bruteforce(distances_matrix) 
print("Optimal Tour		:", optimal_tour)
print("Minimum Distance	:", min_distance)
