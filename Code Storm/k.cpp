#include <iostream>
#include <utility>
#include <vector>
using namespace std;

void dfs(int witch, vector<vector<int>> &graph, vector<bool> &visited) {
  visited[witch] = true;
  for (int neighbor : graph[witch]) {
    if (!visited[neighbor]) {
      dfs(neighbor, graph, visited);
    }
  }
}

int main() {
  int numWitches = 0, numConnections = 0;
  cin >> numWitches >> numConnections;

  vector<vector<int>> graph(numWitches + 1);

  for (int i = 0; i < numConnections; i++) {
    int firstWitch, secondWithch;
    cin >> firstWitch >> secondWithch;
    graph[firstWitch].push_back(secondWithch);
    graph[secondWithch].push_back(firstWitch);
  }

  vector<bool> visited(numWitches + 1, false);
  int components = 0;

  for (int i = 1; i <= numWitches; i++) {
    if (!visited[i]) {
      components++;
      dfs(i, graph, visited);
    }
  }

  cout << components;
  return 0;
}
