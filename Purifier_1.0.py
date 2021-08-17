def loop_through_folders():
    number_of_year = 2017
    number_of_month = 00
    number_of_day = 00
    
    for iterate_years in range(0,2):
        number_of_year = number_of_year + 1
        number_of_month = 00
        
        for iterate_months in range(0, 12):
            number_of_month = number_of_month + 1
            file_name_with_month_and_year = str(number_of_month)+"."+str(number_of_year)
            filled_file_name_with_month_and_year =  file_name_with_month_and_year.zfill(7)
            number_of_day = 00

            for iterate_days in range(0,31):
                number_of_day = number_of_day + 1
                file_name_with_day_month_and_year = str(number_of_day)+"."+filled_file_name_with_month_and_year
                filled_file_name_with_day_month_and_year = file_name_with_day_month_and_year.zfill(10)

                print(filled_file_name_with_day_month_and_year)
    
    #loop_through_files(file_name)

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


