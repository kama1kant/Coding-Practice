from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}

        def hashmapFromUrl(url, hits):
            domain = url.split('.')
            subdomain = ''
            for i in range(len(domain)-1, -1, -1):
                if len(subdomain) > 0:
                    subdomain = domain[i] + '.' + subdomain
                else:
                    subdomain = domain[i]
                
                if subdomain not in hashmap:
                    hashmap[subdomain] = 0
                hashmap[subdomain] += hits
                
        for ele in cpdomains:
            [hits, url] = ele.split(' ')
            hashmapFromUrl(url, int(hits))
        
        ans = []
        for k in hashmap:
            ans.append(str(hashmap[k]) + ' ' + k)
        return ans
                
        
sol = Solution()
output = sol.subdomainVisits(
    ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
print(output)