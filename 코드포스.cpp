#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main (int argc, char** argv){
    int test_case;
    int T = 10;

    for (test_case = 1; test_case <= T; ++test_case){
        int N;
        vector <int> L1;
        int result = 0;
        cin >> N;

        for (int i = 0; i < N; i++){
            int a;
            cin >> a;
            L1.push_back(a);
        }

        for (int i = 0; i < N; i++){
            int value = L1[i];
            if (value == 0){
                continue;
            }
            else{
                if (*max_element(L1.begin()+(i-2), L1.begin()+(i+3)) == value){
                    int large1 = *max_element(L1.begin() + (i-2), L1.begin() + i);
                    int large2 = *max_element(L1.begin() + (i+1), L1.begin() + (i+3));
                    int large = max(large1, large2);
                    result += value - large;
                }
            }
        }
        cout << "#" << test_case << result << endl;
    }
    return 0;
}