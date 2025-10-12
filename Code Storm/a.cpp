#include <iostream>
using namespace std;

int main() {
  int n = 0;
  cin >> n;

  int plants[n];
  int good = 0, bad = 0, noMatter = 0;

  for (int i = 0; i < n; i++) {
    cin >> plants[i];
    if (plants[i] > 0) {
      good++;
    } else if (plants[i] < 0) {
      bad++;
    } else if (plants[i] == 0) {
      noMatter++;
    }
  }

  cout << good << ' ' << bad << ' ' << noMatter;

  return 0;
}
