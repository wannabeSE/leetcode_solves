class Solution {
  List helper(List n, int start, int end, int ele) {
    for (int i = start; i < end; i++) {
      n[i] = ele;
    }
    return n;
  }

  void sortCol(List nums) {
    List count = [0, 0, 0];
    for (int n in nums) {
      count[n] += 1;
    }
    int r = count[0], w = count[1];
    helper(nums, 0, r, 0);
    helper(nums, r, r + w, 1);
    helper(nums, r + w, nums.length, 2);
    print(nums);
  }
}

void main(List<String> args) {
  Solution s = Solution();
  s.sortCol([2, 0, 2, 1, 1, 0]);
}
