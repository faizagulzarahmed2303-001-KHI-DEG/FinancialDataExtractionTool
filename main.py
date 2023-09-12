# import openai
# import os
# from secret_key import openapi_key

# # Set the OpenAI API key
# openai.api_key = openapi_key

# def poem_on_samosa():
#     prompt = "write a poem of samosa only 4 lines"

#     response = openai.Completion.create(
#         engine="text-davinci-002",  # You can use "text-davinci-002" for GPT-3.5-turbo
#         prompt=prompt,
#         max_tokens=50  # You can adjust the max tokens as needed
#     )

#     print(response.choices[0].text)

# if __name__ == '__main__':
#     poem_on_samosa()



# import openai

# # Set your OpenAI API key here
# openai.api_key = "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"

# #this is a news article
# def extract_financial_data(text):
#     prompt = get_prompt_financial() + text
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     content = response.choices[0]['message']['content']
#     print(content)  # Print the content to see the output

#     #chatgpt mei prompt boht matter karta hai
# def get_prompt_financial():
#     return '''Please retrieve company name, revenue, net income, and earnings per share (a.k.a. EPS)
#     from the following news article. If you can't find the information from this article,
#     then return "". Do not make things up.    
#     Then retrieve a stock symbol corresponding to that company. For this, you can use
#     your general knowledge (it doesn't have to be from this article). Always return your
#     response as a valid JSON string. The format of that string should be this, 
#     {
#         "Company Name": "Walmart",
#         "Stock Symbol": "WMT",
#         "Revenue": "12.34 million",
#         "Net Income": "34.78 million",
#         "EPS": "2.1 $"
#     }
#     News Article:
#     ============
#     '''

# if __name__ == '__main__':
#     text = '''CUPERTINO, CALIFORNIA Apple today announced financial results for its fiscal 2023 third quarter ended July 1, 2023. The Company posted quarterly revenue of $81.8 billion, down 1 percent year over year, and quarterly earnings per diluted share of $1.26, up 5 percent year over year. 
#     “We are happy to report that we had an all-time revenue record in Services during the June quarter, driven by over 1 billion paid subscriptions, and we saw continued strength in emerging markets thanks to robust sales of iPhone,” said Tim Cook, Apple’s CEO. “From education to the environment, we are continuing to advance our values, while championing innovation that enriches the lives of our customers and leaves the world better than we found it.”
#     “Our June quarter year-over-year business performance improved from the March quarter, and our installed base of active devices reached an all-time high in every geographic segment,” said Luca Maestri, Apple’s CFO. “During the quarter, we generated very strong operating cash flow of $26 billion, returned over $24 billion to our shareholders, and continued to invest in our long-term growth plans.”
#     Apple’s board of directors has declared a cash dividend of $0.24 per share of the Company’s common stock. The dividend is payable on August 17, 2023, to shareholders of record as of the close of business on August 14, 2023.
#     Apple will provide live streaming of its Q3 2023 financial results conference call beginning at 2:00 p.m. PT on August 3, 2023, at apple.com/investor/earnings-call. The webcast will be available for replay for approximately two weeks thereafter.
#     '''
#     extract_financial_data(text)


import streamlit as st
import pandas as pd
import openai_helper 


col1, col2 = st.columns([3,2])

financial_data_df = pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["", "", "", "", ""]
    })

#table mei text box aye ga.
with col1:
    st.title("Financial Data Extraction tool")
    news_article = st.text_area("paste your financial news article here", height=300)
    if st.button("Extract"):
        financial_data_df = openai_helper.extract_financial_data(news_article)
        print(financial_data_df.to_string(index=False))
       
        
#table col2 mei aye ga.
with col2:
    st.markdown("<br/>" *8, unsafe_allow_html=True)
    st.dataframe(
        financial_data_df,
        column_config={
            "Measure": st.column_config.Column(width=150),
            "Value": st.column_config.Column(width=150)
        },
         hide_index=True
    )


# def extract_company_info(article):
#     # Replace these placeholders with your actual data extraction logic
#     company_name = "Apple Inc"
#     revenue = "23.45 billion $"
#     eps = "12.3 billion $"
    
#     return company_name, revenue, eps

# # Create a Streamlit app
# st.title("News Article Analyzer")
# st.write("Enter a news article and click on 'Extract' to extract company information.")

# # Create a text area for the news article input
# article = st.text_area("News Article", height=300)

# # Create a button to trigger data extraction
# if st.button("Extract"):
#     if article:
#         company_name, revenue, eps = extract_company_info(article)

#         data = {
#             "Measures": ["Company Name", "Revenue", "EPS"],
#             "Values": [company_name, revenue, eps]
#         }

#         df = pd.DataFrame(data)

#         st.table(df)
#     else:
#         st.warning("Please enter a news article")

    