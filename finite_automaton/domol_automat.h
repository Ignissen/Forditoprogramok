#include "automat.h"
#include <ctype.h>

class domol_automat : public Automat
{
public:
    domol_automat();
    domol_automat(std::vector<std::string> alphabet, std::vector<std::vector<int>> state_transitions, int start_state, std::vector<int> accepting_states, std::vector<bool> backup, std::vector<bool> read);

    bool validate(std::string);

private:
    int findAlph(std::string);

    std::vector<bool> backup;
    std::vector<bool> read;
    std::vector<std::string> alphabet;
};