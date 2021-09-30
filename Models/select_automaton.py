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
        initial_state = ''      
        notations = general_dict 
        alphabet = notations['S']
        states = notations['Q']
        initial_q0 = notations['q0']
        if(notations['isDFA'] != True):
            initial_state = initial_q0
        else:
            if(len(initial_q0) == 1):
                initial_state = initial_q0[0]
            elif(len(initial_q0) == 2):
                initial_state = initial_q0[0], initial_q0[1]
            elif(len(initial_q0) == 3):
                initial_state = initial_q0[0], initial_q0[1], initial_q0[2]

        final_states = notations['F']
        list_transition = notations['D']
        if(len(text) > 0 and self.has_symbols(text) == False):
            if(notations['isAFN'] != True and alphabet.__contains__('ε') != True):
                d = Automaton(states, alphabet, list_transition, initial_state, final_states)
                return d.run_with_input_list(text)
            elif (notations['isAFN'] == True):
                x = Automaton(states, alphabet, list_transition, initial_state, final_states)
                return  x.run_with_input_list(text)
            else:
                print('PROBABLEMENTE CONTIENE LA CADENA VACIA! (ε)')
                print('NO SE ACEPTA LA CADENA VACIA EN UN DFA')
                return False
        else:
            return False      