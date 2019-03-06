import random
import math
import copy
import cv2
import numpy as np

class RRT():
  def __init__(self,start,end,r):
    self.start=Node(start[0],start[1])
    self.end=Node(end[0],end[1])
    self.r=r
    self.nlist=[self.start]
    self.img=np.zeros((1500,1500,3),np.uint8)


    
  def traj(self,frame):
    self.frame=frame
    while(1):
     ar=Node(random.randint(0,1600), random.randint(0,2200))
     nin1=self.indexofNearest(self.nlist,ar)
 
     #print ar12.x,ar12
    
     k=0
     a1=(math.sqrt((ar.x-self.nlist[nin1].x)**2+(ar.y-self.nlist[nin1].y)**2))
     c=1
     while k<=self.r:
       print 1
       p=float(self.nlist[nin1].x)+float((ar.x-self.nlist[nin1].x)*k/((math.sqrt((ar.x-self.nlist[nin1].x)**2+(ar.y-self.nlist[nin1].y)**2))))
      
       q=float(self.nlist[nin1].y)+float((ar.y-self.nlist[nin1].y)*k/((math.sqrt((ar.x-self.nlist[nin1].x)**2+(ar.y-self.nlist[nin1].y)**2))))
       k=k+1
       if p>=1460 or p<=460 or q<=50 or q>=1080:
          c=0
          break
       if(self.obstaclecheck(p,q)==1):
         continue
       else:
         c=0
         break
     
     if c:
       cv2.line(self.frame, (int (self.nlist[nin1].x), int(self.nlist[nin1].y)), (int(p),int(q) ), (0, 0, 255), thickness=1, lineType=8)
       cv2.imshow('frame',self.frame)
       cv2.waitKey(1)
       ar12=Node(p,q)
       ar12.parent=nin1 
       self.nlist.append(ar12)
      
        #print 0
       if self.goal_reach(p,q) :
         print "goal!"
         self.nlist.append(ar12)
         self.goal_print(ar12)
         return 1
       #for i in range(0,3):
        ## print 1
         #if p<1 and q<1027:
         #self.img[(int)(p),(int)(q)][i]=127
         #self.frame[(int)(p),(int)(q)][i]=12
  
 
    
       
  
  def goal_reach(self,x,y): 
    if x>=1460 or x<=460 or y<=50 or y>=1080:
     if self.frame[int(y),int(x)][0]<=30 and self.frame[int(y),int(x)][1]>240 and self.frame[int(y),int(x)][2]<=30:
      self.goal=[x,y]
      return 1
    if x>1322 and x<1437 and y<339 and y>269:
     return 1
    else:
      return 0


     
  def indexofNearest(self,points,a):
    min=10000000
    l=0
    for point in points:
      d=math.sqrt((point.y-a.y)**2+(point.x-a.x)**2)
      if(d<min):
       min=d
    
       l=points.index(point)
    return l

  def obstaclecheck(self,y,x):
   print 0
   
   if self.frame[int(x),int(y)][0]<=30 and self.frame[int(x),int(y)][1]<=30 and self.frame[int(x),int(y)][2]<=30:
     print(y,x)
     return 0
   if self.frame[int(x),int(y)][0]>=225 and self.frame[int(x),int(y)][1]<=30 and self.frame[int(x),int(y)][2]<=30:
     print(y,x)   
     return 0
   else:   
    return 1
  
  def goal_print(self,ar):
    while ar.parent!=None:
      k=0
      p=copy.deepcopy(ar.x)
      q=copy.deepcopy(ar.y)
      theta1=math.atan(float(q-self.nlist[ar.parent].y)/float(p-self.nlist[ar.parent].x))
      #while k<=self.r:
       
 
       #if p<1920:
        #p=p+k*math.cos(theta1)
       #else:
        #break
       #if q<1080:
        #q=q+k*math.sin(theta1)
       #else:
        #break
       #for i in range(0,3):
        # self.frame[int(q),int(p)][i]=127
       #k=k+2""
      print 7
      cv2.line(self.img, (int (ar.x), int(ar.y)), (int(p),int(q) ), (0, 0, 255), thickness=1, lineType=8)
      ar=self.nlist[ar.parent]
           
  def video1(self):

   cap = cv2.VideoCapture('path.mkv')
   while(cap.isOpened()):
    ret, frame = cap.read()
  
    q=self.traj(frame)
    if q==1:
      
      break
    
    
    if ret==True:
     print "show"
     cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  #press q to exit
        break
   cap.release()
 
# Closes all the frames
   cv2.destroyAllWindows()

     
    
  
        
class Node():
  def __init__(self,x,y):
    self.x=x
    self.y=y
    self.parent=None
    
  
  


def main():
 start=[576,964]
 goal=[307,1395]
 r=20
 rrt=RRT(start,goal,r)

 cap = cv2.VideoCapture('path.mkv')
 while(cap.isOpened()):
    ret, frame = cap.read()
    #print ret 
    q=rrt.traj(frame)
   # if q==1:
    #  
     # break
    
    print 1
    if ret==True:
    
     cv2.imshow('frame',frame)
    
     if cv2.waitKey(1) & 0xFF == ord('q'):  #press q to exit
        break
 cap.release()
 
# Closes all the frames
 cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
