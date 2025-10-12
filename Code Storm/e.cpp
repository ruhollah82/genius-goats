#include <bits/stdc++.h>
using namespace std;

int main() {
  const long long MOD = 1e9 + 7;
  int n;
  cin >> n;
  vector<vector<int>> g(n, vector<int>(n));
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) {
      cin >> g[i][j];
      if (g[i][j] == 0)
        g[i][j] = 1;
    }

  vector<vector<double>> l(n, vector<double>(n, 0.0));
  vector<vector<long long>> v(n, vector<long long>(n, 0));
  l[0][0] = log(g[0][0]);
  v[0][0] = g[0][0];

  for (int j = 1; j < n; j++) {
    l[0][j] = l[0][j - 1] + log(g[0][j]);
    v[0][j] = v[0][j - 1] * g[0][j] % MOD;
  }

  for (int i = 1; i < n; i++) {
    l[i][0] = l[i - 1][0] + log(g[i][0]);
    v[i][0] = v[i - 1][0] * g[i][0] % MOD;
  }

  for (int i = 1; i < n; i++) {
    for (int j = 1; j < n; j++) {
      if (l[i - 1][j] > l[i][j - 1]) {
        l[i][j] = l[i - 1][j] + log(g[i][j]);
        v[i][j] = v[i - 1][j] * g[i][j] % MOD;
      } else {
        l[i][j] = l[i][j - 1] + log(g[i][j]);
        v[i][j] = v[i][j - 1] * g[i][j] % MOD;
      }
    }
  }

  cout << v[n - 1][n - 1];
  return 0;
}
