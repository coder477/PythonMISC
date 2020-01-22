from datetime import datetime,date  
import pymysql

"""Maximum date from a array of dates, taken as strings"""
class MaximumDateInAnArray:
    def findLongestConseqSubseq(self,arr, n): 
        s = {} 
        ans=0
        for ele in arr: 
            s.add(ele) 
        for i in range(n): 
            if (arr[i]-1) not in s: 
                j=arr[i] 
                while(j in s): 
                    j+=1
                ans=max(ans, j-arr[i]) 
        return ans 
    
    def subArraySum(self,arr, n, sum): 
          
        # Pick a starting  
        # point 
        for i in range(n): 
            curr_sum = arr[i] 
          
            # try all subarrays 
            # starting with 'i' 
            j = i+1
            while j <= n: 
              
                if curr_sum == sum: 
                    print ("Sum found between") 
                    print("indexes %d and %d"%( i, j-1)) 
                      
                    return 1
                      
                if curr_sum > sum or j == n: 
                    break
                  
                curr_sum = curr_sum + arr[j] 
                j += 1
      
        print ("No subarray found") 
        return 0
    
    if __name__ == "__main__":
        userdata={98666:['2018-09-25','2018-09-26','2018-09-28','2018-09-29','2018-09-30','2018-10-02','2018-10-03','2018-10-04','2018-10-05']}
        userdata={98666:['2018-09-25','2018-09-26','2018-09-28','2018-09-29','2018-09-30','2018-10-02','2018-10-03','2018-10-04','2018-10-05']}
        date_strs = userdata[98666]
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in date_strs]
        date_ints = list([d.toordinal() for d in dates])
        date_ints=sorted(date_ints) 
        print(date_ints)
        [1,0,1,1,0,1,1,1]
        [0,0,1,0,0,1,1]
        [0,0,0,0,0,1]
        newarr=[]
        for i in range(1,len(date_ints)):
            
            if(date_ints[i]==date_ints[i-1]+1):
                newarr.append(1)
            else:
                newarr.append(0)
            
                
        print(newarr)
        
        
        
        x=date_ints
        N = 4
        sol = 0
        num=0
        for i in range(0,len(x)-N+1):
            num = x[i]
            got = True
            for j in range(i+1,i+N):
                print("comparing",x[j], num, x[j]-num,1)
                if(x[j]-num ==1) :
                    num = x[j]
                else :
                    got = False
                    break
            if(got) :
                sol=sol+1
            
            
        print(sol)
        
    
