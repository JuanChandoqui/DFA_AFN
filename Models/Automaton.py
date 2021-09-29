class Automaton:
    current_state = None;
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]

    def in_accept_state(self):
        return self.current_state in self.accept_states
    
    def go_to_initial_state(self):
        self.current_state = self.start_state
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
        return self.in_accept_state()

# states = {'q0', 'q1', 'q2', 'q3', 'q4'}
# alphabet = {'a', 'b', 'c'}
# example = ['q0', 'q1']
# print(example[0])

# tf = dict();
# tf[('q0', 'a')] = 'q1'
# tf[('q0', 'a')] = 'q3'
# tf[('q1', 'c')] = 'q2'
# tf[('q2', 'c')] = 'q1'
# tf[('q3', 'b')] = 'q1'
# tf[('q3', 'b')] = 'q4'
# tf[('q4', 'c')] = 'q2'

# if(len(example) == 1):
#     start_state = example [0]
# elif(len(example) == 2):
#     start_state = example [0], example [1]

# accept_states = {'q2', 'q3'}
# print('TF: ', tf)

# d = Automaton(states, alphabet, tf, start_state, accept_states)

# inp_program = list('abc')

# print(d.run_with_input_list(inp_program))