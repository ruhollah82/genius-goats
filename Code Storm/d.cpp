#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B;
ll total_count = 0;

void dfs(ll num, ll prod) {
  if (num > B)
    return;
  if (prod > B)
    return;

  if (num >= A)
    total_count++;

  for (int d = 1; d <= 9; d++) {
    ll new_num = num * 10 + d;
    ll new_prod = prod * d;
    if (new_num > B)
      continue;
    if (new_prod > B)
      continue;
    dfs(new_num, new_prod);
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> A >> B;

  dfs(0, 1);

  cout << total_count << "\n";
  return 0;
}
