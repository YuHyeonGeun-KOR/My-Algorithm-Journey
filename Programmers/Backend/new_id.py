def upper_to_low (new_id):
    return new_id.lower()

def delete_else(new_id):
    new_id_copy= ""
    for i in range(len(new_id)):
        if new_id[i].isalpha() or  new_id[i].isdigit() or new_id[i] == "-" or new_id[i] == "_" or new_id[i] == ".":
           new_id_copy +=new_id[i]
        
            
    return new_id_copy

def delete_double_dot(new_id):
    while ".." in new_id:
        new_id = new_id.replace("..",".")
    
    return new_id
def delete_startend_dot(new_id):
    flag_start = True
    flag_end = True
    

    
    if ord(new_id[0]) == ord("."):
        flag_start = False
    
        
    if ord(new_id[-1]) == ord("."):
        flag_end = False

    if flag_start == False:
        new_id = new_id[1:]
    if flag_end == False:
        new_id = new_id[:-1]

    return new_id

def add_a(new_id):
    if new_id == "":
        new_id = "a"
            
    return new_id  

def fifteen(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
    if ord(new_id[-1]) == ord("."):
        new_id = new_id[:-1]

    return new_id       

def copy(new_id):
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]


    return new_id
                
   
def solution(new_id):
    answer = ''
    new_id = upper_to_low(new_id)
    print(new_id)
    new_id = delete_else(new_id)
    print(new_id)
    new_id = delete_double_dot(new_id)
    print(new_id)
    new_id = delete_startend_dot(new_id)
    print(new_id)
    new_id = add_a(new_id)
    print(new_id)
    new_id = fifteen(new_id)
    print(new_id)
    new_id = copy(new_id)
    print(new_id)
    
 
    return new_id

new_id = "aaaaaaaa.a.a.aaaaaa" 
print(solution(new_id))