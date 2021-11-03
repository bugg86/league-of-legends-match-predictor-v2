import controller as Controller
import model as Model



name = Controller.get_user_input_name()

if (input('Do you want to generate summoner json data? y/n : ')) == 'y' :
    Controller.generate_all_summoner_json(name)

if (input("Do you want to generate summoner's live match data? y/n : ")) == 'y' :
    Controller.generate_live_match_json(name)

if (input('Do you want to generate entry for submission to ML model? y/n : ')) == 'y' :
    Controller.generate_live_match_entry_for_submission(name)

# end = input("How many matches: ")
# Controller.generate_match_list(name, 0, end)
# Controller.generate_matches_json(name)