# ENUMERATE

def intro_enumerate():
    names = ["Alice", "Bob", "Charlie"]

    # without enumerate [manual index]
    index = 0
    for name in names:
        print(index, name)
        index += 1

    for index, name in enumerate(names, start=1): # start default is 0 , can be set with start=1(any integer)
        pass
        print(f"{index} {name}")
 



def get_npi(npi):
    map_to_avoid_ifelif = {
        "111": [{'fname': "a", "npi": "111"}],
        "222": [{'fname': "b", "npi": "222"}],
        "333": [{'fname': "c", "npi": "333"}],
        "444": [{'fname': "d", "npi": "444"}],
        "555": [{'fname': "e", "npi": "555"}],
        "666": [{'fname': "f", "npi": "666"}],
    }
    return map_to_avoid_ifelif.get(npi, [])


def api_fetch():
    from concurrent.futures import ThreadPoolExecutor, as_completed
    all_results = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {}  # <Future at 0x20fbbebb770 state=running>: '111', ..., ..
        
        for npi in ["111","222","333","444","555","666"]:    
            future = executor.submit(get_npi, npi) 
            futures[future] = npi

        for future in as_completed(futures):
            result = future.result()
            if result:
                all_results.extend(result)

        print(all_results)

api_fetch()


# Defines a simple worker function (get_npi) that simulates fetching data for an NPI.

# Uses a dictionary lookup (nice and efficient).

# Returns an empty list if the NPI isn’t found — safe default.

# Creates a thread pool with max_workers=2.

# That means up to two get_npi() calls run concurrently.

# Submits all tasks to the executor and stores futures in a dict.

# The key is the Future object.

# The value (npi) lets you know which task each future corresponds to.

# Uses as_completed(futures) to iterate as each future finishes.

# This ensures results are processed as soon as they’re ready.

# The order of results may differ from the submission order — that’s expected.

# Extends all_results with each returned list.

# Prints all results at the end.