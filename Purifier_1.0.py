def open_files_in_sequence():
    number_of_year = 17
    number_of_month = 00
    number_of_day = 00
    folder_address_prefix = "Test_Data_Folder/"
    
    for iterate_through_years in range(0,2):
        number_of_year = number_of_year + 1
        number_of_month = 00
        folder_address_builder_pt_I = str(number_of_year)

        for iterate_through_months in range(0, 12):
            number_of_month = number_of_month + 1
            number_of_day = 00
            folder_address_builder_pt_II = str(number_of_month).zfill(2) + "." + folder_address_builder_pt_I

            for iterate_through_days in range(0,31):
                number_of_day = number_of_day + 1
                folder_address_builder_pt_III =  str(number_of_day).zfill(2) + "." + folder_address_builder_pt_II
                folder_address = folder_address_prefix + folder_address_builder_pt_I + "/" + folder_address_builder_pt_II + "/" + folder_address_builder_pt_III + "/ibiza.txt"
                
                try:
                    if(open (folder_address, "r", encoding="utf-8-sig")):
                        print("P" + folder_address)
                        print("True")
                except:
                    print("False")
                    print(folder_address)
                
    #find_valid_matches_for_suggested_file_names(file_name)
    
    #loop_through_files(file_name)

def find_valid_matches_for_suggested_file_names(file_name):
    #loop through folders and sub folders, 
    #when a match is found pass it forward 
    try:
        phrase = "31.12.2019" in file_name
        print(phrase)
    except:
        print("Not found")


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
generate_possible_names_of_files()


