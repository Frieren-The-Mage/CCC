#include <bits/stdc++.h>

#define int long long
#define pii pair<int, int>

using namespace std;

/* 
https://dmoj.ca/problem/ccc25s3
Honestly not the worst problem, idea is ok
Implementation is SO MUCH easier in cpp than python
Multiset kinda op ngl
*/

signed main() {
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n, m, q;
    cin >> n >> m >> q;

    multiset<int, greater<int>> arr[m + 1];

    // Padding
    for (int i = 1; i < m + 1; i++) {
        arr[i].emplace(0);
        arr[i].emplace(0);
    }

    pii info[n + 1]; // {color, prettiness}

    for (int i = 1; i < n + 1; i++) {
        int c, p;
        cin >> c >> p;
        arr[c].emplace(p);
        info[i] = {c, p};
    }

    // First best, second best. Keep running total for first
    multiset<int> first;
    multiset<int, greater<int>> second;

    int tot = 0;
    for (int i = 1; i < m + 1; i++) {
        first.emplace(*arr[i].begin());
        second.emplace(*next(arr[i].begin()));
        tot += *arr[i].begin();
    }

    // Extract Answer
    auto find_ans = [&]() {
        // Take the maximum second instead of minimum first
        int ans = max(tot, tot - *first.begin() + *second.begin());
        return ans;
    };

    // Remove old values in first and second
    auto remove_old = [&](int i) {
        auto it = first.find(*arr[i].begin());
        tot -= *it;
        first.erase(it);

        it = second.find(*next(arr[i].begin()));
        second.erase(it);
    };

    // Add new values to first and second
    auto add_new = [&](int i) {
        first.emplace(*arr[i].begin());
        tot += *arr[i].begin();
        second.emplace(*next(arr[i].begin()));
    };

    int ans = find_ans();
    cout << ans << endl;

    for (int _ = 0; _ < q; _++) {
        int t, a, b;
        cin >> t >> a >> b;

        if (t == 1) {
            int i = a;
            int c = b;

            remove_old(info[i].first);
            remove_old(c);

            // Find and remove the prettiness in old multiset
            auto it = arr[info[i].first].find(info[i].second);
            arr[info[i].first].erase(it);

            // Update old multiset
            add_new(info[i].first);

            // Add color into new multiset and update new multiset
            info[i].first = c;
            arr[c].emplace(info[i].second);
            add_new(info[i].first);
        }

        if (t == 2) {
            int i = a;
            int p = b;

            remove_old(info[i].first);

            // Find and remove old color
            auto it = arr[info[i].first].find(info[i].second);
            arr[info[i].first].erase(it);

            // Update new color
            info[i].second = p;
            arr[info[i].first].emplace(p);

            add_new(info[i].first);
        }

        cout << find_ans() << endl;
    }

    return 0;
}
