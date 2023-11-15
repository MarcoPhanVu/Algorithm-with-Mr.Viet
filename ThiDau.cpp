#include <iostream>
#include <string>
// #include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int bestSchedule(vector <int> dateList, vector <int> dateValue, int minRestRange) {
    // int result = 0, totalDate = dateList.size();
    vector <int> bestSolution(totalDate);
    
    bestSolution[0] = dateList[0];

    for (int i = 1; i < totalDate; i++) {
        for (int j = i-1; j >= 0; j--) { // Trace from the newest day
            if (dateList[i] - dateList[j] >= minRestRange) {
                bestSolution[i] = max(bestSolution[i-1], bestSolution[j] + dateValue[i]);
                // break; // Shorten the algorithm, prune the remaining operations
            } else {
                bestSolution[i] = max(bestSolution[i-1], dateValue[i]);
            }
        }
    }
    
    return bestSolution[totalDate - 1];
}

int main() {
    int dateAmount, minRestRange;
    cin >> dateAmount >> minRestRange;
    
    vector <int> dateList(dateAmount), dateValue(dateAmount);

    for (int i = 0; i < dateAmount; i++) {
        cin >> dateList[i];
    }

    for (int i = 0; i < dateAmount; i++) {
        cin >> dateValue[i];
    }

    
    int result = bestSchedule(dateList, dateValue, minRestRange);
    cout << result << "\n";

    return 0;
}