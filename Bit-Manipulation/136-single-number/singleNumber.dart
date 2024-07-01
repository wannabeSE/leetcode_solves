int singleNumber(List nums) {
  int res = 0;
  for (int n in nums) {
    res = res ^ n;
  }
  return res;
}

void main(List<String> args) {
  print(singleNumber([2, 2, 1]));
}
