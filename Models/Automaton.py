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


# states = {'q0', 'q1', 'q2'}
# alphabet = {'a', 'b'}

# tf = dict();
# tf[('q0', 'b')] = 'q1'
# tf[('q0', 'b')] = 'q2'
# tf[('q1', 'a')] = 'q2'
# tf[('q2', 'a')] = 'q2'
# tf[('q2', 'b')] = 'q2'
# start_state = 'q0'
# accept_states = {'q2'}
# print('TF: ', tf)

# d = Automaton(states, alphabet, tf, start_state, accept_states)

# inp_program = list('babab')

# print(d.run_with_input_list(inp_program))