# CSCI 0451 S25 Project Proposal: Dark Web Marketplace Analysis: Tracking Trends in the Dark Web Economy

### By: Umman Azan and PB

## Abstract:  
For our project, we plan to analyze a dataset from the [Agora Marketplace](https://www.kaggle.com/datasets/philipjames11/dark-net-marketplace-drug-data-agora-20142015?resource=download). This dataset contains over 100,000 unique listings of items such as drugs, weapons, services, and more, recorded between 2014 and 2015. Our goal is to uncover trends related to pricing, vendor locations, and shipping destinations across these various categories. Using machine learning techniques, we aim to identify correlations between item types (drugs, weapons, services) and regions, which could provide valuable insights into the dark web economy. Success will be measured by how well we can highlight meaningful patterns and predict future pricing or vendor locations based on historical data and evaluating our accuracy score on the train data on the test data.

## Motivation and Question:
- **What problem are we solving, and why does it matter?**  
  The dark web marketplace, including drug trade, weapons sales, and illicit services, presents challenges for law enforcement and public health efforts. By analyzing transaction data from Agora, we can gain insights into the patterns within these illicit markets and potentially identify high-risk vendors or regions. This analysis could play a key role in curbing illegal activities on online marketplaces by providing data-driven insights into the flow of goods.

- **What specific question(s) do we intend to answer?**  
  - Can we predict the regions where different types of goods (drugs, weapons, services) are most commonly shipped?  
  - What pricing patterns can be seen across different product categories and geographic locations?  
  - Is there a relationship between vendor ratings and the pricing of goods, and does this vary by category (e.g., drugs vs. services)?  
  - What are the most purchased goods or items, and what trends can we observe when considering these items alongside other variables such as price, category, and vendor location?

## Planned Deliverables:
1. **Main ML application**  
   - We’ll apply both supervised and unsupervised learning techniques to identify patterns within the Agora marketplace data. We plan to focus on categorizing items based on their shipping destinations, price, and vendor information. Additionally, we plan to experiment with different regression models like logistic regression or random forest regression to predict pricing trends across different categories using historical data.

2. **Exploratory Data Analysis and Prediction Model**  
   - We’ll create a Jupyter notebook to perform exploratory data analysis, by pretty much just being curious and following our intuition through visualizations to see whether we can spot any patterns. For example, visualizing the distribution of prices across different categories, the most commonly listed items, and geographic data about vendors. Through that, we’ll better understand how product categories, such as drugs, weapons, and services, relate to pricing and location.
   - Our goal is to build a model that predicts pricing trends based on product categories, vendor data, and shipping destinations. This will help us forecast pricing behavior and identify larger trends in the marketplace, potentially helping law enforcement or others interested in understanding the flow of illicit goods globally.

-We plan to write a detailed blog post about our final results, following the computational essay style. The post will include:
- Thoughtfully composed English paragraphs explaining our approach and results.
- Clear explanations of the code used for data preprocessing, model building, and evaluation.
- Well-labeled visualizations to help readers understand trends, correlations, and the results of our predictive models.


- **Success measurements** 
   - **Full Success**: A fully functioning model that predicts prices and (hopefully) precise shipping destinations across all item categories, complete with visualizations and performance metrics. (Hoping it won’t be enforcing bias and stereotypes *fingers crossed*)
   - **Partial Success**: If we face challenges (such as sparse data or computational limitations), we will still provide exploratory analysis with meaningful insights into market trends, pricing patterns, and vendor behavior, mostly relying on plots and other visualizations.

## Resources Required
- **Data**  
  - The primary dataset is the *Agora Dark Web Marketplace Data* from Kaggle. It includes vendor information, product categories (drugs, weapons, services, etc.), prices, ratings, and shipping data. This dataset is essential for exploring correlations within the marketplace.
  - **Dataset link**: [Dark Net Marketplace Data (Agora 2014-2015)](https://www.kaggle.com/datasets/philipjames11/dark-net-marketplace-drug-data-agora-20142015/data)

- **Computing Power**  
  - We plan to use Google Colab for our preliminary analysis and model development, as it offers easy access to computational resources and GPU support for training models.  
  - If the resources available in Colab fall short, we’ll reach out for permission to use the BIG GUNS, a.k.a. Middlebury Cluster.

- **Libraries**  
  - We’ll be using popular Python libraries like pandas, NumPy, PyTorch, Scikit-learn, and Matplotlib for data processing, machine learning, and visualizations.

# What we will learn 

- **Prashant Babu**: I look forward to learning more about and working with large datasets, like the dark web dataset, and exploring economic patterns in these markets. Additionally, I am looking forward to improving my data visualization skills and gaining hands-on experience with version control (Git).

## Risk Statement
1. **Lack of Data**: Some categories, such as specific types of weapons or services, may have insufficient data, leading to unreliable conclusions or predictions.
2. **Ethical Considerations**: Handling sensitive data from the dark web requires caution. We must make sure that no illegal activities are promoted or exploited, and we need to be mindful of privacy and confidentiality when working with this type of data.

## Ethics Statement
1. **Who Benefits?**  
   This project would benefit law enforcement agencies, policymakers, and researchers studying the dark web as we will be sharing insights into the economic patterns of illegal markets.
   
2. **Who might be Harmed?**  
   This analysis does not directly affect individuals involved in the marketplace but may raise concerns about privacy, even though the data has been anonymized. As it does identify regions and keywords, certain groups and places might be targeted by law enforcement agencies and it might not necessarily be solely based on “just” assumptions. Also the keywords can unintentionally give the impression of solidifying stereotypes such as the increased use of the N-word or R-word in the context of different products and items, as we can’t really have a fair idea of who the “customers” are or what their identities are. For all we know, it could be skewed through different hidden factors. 
   
3. **Will the World become a better place**  
   - We assume that the data collected from Agora is a representative sample of the dark web marketplace. Assuming that the marketplace behavior from 2014–2015 still holds relevance for understanding today’s dark web trade dynamics including the fact that other marketplaces in the Dark Web show similar behavioral and purchase patterns we believe our project would help make the world a slightly better place.
- Through these assumptions, law enforcement will be able to target and crack down on such drug and arms groups and open-illegal sales on the internet which can be accessed by anyone with little technical knowledge, making the world a overall better place one step at a time.

## Tentative Timeline
- **Week 9 Checkpoint**:  
 - Data preprocessing and cleaning completed.  
 - Figure out at least 6 variables and categories we want to plot,
	

- **Week 10 Checkpoint**:  
  - Initial exploratory data analysis done, including visualizations of most item categories, prices, and vendor locations.
- Preliminary scatter maps, heatmaps etc. done to find correlation between different featuresets/variables.
 - Must use these insights to decide how to build model from there.
- **Week 11 Checkpoint**:  
  - We will build and train our regression model
  - We will get insights into correlations between item categories, pricing, and vendor regions and also compare the model’s accuracy through score with the testers.

- **Final Presentations**:  
  - The final report and presentation will be completed, including an in-depth discussion of our findings and a summary of key trends identified through the analysis.

