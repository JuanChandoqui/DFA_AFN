from Models.read_text_file import ReadTextFile
from Models.Automaton import Automaton

general_dict = dict()

class SelectAutomaton():
    def read_text_file(self, file):
        global general_dict
        content_text_file = ReadTextFile(file)
        notations = content_text_file.get_values_from_text_file()
        general_dict = notations
        print(notations)
        return notations
    
    def automaton_function(self,text):       
        notations = general_dict
        print(notations['S'])   
        alphabet = notations['S']
        states = notations['Q']
        initial_state = notations['q0']
        final_states = notations['F']
        list_transition = notations['D']
    
        d = Automaton(states, alphabet, list_transition, initial_state, final_states)
        return d.run_with_input_list(text)      