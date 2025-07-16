movie=["red dargon" ,"ganster","theri","mersal","salar"]
print(movie)
print(movie[1],movie[4])
#dictionary
book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
}
book["publisher"] = "secker and warbug"
for key, value in book.items():
    print("key:",key, "value:",value)
    
#with fucntions
def analyze_list(my_list):
    unique_elements = set(my_list)
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    return unique_elements, counts

# Test
data = [1, 2, 2, 3, 3, 3, 4]
unique, count_dict = analyze_list(data)
print("Unique elements:", unique)
print("Element counts:", count_dict)
