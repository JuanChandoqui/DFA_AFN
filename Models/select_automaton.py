from Models.read_text_file import ReadTextFile
from Models.Automaton import Automaton
from string import punctuation

general_dict = dict()

class SelectAutomaton():
    def read_text_file(self, file):
        global general_dict
        content_text_file = ReadTextFile(file)
        notations = content_text_file.get_values_from_text_file()
        general_dict = notations
        return notations

    def has_symbols(self, text):
        return any(c in punctuation for c in text) 
    
    def automaton_function(self,text):       
        notations = general_dict 
        alphabet = notations['S']
        states = notations['Q']
        initial_state = notations['q0']
        final_states = notations['F']
        list_transition = notations['D']
        if(len(text) > 0 and self.has_symbols(text) == False):
            d = Automaton(states, alphabet, list_transition, initial_state, final_states)
            return d.run_with_input_list(text)
        else:
            return False      