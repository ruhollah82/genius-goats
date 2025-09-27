#include <bits/stdc++.h>
using namespace std;

struct point {
  int a;
  int b;
};

bool compare(point u, point v) { return (u.a - u.b > v.a - v.b); }

int main() {

  int x, y;
  vector<point> list;

  cin >> x >> y;
  for (int i = 0; i < x; i++) {
    point temp;
    cin >> temp.a >> temp.b;
    list.push_back(temp);
  }

  sort(list.begin(), list.end(), compare);

  int result = 0;
  for (int i = 0; i < x; i++) {
    if (i < y) {
      result += list[i].a;
    } else {
      result += list[i].b;
    }
  }
  cout << result;
}