#include "automat.h"

Automat::Automat()
{

}

Automat::Automat(/*std::vector<int> states, */std::vector<char> alphabet, std::vector<std::vector<int>> state_transitions, int start_state, std::vector<int> accepting_states)
{
    //this->states = states;
    this->alphabet = alphabet;
    this->state_transitions = state_transitions;
    this->start_state = this->state = start_state;
    this->accepting_states = accepting_states;
}

bool Automat::validate(std::string s)
{
    state = start_state;
    for(int i = 0; i < s.length(); i++)
    {
        try
        {
            int alph = findAlph(s[i]);
            state = state_transitions[state][alph];
            if(state == 0)
            {
                return false;
            }
        }
        catch(const std::string e)
        {
            return false;
        }
        
    }
    return isInAcceptingState();
}

int Automat::findAlph(char c)
{
    for(int i = 0; i < alphabet.size(); i++)
    {
        if(alphabet[i] == c)
        {
            return i;
        }
    }
    throw std::string("Item Not Found In Vector.");
}

int Automat::getState() const
{
    return this->state;
}

bool Automat::isInAcceptingState()
{
    for (int i = 0; i < accepting_states.size(); i++)
    {
        if(accepting_states[i] == state)
        {
            return true;
        }
    }
    return false;
}