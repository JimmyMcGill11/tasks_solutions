#include <iostream>

using namespace std;

int main() {
  int numOfDays = 30;
  bool checkDays = true;
  cout << "Do You Want To Enter The Steps of The Month or a Specific Days?"
  << endl << "Answer With:\n[1 => Month]\n[0 => Days From Your Choice]" << endl;
  cin >> checkDays;

  if (checkDays == false) {
    cout << "Enter Your Number of Days: ";
    cin >> numOfDays;
  }
  int dailySteps[numOfDays];

  cout << "Now Enter Your Step per Day:" << endl;
  for (int i = 0; i < numOfDays; i++) {
    cin >> dailySteps[i];
  }

  // Lowest Steps per Day.
  int lowestSteps = INT_MAX;
  for (int i = 0; i < numOfDays; i++) {
    if (dailySteps[i] < lowestSteps) lowestSteps = dailySteps[i];
  }

  // Highest Steps per Day.
  int highestSteps = INT_MIN;
  for (int i = 0; i < numOfDays; i++) {
    if (dailySteps[i] > highestSteps) highestSteps = dailySteps[i];
  }

  // Average Daily Steps.
  double averge = 0;
  for (int step : dailySteps) averge += step;
  averge /= numOfDays;

  // Sorting Steps Descending Order.
  int temp;
  for (int i = 0; i < numOfDays; i++) {
    for (int j = 0; j < numOfDays; j++) {
      if (dailySteps[j] < dailySteps[j + 1]) {
        temp = dailySteps[j];
        dailySteps[j] = dailySteps[j + 1];
        dailySteps[j + 1] = temp;
      }
    }
  }

  // Statistics Steps
  cout << "-----------------------------------------------------------------------------------------------------------------------------------------" << endl
  << "Here is Your Statistics for " << numOfDays << " Day:-" << endl
  << "\nHighest Step Count: " << highestSteps << endl
  << "Lowest Step Count: " << lowestSteps << endl;

  // For Limit Averge's Float
  printf("\nAverage Daily Steps: %.2f Step per Day\n", averge);

  cout << "\nSteps in Descending Order: [ ";
  for (int i : dailySteps) {
    cout << i << " ";
  }
  cout << "]" << endl;
  cout << "-----------------------------------------------------------------------------------------------------------------------------------------" << endl;
}
