#include <iostream>
#include <string>
// #include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> knapSack(vector <int> itemValue, vector <int> itemWeight, int maxWeight) {
    vector <vector <int>> bestSolution(itemValue.size() + 1, vector <int> (maxWeight + 1, 0));
    
    vector <int> trackVec(itemValue.size() + 1, 0);
    
    // init bestSolutionTable
    // for (int i = 0; i <= maxWeight; i++) {
    //     vector <int> tempVec(maxWeight + 1, 0); // Size = maxWeight+1, values = 0
    
    //     bestSolution.push_back(tempVec);
    // }
    
    // DP
    // All start from 1
    for (int i = 1; i <= itemValue.size(); i++) {
        for (int j = 1; j < maxWeight; j++) {
            if (itemWeight[i] <= j) {
                bestSolution[i][j] = max(   bestSolution[i-1][j],
                                            bestSolution[i-1][j - itemWeight[i]] + itemValue[i]
                                        );
            } else {
                bestSolution[i][j] = bestSolution[i - 1][j];
            }
        }
    }
    
    
    // Tracking Solution
    // int tempWeightCount = maxWeight;
    for (int i = itemValue.size() - 1, tempWeightCount = maxWeight; i > 0; i--) { // I > 0???
        if (bestSolution[i][tempWeightCount] != bestSolution[i-1][tempWeightCount]) {
            trackVec.push_back(i); // Position
            tempWeightCount -= itemWeight[i];
        }
        cout << "\ntrackVec[" << i << "]: \n";
    }
    
    return trackVec;
}

int main() {
    int amount, maxWeight;
    cin >> amount >> maxWeight;
    
    vector <int> itemValue(amount + 1), itemWeight(amount + 1); // + 1 because item count start from 1
    itemValue[0] = itemWeight[0] = 0;
    
    for (int i = 1; i <= amount; i++) {
        cin >> itemValue[i] >> itemWeight[i];
    }

    vector <int> result = knapSack(itemValue, itemWeight, maxWeight);

    cout << "\n\nResult";

    for (int i = 1; i <= result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << "\n\n";

    // for (int i = 0; i <= amount; i++) {
    //     cout << "itemValue[" << i << "]: " << itemValue[i] << "\n";
    //     cout << "itemWeight[" << i << "]: " << itemWeight[i] << "\n";
    // }
}