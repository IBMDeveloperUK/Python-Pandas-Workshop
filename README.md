# Data Science - Python and Pandas

Pandas is one of the main Python libraries for manipulating and analysing structured data and one of the first things to learn if you want to get started with data science.

This workshop is an introduction to Pandas where you will learn about:
- Jupyter notebooks
- Pandas data structures
- Transforming and exploring data
- Visualising data

After an introduction to each of the subjects there will be some exercises to practice what you have learned.

## Getting Started with Jupyter Notebooks

Jupyter notebooks are an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. 

In this workshop we will use IBM Watson Studio to run a notebook. For this you will need an IBM Cloud account. The following steps will show you how sign up and get started. When you have the notebook up and running we will go through the notebook. 

## IBM Cloud

- [Sign up](https://ibm.biz/BdZCKW) for an IBM Cloud account

- Access Watson Studio. At the top of your IBM Cloud dashboard click `Create Resource`. You can find the dashboard under the hamburger menu at the top left:

![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/dashboard.png)

- Search for Watson Studio and click on the tile:

![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/studio.png)

- Select the Lite plan and click `Create`.
- Go back to the dashboard and click on your Watson Studio service and then click `Get Started`. Alternatively, go directly to [Watson Studio](https://eu-gb.dataplatform.ibm.com):

![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/launch.png)

## IBM Watson Studio

- Open [IBM Watson Studio](https://eu-gb.dataplatform.ibm.com/)
- Create a new project by clicking on `Get Started` and `New Project`. 
 
 ![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/new-project.png)
 
- Give your Project a name.
- Select an Object Storage from the drop-down menu or create a new one for free. This is used to store the notebooks and data. **Do not forget to click refresh when returning to the Project page.**
- click `Create`.  

## Add Data to the Project

## Load and Run a Notebook

-  Add a new notebook. Go to the `Assets` tab at the top of the Project page. Scroll down to `Notebooks` and click +. Choose one of these options by clicking on the tabs:
   - **Blank**: Create a new blank notebook
   - **From File**: Choose a notebook file from your computer
   - **From URL**: Choose new notebook `From URL`. Give your notebook a name and copy the URL `https://github.com/IBMDeveloperUK/pandas-workshop/blob/master/pandas-workshop.ipynb`
 
- Select a runtime and click `Create Notebook`. 
  
 * The notebook will load. 
 
To run the notebook each code cell in the notebook needs to be executed, in order, from top to bottom.

Every code cell is selectable and is preceded by a tag in the left margin. The tagformat is `In [x]:`. Depending on the state of the notebook, the `x` can be:

1. A blank, this indicates that the cell has never been executed.
2. A number, this number represents the relative order this code step was executed.
3. A `*`, this indicates that the cell is currently executing.

To execute the code cells in your notebook select the cell, and then press the `Play` button in the toolbar.



