class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> umap1, umap2;
        int n1 = s.size(), n2 = t.size();
        for(int i= 0; i<n1;i++)
        {
            umap1[s[i]]++;
        }

        for(int i= 0; i<n2;i++)
        {
            umap2[t[i]]++;
        }

        unordered_map<char, int>::iterator itr;
        for(itr = umap1.begin(); itr!=umap1.end(); itr++)
        {
            char c = itr->first;
            if(umap1[c]!=umap2[c])
                return false;
        }
        for(itr = umap2.begin(); itr!=umap2.end(); itr++)
        {
            char c = itr->first;
            if(umap1[c]!=umap2[c])
                return false;
        }
        return true;
    }
};
