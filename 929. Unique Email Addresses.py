class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            local_name,domain_name = email.split("@")
            local_name=local_name.split('+')[0]
            local_name ="".join(local_name.split('.'))      
            email = local_name +'@' + domain_name
            email_set.add(email)
        return len(email_set)
            
