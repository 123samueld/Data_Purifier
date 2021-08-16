def loop_through_folders():
    file_name = "1.0"
    loop_through_files(file_name)

def loop_through_files(file_name):
    print("File name is: " + file_name)
    
    """ 
    #file_names = [ibiza, miami, naples]
    #try finding city name
    #except pass over vacant names
    file_index_number = 0
    for increment in range(0,3):
        index_number = index_number + 1
        file_name_iterations = "ibiza" + str(index_number) + ".txt"
        file_address = "Test_Folder/" + file_name_iterations
        with open (file_address, "r", encoding="utf-8-sig") as f:
            string = f.read()
        print(string)
        #print(file_address)
""" 
loop_through_folders()

