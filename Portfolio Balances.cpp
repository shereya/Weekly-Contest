//cumulative sum approach
long maxValue(int n, vector<vector<int>>rounds) {
    vector<long>invest;
    for(int i=0;i<n+1;i++)
    {
        invest.push_back(0);
    }
    for(int i=0;i<rounds.size();i++)
    {
        long l=rounds[i][0]-1;
        long r=rounds[i][1];
        long a=rounds[i][2];
        invest[l]=invest[l]+a;
        invest[r]=invest[r]-a;
    }
    for(int i=0;i<invest.size();i++)
    {
        invest[i]=invest[i-1]+invest[i];
    }
    return *max_element(invest.begin(),invest.end());
}
