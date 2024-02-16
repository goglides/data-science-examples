
## Retrieval augmented generation
 
    In retrieval augmented generation (RAG), an LLM retrieves contextual documents from an external dataset as part of its execution. 

    This is useful if we want to ask question about specific documents (e.g., our PDFs, a set of videos, etc).
    in this notebook , we will focus  on pdf and Excel 

![alt text](RAG.jpg)

## 1. financial statements (excel)

### steps 
1. Load and Read Excel File:

2. Begin by loading the financial data from the Excel file using a reliable library, such as pandas, to facilitate further processing.
Data Preprocessing:

3. Preprocess the data to handle any missing values. Ensure that the data is clean and ready for subsequent transformations.
Convert Excel File into String:

4. Transform the preprocessed data into a unified string format, facilitating subsequent natural language processing tasks.
Split Data into Chunks Based on Headers:

5. Segment the string data into chunks, focusing on headers to delineate different sections. Each financial statement or related information should be treated as an independent unit.
Hugging Face Embeddings:

6. Leverage Hugging Face embeddings to convert the text data into meaningful numerical representations, capturing semantic relationships for enhanced analysis.
FAISS Vector Database:

7. Establish a FAISS vector database using the embedded chunks, providing an efficient platform for similarity search and clustering of dense vectors.
Question Formulation:

8. Formulate specific questions based on the financial context to extract targeted information. This step is crucial for    guiding the subsequent retrieval process.
Retrieval:

9. Utilize the FAISS vector database to retrieve relevant chunks based on the formulated questions, narrowing down the search space and enhancing efficiency.
Retrieval + Prompt + LLM (GPT-3.5):

10. Enhance the retrieval process by incorporating a prompt to further refine results using a large language model (LLM) such as GPT-3.5. This step adds contextual understanding and depth to the retrieved information.

#### Faiss 
    is an open-source library designed for efficient similarity search and clustering of dense vectors, making it suitable for handling massive vector sets that surpass the capacity of random-access memory (RAM). The library offers various methods for similarity search, utilizing vector comparisons based on L2 distances, dot products, and cosine similarity.
        

## Benchmark Questions asked
-----------------------------------------------------Financial Statments----------------------------------------------
###  Income Statement:
#### What is Saudi Aramco's total revenue for the last quarter or most recent fiscal year?
#### Answer:

```
Saudi Aramco's total revenues in the last quarter amounted to 424,095 million riyals, and for the last fiscal year they amounted to 1,244,119 million riyals.

```

### Balance Sheet:
#### The current assets of Saudi Aramco, and how have they changed over the past year?
#### Answer
```
Copilot: Saudi Aramco's current assets have changed over the past year. According to the data provided, current assets for the period ending 09-30-2023 amounted to 794,519 and for the period ending 09-30-2022 853,149. This indicates a decrease in current assets from 2022 to 2023.

Current asset categories include bank balances and cash, trade receivables, inventory, short-term investments, due from government, and other assets and receivables - current.

```

### Cash Flow Statement: 
#### What are the main sources and uses of cash in Saudi Aramco’s operating activities?

#### Answer
```
Copilot: The sources and main uses of cash in the operating activities of Saudi Aramco can be found in the cash flow statement. According to the provided information, the net cash flows from operating activities for the company amounted to $392,356 million in the recent period. Operating cash flow was obtained from various sources, including profit before zakat and income tax from continuing operations, adjustments for financing costs, depreciation and amortization, financing revenues, and other cash flows classified as operating activities.

Additionally, there were adjustments related to changes in working capital, such as those associated with inventory, trade accounts payable, taxes payable, government dues payable, and other liabilities and receivables.
```
-----------------------------------------------Financial Report----------------------------------------------------

## 1. Financial Report (pdf) 

### steps 
1. Load Data and Read PDF File:

2. Initiate the process by loading and reading the data from the PDF file. Use suitable libraries, such as langchain PyPDFLoader , to seamlessly extract information from the document.
Split Data (Chunk Size = 6000, Chunk Overlap = 1200):

3. Implement data segmentation into chunks, optimizing the chunk size to 6000 and allowing a 1200-character overlap using CharacterTextSplitter, This ensures a comprehensive coverage of the PDF content.
Hugging Face Embeddings:

4. Apply Hugging Face embeddings to transform the segmented data into meaningful numerical representations, capturing contextual relationships for subsequent analysis.
FAISS Vector Database:

5. Create a FAISS vector database using the embedded chunks, facilitating efficient similarity search and clustering of dense vectors for enhanced data organization.
Question Formulation:

6. Formulate specific questions tailored to the PDF content, serving as a guide for subsequent retrieval and analysis. This step is essential for extracting relevant information.
Retrieval:

7. Utilize the FAISS vector database to retrieve chunks based on the formulated questions. This step streamlines the search process, improving efficiency and accuracy.
Retrieval + Prompt + LLM (GPT-3.5):

8. Elevate the retrieval process by incorporating a prompt, leveraging a large language model (LLM) such as GPT-3.5. This additional step enhances the depth and context of the retrieved information.
Output:

9. Present the final output, incorporating the retrieved and processed information from the PDF document. Ensure clarity and coherence in the output for seamless analysis or subsequent decision-making processes.

### Management Discussion and Analysis (MD&A): 

#### What insights does management provide in the sale, purchase and acquisition process regarding the challenges and opportunities facing Saudi Aramco?

#### Answer
```
Copilot:
Saudi Aramco's management provides insights into the sales, purchases, and acquisitions process, highlighting the challenges andopportunities facing the company. The company operates within the Kingdom and has interests in refining, petrochemicals, distribution, marketing, and storage facilities outside the Kingdom. Management regularly evaluates operational sectors based on revenues, costs, a wide range of key performance indicators, and sector profitability. This assessment is crucial for resource allocation and performance evaluation.


Furthermore, the company's financial data reveals movements in financial assets, such as option rights and financial liabilities, due to changes in the unrealized fair value of those contracts during the period.
        
These movements are primarily attributed to the buying and selling of financial derivative contracts, including recognizing profits or losses resulting from adjusting financial derivatives to fair value.


In addition to management discussion on risks and factors affecting the company's financial position and operations, including oil and gas supply and demand, price volatility, global economic market conditions, competition, climate 
change concerns, and risks associated with ongoing projects and acquisitions. It provides insightful perspectives on 
the challenges and opportunities facing Saudi Aramco.
It is important to note that the company's financial information is prepared and presented in accordance with the International Accounting Standard 34 and other standards and releases issued by the Saudi Organization for Certified Public Accountants (SOCPA). 


The company also provides financial metrics not in compliance with international standards to complement international financial reporting standards, offering a deeper understanding of Saudi Aramco's operational results, cash flows, and financial position from a management perspective. These measures are provided in addition to international financial reporting standards and are reconciled in the Non-IFRS Measures and Reconciliation section in the interim report

```

    
    
