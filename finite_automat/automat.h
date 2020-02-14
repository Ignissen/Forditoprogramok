#include <vector>
#include <string>

class Automat
{
public:
    Automat();
    Automat(/*std::vector<int> states, */std::vector<char> alphabet, std::vector<std::vector<int>> state_transitions, int start_state, std::vector<int> accepting_states);

    bool validate(std::string);

    int getState() const;

private:
    int findAlph(char);
    bool isInAcceptingState();
    //std::vector<int> states;
    std::vector<char> alphabet;
    std::vector<std::vector<int>> state_transitions;
    int state;
    int start_state;
    std::vector<int> accepting_states;
};