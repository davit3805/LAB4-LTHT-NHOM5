#include <iostream>
using namespace std;

int phase4(int a1, int a2, int a3) {
    int result;
    int v4;

    v4 = (a3 - a2) / 2 + a2;

    if (v4 <= a1) {
        if (v4 >= a1) {return 0; }
        else { result = 2*phase4(a1, v4+1,a3) + 1; }
    }
    else { result = 2*phase4(a1, a2, v4-1); }
    
    return result;
}

int main() {
    for (int v3 = 0; v3 <= 14; v3++) {
        cout << v3 << " " << phase4(v3, 0, 14) << endl;
    }
    return 0;
}
