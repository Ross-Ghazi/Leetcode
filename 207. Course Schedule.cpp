class Solution {
public:
  bool flag = true;
  unordered_map<int, vector<int>> dic;
  unordered_set<int> seen;
  unordered_set<int> cycle;
  void check(int c) {

    if (cycle.count(c) == 1) {
      flag = false;
      return;
    }
    if (flag == false || seen.count(c) == 1)
      return;

    cycle.insert(c);
    for (auto course : dic[c]) {
      check(course);
    }
    cycle.erase(c);
    seen.insert(c);
  }
  bool canFinish(int numCourses, vector<vector<int>> &prerequisites) {

    for (auto pair : prerequisites) {
      dic[pair[0]].push_back(pair[1]);
    }
    for (int c = 0; c < numCourses; c++) {
      if (seen.count(c) == 0)
        check(c);
    }

    return flag;
  }
};
