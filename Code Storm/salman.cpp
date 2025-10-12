#include <iostream>
using namespace std;
int main() {
  int n = 0, even = 0, odd = 0;
  cin >> n;
  int numbers[n];

  for (int i = 0; i < n; i++) {
    cin >> numbers[i];
    if (numbers[i] % 2 == 0) {
      even += numbers[i];
    } else {
      odd += numbers[i];
    }
  }

  cout << abs(even - odd);

  return 0;
}
