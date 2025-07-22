
/*
https://dmoj.ca/problem/ccc09s5
Alright problem in my opinion, mainly did it for some geometry practice
Spent 20 minutes trying to find out what's wrong with my code.
Lesson learned: Don't always define int long long
*/

#include<bits/stdc++.h>
// #define int long long
using namespace std;

signed main() {
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n, m, k;
    cin >> n >> m >> k;

    int diff[n][m + 1];
    for (int i = 0; i < n; i++) fill(diff[i], diff[i] + m + 1, 0);

    auto dist = [&](int r, int val) {
        return (int) floor(sqrt(r * r - val * val));
    };

    for (int _ = 0; _ < k; _++) {
        int x, y, r, b;
        cin >> x >> y >> r >> b;

        y = n - y + 1;
        x--;
        y--;

        swap(x, y);

        for (int i = x - r; i < x + r + 1; i++) {
            if (i < 0 or i >= n) continue;

            auto d = dist(r, (abs(i - x)));

            assert (y - d < m);
            assert (y + d + 1 >= 0);
            diff[i][max(0, y - d)] += b;
            diff[i][min(y + d + 1, m)] -= b;

        }
    }

    int grid[n][m];
    for (int i = 0; i < n; i++) fill(grid[i], grid[i] + m, 0);

    for (int i = 0; i < n; i++) {
        grid[i][0] = diff[i][0];

        for (int j = 1; j < m; j++) grid[i][j] = grid[i][j - 1] + diff[i][j];
    }

    int best = 0;
    int tot = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) best = max(best, grid[i][j]);
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == best) tot++;
        }
    }

    cout << best << endl << tot << endl;

    return 0;
}
