#include <bits/stdc++.h>
#define int long long

using namespace std;

/*
https://dmoj.ca/problem/ccc25s4
Interesting graph problem
First observe that unlike normal Dijkstra's
you cannot find the shortest path to a node
by looking at the previous shortest path's
to its neighbors.

So to find the shortest path to a node:
1. Look at all it's neighbors
2. Find all possible edges you possibly could've gotten to that neighbor
3. Find the shortest path ending at the edge in step 2, and compare

This can be done with a Dijkstra based on the edges, instead of the nodes
I labeled the edges 1, 2, ... M
And to make things easier, I added 1 new edge and 1 new node
0 1 0 (An edge from node 0 to node 1 with weight 0)
*/

signed main() {
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<tuple<int, int, int>> adj_list [n + 1];
    //adj_list[u] = (v, w, i)
    adj_list[1].push_back(make_tuple(0, 0, 0));

    vector<tuple<int, int, int>> edges;
    edges.push_back(make_tuple(0, 1, 0));
    //edges[i] = (ai, bi, wi)

    vector<int> options;
    // The possible ending edges to reach node N

    for (int i = 1; i < m + 1; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        adj_list[a].push_back(make_tuple(b, c, i));
        adj_list[b].push_back(make_tuple(a, c, i));

        edges.push_back(make_tuple(a, b, c));


        if (a == n || b == n) {
            options.push_back(i);
        }
    }
    int dist [m + 1];
    // Define dist[i] = min cost found so far such that
    // i is the last road

    for (int i = 0; i < m + 1; i++) {
            dist[i] = LONG_LONG_MAX;
    }

    // Base Case
    dist[0] = 0;

    priority_queue<tuple<int, int, int>> heap;
    heap.push(make_tuple(0, 1, 0));
    //Running cost, current node, index of previous edge

    while (!heap.empty()) {
        int cost, node, prev;
        cost = -1 * (get<0>(heap.top()));
        node = get<1>(heap.top());
        prev = get<2>(heap.top());
        heap.pop();

        int val = get<2>(edges[prev]);

        if (cost > dist[prev]) {
            continue;
        }

        for (auto e : adj_list[node]) {
            int v, c, i;
            v = get<0>(e);
            c = get<1>(e);
            i = get<2>(e);

            if (cost + abs(val - c) < dist[i]) {
                dist[i] = cost + abs(val - c);
                heap.push(make_tuple(-1 * (cost + abs(val - c)), v, i));
            }

        }
    }
    int ans = LONG_LONG_MAX;

    for (int i : options) {
        if (dist[i] < ans) {
            ans = dist[i];
        }
    }
    cout << ans;
    return 0;
}
