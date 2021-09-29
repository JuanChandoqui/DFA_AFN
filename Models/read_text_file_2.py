class ReadTextFile2():

    def read_text_file(self):
        f = open('./DFN.txt', 'r', encoding='utf-8')
        values = f.readlines()
        return values
                
    def get_values_from_text_file(self):
        content_text_file = self.read_text_file()
        value_list = []
        list_transitions = []
        aux_list = []
        isDFA = True
        initial_pair_keys = False

        alphabet = ''
        states = ''
        initial_state = ''
        final_states = ''
        transitions = ''

        set_alphabet = set()
        set_states = set()
        list_initial_states = list() #<--- only for AFN
        set_final_states = set()
        tf = dict() #<---- table of transitions
        
        notation_dict = dict()

        i = 0
        j = 0
        concat_string = ''

        for index in content_text_file:
            value_list.append(index.splitlines(False)[0].replace(' ', ''))

        for index in value_list:
            if(index.startswith('S')):
                alphabet = index.split('=',1)[-1].replace(',', '').replace('{', '').replace('}','')
            elif (index.startswith('Q')):
                states = index.split('=',1)[-1]
            elif (index.startswith('q0')):
                initial_state = index.split('=',1)[-1]
            elif (index.startswith('F')):
                final_states = index.split('=',1)[-1]
            elif (index.startswith('D')):
                transitions = index.split('=',1)[-1]

        #----- get alphabet -----------------------------------
        for value in alphabet:
            set_alphabet.add(value)

        #----- get states -------------------------------------
        if(states[0].startswith('{')):
            while(states[i].endswith('}') != True):
                j = i
                while(states[j] != ',' and states[j] != '}'):
                    if(states[j] != '{'):
                        concat_string = concat_string + states[j]; 
                    j+=1
                i = j            
                set_states.add(concat_string)
                concat_string = ''
                if(i<len(states) - 1):         
                    i+=1

        i = 0
        j = 0
        
         #----- get initial states (If is a AFN) ---------------------------------
        if(initial_state[0].startswith('{')):
            initial_pair_keys = True
            while(initial_state[i].endswith('}') != True):
                j = i
                while(initial_state[j] != ',' and initial_state[j] != '}'):
                    if(initial_state[j] != '{'):
                        concat_string = concat_string + initial_state[j]; 
                    j+=1
                i = j            
                list_initial_states.append(concat_string)
                concat_string = ''
                if(i < len(initial_state) - 1):         
                    i+=1

        i = 0
        j = 0

        #----- get final states ----------------------------------------
        if(final_states[0].startswith('{')):
            while(final_states[i].endswith('}') != True):
                j = i
                while(final_states[j] != ',' and final_states[j] != '}'):
                    if(final_states[j] != '{'):
                        concat_string = concat_string + final_states[j]; 
                    j+=1
                i = j            
                set_final_states.add(concat_string)
                concat_string = ''
                if(i < len(final_states) - 1):         
                    i+=1
               
        i = 0
        j = 0

        start_transitions = False
        final_transition = False

        #----- get transitions ---------------------------------------------------------------------
        if(transitions[0].startswith('{')):
            while(i < len(transitions) and transitions[i].endswith('}') != True):            
                if(transitions[i] == '('):
                    aux_list.clear()       
                    start_transitions = True
                
                if(start_transitions):
                    j = i                    
                    while(j < len(transitions) and transitions[j] != ',' and transitions != ')'): 
                        if(transitions [j] != '(' and transitions [j] != ')' and transitions [j] != '}' and transitions [j] != '{'):
                            concat_string = concat_string + transitions[j]                      
                        j+=1
                        if(j < len(transitions) and (transitions[j] == ',' or transitions[j] == '}') and concat_string !=''):
                            aux_list.append(concat_string)
                            concat_string = ''
                        if(j < len(transitions) and transitions[j] == ')'):
                            final_transition = True

                    if(final_transition and len(aux_list) >= 3):
                        concatenate_tuples = tuple(aux_list)
                        list_transitions.append(concatenate_tuples)           
                    i = j                     
                i+=1
        
        new_list = []
        list_index = []
        for x in range(len(list_transitions)):
            if(len(list_transitions[x]) > 3):
                list_index.append(x)
                for y in range (len(list_transitions[x])):
                    print('Y', y, ': ', list_transitions[x][y])
                    if(y < 2):
                        new_list.append(list_transitions[x][y])
                    if(y >= 2):
                        new_list.append(list_transitions[x][y])
                        concatenate_tuples = tuple(new_list)
                        list_transitions.append(concatenate_tuples)
                        del new_list[-1]

        
        for z in list_index:
            del list_transitions[z]  #eliminate a item of list for index      
        print(list_transitions)

        #----- get table of transitions -----------------------------------------------
        for i in range (len(list_transitions)):
            tf[(list_transitions[i][0], list_transitions[i][1])] = list_transitions[i][2]         

            if(initial_pair_keys == False):
                notation_dict = {'S': set_alphabet, 'Q': set_states, 'q0': initial_state, 'F': set_final_states, 'D': tf, 'isDFA': initial_pair_keys}
            else:
                notation_dict = {'S': set_alphabet, 'Q': set_states, 'q0': list_initial_states, 'F': set_final_states, 'D': tf, 'isDFA': initial_pair_keys}

        return notation_dict

d = ReadTextFile2()
d.get_values_from_text_file()