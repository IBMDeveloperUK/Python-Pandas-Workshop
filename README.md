# Data Science - Python and Pandas

Pandas is one of the main Python libraries for manipulating and analysing structured data and one of the first things to learn if you want to get started with data science.

This workshop is an introduction to Pandas where you will learn about:
- Jupyter notebooks
- Pandas data structures
- Transforming and exploring data
- Visualising data

After an interactive overview for each of the subjects there will be some exercises to practice what you have learned. 

## Getting Started with Jupyter Notebooks

Jupyter notebooks are an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. 

In this workshop we will use IBM Watson Studio to run a notebook. For this you will need an IBM Cloud account. The following steps will show you how sign up and get started. When you have the notebook up and running we will go through the notebook. 

## IBM Cloud

- [Sign up](https://ibm.biz/pandas_workshop) for an IBM Cloud account

- At the top of the Resources page click `Create Resource`. You can find the resources under the hamburger menu at the top left:

 ![](https://github.com/IBMDeveloperUK/pandas-workshop/blob/master/images/resources.png)
 
- Search for Watson Studio and click on the tile:

![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/studio.png)

- Select the Lite plan and click `Create`.
- Go back to the Resources list and click on your Watson Studio service and then click `Get Started`. 

![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/launch.png)

## IBM Watson Studio

- You should now be in Watson Studio.
- Create a new project by clicking on `Get Started` and `New Project`, or `Create Project`
- Give your Project a name.
- Select an Object Storage from the drop-down menu or create a new one for free. This is used to store the notebooks and data. **Do not forget to click refresh when returning to the Project page.**
- click `Create`.  

## Add Data to the Project

- We will analyse data about the sizes of jeans pockets in this workshop. To do this you need to add the data to your project.
- Download the `measurements.csv` file from [here](https://github.com/the-pudding/data/tree/master/pockets) to your laptop. A big thanks to Jan Diehm and Amber Thomas for going around shops, measuring the jeans and putting the data online for everyone to use.  
- Add this file to your newly created project in Watson Studio by uploading the file in the right side menu (click the 1010 button if you do not see this): 

 ![](https://github.com/IBMDeveloperUK/pandas-workshop/blob/master/images/upload.png)

## Load and Run a Notebook

-  Add a new notebook. Click `Add to project` and choose `Notebook`:

![](https://github.com/IBMDeveloperUK/pandas-workshop/blob/master/images/addnotebook.png)

- Choose new notebook `From URL`. Give your notebook a name and copy the URL `https://github.com/IBMDeveloperUK/pandas-workshop/blob/master/pandas-workshop.ipynb`
- Select the default runtime and click `Create Notebook`. 
-  The notebook will load. 
 
You are now ready to follow along with the workshop in the notebook!



