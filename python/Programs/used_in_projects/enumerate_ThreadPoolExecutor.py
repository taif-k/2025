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
    import random, time
    time.sleep(random.uniform(0.5, 3.0))
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
    # all_results_using_append = []
    # all_results_using_extend = []
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {}  # <Future at 0x20fbbebb770 state=running>: '111', ..., ..
        
        for npi in ["111","222","333","444","555","666"]:    
            future = executor.submit(get_npi, npi)  # imm returns future object (fulfill or pending state)
            futures[future] = npi

        for future in as_completed(futures): # it gives completion order from future dict
            print(f"npi done: {futures[future]}")
            result = future.result()
            print(result)
            # all_results_using_append.append(result) # [[{}],[{}]...] 
            # all_results_using_extend.extend(result)  # [{},{}...]

        # print(all_results_using_extend)
        # print(all_results_using_append)

api_fetch()
