import json

from collections import defaultdict
import heapq


user_to_fallowers = [{"id": "id1", "name": "name1", "followers": ["id2","id5","id6"]},
           {"id": "id2", "name": "name2", "followers": ["id1"]},
           {"id": "id3", "name": "name3", "followers": ["id5","id1","id6"]},
           {"id": "id4", "name": "name4", "followers": ["id2"]},
           {"id": "id5", "name": "name5", "followers": ["id3","id1","id6"]},
           {"id": "id6", "name": "name6", "followers": ["id3","id1","id5"]}]

json_with_tuples = [
    {"name": "aa", "age": 30, "address": {"city": "New York", "zipcode": "10001"}, "kidss": ("Eli", "Zal", {"Yon": "Arye"})},
    {"name": "bb", "age": 45, "address": {"city": "LS", "zipcode": "10055"}, "kidss": ("Eli", "David"), "houses":["BB", "BBC"]}
]
json_without_tuples = [
    {"name": "aa", "age": 30, "address": {"city": "New York", "zipcode": "10001"}, "kidss": ["Eli", "Zal", {"Yon": "Arye"}]},
    {"name": "bb", "age": 45, "address": {"city": "LS", "zipcode": "10055"}, "kidss": ["Eli", "David"], "houses":["BB", "BBC"]}
]

def dijkstra(users, src, target):
    if src==target:
        return(0, src)
    g ={}
    for user in users:
        g[user["id"]] = user["followers"]

    q = [(0, src, [])]
    visited, dist = set(), {src: 0.0}
    while q:
        cost, v, path = heapq.heappop(q)
        if v not in visited:
            visited.add(v)
            path.append(v)
            # if v == target:
            #     return (cost, path)
            
            for v2 in g[v]:
                if v2 == target:
                    path.append(v2)
                    return (cost+1, path)
                if v2 in visited:
                    continue
                if cost + 1 < dist.get(v2, float('inf')):
                    # dist[v2] = cost + 1
                    heapq.heappush(q, (cost + 1, v2, path)) 
    return (float('inf'), ())
path_length = dijkstra(user_to_fallowers, "id4" , "id3")
t=0
def print_fallowers_in_topolagical_orderutils(user_to_fallowers, user, visited, stack):
    for fallower in user_to_fallowers[user]:
        if fallower not in visited:
            visited.add(fallower)
            print_fallowers_in_topolagical_orderutils(user_to_fallowers, fallower, visited, stack)
    stack.append(user)

def print_fallowers_in_topolagical_order(users):
    user_to_fallowers = {}
    for user in users:
        user_to_fallowers[user["id"]] = user["followers"]
    visited = set()
    stack= []
    for user in user_to_fallowers:
        if user not in visited:
            visited.add(user)
            print_fallowers_in_topolagical_orderutils(user_to_fallowers, user, visited, stack)
    print(stack)

print_fallowers_in_topolagical_order(user_to_fallowers)


def get_followed_names(data):
    id_to_name_dict = {}
    for user in data:
        id_to_name_dict[user['id']] = user['name']

    user_to_followed = {}
    for user in data:
        followed_name = user['name']
        for follower in user['followers']:
            follower_name = id_to_name_dict[follower]
            if follower_name not in user_to_followed:
                user_to_followed[follower_name]=[]
            user_to_followed[follower_name].append(followed_name)

    user_to_followed = get_followed_names(user_to_fallowers)
    print("printing not sorted")
    for user, followed in user_to_followed.items():
        print (f"user: {user} has these followed: {followed}")

    # print sorted
    print("\nprinting sorted")
    for user in sorted(user_to_followed):
        print (f"user: {user} has these followed: {user_to_followed[user]}")
        
# get_followed_names(data1)    
# print(json.dumps(json_with_tuples, indent=4)) # will print tuples as arrays          


### Still printing tuples as arrys
# def print_nested_object(data, indentation=0):
#     if isinstance(data, list):
#         for item in data:
#             print_nested_object(item, indentation +1)
#     elif isinstance(data, dict):
#         print()

def print_nested_object_with_tuples_util(obj):
    """
    Recursively converts all tuples in a nested JSON-like structure to a special format.
    """
    if isinstance(obj, tuple):
        return {"__tuple__": [print_nested_object_with_tuples_util(item) for item in obj]}
    elif isinstance(obj, list):
        return [print_nested_object_with_tuples_util(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: print_nested_object_with_tuples_util(value) for key, value in obj.items()}
    else:
        return obj

def print_nested_object_with_tuples(obj):
    # Convert the JSON with tuples to a serializable format
    converted_json = print_nested_object_with_tuples_util(obj)

    # Serialize with pretty printing
    serialized = json.dumps(converted_json, indent=4)
    print(serialized)
# print_nested_object_with_tuples(json_with_tuples)


def print_nested(obj, indent=0, same_line=False):
    """
    Recursively prints a JSON-like structure with proper indentation.
    Converts tuples into a special representation with '__tuple__'.
    """
    spaces = " " * indent 
    same_line_space = '' if same_line else spaces
    if isinstance(obj, dict):
        print(f"{spaces}{{")
        for key, value in obj.items():
            print(f"{spaces}  \"{key}\": ", end="")
            print_nested(value, indent + 2, same_line=True)
        print(f"{spaces}}}")
    elif isinstance(obj, list):
        print(f"[")
        for item in obj:
            print_nested(item, indent + 2)
        print(f"{spaces}]")
    # elif isinstance(obj, tuple):
    #     print(f"{spaces}{{\"__tuple__\": [")
    #     for item in obj:
    #         print_nested(item, indent + 2)
    #     print(f"{spaces}]}}")
    elif isinstance(obj, str):
        print(f"{same_line_space}\"{obj}\"")
    else:
        print(f"{same_line_space}{obj}")


# Print the JSON-like structure with proper indentation
# print_nested(json_without_tuples, indent=0)
