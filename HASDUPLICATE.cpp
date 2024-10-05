#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        bool output = false;
        vector<int> nums_check;
        for (int i=0;i<nums.size();i++){
            if (find(nums_check.begin(), nums_check.end(), nums[i]) != nums_check.end(){
                output = true;
                break;
            }
            nums_check.push_back(nums[i]);
        }
        return output;
    }
};