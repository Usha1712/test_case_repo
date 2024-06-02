import json
import time

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def make_hashable(obj):
    """
    Recursively convert dictionaries and lists to hashable types.
    """
    if isinstance(obj, dict):
        return frozenset((key, make_hashable(value)) for key, value in obj.items())
    elif isinstance(obj, list):
        return tuple(make_hashable(item) for item in obj)
    else:
        return obj

def find_similar_test_cases(test_cases):
    clusters = {}
    for test_case in test_cases:
        # Convert input and output to hashable types
        input_hashable = make_hashable(test_case['input'])
        output_hashable = make_hashable(test_case['output'])
        key = (input_hashable, output_hashable)
        if key not in clusters:
            clusters[key] = []
        clusters[key].append(test_case)
    return clusters

def process_execution_logs(execution_logs):
    total_time = sum(log['execution_time'] for log in execution_logs)
    return total_time

def simulate_test_execution(test_cases):
    total_time = 0
    for test_case in test_cases:
        total_time += test_case['execution_time']
    return total_time

def main():
    # Load data
    data = load_data('test_data.json')
    test_cases = data['test_cases']
    execution_logs = data['execution_logs']

    # Normal execution time without optimization
    start_time = time.time()
    normal_execution_time = simulate_test_execution(test_cases)
    normal_time_taken = time.time() - start_time

    print(f"Normal Execution Time (simulated): {normal_execution_time} seconds")
    print(f"Normal Time Taken: {normal_time_taken:.4f} seconds\n")

    # Group similar test cases
    similar_test_case_groups = find_similar_test_cases(test_cases)
    print("Similar Test Case Groups:")
    for key, group in similar_test_case_groups.items():
        print(f"Group {key}: {[tc['name'] for tc in group]}")

    # Optimized execution time after grouping
    start_time = time.time()
    optimized_execution_time = sum(min(tc['execution_time'] for tc in group) for group in similar_test_case_groups.values())
    optimized_time_taken = time.time() - start_time

    print(f"\nOptimized Execution Time (simulated): {optimized_execution_time} seconds")
    print(f"Optimized Time Taken: {optimized_time_taken:.4f} seconds\n")

    # Calculate total execution time from logs
    total_execution_time_from_logs = process_execution_logs(execution_logs)
    print(f"Total Execution Time from Logs: {total_execution_time_from_logs}")

if __name__ == "__main__":
    main()