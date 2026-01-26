Q1:
Python 3 MCQ1 min 40 pts
Given the Python 3 code below, which of these statements are true?
class Animal:
  pass

class Dog(Animal):
  def cry():
    print('woof')
    
Dog inherits from Animal #Answer
Dog inherits from object  #Answer
---------------------------------------------------------------------------
Q2:
- Square a value
Language knowledge (40 pts) Python 3MCQ35 sec40 pts

Which of the following choices can be used to compute the squared value of val?

val*val  #Answer
pow(val,2) #Answer
val**2 #answer

------------------------------------------------------------------
Q3:
Mapping Language knowledge (60 pts)
Python 3 MCQ 45 sec 60 pts
Which of the following instructions let you transform a list of strings 
strs = ['0', '1', '2']
 
into a list of integers 
[0,1,2] ?

Check all valid answers.

list(map(int, strs)) #Answer
[int(x) for x in strs] #Answer
strs.map(lambda x: int(x))
None of the above
------------------------------------------------------------------
Q4:
Optional parameters Language knowledge (60 pts)
Python 3 MCQ 45 sec 60 pts
Consider the following function:

def func(b=0, c=1, d=2):
   print(b,c,d)
 
Which instruction(s) will print the following line: 1 1 3?

Check all valid answers.
  
func(d=3, b=1)  #ANSWER
func()
func(1,1,3) #ANSWER
func(b="1 1 3", c=None, d=None)
None of the above
------------------------------------------------------------------
Q5:
The "set" type
Language knowledge (60 pts)
Python 3 MCQ 45 sec 60 pts
Which of these is of type set?

Check all valid answers.
  
set() #ANSWER
{1,2,3} #ANSWER
{}
set([1,2,3]) #ANSWER
{1,2,3,3} #ANSWER
(1,2,3)
------------------------------------------------------------------
Q6:
Iterate over a string
Language knowledge (60 pts) Python 3 MCQ 35 sec 60 pts
Which of these instructions can be used to iterate over the characters of the string string?

Check all valid answers.
  
for c in string:  #ANSWER
for c in string.split(''):
for c in list(string):  #ANSWER
with string as c:
------------------------------------------------------------------
Q7:
Execution order
Language knowledge (40 pts) Python 3 MCQ 1 min 40 pts
The code below is in a file called file.py. 
If you run the python3 file.py command, in what order will the code blocks be executed?
#code block A - start
# ...
#code block A - end
def main():
    #code block B - start
    # ...    
    #code block B - end

if __name__ == '__main__':
    main()
#code block C - start
# ...
#code block C - end

A then B then C  #ANSWER
only B is executed
A then B
A then C then B
A then C
------------------------------------------------------------------
Q8:
Existence of key in a dict Language knowledge (40 pts) Python 3 MCQ 1 min 40 pts
Which of these instructions can you use to check if the key "Bob" is present in the phonebook dictionary?
 
"Bob" in phonebook  #ANSWER
phonebook["Bob"] is not None
phonebook["Bob"] != None
phonebook.Bob != None
phonebook.contains("Bob")
------------------------------------------------------------------
Q9:
Concatenate lists
Language knowledge (60 pts) Python 3 MCQ 35 sec 60 pts
Which of these instructions can you use to concatenate the two lists a and b?
 
a.append(b)
a.concat(b)
a & b
a + b  #ANSWER
------------------------------------------------------------------
Q10:
append()
Language knowledge (40 pts) Python 3 MCQ 30 sec 40 pts
Which of these instructions adds 5 to the following list?
 arr = [1,2,3,4]

arr.add(5)
arr.append(5)  #ANSWER
arr.push(5)
arr += 5
------------------------------------------------------------------
Q11:
Object instantiation
Language knowledge (20 pts) Python 3 MCQ 45 sec 20 pts
How does one create a new instance point of the following object:
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
      
point = new Point(x, y)
point = Point(point, x, y)
point = Point(x, y)  #ANSWER
------------------------------------------------------------------
Q12:
For loop
Language knowledge (20 pts) Python 3 MCQ 35 sec 20 pts
How would you iterate over the following list: arr = [1, 2, 3, 4, 5]?

for n in arr: #ANSWER
for n : arr:
foreach n of arr:
------------------------------------------------------------------
Q13: Agile 
Release Scrum roles (40 pts) Agile MCQ 1 min 30 sec 40 pts
You are planning the next release with the Product Owner. Usually, release activities are covered by the Release Manager but he is planning to take a long vacation and you need to find someone to cover these activities.
 
Who is best suited to do this?

Developers  #Answer
Product Owner
Scrum Master
You need to pause the releases until you find another Release Manager
Manual tester
DevOps specialist
------------------------------------------------------------------
Q14: Agile
Daily Scrum definition Scrum events (20 pts) Agile MCQ 45 sec 20 pts

Select all the correct statements regarding Daily Scrums.

This should necessarily be the first thing the team does in the morning
It should be long enough to cover all updates and answer everyone’s questions
It can be facilitated by anyone in the  development team  #ANSWER
It should last up to 15 minutes  #ANSWER
It should be facilitated by the Product Owner
It should be held at the same time every day #ANSWER
------------------------------------------------------------------
Q15: Internal conflict resolution
Scrum rules (40 pts)
Agile MCQ 2 min 40 pts
You are a developer of a newly formed Scrum team. 
One of your teammates does not attend Daily Scrums and prefers to avoid any interactions except during the sprint planning and the sprint retrospective.
 
What are two the best actions you can take?

Discuss it during the sprint retrospective  #ANSWER
Ask the Scrum Master to help with this situation  #ANSWER
Let it be; each developer is an autonomous and competent member who must find their own most productive workflow
Ask the Project Manager to replace this person
Ask the Product Owner to reduce the workload accordingly
Replace the Daily Scrums with offline written communication so that the reluctant colleague can still access the meeting minutes
------------------------------------------------------------------
Q16:
Backlog refinement
Scrum roles (40 pts) Agile MCQ 1 min 30 sec 40 pts
You are a developer on a newly formed Scrum team for a brand new product. 
During the second sprint, the Product Owner has asked developers to review potential bug reports and add more edge cases to the tests.
 
What is the best action you can do?

Reject. It is the Product Owner's sole responsibility to refine tasks.
Accept. Task refinement is the responsibility of the entire Scrum team.  #ANSWER
Ask external testers to write the additional edge cases.
Ask the Scrum Master to coach the Product Owner about how to write edge cases.
------------------------------------------------------------------
Q17:
User stories contain what to build, but not how to build it 
Scrum artifacts (40 pts) Agile MCQ 1 min 40 pts
User stories contain information for the business and Scrum team on the work to be done.
 
What is commonly found in user stories?

What to build  #ANSWER
How to build it
Acceptance Criteria  #ANSWER
Size Estimate  #ANSWER
------------------------------------------------------------------
Q18: Cyber
Password cracking
Cyber Attack (20 pts) Cyber Security MCQ 35 sec 20 pts
Which of the following is the fastest attack to crack a password hash?

Brute force attack
Rainbow table attack  #ANSWER
Dictionary attack
Cache poisoning attack
------------------------------------------------------------------
Q19: Cyber
Web Reverse Shell
Cyber Attack (20 pts) Cyber Security MCQ 30 sec 20 pts

What user would an attacker be on a Web Reverse Shell?

root
www-data  #ANSWER
web-user
daemon
user
------------------------------------------------------------------
Q20:
SSO - SAML
Security Knowledge (40 pts) Cyber Security MCQ 1 min 40 pts
Which protocol cannot be used for the SSO AUTH methods shown below (in red)? (PIC below) 
 

OAuth
SAML
OTP  #ANSWER
OpenID
------------------------------------------------------------------
Q21:
Privilege Escalation NOPASSWD
Cyber Attack (40 pts) Cyber Security MCQ 35 sec 40 pts
What attack vector can be used in the following case?
 

Privilege Escalation  #ANSWER
Buffer Overflow
Remote Code Execution
Command Injection
Denial of Service
------------------------------------------------------------------
Q22:
Port scanning Cyber Attack (20 pts) Cyber Security MCQ 50 sec 20 pts
What process is demonstrated in the following picture?
code in images
 

SQL Injection
Website Denial-of-Service
DNS Resolution
Port Scanning  #ANSWER
Port Injection
DNS Spoofing
------------------------------------------------------------------
Q23:
CSRF protection
Security Measures (20 pts) Cyber Security MCQ 30 sec 20 pts

Which of the following represents the primarly protection method against CSRF?
Input Validation
CSP Rules
CSRF Tokens  #ANSWER
Prepared Statements
------------------------------------------------------------------
Q24:
Network Security: Secure TCP ports
Security Knowledge (20 pts) Cyber Security MCQ 30 sec 20 pts

Choose one of the official IANA TCP ports that is secure by default.

Port 23
Port 20
Port 22 #ANSWER
Port 21
------------------------------------------------------------------
Q25:
K-Means
Machine Learning (50 pts) Data Science MCQ 1 min 50 pts
Which of the following is false about the standard K-Means algorithm (Lloyd's algorithm)?
                                                                      
The algorithm will always converge after a finite number of iterations
The algorithm uses Euclidean distance in figuring out which cluster to assign a point to
The algorithm will optimize the initial locations of the cluster centers  #ANSWER
You must provide the number of clusters (K) as an argument for the algorithm
------------------------------------------------------------------
Q26:
One-Hot Encoding
Machine Learning (50 pts) Data Science MCQ 1 min 50 pts
Which of the following variables would it make sense to provide a one-hot encoding for?
                                                                                  
A variable representing whether or not a college student lives on campus
A variable representing a college student's major   #ANSWER
A variable representing a college student's weight (in kilograms)
A variable representing a college student's GPA (out of 4.0)
------------------------------------------------------------------
Q27:
[ML] Feature Selection (Standard) Machine Learning (20 pts) Data Science MCQ 1 min 20 pts
You want to optimize a prediction model. What methods can be used to select the most important variables?

Multiple answers expected.
  
Latent Dirichlet Allocation
Chi-squared test  #ANSWER
Lasso regularization  #ANSWER
One Hot Encoder
------------------------------------------------------------------
Q 28:
[LinearAlgebra] Matrix inversion
Linear Algebra (80 pts) Data Science MCQ 5 min 80 pts
Among these three matrices, which ones are invertible?
(2nd pic)

One or more answers expected.
  
Matrix 1 is invertible
Matrix 2 is invertible  #ANSWER
Matrix 3 is invertible  #ANSWER
------------------------------------------------------------------
Q 29:
[Statistics] Normal distribution
Statistics (80 pts) Data Science MCQ 5 min 80 pts
In the context of a statistical survey, you sampled the salaries of a collaborative corporate structure. 
These salaries follow a normal distribution: the mean equals $2,500 and the standard deviation equals $500.

By using Chebyshev's inequality (see formula below), estimate the lower bound of the probability that the salary of a randomly selected employee of this company is between $1,900 and $3,100.

pic 3
 
(with α > 0)
X is a random variable with finite expected value E[X] and finite variance σ²

100 %
70 %
50 %
30 %  #ANSWER
0 %
------------------------------------------------------------------
Q30:
[ML] Grid Search Machine Learning (40 pts) Data Science MCQ 2 min 40 pts
What is true about the Grid Search method used for hyperparameters optimization? 

Grid Search can't be executed in parallel as an iteration depends on the results of the previous iterations
Grid Search can find the optimal combination for a maximum of two hyperparameters
Grid Search must define a metric, the score, which is used to find optimal hyperparameters  #ANSWER
Grid Search is only used in the context of Deep Learning algorithms
------------------------------------------------------------------
Q31:
[Statistics] Statistical test
Statistics (40 pts) Data Science MCQ 2 min 40 pts
A digital catalogues publisher conducted a survey related to wine consumption in various countries.
The average wine consumption per citizen per year in the U.S. is 2.94 gallons. 
You observe that in your state, wine consumption is much higher. As a result, you do a simple random sampling of the wine consumption dataset with the goal of validating your observation.
In order to conduct a one-tailed hypothesis test, how would you define the hypotheses?

H0 is the exact (point) null hypothesis, Ha is the alternative hypothesis.
H0 : m > 2.94 ; Ha= : m < 2.94
H0 : m = 2.94 ; Ha= : m > 2.94  #ANSWER
H0 : m < 2.94 ; Ha= : m = 2.94
H0 : m = 2.94 ; Ha= : m < 2.94
H0 : m < 2.94 ; Ha= : m > 2.94
H0 : m > 2.94 ; Ha= : m = 2.94                                           
------------------------------------------------------------------
Q32:
[ML] Optimal number of clusters
Machine Learning (40 pts) Data Science MCQ 45 sec 40 pts
You executed the k-means algorithm using different values for k on a given dataset and transfered the results on the graph below.

What is the optimal number of clusters (k) for this dataset? (pic 4)

10
9
7
4  #ANSWER
2
------------------------------------------------------------------
Q33:
[ML] Random Forest vs Decision tree Machine Learning (20 pts) Data Science MCQ 45 sec 20 pts
What is the advantage of using a Random Forest algorithm over a Decision Tree algorithm?

A Random Forest algorithm can process continuous variables whereas a Decision Tree can only process categorical variables
A Random Forest algorithm can be used for regression whereas Decision Trees are only used for classification
The Random Forest algorithm can reduce overfitting #ANSWER
------------------------------------------------------------------
Q34:
[DeepLearning] Neural networks basics Deep Learning (20 pts) Data Science MCQ 40 sec 20 pts

Backpropagation is a method used in artificial neural networks to ...
Backpropagate hyperparameters through network layers
Backpropagate data through network layers
Backpropagate errors through network layers  #ANSWER
------------------------------------------------------------------
Q35:
[agriculture.csv] Sum across rows and columns
Problem solving (80 pts) Dataset analysis MCQ 6 min 80 pts
You are given an agriculture dataset, agriculture.csv. 
Each row of the dataset represents a particular agriculture item produced in a given country and the amount of production between the years 1965-2017.
The Item column contains the name of the agriculture item while the Country column represents the country that is producing the item. The columns labeled with years represent the amount of production (in kilotons) of the item by the given country in a particular year. Note that some of the production amounts may be missing.

Which country had the highest total production (across all items) from 1965-2017? Treat each missing production amount as 0.

Country22
Country87
Country125
Country166
Country35  #ANSWER
Country132
------------------------------------------------------------------
Q36:
[shirts.csv] Average of computed field
Problem solving (80 pts) Dataset analysis MCQ 6 min 80 pts
You are given a shirt retail dataset, shirts.csv. Each row of the dataset represents a shipment of shirts ordered by a retail company.
The ShirtSize column represents the size of the shirts that were ordered for shipment. The Quantity column represents the number of shirts that were ordered, while the Price column represents the price for each individual shirt.

What is the average cost for shipments of Large shirts? We define cost as the quantity of shirts multiplied by the price per shirt.
1957.58
2074.84
2020.59  #ANSWER
2133.16
------------------------------------------------------------------
Q37:
[videogames.csv] Number of rows by value with condition
Problem solving (80 pts) Dataset analysis MCQ 6 min 80 pts
You are given a video games dataset, videogames.csv. Each row of the dataset represents a particular video game, with information about the game itself and its revenue across the world.
The Platform column represents the gaming platform that the video game was launched on. The Genre column represents the genre of the video game.

For video games launched on the "Wii" platform, what is the most common genre?

Action
Adventure
Strategy
Racing
Misc  #ANSWER
Simulation
------------------------------------------------------------------
Q39:
[companyrevenue.csv] Number of rows by value
Problem solving (40 pts) Dataset analysis MCQ 5 min 40 pts
You are given a company revenue dataset, companyrevenue.csv. 
Each row of the dataset represents a particular company.
The Headquarters column represents the city that a company is headquartered in.

Which five cities headquarter the most companies, in descending order of the number of companies located in the city?

San Francisco, San Jose, New York, Los Angeles, Philadelphia
San Francisco, New York, San Jose, Boulder, Los Angeles  #ANSWER
Los Angeles, San Francisco, San Jose, Chicago, New York
New York, Los Angeles, San Francisco, Philadelphia, Seattle
New York, Los Angeles, San Francisco, Seattle, Chicago
------------------------------------------------------------------
Q40:
[news.csv] Distinct values in a column
Problem solving (40 pts) Dataset analysis MCQ 5 min 40 pts
You are given a news stories dataset, news.csv. 

What are the categories in the dataset that a news article can be labeled as?

Sports, Global, Finance
Sports, Global, Science, Finance
Sports, Global, Science, Business  #ANSWER
Global, Business, Science
------------------------------------------------------------------
Q41:
Docker storage: Best practice
Language knowledge (40 pts) Docker MCQ 1 min 30 sec 40 pts
Which of the following statements would you qualify as a best practice regarding the management of data for a dockerized application?
 
Multiple answers expected
Try to store application data in the container’s writable layer using a storage driver
Try to use bind mounts instead of using volume mounts
Use a secrets mount for sensitive data such as passwords  #ANSWER
Use a tmpfs mount if your application produces a lot of non-persistent data  #ANSWER
------------------------------------------------------------------
Q42:
Docker swarm: Getting service logs
Problem solving (40 pts) Docker MCQ 55 sec 40 pts
A user reported that a docker swarm service billing-manager has stopped working properly.
 
Your cluster is still using the default logging drivers.
 
Which command should you use to gather information for troubleshooting purposes?
                                                  
docker service logs billing-manager  #ANSWER
docker logs billing-manager
docker container logs billing-manager
docker swarm logs billing-manager
------------------------------------------------------------------
Q43:
Docker image: Building image
Language knowledge (20 pts) Docker MCQ 50 sec 20 pts
Which command will build a docker image with the name webportal and tag 1.0 using the Dockerfile available in the current directory?

docker build -t webportal:1.0 .  #ANSWER
docker build webportal:1.0 -f .
docker build . --name=webportal:1.0
docker build webportal -t 1.0 .
------------------------------------------------------------------
Q44:
Docker registry: Login to server
Language knowledge (20 pts) Docker MCQ 45 sec 20 pts
What command can be used to log in to the docker registry "docker-registry.company.com" using user "jerry"?

docker login --username=jerry --serverurl=docker-registry.company.com
docker login --username=jerry docker-registry.company.com  #ANSWER
docker login -u jerry -h docker-registry.company.com
docker login jerry docker-registry.company.com
------------------------------------------------------------------
Q45:
Docker image: Pulling image
Language knowledge (20 pts) Docker MCQ 30 sec 20 pts
You need the image nginx with tag latest to be available on your local docker storage. 
You decide to get this image from a default public repository.
 
Which command should you use?

docker pull nginx:latest  #ANSWER
docker push nginx:latest
docker get nginx:latest
docker download nginx:latest
------------------------------------------------------------------
Q46: EXCEL
Pivot table fields
Pivot tables (20 pts) Excel MCQ 3 min 20 pts
You are working with the following data:

Using a pivot table, you want to compute the quantity sold in 2010, broken down by priority, like the following: (PIC)
 
What columns should you put in the pivot table fields? 

Filters = order_date  #ANSWER
Filters = priority
Filters = quantity
Columns = order_date
Columns = priority
Columns = quantity
Rows = order_date
Rows = priority  #ANSWER
Rows = quantity
Values = order_date
Values = priority
Values = quantity  #ANSWER
------------------------------------------------------------------
Q47:
Conditional formatting
Advanced features (20 pts) Excel MCQ 1 min 20 pts
You have some numbers in column B.
 
What feature can you use to quickly identify negative numbers like below? (PIC)
 

Conditional formatting  #ANSWER
IF formula
Pivot table
Table
Data validation
------------------------------------------------------------------
Q48:
IF arguments order
Formula (20 pts) Excel MCQ 1 min 20 pts
You want to display Approved if a value in cell A1 is greater than 100, and Denied otherwise.
 
What formula should you use?

=IF(A1>100, 'Approved', 'Denied')  #ANSWER
=IF(A1>100, 'Denied', 'Approved')
=CASE(A1>100, 'Approved', 'Denied')
=A1>100 ? 'Approved' : 'Denied'
------------------------------------------------------------------
Q49:
Selecting the right chart - Pie chart
Data visualization (20 pts) Excel MCQ 1 min 20 pts
You want to compare the relative weight of large customers in your sales data.
 
Which type of chart is best suited for displaying relative proportions?
Line chart
Pie chart  #ANSWER
Bar chart with multiple bars
Scatter chart
Waterfall chart
------------------------------------------------------------------
Q50:
Plot 3d: plot3 Graphics (20 pts) Matlab MCQ 30 sec 20 pts
Which command would you use to obtain a figure like the one displayed above? ( last pic)

plot3  #ANSWER
pot3d
pot3D
meshplot
------------------------------------------------------------------
Q51:
Vector indexing
Arrays (20 pts) Matlab MCQ 30 sec 20 pts
Which statement is true regarding indexing in MATLAB?

The first element of the vector v is accessed using v(1)  #ANSWER
The first element of the vector v is accessed using v(0)
The first element of the vector v is accessed using v[0]

------------------------------------------------------------------
