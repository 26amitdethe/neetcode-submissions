class Solution:
    weird_join_string = "#$@#$^"
    empty_list_flag = "EMPTY_LIST_FLAG"
    def encode(self, strs: List[str]) -> str:
        if not strs: 
            return self.empty_list_flag
        a = self.weird_join_string.join(strs)
        return(a)

    def decode(self, s: str) -> List[str]:
        if s == self.empty_list_flag:
            return []
        return s.split(self.weird_join_string)
       