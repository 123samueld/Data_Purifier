def loop_through_files():
    index_number = 0
    for incrament in range(0,3):
        index_number = index_number + 1
        file_name_iterations = "ibiza" + str(index_number) + ".txt"
        file_address = "Test_Folder/" + file_name_iterations
        #file_address = file_name_iterations

        with open (file_address, "r", encoding="utf-8-sig") as f:
            string = f.read()
        print(string)
        #print(file_address)

loop_through_files()

