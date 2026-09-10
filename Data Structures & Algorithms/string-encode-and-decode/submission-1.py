class Solution:

    def encode(self, strs: List[str]) -> str:

        if strs == []:
            return ''

        payload = ""
        metadata = ""
        for string in strs:
            payload += string
            metadata += str(len(string)) + ","
        return f"{metadata[:-1]}:{payload}"

    def decode(self, s: str) -> List[str]:

        if s == '':
            return []

        i = s.index(':')
        metadata = s[:i]
        payload = s[i + 1:]

        lengths = [int(l) for l in metadata.split(",")]
        strs = []
        for length in lengths:
            strs.append(payload[:length])
            payload = payload[length:]
        return strs