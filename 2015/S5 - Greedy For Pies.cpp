//https://dmoj.ca/problem/ccc15s5
//Main logic that really makes this problem easier is
//When we add one more pie in the original pile, we have a few choices:
  // Take this pie
  // Skip this pie
  // Add new pie and take it
  // Add new pie and don't take it, take the original pie
  // Add new pie and take it, don't take the original pie
// Implementation is a lot harder, but the logic above is very similar to Knapsack

#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main() {
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int a[n + 1];
    a[0] = 0;

    for (int i = 1; i < n + 1; i++) {
        cin >> a[i];
    }

    int m;
    cin >> m;
    int b[m + 1];
    b[0] = 0;

    for (int i = 1; i < m + 1; i++) {
        cin >> b[i];
    }
    sort(b, b + m + 1);

    int dp[n + 1][m + 2][m + 2][2];

    for (int i = 0; i < n + 1; i++) {
        for (int j = 0; j < m + 2; j++) {
            for (int k = 0; k < m + 2; k++) {
                dp[i][j][k][0] = LONG_LONG_MIN;
                dp[i][j][k][1] = LONG_LONG_MIN;
            }
        }
    }

    dp[0][0][m][1] = b[m];
    dp[0][0][m + 1][0] = 0;

    for (int j = 1; j < m + 1; j++) {
        for (int k = m + 1; k > m - j - 1; k--) {
            dp[0][j][k][1] = accumulate(b + k, b + m + 1, 0);

            if ((m + 1 - k) - j <= 0) {
                dp[0][j][k][0] = accumulate(b + k, b + m + 1, 0);
            }
        }
    }

    for (int i = 1; i < n + 1; i++) {
        dp[i][0][m + 1][1] = a[i] + dp[i - 1][0][m + 1][0];
        dp[i][0][m + 1][0] = max(dp[i - 1][0][m + 1][0],
            dp[i - 1][0][m + 1][1]);
    }

    for (int i = 1; i < n + 1; i++) {
        for (int j = 0; j < m + 1; j++) {
            for (int k = m + 1; k > j; k--) {

                if (j == 0 and k == m + 1) {
                    continue;
                }

                if (not((m + 1 - k) - (i + j) <= 1)) {
                    continue;
                }

                if (j == 0) {
                    dp[i][j][k][1] = a[i] + dp[i - 1][j][k][0];

                    dp[i][j][k][0] = max(dp[i][j][k][0],
                                    max(dp[i - 1][j][k][0],
                                    dp[i - 1][j][k][1]));

                    dp[i][j][k][0] = max(dp[i][j][k][0],
                                    b[k] + dp[i - 1][j][k + 1][0]);

                    continue;
                }

                if (k == m + 1) {
                    dp[i][j][k][1] = max(dp[i][j][k][1], a[i] + dp[i - 1][j][k][0]);

                    dp[i][j][k][0] = max(dp[i][j][k][0],
                                        max(dp[i - 1][j][k][0],
                                        dp[i - 1][j][k][1]));

                    dp[i][j][k][0] = max(dp[i][j][k][0],
                                        max(dp[i][j - 1][k][0],
                                        dp[i][j - 1][k][1]));
                    dp[i][j][k][1] = max(dp[i][j][k][1],
                                        a[i] + max(dp[i - 1][j - 1][k][0],
                                        dp[i - 1][j - 1][k][1]));

                    continue;
                }

           dp[i][j][k][1] = max(dp[i][j][k][1], a[i] + dp[i - 1][j][k][0]);

           dp[i][j][k][0] = max(dp[i][j][k][0],
                                max(dp[i - 1][j][k][0],
                                    dp[i - 1][j][k][1]));

           dp[i][j][k][0] = max(dp[i][j][k][0],
                                max(dp[i - 1][j - 1][k][0],
                                    dp[i - 1][j - 1][k][1]));
           dp[i][j][k][1] =  max(dp[i][j][k][1],
                               a[i] + max(dp[i - 1][j - 1][k][0],
                               dp[i - 1][j - 1][k][1]));

           dp[i][j][k][0] = max(dp[i][j][k][0],
                               b[k] + dp[i - 1][j][k + 1][0]);
            }
        }
    }

    int ans = LONG_LONG_MIN;

    for (int i = 0; i < m + 1; i++) {
        ans = max(ans, dp[n][i][i + 1][0]);
        ans = max(ans, dp[n][i][i + 1][1]);
    }

    cout << ans;

    return 0;
}
