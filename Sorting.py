import random

class sorting:
    
    def meta(self,li):
        print('list: {}'.format(li))
        print('lenght: {}'.format(len(li)))

    def bubble_sort(self,li):
        for j in range(len(li)):
            for i in range(0,len(li)-j-1):
                if li[i]>li[i+1]:
                    li[i],li[i+1]=li[i+1],li[i]
        
        return li

    def insertion_sort(self,li):
        for i in range(1,len(li)):
            key = li[i]
            j=i-1
            while j>=0 and key < li[j]:
                li[j+1] = li[j]
                j-=1
            li[j+1]=key

        return li

    def count_sort(self,li):
        count_arr_len = max(li)+1
        count_arr=[0]*count_arr_len
        k=0

        for i in li:
            count_arr[i]+=1

        for i in range(count_arr_len):
            while count_arr[i]>0:
                li[k] = i
                k+=1
                count_arr[i]-=1

        return li

    def merge_sort(self,li):
        if len(li)<2:
            return li
        result=[]
        mid = int(len(li)/2)
        l = self.merge_sort(li[:mid])
        r = self.merge_sort(li[mid:])
        while (len(l)>0 and len(r)>0):
            if l[0] > r[0]:
                result.append(r[0])
                r.pop(0)
            else:
                result.append(l[0])
                l.pop(0)
        result+=l
        result+=r
        return result

    def quick_sort(self,li):
        
        def q_sort(li,low,high):
            if low < high:
                pi = partition(li, low, high)
                q_sort(li, low, pi-1)
                q_sort(li, pi+1, high)

        def partition(li,low,high):
            i= low-1
            pivot = li[high]
            for j in range(low,high):
                if li[j]<=pivot:
                    i+=1
                    li[i],li[j]=li[j],li[i]
            li[i+1],li[high]=li[high],li[i+1]
            return (i+1)
        
        low =0 
        high = len(li)-1
        q_sort(li,low,high)
        return li
