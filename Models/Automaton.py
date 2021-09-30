class Automaton:
    current_state = None;
    keyslist = [];
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        self.generateKeys()

    def generateKeys(self):
        for i in range(len(self.transition_function)):
            self.keyslist.append((self.transition_function[i][0]))

    def search(self,state,input):
        valor = None
        for i in range(len(self.transition_function)):
            if (state == self.transition_function[i][0][0] and input == self.transition_function[i][0][1]):
                valor = self.transition_function[i][1]

        return valor

    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.keyslist):
            self.current_state = None
            return
        self.current_state = self.search(self.current_state, input_value)
        

    def in_accept_state(self):
        return self.current_state in self.accept_states
    
    def go_to_initial_state(self):
        self.current_state = self.start_state
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
        return self.in_accept_state()