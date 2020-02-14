#include <iostream>
#include "automat.h"

using std::cout;
using std::cin;
using std::endl;

int main(int argc, char* argv[])
{
    std::vector<char> alph = {'a', 'b'};
    std::vector<std::vector<int>> state_transitions = {{0, 0},{1, 2}, {0, 2}};
    std::vector<int> accept = {2};
    int start = 1;
    Automat a(alph, state_transitions,start, accept);
    if(a.validate("aabaaabbbbbbbb"))
    {
        cout << "A gép elfogadta a sztringet." <<endl;
    }
    else
    {
        cout << "A gép nem fogadta el a sztringet." <<endl;
    }
    
    cout << "A szöveg beolvasása után a gép a(z)" << a.getState() << ". állapotba került." << endl;

    return 0;
}