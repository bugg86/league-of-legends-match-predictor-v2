import controller as Controller
import model as Model



name = Controller.get_user_input_name()

end = input("How many matches: ")

# Model.get_match_list(name, 0, end)

Controller.generate_match_list(name, 0, end)
Controller.generate_matches_json(name)