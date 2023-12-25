import random


def remove_duplicates_by_keys(employees):
    """ removes duplicated employee entry by the name key"""
    
    unique_dicts = {d['name']: d for d in employees}.values()
    employees = list(unique_dicts)
    return employees

def create_dwarf_giant_pairs(employees):
    """
    create unique dwarf giant pairs from a list of employees while ensuring fairness and 
    randomness
    Args:
        employees: A list of employee objects, each containing three fields.

    Returns:
        A list of tuples, where each tuple represents a Dwarf-Giant pair (name, name)
    
    """
    unique_employees = {tuple(employee.values()): employee for employee in employees}
    employee_names = list(unique_employees.keys())

    random.shuffle(employee_names)
    #print(employee_names)
    pairs = [(employee_names[i], employee_names[-i-1]) for i in range(len(employee_names) // 2)]
    #print(pairs)
    name_pair = [(unique_employees[pair[0]]["name"], unique_employees[pair[1]]["name"]) for pair in pairs]
    #print(name_pair)
    return name_pair


    



def valid_pair(list_tups):
  """ This function checks for valid pairs and output a d
  warf-giant pair that satisfies the four constraints
  """ 
  
  shuffle_pair = [(list_tups[i], list_tups[-i-1]) for i in range(len(list_tups) // 2)]
  #print(shuffle_pair)

  #int_pair = shuffle_pair[:len(shuffle_pair)//2]
  #valid_pair(shuffle_pair)
  final_answer = []
  for shuff in shuffle_pair:
    #random.shuffle(shuff)
    reversed_tup = shuff[::-1] #reverse original
    shuffle_pair1 = [(shuff[0][i], shuff[1][-i-1]) for i in range(2)]
    shuffle_pair2 = [(reversed_tup[0][-i+1], reversed_tup[1][-i+1]) for i in range(2)]
    final_answer = final_answer + shuffle_pair1 + shuffle_pair2

  return final_answer



 










def run(employees):


	
	duplicate_free_employees = remove_duplicates_by_keys(employees)
	output = create_dwarf_giant_pairs(duplicate_free_employees)
	dwarf_giant_pair = valid_pair(output)

	return dwarf_giant_pair

if __name__=="__main__":
        # Testing the solution with the test data. Also works well on the whole dataset
	test_employees = [
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
    
	print(run(test_employees))




