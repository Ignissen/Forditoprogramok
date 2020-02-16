#include "domol_automat.h"

domol_automat::domol_automat() : Automat()
{

}

domol_automat::domol_automat(std::vector<std::string> alph, std::vector<std::vector<int>> st_transition, int start_st, std::vector<int> acc_sts, std::vector<bool> backup, std::vector<bool> read) : Automat({'c'}, st_transition, start_st, acc_sts)
{
    this->alphabet = alph;
    this->backup = backup;
    this->read = read;
}

bool domol_automat::validate(std::string s)
{
    state = start_state;
    for(int i = 0; i < s.length();)
    {
        try
        {
            int alph;
            if(backup[state])
            {
                i--;
            }
            if(read[state])
            {
                std::string Type;
                if(isdigit(s[i]))
                {
                    Type = "number";
                }
                else
                {
                    switch(s[i])
                    {
                        case '{':
                            Type = "{";
                            break;
                        case '}':
                            Type = "}";
                            break;
                        case '(':
                            Type = "(";
                            break;
                        case ')':
                            Type = ")";
                            break;
                        case '*':
                            Type = "*";
                            break;
                        case ';':
                            Type = ";";
                            break;
                        case '=':
                            Type = "=";
                            break;
                        case '<':
                            Type = "<";
                            break;
                        case '>':
                            Type = ">";
                            break;
                        case ' ':
                            Type = "space";
                            break;
                        case '$':
                            Type = "$";
                            break;
                        default:
                            if(s[i] == 'a' || s[i] == 'á' ||  s[i] == 'b' ||  s[i] == 'c' ||  s[i] == 'd' ||  s[i] == 'e' || s[i] == 'é' ||  s[i] == 'f' ||  s[i] == 'g' ||  s[i] == 'h' ||  s[i] == 'i' || s[i] == 'í' || s[i] == 'j' ||  s[i] == 'k' ||  s[i] == 'l' ||  s[i] == 'm' ||  s[i] == 'n' ||  s[i] == 'o' || s[i] == 'ó' || s[i] == 'ö' || s[i] == 'ő' || s[i] == 'p' ||  s[i] == 'q' ||  s[i] == 'r' ||  s[i] == 's' ||  s[i] == 't' ||  s[i] == 'u' || s[i] == 'ú' || s[i] == 'ü' || s[i] == 'ű' ||  s[i] == 'v' ||  s[i] == 'w' ||  s[i] == 'x' ||  s[i] == 'y' ||  s[i] == 'z' ||  s[i] == 'A' || s[i] == 'Á' || s[i] == 'B' ||  s[i] == 'C' ||  s[i] == 'D' ||  s[i] == 'E' || s[i] == 'É' || s[i] == 'F' ||  s[i] == 'G' ||  s[i] == 'H' ||  s[i] == 'I' || s[i] == 'Í' ||  s[i] == 'J' ||  s[i] == 'K' ||  s[i] == 'L' ||  s[i] == 'M' ||  s[i] == 'N' ||  s[i] == 'O' || s[i] == 'Ó' || s[i] == 'Ö' || s[i] == 'Ő' || s[i] == 'P' ||  s[i] == 'Q' ||  s[i] == 'R' ||  s[i] == 'S' ||  s[i] == 'T' ||  s[i] == 'U' || s[i] == 'Ú' || s[i] == 'Ü' || s[i] == 'Ű' || s[i] == 'V' ||  s[i] == 'W' ||  s[i] == 'X' ||  s[i] == 'Y' ||  s[i] == 'Z')
                            {
                                Type = "letter";
                            }
                            else
                                Type = "other";
                    }
                }
                alph = findAlph(Type);
            }
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

int domol_automat::findAlph(std::string s)
{
    for(int i = 0; i < alphabet.size(); i++)
    {
        if(alphabet[i] == s)
        {
            return i;
        }
    }
    throw std::string("Item Not Found In Vector.");
}