#include <iostream>
using namespace std;
double median(vector<int> a, vector<int> b){
    int size1 = a.size();
    int size2 =  b.size();
    int t = size1 + size2;
    int onLeft = (size1 + size2 + 1) / 2;
    if(size1 > size2){
        return median(b, a);
    }
    int low = 0, high = size1;
    while (low <= high)
    {
        int mid1 = (low + high) / 2;
        int mid2 = onLeft - mid1;
        int l1 = INT_MIN, l2 = INT_MIN;
        int r1 = INT_MAX, r2 = INT_MAX;
        if (mid1 - 1 >= 0) l1 = a[mid1 - 1];
        if (mid2 - 1 >= 0) l2 = b[mid2 - 1];
        if (mid1 < size1) r1 = a[mid1];
        if (mid2 < size2) r2 = b[mid2];
        if (l1 <= r2 && l2 <= r1)
        {
            if (t%2 == 0)
            {
                return (double)(max(l1, l2) + min(r1, r2)) / 2.0;
            }
            return max(l1, l2);
        }
        else if(l1 > r2){
            high = mid1 - 1;
        }
        else {
            low = mid1 + 1;
        }
    }
    return 0;
}
int main(){
    vector<int> A;
    vector<int> B;
    A.push_back(1);
    A.push_back(2);
    B.push_back(3);
    B.push_back(4);
    cout << median(A, B) << endl;
    return 0;
}