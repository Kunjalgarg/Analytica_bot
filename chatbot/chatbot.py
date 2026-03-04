
import pandas as pd
import matplotlib.pyplot as plt
import os
import re
import difflib
import io

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   #current directory
csv_path = os.path.join(BASE_DIR, "../cleaned_data/diamond_cleaned_data.csv")  #path to cleaned data

df = pd.read_csv(csv_path)     #reading cleaned data

df['rounded'] = df['cut'].round(3)       #rounding cut values to 3 decimal places
df['label'] = df['rounded'].map({            #mapping cut values to labels
    -2.484: "Worst",
    -1.511: "Good",
    -0.538: "Best",
     0.435: "Premium",
     1.408: "Ideal"
})

df['label'] = df['label'].str.lower()             #lowercase labels
df['clarity'] = df['clarity'].astype(str).str.strip().str.lower()  
df['color'] = df['color'].astype(str).str.strip().str.lower() 

COLUMNS = list(df.columns)        
LABELS = df['label'].dropna().unique()        #unique labels
CLARITY_VALUES = df['clarity'].unique()       
COLOR_VALUES = df['color'].unique()

#First message from Analytica 
print("\nHi I'm Analytica, let's analyse some diamond data together!")
print("Type 'help' for commanads and 'exit' to stop\n")

def extract_cut(tokens):                #extraction from tokens
    for t in tokens:
        if t in LABELS:
            return t
        match = difflib.get_close_matches(t, LABELS, n=1, cutoff=0.7)     #fuzzy matching
        if match:
            return match[0]                      
    return None


def extract_clarity(tokens):                 #extracting clarity from tokens
    for i in range(len(tokens)):
        if tokens[i] == "clarity" and i + 1 < len(tokens):              
            if tokens[i + 1] in CLARITY_VALUES:
                return tokens[i + 1]
    return None


def extract_color(tokens):                     #extracting color from tokens
    for i in range(len(tokens)):
        if tokens[i] == "color" and i + 1 < len(tokens):
            if tokens[i + 1] in COLOR_VALUES:                   
                return tokens[i + 1]
    return None


def extract_price(query):                   #extracting price conditions from query
    nums = re.findall(r'\d+', query)                 #finding numbers in query
    if not nums:
        return None
    value = int(nums[0])
    if "under" in query or "below" in query:               
        return ("<", value)                                      #less than condition
    if "above" in query or "over" in query:
        return (">", value)                                      #greater than condition
    return None

# Graph plotting function

def plot_graph(query):        
    graph_type = None
    x_col = None
    y_col = None

    #type of graph extraction
    if "bar" in query:
        graph_type = "bar"
    elif "scatter" in query:
        graph_type = "scatter"
    elif "box" in query:
        graph_type = "box"
    elif "histogram" in query or "hist" in query:
        graph_type = "hist"

    if not graph_type:
        return None

    #column identification
    for col in df.columns:               
        if col.lower() in query:
            if not x_col:
                x_col = col
            elif not y_col:
                y_col = col

    # Default 'vs' columns for graphs
    if graph_type == "scatter" and x_col and not y_col:
        y_col = "price"

    if graph_type == "bar" and x_col and not y_col:
        y_col = "depth"

    #actual graph plotting
    try:
        if graph_type == "scatter":
            df.plot.scatter(x=x_col, y=y_col)
            plt.show()
            return f"Scatter plot plotted ({x_col} vs {y_col})"

        if graph_type == "bar":
            df.groupby(x_col)[y_col].mean().plot(kind='bar')
            plt.ylabel(f"Average {y_col}")
            plt.show()
            return f"Bar graph plotted ({x_col} vs {y_col})"

        if graph_type == "box":
            df.boxplot(column=x_col)
            plt.show()
            return f"Box plot plotted ({x_col})"

        if graph_type == "hist":
            df[x_col].plot(kind='hist')
            plt.show()
            return f"Histogram plotted ({x_col})"

    except Exception as e:
        return f"Could not plot graph: {e}"

# this is the main fucntion that handles user queries
def chatbot(user_query):
    q = user_query.lower()
    tokens = q.split()
    data = df.copy()

    if "help" in q:                               #help message
        return """

BASIC:
- rows
- columns
- summary
- head
- tail
- info
- shape
- sample
- average price by cut
- count by clarity

STATISTICS:
- min price
- max depth
- average carat
- median table

DISTINCT/UNIQUE:
- unique cuts
- distinct values
- distinct values for cut

FILTERS:
- worst cut
- good cut
- best cut
- premium cut
- ideal cut
- ideal cut under 5000
- ideal cut above 10000
- ideal cut clarity vs color
- ideal cut clarity si1 color d

RANKINGS:
- top 5 expensive diamonds	
- top 10 cheap diamonds

GRAPHS: (need to specify type of graph)
- plot bar clarity vs depth                          
- plot scatter color
- plot histogram price
- plot box depth

"""

    if "plot" in q:                                 #graph plotting
        graph_response = plot_graph(q)
        if graph_response:
            return graph_response

    if "distinct values" in q:                               
        for col in COLUMNS:
            if col in q:
                return df[col].unique()
        return {col: df[col].unique() for col in COLUMNS}
    
    if "unique" in q:
        if "cut" in q:
            return df['label'].unique()
        if "clarity" in q:
            return df['clarity'].unique()
        if "color" in q:
            return df['color'].unique()


    # Basics
    if "rows" in q:
        return f"Total rows: {len(df)}"

    if "columns" in q:
        return COLUMNS
    
    if "summary" in q:
        return df.describe()
    
    if q == "head":          #gives top 5 rows
        return df.head()

    if q == "tail":             #gives last 5 rows
        return df.tail()

    if q.strip() == "info":                  #info regarding dataframe
        buffer = io.StringIO()      
        df.info(buf=buffer)
        return buffer.getvalue()

    if "shape" in q:                                             #rows x columns
        return f"Rows: {df.shape[0]}, Columns: {df.shape[1]}"

    if "sample" in q:                                            #random sample of 5 rows
        return df.sample(5)

    if "count by cut" in q:
        return df['cut_label'].value_counts()

    if "count by clarity" in q:
        return df['clarity'].value_counts()

    if "count by color" in q:
        return df['color'].value_counts()
    
    # Statistics operations
    stats_words = ["min", "max", "average", "mean", "median"]

    for stat in stats_words:
        if stat in q:
            for col in COLUMNS:
                if col.lower() in q:
                    series = df[col]
                    if pd.api.types.is_numeric_dtype(series):
                        if stat == "min":
                            return f"Min {col}: {series.min()}"
                        if stat == "max":
                            return f"Max {col}: {series.max()}"
                        if stat in ["average", "mean"]:
                            return f"Average {col}: {series.mean():.2f}"
                        if stat == "median":
                            return f"Median {col}: {series.median()}"
                    else:
                        if stat in ["min", "max"]:                             
                            return f"{stat.capitalize()} {col} (lexical): {series.min() if stat=='min' else series.max()}"           #lexical min/max for non-numeric
                        else:
                            return f" {stat} not applicable to categorical column '{col}'"

    # Filters
    cut = extract_cut(tokens)
    clarity = extract_clarity(tokens)
    color = extract_color(tokens)
    price = extract_price(q)

    if cut:
        data = data[data['label'] == cut]
    if clarity:
        data = data[data['clarity'] == clarity]
    if color:
        data = data[data['color'] == color]
    if price:
        op, val = price
        data = data[data['price'] < val] if op == "<" else data[data['price'] > val]

    if cut or clarity or color or price:
        return data.head(10)

    if "top" in q:
        nums = re.findall(r'\d+', q)
        n = int(nums[0]) if nums else 5

        if "expensive" in q:                                             #top n expensive diamonds
            return df.sort_values(by='price', ascending=False).head(n)

        if "cheapest diamond" in q or q.strip() == "cheapest":                   #cheapest diamond
            row = df.loc[df['price'].idxmin()]
            return f"Cheapest diamond:\n\n{row}"
        
    if "by" in q:                                               #group by operations
        if "average" in q and "price" in q:
            for col in ['label', 'clarity', 'color']:
                if col.replace('_label','') in q:
                    return df.groupby(col)['price'].mean()

        if "count" in q:                                             #count by category
            for col in ['label', 'clarity', 'color']:
                if col.replace('_label','') in q:
                    return df[col].value_counts()

    return "Unknown command. Type 'help'"

# Main loop

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Ana: Goodbye!")
        break
    print("Ana:", chatbot(user_input), "\n")
