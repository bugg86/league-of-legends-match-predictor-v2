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

# end = input("How many matches: ")
# Controller.generate_match_list(name, 0, end)
# Controller.generate_matches_json(name)