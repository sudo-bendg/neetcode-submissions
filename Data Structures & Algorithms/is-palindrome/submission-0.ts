class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {

        s = s.toLowerCase().replace(/[^a-z0-9]/g, '')

        let left: number = 0;
        let right: number = s.length - 1;

        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
}
