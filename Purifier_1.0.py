def open_files_in_sequence():
    number_of_year = 17
    number_of_month = 00
    number_of_day = 00
    folder_address_prefix = "Test_Data_Folder/"
    names_of_cities_to_iterate = ["Ibiza", "Miami", "Venice"]
    number_of_cities = len(names_of_cities_to_iterate)
    
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
                folder_address = folder_address_prefix + folder_address_builder_pt_I + "/" + folder_address_builder_pt_II + "/" + folder_address_builder_pt_III
                
                for city_iteration_index_number in range(0, number_of_cities):
                    city = names_of_cities_to_iterate[city_iteration_index_number]
                    file_name = folder_address + "/" + city + ".csv"    
                    try:
                        if(open (file_name, "r", encoding="utf-8-sig")):
                            extract_raw_data_from_files(file_name)                            
                    except:
                        pass
                        
                    
                
def extract_raw_data_from_files(file_name):
    with open(file_name,"r") as file_data:
        raw_file_data = file_data.read()
    identify_valuable_file_data(raw_file_data)

def identify_valuable_file_data(raw_file_data):
    #Find hostel name
    start_of_name_search_term = "ShowAll=1"
    end_of_name_search_term = "https://"
    length_of_start_search_term =len(start_of_name_search_term)
    length_of_end_search_term =len(end_of_name_search_term)
    starting_place_counter = 0
    ending_place_counter = 125
    for i in range(0,len(raw_file_data)):
        start_place =  raw_file_data.index(start_of_name_search_term, starting_place_counter) + 12
        end_place = raw_file_data.index(end_of_name_search_term, ending_place_counter) - 3
        #length_of_name = end_place - start_place
        name = raw_file_data[start_place:end_place]
        print("The name of the hostel is: "  + name)
        print(start_place)
        print(end_place)
        print(ending_place_counter)
        starting_place_counter = start_place + length_of_start_search_term
        ending_place_counter = start_place + 300




open_files_in_sequence()


