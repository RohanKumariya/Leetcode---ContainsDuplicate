''' Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

-- If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

-- If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
For example, "m.y+name@email.com" will be forwarded to "my@email.com".

It is possible to use both of these rules at the same time.
Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"] -- Output: 2

Example 2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"] -- Output: 3 '''



#Very long yet easy to understand code which is quiet efficient with o(n) time complexity
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #Initiate hashmap for result
        hashset = set()
      
        #This is the only loop iteration.
        for i in emails:
            dom = ""
            totname = ''
            name = ""
            k = ''
          
            #Here domain name and the name is split 
            i = i.split('@')
            dom += i[1]
            name += i[0]
            name = name.replace('.',"")
            name = name.split('+')
            totname += name[0]

            #Both name and domain name is added to a string 
            k += dom
            k += totname

            #Adding k to the hashset and returing length of hashset would give the result.
            hashset.add(k)
        return len(hashset)
