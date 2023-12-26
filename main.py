import random


employees = [
	{
		"department": "R&D",
		"name": "emp1",
		"age": 46
	},
	{
		"department": "Sales",
		"name": "emp2",
		"age": 28
	},
	{
		"department": "R&D",
		"name": "emp3",
		"age": 33
	},
	{
		"department": "R&D",
		"name": "emp4",
		"age": 29
	}
				]


def remove_duplicates_by_all_values(employees):
    """
    removes all dulicated employees values
    """
    seen = set()
    unique_dicts = []
    for d in employees:
        key = tuple(d.values())  # Combine all values as a key
        if key not in seen:
            unique_dicts.append(d)
            seen.add(key)
    return unique_dicts


def listify(employees):
    """
    Extracts all employee names into a list
    
    """
    outer_list = []
    for j in range(len(employees)):
        
        outer_list.append(employees[j]["name"])
    return outer_list


def dwarf_giant(outer_list):
    """
    Creates a unique list of tuples that satisfies all
    constraints
    """
      
    pair =[]
    count = len(outer_list)
    for i in range(len(outer_list)-1):
                tup = (outer_list[i], outer_list[i+1])
                pair.append(tup)
                i+=1
    pair.append((outer_list[-1], outer_list[0]))
    return pair

     

if __name__=="__main__":

    employees = remove_duplicates_by_all_values(employees)
    outer_list =listify(employees) 
    random.shuffle(outer_list) 
    pairs = dwarf_giant(outer_list)
    print(pairs)
    

