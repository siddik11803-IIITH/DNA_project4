while(1):
    input_string = input("mysql> ")
    data_array = {}
    if(input_string == "quit" or input_string == "exit"):
        break
    simpler_string = input_string.split(' ')
    if(simpler_string[0].upper() == "UPDATE"):
        print("Update")    
        # Write code for updating
    elif(simpler_string[0].lower() == "add"):
        print("Add")
        #write code for adding
    elif(simpler_string[0].lower() == "remove"):
        print("Delete")
        #write code for deleting
    elif(simpler_string[0].lower() == "getmatchdata"):
        print("Get match data")
        # write the code for retreiving match data
    
