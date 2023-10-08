#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        vector<int> sequence(n);
        for (int i = 0; i < n; ++i) {
            cin >> sequence[i];
        }
        
        long long total_sum = 0;
        long long current_max = sequence[0];
        bool is_positive = current_max > 0;
        
        for (int i = 0; i < n; ++i) {
            int num = sequence[i];
            
            if (is_positive == (num > 0)) {
                current_max = max(current_max, (long long)num);
            } else {
                total_sum += current_max;
                current_max = (long long)num;
                is_positive = (num > 0);
            }
        }
        
        total_sum += current_max;
        cout << total_sum << endl;
    }
    
    return 0;
}
