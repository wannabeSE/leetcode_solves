class Solution {
  List<int> twoSum(List<int> numbers, int target) {
    int left = 0;
    int right = numbers.length - 1;
    while (left < right) {
      int sum = numbers[left] + numbers[right];
      if (sum == target) {
        return [left + 1, right + 1];
      } else if (sum > target) {
        right--;
      } else {
        left++;
      }
    }
    return [];
  }
}

void main(List<String> args) {
  Solution s = Solution();
  var res = s.twoSum([2, 3, 4], 6);
  print(res);
}
