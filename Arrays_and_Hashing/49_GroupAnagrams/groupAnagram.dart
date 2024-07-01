List<List<String>> groupAnagram(List strs) {
  Map<String, List<String>> res = {};
  for (String s in strs) {
    List<int> count = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      count[s.codeUnitAt(i) - 'a'.codeUnitAt(0)] += 1;
    }
    String key = count.toString();
    if (!res.containsKey(key)) {
      res[key] = [];
    }
    res[key]!.add(s);
  }
  return res.values.toList();
}

void main(List<String> args) {
  print(groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]));
}
