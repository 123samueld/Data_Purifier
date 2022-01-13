import os
import os.path

def open_files_in_sequence():
    number_of_year = 18
    number_of_month = 00
    number_of_day = 00
    folder_address_prefix = "Test_Data_Folder/"
    names_of_cities_to_iterate = [
        "bangkok",
        "granada",
        "hong_kong",
        "ibiza",
        "istanbul",
        "london",
        "melbourne",
        "miami",
        "naples",
        "paris",
        "prague",
        "rio_de_janeiro",
        "rome",
        "sydney",
        "toyko", 
        "venice"]
    number_of_cities = len(names_of_cities_to_iterate)
    for iterate_through_years in range(0,1):
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
                            extract_raw_data_from_files(file_name, city)                           
                    except:
                        pass
                        
                    
                
def extract_raw_data_from_files(file_name, city):
    city = city
    with open(file_name,"r") as file_data:
        raw_file_data = file_data.read()
    identify_column_names_and_data_blocks(raw_file_data, city)

def identify_column_names_and_data_blocks(raw_file_data, city):
    city = city
    data_blocks = raw_file_data.split('","')
    column_names = data_blocks[0].split(',')
    correct_column_order(column_names, data_blocks, city)

def correct_column_order(column_names, data_blocks, city):
    city = city
    data_blocks = data_blocks
    for l in range(0, len(data_blocks)):
        hostel_name_column_index = 2
        if column_names[4] == "rAy_ting":
            rating_column_index = 4
        else:
            if column_names[5] == "rAy_ting":
                rating_column_index = 5
                room_column_index = 7
                dorm_column_index = 6
            else: 
                if column_names[7] == "rAy_ting":
                    rating_column_index = 7
                    room_column_index = 6
                    dorm_column_index = 5           
    save_data_into_new_files_and_folders(city, data_blocks, hostel_name_column_index, rating_column_index, room_column_index, dorm_column_index)

def save_data_into_new_files_and_folders(city, data_blocks, hostel_name_column_index, rating_column_index, room_column_index, dorm_column_index):
    city = city
    purified_data = []
    loop_step_counter = 0
    for k in range(0, len(data_blocks)):
        if (loop_step_counter-1) % 8 == 0:
            purified_data.append(data_blocks[hostel_name_column_index+loop_step_counter-1])
            purified_data.append(data_blocks[rating_column_index+loop_step_counter-1])
            purified_data.append(data_blocks[room_column_index+loop_step_counter-1])
            purified_data.append(data_blocks[dorm_column_index+loop_step_counter-1])
        loop_step_counter += 1
    print(city)
    print(purified_data)


open_files_in_sequence()


