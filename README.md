# Mushroom Classification

Safe to eat or deadly poison? 
Based on the characteristics of a mushroom the application predicts whether the mushroom is edible or poisonous.

---
**_ATTENTION!!!_**  

This is a student project which is by no means intended to be  actually used to identify edible mushrooms! 

---

## Data

The data can be found in de data folder. It is downloaded from the UC Irvine Machine Learning repository: https://archive.ics.uci.edu/dataset/848/secondary+mushroom+dataset

More information about the data can be found in the following paper:

Dennis Wagner, D. Heider, Georges Hattab. - *Mushroom data creation, curation, and simulation to support classification tasks* (2021) - Published in Scientific Reports

### Variable Information
One binary class divided in edible=e and poisonous=p (with the latter one also containing mushrooms of unknown edibility).
Twenty remaining variables (n: nominal, m: metrical)
1. cap-diameter (m): float number in cm
2. cap-shape (n): bell=b, conical=c, convex=x, flat=f,
sunken=s, spherical=p, others=o
3. cap-surface (n): fibrous=i, grooves=g, scaly=y, smooth=s,
shiny=h, leathery=l, silky=k, sticky=t,
wrinkled=w, fleshy=e
4. cap-color (n): brown=n, buff=b, gray=g, green=r, pink=p,
purple=u, red=e, white=w, yellow=y, blue=l,
orange=o, black=k
5. does-bruise-bleed (n): bruises-or-bleeding=t,no=f
6. gill-attachment (n): adnate=a, adnexed=x, decurrent=d, free=e,
sinuate=s, pores=p, none=f, unknown=?
7. gill-spacing (n): close=c, distant=d, none=f
8. gill-color (n): see cap-color + none=f
9. stem-height (m): float number in cm
10. stem-width (m): float number in mm
11. stem-root (n): bulbous=b, swollen=s, club=c, cup=u, equal=e,
rhizomorphs=z, rooted=r
12. stem-surface (n): see cap-surface + none=f
13. stem-color (n): see cap-color + none=f
14. veil-type (n): partial=p, universal=u
15. veil-color (n): see cap-color + none=f
16. has-ring (n): ring=t, none=f
17. ring-type (n): cobwebby=c, evanescent=e, flaring=r, grooved=g,
large=l, pendant=p, sheathing=s, zone=z, scaly=y, movable=m, none=f, unknown=?
18. spore-print-color (n): see cap color
19. habitat (n): grasses=g, leaves=l, meadows=m, paths=p, heaths=h,
urban=u, waste=w, woods=d
20. season (n): spring=s, summer=u, autumn=a, winter=w


## Setting up the environment

Conda was used to manage the Python environment for this project. The packages are listed in the `environment.yml` file. The following command can be used to set up the envirment (also see the conda documentation about [Creating an environment from an environment.yml file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)):
```
conda env create -f environment.yml
```

## Exploraroty Data Analysis
The data exploration can be found in the notebook `notebook.ipynb`.

## Training the Model and Hyperparameter Tuning
The evaluation of the models and tuning of the hyperparameters can also be found in the notebook `notebook.ipynb`. The final model can be trained with the `train.py` script.

## Deployment
The model is deployed as a Flask app in a Docker container. The Docker image can be build with the `Dockerfile`. This can be done with the following docker command (while in the main repository folder):
```
docker build -t mushroom-app .
```  
The next step is to spin up the docker container:
```
docker run -it --rm -p 9696:9696 mushroom-app 
```
The app is now exposed on port 9696 through the POST method `predict`. Sample code for how to test and use the app is provided in the notebook `notebook.ipynb`.

The app is deployed on Azure using the [Azure Container Apps](https://azure.microsoft.com/en-us/products/container-apps) service. This was done using VS code extensions, as described in [Quickstart: Deploy to Azure Container Apps using Visual Studio Code](https://learn.microsoft.com/en-us/azure/container-apps/deploy-visual-studio-code). The app is exposed on the following url: 
```
url = 'https://mushroom-app.orangepebble-a9df90f9.westeurope.azurecontainerapps.io'
```
In the notebook `notebook.ipynb` there is sample code to test and use the deployed app.

