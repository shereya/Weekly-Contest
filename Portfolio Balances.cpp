long maxValue(int n, vector<vector<int>> rounds) {
    vector<long>invest;
    for(int i=0;i<n;i++)
    {
        invest.push_back(0);
    }
    for(int i=0;i<rounds.size();i++)
    {
        long l=rounds[i][0]-1;
        long r=rounds[i][1]-1;
        long amount=rounds[i][2];
        for(int j=l;j<=r;j++)
        {
            invest[j]=invest[j]+amount;
        }
    }
    return *max_element(invest.begin(),invest.end());
}
