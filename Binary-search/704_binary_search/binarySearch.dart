class Solution {
  int search(List<int> nums, int target) {
    int l = 0;
    int r = nums.length - 1;
    while (l <= r) {
      int mid = (l + r) ~/ 2;
      if (nums[mid] == target) {
        return mid;
      } else if (nums[mid] > target) {
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    }
    return -1;
  }
}

void main(List<String> args) {
  Solution s = Solution();
  print(s.search([-1, 0, 3, 5, 9, 12], 9));
}
