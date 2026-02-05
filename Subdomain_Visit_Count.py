class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom_count = {}
        
        for dom in cpdomains:
            count,domain = map(str,dom.split(" "))
            
            domains = [domain]
            for i in range(len(domain)-1,-1,-1):
                if domain[i] == ".":
                    domains.append(domain[i+1:])
                    
            for d in domains:
                dom_count[d] = dom_count.get(d,0)+int(count)

        res = []

        for key,val in dom_count.items():
            res.append(f"{val} {key}")

        return res
