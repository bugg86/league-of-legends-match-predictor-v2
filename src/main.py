import controller as Controller
import model as Model
import time



name = Controller.get_user_input_name()

if (input('Do you want to generate summoner json data? y/n : ')) == 'y' :
    start = time.time()
    Controller.generate_all_summoner_json(name)
    end = time.time()
    print('Runtime is {:.3f}s'.format(end - start))

if (input("Do you want to generate summoner's live match data? y/n : ")) == 'y' :
    start = time.time()
    Controller.generate_live_match_json(name)
    end = time.time()
    print('Runtime is {:.3f}s'.format(end - start))

if (input('Do you want to generate entry for submission to ML model? y/n : ')) == 'y' :
    start = time.time()
    Controller.generate_live_match_entry_for_submission(name)
    end = time.time()
    print('Runtime is {:.3f}s'.format(end - start))

if (input("Do you want to generate a summoner's match history? y/n : ")) == 'y' :
    endIndex = input("How many matches: ")
    startIndex = input("Starting index: ")
    start = time.time()
    Controller.generate_match_list(name, startIndex, endIndex)
    end = time.time()
    print('Runtime is {:.3f}s'.format(end - start))
    
    if (input("Do you want to generate the json files for the matches? y/n : ")) == 'y' :
        start = time.time()
        Controller.generate_matches_json(name)
        end = time.time()
        print('Runtime is {:.3f}s'.format(end - start))
        
if (input("Do you want to add match data to the dataset for the ML model? y/n : ")) == 'y' :
    start = time.time()
    Controller.generate_match_dataset(name)
    end= time.time()
    print('Runtime is {:.3f}s'.format(end - start))