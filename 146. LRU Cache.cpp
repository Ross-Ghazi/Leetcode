
//ref:
// https://www.youtube.com/watch?v=NDpwj0VWz1U&ab_channel=NickWhite
// https://leetcode.com/problems/lru-cache/editorial/
// https://leetcode.com/problems/lru-cache/solutions/45912/clean-short-standard-c-solution-not-writing-c-in-c-like-all-other-lengthy-ones/
//https://leetcode.com/problems/lru-cache/solutions/45912/clean-short-standard-c-solution-not-writing-c-in-c-like-all-other-lengthy-ones/comments/1090733
// we use map/dic and then the values of this map are nodes on double link list
class LRUCache {
    int capacity;
    list<pair<int, int>> li;
    unordered_map<int, list<pair<int, int>>::iterator> um; 

public:
    LRUCache(int capacity) : capacity{capacity} {}
    
    int get(int key) {
        if (um.find(key) == um.end()) return -1;
        li.splice(li.begin(), li, um[key]);
        return um[key]->second;
    }
    
    void put(int key, int value) {
        if (get(key) != -1) {
            um[key]->second = value;
            return;
        }
        
        if (um.size() == capacity) {
            int delKey = li.back().first;
            li.pop_back();
            um.erase(delKey);
        }
        
        li.emplace_front(key, value);
        um[key] = li.begin();
    }
};
