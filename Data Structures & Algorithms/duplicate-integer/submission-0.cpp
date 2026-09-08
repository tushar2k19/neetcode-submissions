class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> umap;
        int n = nums.size();

        for(int i= 0 ;i<n;i++)
        {
            if(umap.find(nums[i])==umap.end()){
                umap[nums[i]]++;
                cout << umap.size() << endl;
            }
            else 
                return true; 
        }
        return false;
    }
};
