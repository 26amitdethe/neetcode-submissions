class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        prev = ""
        for i in s:
            if prev=="[" and i=="]":
                st.pop()
            elif prev=="{" and i=="}":
                st.pop()
            elif prev=="(" and i==")":
                st.pop()
            else:
                prev = i
                st.append(i)
                continue
            prev = st[-1] if st else ""
        return st==[]