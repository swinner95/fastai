# Datasets and Datastores

The AzureML studio allows the user to manage their dataset and datastores directly inside the portal. 

A Dataset is a resource for exploring, transforming and managing data in Azure Machine Learning. 
Datasets enable:

- Easy access to data: without worrying about connection strings or data paths. Only keep a single copy of data in the storage service of your choice.

- Training with big data: seamless integration with Azure Machine Learning features like labelling, training products and pipelines. Users can share and reuse datasets in various experiments.

- Tracking data usage: Azure ML automatically tracks which version of the dataset was used for the ML experiment and produced which model.


## Uploading a Dataset to AzureML studio

1. Download the images in the data folder locally. 

2. Navigate to the left pane of your workspace. Select Datasets under the Assets section.
![datasets](./datsets1.png)

3. Click on 'Create dataset' and choose 'From local files'. Name the dataset for example 'bread-pudding' and then click 'Next'. Make sure to leave the dataset type as File.(You will need to do this for each class of food that you will like to classify.)
![](dataset2.PNG)

4. Click 'Browse', choose the image files you had downloaded for that class of food, and click 'Next' to create the dataset in the workspace's default Blob storage.

5. Click 'Next' and select 'Create' in the "Confirm Details" section. 
![](dataset3.PNG)

For more information on datasets, see the how-to for more information on creating and using Datasets. https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-create-register-datasets
