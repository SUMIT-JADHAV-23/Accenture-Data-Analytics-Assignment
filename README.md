# README
## Project Details
Read and analyze a client project brief to understand the client and business problem, identify the requirements that need to be delivered, and identify which tasks we need to focus on as a data analyst

### Client Data Set
- Content data
- Reaction type Data
- Reaction data 

## Output of Program
 The program gievs one excel file "A Cleaned dataset"
 
- ### In  A Cleaned dataest.xlsx file
   In [A Cleaned dataest.xlsx](https://github.com/SUMIT-JADHAV-23/Accenture-Data-Analytics-Assignment/blob/master/A%20cleaned%20dataset.xlsx),  a detailed result is provided with columns such as below 
  - Content ID	
  - Reaction Type	
  - Datetime	
  - Content Type	
  - Category	
  - Sentiment	
  - Score

- ### Outputs
  - **Top 5 Categories**
  
  |  Category      | Counts |
  |----------------|--------|
  | Animals        | 1897   |
  | Science        | 1796   |
  | Healthy Eating | 1717   |
  | Food           | 1699   |
  | Technology     | 1698   |

  - **Top 5 Reaction Type**
  
   | Reaction    | Counts   | 
   |-------------|----------|
   | heart       | 1622     |
   | scared      | 1572     |  
   | peeking     | 1559     |
   | hate        | 1552     |
   | interested  | 1549     |


## Project Report

Developed a comprehensive [Project Report](https://github.com/SUMIT-JADHAV-23/Accenture-Data-Analytics-Assignment/blob/master/Project%20Report%20.pdf) presentation in PowerPoint that analyzes and reports on the client's content performance, offering valuable insights, and presenting actionable recommendations for optimization


## Instructions
- In [Accenture Assignment](https://github.com/SUMIT-JADHAV-23/Accenture-Data-Analytics-Assignment), We have to focus on following steps :
  - Data Reading and Understanding:
    -  Read the provided data from the Excel file.
  - Delete Unwanted Data Columns:
    -  From Content_Data drop Unwanted "URl","User ID"
  - Data Organization :
    - Clean and Replace the  annotation  with  blank space
  - Data Cleaning:
    - Drop null values rows 
  - Data Merging :
    - Merge data on common identifier "Content ID","Type"
  - Insights
    - Top 5 Categories
    - Top 5 Reaction
- You can see the Source Code [Here](https://github.com/SUMIT-JADHAV-23/Accenture-Data-Analytics-Assignment/blob/master/test.py)
