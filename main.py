def take_data(question, flag):
    x = input(question)
    if(x == "" and flag == "p"):
        return "NULL"
    else:
        return x
# if the flag is p, then it means that it cannot be null, hence to denote an error, we put NULL

def add_new_ball():
    dict = {}
    dict['ball_id'] = take_data("Ball ID: ", "p")
    dict['match_id'] =take_data("Match ID: ", "p")
    dict['innings_id'] = take_data("Innings ID: ", "p")
    dict['day'] = take_data("Day of the Match: (Only for tests) ", "n")
    dict['batting_team_id'] = take_data("Batting Team ID: ", "p")
    dict['bowling_team_id'] = take_data("Bowling Team ID: ", "p")
    dict['over_number'] = take_data("Number of the over: ", "p")
    dict['ball_no_over'] = take_data("No. of ball in the over: ", "p")
    dict['batter_id'] = take_data("ID of the batsman: ", "p")
    dict['bowler_id'] = take_data("ID of the bowler: ", "p")
    dict['runs_batter'] = take_data("Runs Scored: ", "p")
    dict['extras'] = take_data("Extra Runs: ", "p")
    dict['wicket'] = {}
    dict["wicket"]['yes_no'] = take_data("Wicket(Y/N): ", "p")
    dict["wicket"]['type'] = take_data("Type Of wicket: ", "p")
    dict["wicket"]['catcher_id'] = take_data("Catcher ID:(Only for catch outs): ", "n")
    #Now we have the dictionary with all the data in it. We just have to write SQL queries

def add_new_ground():
    dict = {}
    dict['ground_id'] = take_data("Ground ID: ", "p")
    dict['name'] = take_data("Name of the Ground: ", "p")
    dict['place'] = take_data("City/Town of the Ground: ", "p")
    dict['owner'] = take_data("Owner of the ground: ", "p")
    dict['bowler_ends'] = {}
    dict["bowler_ends"]['end_1'] = take_data("Bowler End 1: ", "p")
    dict["bowler_ends"]['end_2'] = take_data("Bowler End 2: ", "p")
    
def mod_ball():
    p_key = input("Ball ID: ")
    # We have to first find the thing about to be modeified with it's and 


def mod_ground():
    p_key = input("Ground ID: ")
    print("Match data update")



def mod_player():
    p_key = input("Player ID: ")
    print("Modify player data")



while(1):
    input_string = input('\033[1m'+ '\033[4m' +'\033[94m' +  "mysql>" + '\033[0m' + " ")
    
    if(input_string == "quit" or input_string == "exit"):
        break
    simpler_string = input_string.split(' ')
    if(simpler_string[0].upper() == "UPDATE"):
        
        # Write code for updating
        # for updating the status of runs on a ball
    
            if(simpler_string[1].lower() == "balls"):
                mod_ball()
            # write code for updating the match data
            if(simpler_string[1].lower() == "match"):
            #write code for updating the player data
                mod_ground()
            if(simpler_string[1].lower() == "player"):
                mod_player()
        
    elif(simpler_string[0].lower() == "add"):
        
        #section for adding a new ball data
            if(simpler_string[1].lower() == "ball"):
                add_new_ball()
            # section for a new ground
            if(simpler_string[1].lower() == "ground"):
                add_new_ground()
    elif(simpler_string[0].lower() == "remove" or simpler_string[0].lower() == "delete"):
        print("Delete")
        #write code for deleting the data of a ball
    elif(simpler_string[0].lower() == "getmatchdata"):
        print("Get match data")
        # write the code for retreiving match data
    elif(simpler_string[0].lower() == "getteamdata"):
        #write code for getting team data
        print("Get Team Data")
    elif(simpler_string[0].lower() == "getplayerdata"):
        print("Get player Data")
        # We have to write code for getting player data and be able to handle the conditions
    
    
