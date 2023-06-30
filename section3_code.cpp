#include <iostream>
#include <cstdlib>
#include <climits>
#include <algorithm>

using namespace :: std;

int main() {
    int a[100];
    int result[2];

    std::cout << "Enter integers separated by one space (press enter to finish): ";

    string input;
    getline(cin, input);

    size_t pos = 0;
    int size = 0;

    while ((pos = input.find(' ')) != string::npos) {
        a[size++] = stoi(input.substr(0, pos));
        input.erase(0, pos + 1);
    }

    if (!input.empty()) {
        a[size++] = stoi(input);
    }

    sort(a, a + size);

    if (a[0] < 0) {
        if (a[size - 1] <= 0) {
            result[0] = a[size - 2];
            result[1] = a[size - 1];
        }

        else {
            int minsum = INT_MAX;
            int absdiff = INT_MAX;

            for (int i = 0; i < size; i++) {
                for (int j = i + 1; j < size; j++) {

                    int diff = abs(abs(a[i]) - abs(a[j]));
                    int sum = abs(a[i] + a[j]);

                    if (minsum > sum || (sum == minsum && diff < absdiff)) {
                        minsum = sum;
                        absdiff = diff;

                        result[0] = a[i];
                        result[1] = a[j];
                    }
                }
            }
        }
    }

    else {
        result[0] = a[0];
        result[1] = a[1];
    }

    std::cout << "Result: [" << result[0] << "," << result[1] << "]" << endl;
}