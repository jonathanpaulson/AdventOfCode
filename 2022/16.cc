#include <vector>
#include <set>
#include <sstream>
#include <cassert>
#include <tuple>
#include <unordered_map>
#include <iostream>
#include <map>
#include <utility>
using namespace std;
using ll = int64_t;
using pll = pair<ll,ll>;

vector<ll> R;
vector<vector<ll>> E;

ll best = 0;
vector<ll> DP;
ll f(ll p1, ll U, ll time, ll other_players) {
  if(time == 0) {
    return other_players>0 ? f(0,U,26,other_players-1) : 0LL;
  }

  auto key = U*R.size()*31*2 + p1*31*2 + time*2 + other_players;
  if(DP[key]>=0) {
    return DP[key];
  }

  ll ans = 0;
  bool no_p1 = ((U & (1LL<<p1)) == 0);
  if(no_p1 && R[p1]>0) {
    ll newU = U | (1LL<<p1);
    assert(newU > U);
    ans = max(ans, (time-1)*R[p1] + f(p1, newU, time-1, other_players));
  }
  for(auto& y : E[p1]) {
    ans = max(ans, f(y, U, time-1, other_players));
  }
  DP[key] = ans;
  /*if(DP.size() % 100000 == 0) {
    //cerr << DP.size() << " best=" << best << endl;
  }*/
  return ans;
}

int main() {
  map<string, pair<ll, vector<string>>> INPUT;
  while(!cin.eof()) {
    string S;
    getline(cin, S);
    std::istringstream iss(S);
    std::string word;

    ll idx = 0;
    string id;
    ll rate = 0;
    vector<string> NBR;
    while (std::getline(iss, word, ' ')) {
      if(idx == 1) {
        id = word;
      } else if(idx == 4) {
        rate = stoll(word.substr(5, word.size()-6));
      } else if(idx >= 9) {
        if(word[word.size()-1]==',') {
          word = word.substr(0, word.size()-1);
        }
        NBR.push_back(word);
      }
      idx++;
    }
    INPUT[id] = make_pair(rate, NBR);
  }

  ll n = INPUT.size();
  map<string, int> INDEX_OF;
  vector<string> ORDER;
  ll nonzero = 0;
  // Convenient to have the start position have index 0
  for(auto& p : INPUT) {
    if(p.first == "AA") {
      INDEX_OF[p.first] = ORDER.size();
      ORDER.push_back(p.first);
      nonzero++;
    }
  }
  // put valves with non-zero flow rate first
  for(auto& p : INPUT) {
    if(p.second.first > 0) {
      INDEX_OF[p.first] = ORDER.size();
      ORDER.push_back(p.first);
      nonzero++;
    }
  }
  for(auto& p : INPUT) {
    if(INDEX_OF.count(p.first)==0) {
      INDEX_OF[p.first] = ORDER.size();
      ORDER.push_back(p.first);
    }
  }

  R = vector<ll>(n, 0);
  for(ll i=0; i<n; i++) {
    R[i] = INPUT[ORDER[i]].first;
  }
  E = vector<vector<ll>>(n, vector<ll>{});
  for(ll i=0; i<n; i++) {
    for(auto& y : INPUT[ORDER[i]].second) {
      E[i].push_back(INDEX_OF[y]);
    }
  }

  DP = vector<ll>((1L<<nonzero) * n * 31 * 2, -1);
  //cerr << "DP size=" << DP.size() << endl;
  ll p1 = f(0,0,30,false);
  ll p2 = f(0,0,26,true);
  cout << p1 << endl;
  cout << p2 << endl;
}
