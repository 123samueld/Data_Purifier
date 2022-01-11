import os
import os.path
from typing import Text



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
    identify_data_block_positions(raw_file_data)

def identify_data_block_positions(raw_file_data):
    comma = ","
    comma_position_counter = 0
    comma_position_list = []
    data_blocks = raw_file_data.split('", ')
    """
    #Build comma position list
    for i in range(0, len(raw_file_data)):
        if raw_file_data[i] == comma:
            comma_position_list.append(comma_position_counter)  

        comma_position_counter = comma_position_counter + 1
    
    #create_data_block_list(comma_position_list, raw_file_data)
"""

def create_data_block_list(comma_position_list, raw_file_data):
    data_block_list = []
    for j in range(0,len(comma_position_list)):
        if j+1 == len(comma_position_list):
            start = comma_position_list[j-1]   
            end = comma_position_list[j]
            break
        else:
            start = comma_position_list[j]
            end = comma_position_list[j+1]
        data_block = raw_file_data[start+1:end]
        data_block_list.append(data_block)

    pull_useful_data_out_of_blocks(data_block_list)

def pull_useful_data_out_of_blocks(data_block_list):
    data_block_index_for_name = 1
    data_block_index_for_rating = 3
    data_block_index_for_alternating = 4
    data_block_index_for_room = 0
    data_block_index_for_dorm = 0
    loop_step_counter = 0
    for k in range(0, len(data_block_list)):
        if (loop_step_counter-1) % 8 == 0:
            print(data_block_list[loop_step_counter])
            print(data_block_list[loop_step_counter+2])
            if data_block_list[loop_step_counter+3][1:8] == "Selling":
                print(data_block_list[loop_step_counter+5])
                print(data_block_list[loop_step_counter+6])
                print(data_block_list[loop_step_counter+7])
                print("Break 5")
            else:
                print(data_block_list[loop_step_counter+3])
                print(data_block_list[loop_step_counter+4])
                print("Break 4")

        loop_step_counter += 1
        


open_files_in_sequence()


